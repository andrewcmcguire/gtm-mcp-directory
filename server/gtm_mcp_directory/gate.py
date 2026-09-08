"""gate.py: the key check in front of the hosted MCP endpoint, and the access-request intake.

An ASGI wrapper around the FastMCP HTTP app. It runs only when GTM_DIRECTORY_KEYS_DB is set
(the hosted copy on the box); a local install never sees it. Three jobs:

1. Every request under the MCP base path must carry a valid key, presented one of three ways:
     Authorization: Bearer gtmd_...          (Cursor, Claude Code, anything that sends headers)
     X-API-Key: gtmd_...
     <base path>/k/gtmd_...                  (clients that only take a URL, such as claude.ai)
   The per-key URL form is rewritten to the base path before the MCP app sees it. A missing or
   revoked key gets 401 with a JSON body that names the request page. A valid key adds one to
   that key's call count and stamps the day; nothing about the call itself is recorded.

2. POST <access path> takes the request form from the site (application/x-www-form-urlencoded):
   name, email, company, use_case, client, consent, and a honeypot named "website". It stores
   the request and redirects to the thank-you page. Validation misses redirect back to the form.
   Five requests an hour per address is the ceiling; the address is stored only as a salted hash.

3. GET <base path>/health answers 200 with the build date, for the publish rail's live check.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import re
import time
import urllib.parse
from typing import Any, Callable, Optional

from . import keys as keystore

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[a-z]{2,}$", re.I)
FREE_MAIL = {"gmail.com", "googlemail.com", "yahoo.com", "yahoo.co.uk", "hotmail.com", "outlook.com", "live.com", "msn.com", "icloud.com",
             "me.com", "aol.com", "proton.me", "protonmail.com", "pm.me", "gmx.com", "gmx.de", "mail.com", "yandex.com", "zoho.com",
             "fastmail.com", "hey.com", "duck.com", "tutanota.com", "mail.ru", "qq.com", "163.com"}


def is_free_mail(email: str) -> bool:
    return email.rsplit("@", 1)[-1].lower() in FREE_MAIL


class KeyGate:
    def __init__(self, app: Callable, base_path: str, db_path: str, form_url: str, sent_url: str,
                 access_path: str = "/gtm-directory/api/access", generated_on: Optional[str] = None) -> None:
        self.app = app
        self.base = base_path.rstrip("/")
        self.db_path = db_path
        self.form_url = form_url
        self.sent_url = sent_url
        self.access_path = access_path.rstrip("/")
        self.generated_on = generated_on
        self._conn = None
        self._cache: dict[str, tuple[float, Optional[int]]] = {}
        self._salt = dt.date.today().isoformat() + os.environ.get("GTM_GATE_SALT", "gtm-directory")

    # --- storage -----------------------------------------------------------------------------
    def conn(self):
        if self._conn is None:
            self._conn = keystore.init(self.db_path)
        return self._conn

    def key_id_for(self, plaintext: str) -> Optional[int]:
        """Valid key -> id, else None. A 20 second cache keeps the hot path off the disk."""
        hit = self._cache.get(plaintext)
        if hit and hit[0] > time.time():
            return hit[1]
        row = keystore.verify(self.conn(), plaintext)
        kid = int(row["id"]) if row else None
        if len(self._cache) > 5000:
            self._cache.clear()
        self._cache[plaintext] = (time.time() + 20, kid)
        return kid

    # --- helpers -----------------------------------------------------------------------------
    @staticmethod
    def _headers(scope) -> dict[str, str]:
        return {k.decode("latin-1").lower(): v.decode("latin-1") for k, v in scope.get("headers") or []}

    def _client_ip(self, headers: dict[str, str], scope) -> str:
        ip = headers.get("cf-connecting-ip") or (headers.get("x-forwarded-for") or "").split(",")[0].strip()
        if not ip and scope.get("client"):
            ip = scope["client"][0]
        return ip or "unknown"

    def _ip_hash(self, ip: str) -> str:
        return hashlib.sha256((self._salt + ip).encode()).hexdigest()[:24]

    async def _send(self, send, status: int, body: bytes, ctype: str = "application/json", extra: Optional[list] = None) -> None:
        headers = [(b"content-type", ctype.encode()), (b"content-length", str(len(body)).encode()), (b"cache-control", b"no-store")]
        headers += extra or []
        await send({"type": "http.response.start", "status": status, "headers": headers})
        await send({"type": "http.response.body", "body": body})

    async def _redirect(self, send, url: str) -> None:
        await self._send(send, 303, b"", "text/plain", [(b"location", url.encode())])

    async def _read_body(self, receive, limit: int = 64_000) -> bytes:
        body = b""
        while True:
            msg = await receive()
            body += msg.get("body", b"")
            if len(body) > limit:
                return body[:limit]
            if not msg.get("more_body"):
                return body

    # --- ASGI ---------------------------------------------------------------------------------
    async def __call__(self, scope, receive, send):
        if scope["type"] != "http":
            return await self.app(scope, receive, send)  # lifespan and websockets pass straight through
        path = scope.get("path") or "/"
        if path.rstrip("/") == self.access_path:
            return await self.handle_access(scope, receive, send)
        if path == self.base + "/health":
            body = json.dumps({"ok": True, "generated_on": self.generated_on, "gate": "key required", "request_a_key": self.form_url}).encode()
            return await self._send(send, 200, body)
        if path != self.base and not path.startswith(self.base + "/"):
            return await self._send(send, 404, json.dumps({"error": "not found", "mcp": self.base, "request_a_key": self.form_url}).encode())

        headers = self._headers(scope)
        key = None
        rest = path[len(self.base):]
        if rest.startswith("/k/"):
            key = rest[3:].split("/", 1)[0]
            new_path = self.base + rest[3 + len(key):]
            scope = dict(scope, path=new_path or self.base, raw_path=(new_path or self.base).encode())
        if not key:
            auth = headers.get("authorization", "")
            if auth.lower().startswith("bearer "):
                key = auth[7:].strip()
        if not key:
            key = headers.get("x-api-key", "").strip()
        if not key:
            qs = urllib.parse.parse_qs(scope.get("query_string", b"").decode("latin-1"))
            if qs.get("key"):
                key = qs["key"][0]
                qs.pop("key", None)
                scope = dict(scope, query_string=urllib.parse.urlencode(qs, doseq=True).encode("latin-1"))
        kid = self.key_id_for(key) if key else None
        if not kid:
            body = json.dumps({
                "jsonrpc": "2.0", "id": None,
                "error": {"code": -32001, "message": "This hosted copy of The GTM MCP Directory needs a free key.",
                          "data": {"request_a_key": self.form_url,
                                   "how": "Send it as Authorization: Bearer gtmd_..., as X-API-Key, or put it in the URL as %s/k/gtmd_..." % self.base,
                                   "local_install_needs_no_key": "https://github.com/andrewcmcguire/gtm-mcp-directory"}},
            }).encode()
            return await self._send(send, 401, body, extra=[(b"www-authenticate", b'Bearer realm="gtm-directory", error="invalid_token"')])
        try:
            keystore.record_use(self.conn(), kid)
        except Exception:  # noqa: BLE001  a counting failure must never block an answer
            pass
        return await self.app(scope, receive, send)

    # --- the request form ---------------------------------------------------------------------
    async def handle_access(self, scope, receive, send):
        method = scope.get("method", "GET").upper()
        if method == "GET":
            return await self._redirect(send, self.form_url)
        if method != "POST":
            return await self._send(send, 405, b'{"error":"POST the form"}')
        headers = self._headers(scope)
        raw = await self._read_body(receive)
        ctype = headers.get("content-type", "")
        fields: dict[str, Any] = {}
        if "application/json" in ctype:
            try:
                fields = json.loads(raw.decode("utf-8", "replace") or "{}")
            except ValueError:
                fields = {}
        else:
            fields = {k: v[0] for k, v in urllib.parse.parse_qs(raw.decode("utf-8", "replace"), keep_blank_values=True).items()}
        g = lambda k: str(fields.get(k, "") or "").strip()  # noqa: E731
        name, email, company, use_case, client = g("name"), g("email").lower(), g("company"), g("use_case"), g("client")
        consent = g("consent").lower() in ("on", "1", "true", "yes")
        honeypot = bool(g("website"))
        ip_hash = self._ip_hash(self._client_ip(headers, scope))
        ok = bool(name) and bool(EMAIL_RE.match(email)) and len(use_case) >= 20 and consent
        if not ok and not honeypot:
            return await self._redirect(send, self.form_url + "?error=1")
        try:
            conn = self.conn()
            if keystore.recent_request_count(conn, ip_hash, hours=1) >= 5:
                return await self._redirect(send, self.form_url + "?error=rate")
            keystore.add_request(conn, name, email, company, use_case, client, consent, ip_hash, headers.get("user-agent", ""), honeypot)
        except Exception:  # noqa: BLE001
            return await self._redirect(send, self.form_url + "?error=store")
        if "application/json" in ctype:
            return await self._send(send, 200, json.dumps({"ok": True, "next": self.sent_url}).encode())
        return await self._redirect(send, self.sent_url)


def wrap(app: Callable, base_path: str, generated_on: Optional[str] = None) -> Callable:
    """Wrap the MCP app in the gate when a key store is configured; otherwise return it as is."""
    db = keystore.db_path()
    if not db:
        return app
    form_url = os.environ.get("GTM_ACCESS_FORM_URL", "https://andrewcmcguire.com/gtm-directory/access/")
    sent_url = os.environ.get("GTM_ACCESS_SENT_URL", "https://andrewcmcguire.com/gtm-directory/access/sent")
    access_path = os.environ.get("GTM_ACCESS_PATH", "/gtm-directory/api/access")
    return KeyGate(app, base_path, db, form_url, sent_url, access_path, generated_on)
