"""keys.py: the key store behind the hosted endpoint, and the access-request queue.

The hosted copy of the directory at andrewcmcguire.com/gtm-directory/api/mcp needs a key
since 2026-09-08 (Drew: "make sure you need a key that I can manage"). This module is the
whole of that: a SQLite file on the box, a handful of functions the HTTP gate calls on
every request, and a command line for the operator and the access desk.

    python -m gtm_mcp_directory.keys init
    python -m gtm_mcp_directory.keys issue --name "Jane Doe" --email jane@acme.com --org Acme --note "asked on 2026-09-08"
    python -m gtm_mcp_directory.keys list
    python -m gtm_mcp_directory.keys revoke gtmd_ab12cd34
    python -m gtm_mcp_directory.keys requests           # pending access requests
    python -m gtm_mcp_directory.keys approve 7          # issue a key for request 7
    python -m gtm_mcp_directory.keys deny 7 --reason "no use case given"
    python -m gtm_mcp_directory.keys stats

What is stored about a key holder: name, email, organisation, a note, when it was issued,
when it was revoked, the number of calls and the date it was last used, and a per-day call
count. Nothing about the calls themselves: no query text, no tool arguments. The key itself
is stored only as a SHA-256 hash; the plaintext is shown once, at issue time, and never
again. The database path comes from GTM_DIRECTORY_KEYS_DB; when that is unset the local
server runs with no gate at all, which is the right default for a package anyone can install.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import os
import secrets
import sqlite3
import sys
from typing import Any, Optional

KEY_PREFIX = "gtmd_"
DB_ENV = "GTM_DIRECTORY_KEYS_DB"

SCHEMA = """
CREATE TABLE IF NOT EXISTS keys (
  id INTEGER PRIMARY KEY,
  prefix TEXT NOT NULL,
  key_hash TEXT NOT NULL UNIQUE,
  name TEXT, email TEXT, org TEXT, note TEXT,
  status TEXT NOT NULL DEFAULT 'active',
  created TEXT NOT NULL, revoked TEXT, last_used TEXT,
  calls INTEGER NOT NULL DEFAULT 0,
  issued_by TEXT, request_id INTEGER
);
CREATE TABLE IF NOT EXISTS usage (
  key_id INTEGER NOT NULL, day TEXT NOT NULL, calls INTEGER NOT NULL DEFAULT 0,
  PRIMARY KEY (key_id, day)
);
CREATE TABLE IF NOT EXISTS requests (
  id INTEGER PRIMARY KEY,
  created TEXT NOT NULL,
  name TEXT, email TEXT, company TEXT, use_case TEXT, client TEXT,
  consent INTEGER NOT NULL DEFAULT 0,
  ip_hash TEXT, user_agent TEXT,
  honeypot INTEGER NOT NULL DEFAULT 0,
  status TEXT NOT NULL DEFAULT 'pending',
  decision TEXT, decided TEXT, decided_by TEXT,
  key_id INTEGER, delivery TEXT, delivered TEXT, notes TEXT
);
CREATE INDEX IF NOT EXISTS requests_status ON requests(status);
"""


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()


def today() -> str:
    return dt.date.today().isoformat()


def db_path() -> Optional[str]:
    p = os.environ.get(DB_ENV, "").strip()
    return p or None


def connect(path: Optional[str] = None) -> sqlite3.Connection:
    path = path or db_path()
    if not path:
        raise RuntimeError("%s is not set; the key store has no location" % DB_ENV)
    os.makedirs(os.path.dirname(os.path.abspath(path)) or ".", exist_ok=True)
    conn = sqlite3.connect(path, timeout=5, isolation_level=None, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA busy_timeout=5000")
    return conn


def init(path: Optional[str] = None) -> sqlite3.Connection:
    conn = connect(path)
    conn.executescript(SCHEMA)
    return conn


def hash_key(plaintext: str) -> str:
    return hashlib.sha256(plaintext.encode("utf-8")).hexdigest()


def looks_like_key(s: str) -> bool:
    return bool(s) and s.startswith(KEY_PREFIX) and 20 <= len(s) <= 80 and all(c.isalnum() or c in "-_" for c in s[len(KEY_PREFIX):])


def issue(conn: sqlite3.Connection, name: str, email: str, org: str = "", note: str = "",
          issued_by: str = "operator", request_id: Optional[int] = None) -> tuple[str, sqlite3.Row]:
    """Create a key. Returns (plaintext, row). The plaintext is never stored."""
    plaintext = KEY_PREFIX + secrets.token_urlsafe(24)
    cur = conn.execute(
        "INSERT INTO keys (prefix, key_hash, name, email, org, note, created, issued_by, request_id) VALUES (?,?,?,?,?,?,?,?,?)",
        (plaintext[:13], hash_key(plaintext), name.strip(), email.strip().lower(), org.strip(), note.strip(), now(), issued_by, request_id),
    )
    row = conn.execute("SELECT * FROM keys WHERE id=?", (cur.lastrowid,)).fetchone()
    return plaintext, row


def verify(conn: sqlite3.Connection, plaintext: str) -> Optional[sqlite3.Row]:
    if not looks_like_key(plaintext):
        return None
    row = conn.execute("SELECT * FROM keys WHERE key_hash=? AND status='active'", (hash_key(plaintext),)).fetchone()
    return row


def record_use(conn: sqlite3.Connection, key_id: int) -> None:
    d = today()
    conn.execute("UPDATE keys SET calls=calls+1, last_used=? WHERE id=?", (d, key_id))
    conn.execute("INSERT INTO usage (key_id, day, calls) VALUES (?,?,1) ON CONFLICT(key_id, day) DO UPDATE SET calls=calls+1", (key_id, d))


def revoke(conn: sqlite3.Connection, prefix_or_id: str, by: str = "operator") -> int:
    if prefix_or_id.isdigit():
        cur = conn.execute("UPDATE keys SET status='revoked', revoked=?, note=note || ' | revoked by ' || ? WHERE id=? AND status='active'", (now(), by, int(prefix_or_id)))
    else:
        cur = conn.execute("UPDATE keys SET status='revoked', revoked=?, note=note || ' | revoked by ' || ? WHERE prefix=? AND status='active'", (now(), by, prefix_or_id[:13]))
    return cur.rowcount


def list_keys(conn: sqlite3.Connection, status: Optional[str] = None) -> list[sqlite3.Row]:
    if status:
        return conn.execute("SELECT * FROM keys WHERE status=? ORDER BY id", (status,)).fetchall()
    return conn.execute("SELECT * FROM keys ORDER BY id").fetchall()


def add_request(conn: sqlite3.Connection, name: str, email: str, company: str, use_case: str, client: str,
                consent: bool, ip_hash: str, user_agent: str, honeypot: bool) -> int:
    cur = conn.execute(
        "INSERT INTO requests (created, name, email, company, use_case, client, consent, ip_hash, user_agent, honeypot, status) VALUES (?,?,?,?,?,?,?,?,?,?,?)",
        (now(), name[:200], email[:200].lower(), company[:200], use_case[:2000], client[:60], 1 if consent else 0, ip_hash, user_agent[:300],
         1 if honeypot else 0, "spam" if honeypot else "pending"),
    )
    return int(cur.lastrowid)


def recent_request_count(conn: sqlite3.Connection, ip_hash: str, hours: int = 1) -> int:
    since = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(hours=hours)).replace(microsecond=0).isoformat()
    return int(conn.execute("SELECT COUNT(*) FROM requests WHERE ip_hash=? AND created>=?", (ip_hash, since)).fetchone()[0])


def pending_requests(conn: sqlite3.Connection) -> list[sqlite3.Row]:
    return conn.execute("SELECT * FROM requests WHERE status='pending' ORDER BY id").fetchall()


def requests_by_status(conn: sqlite3.Connection, status: str) -> list[sqlite3.Row]:
    return conn.execute("SELECT * FROM requests WHERE status=? ORDER BY id", (status,)).fetchall()


def approve_request(conn: sqlite3.Connection, request_id: int, by: str, note: str = "") -> tuple[str, sqlite3.Row, sqlite3.Row]:
    req = conn.execute("SELECT * FROM requests WHERE id=?", (request_id,)).fetchone()
    if not req:
        raise KeyError("no request %d" % request_id)
    if req["status"] not in ("pending", "needs-drew"):
        raise ValueError("request %d is %s, not open" % (request_id, req["status"]))
    plaintext, key = issue(conn, req["name"] or "", req["email"] or "", req["company"] or "",
                           note or ("request %d: %s" % (request_id, (req["use_case"] or "")[:120])), issued_by=by, request_id=request_id)
    conn.execute("UPDATE requests SET status='approved', decision='approved', decided=?, decided_by=?, key_id=? WHERE id=?", (now(), by, key["id"], request_id))
    return plaintext, key, conn.execute("SELECT * FROM requests WHERE id=?", (request_id,)).fetchone()


def deny_request(conn: sqlite3.Connection, request_id: int, by: str, reason: str) -> None:
    conn.execute("UPDATE requests SET status='denied', decision=?, decided=?, decided_by=? WHERE id=? AND status IN ('pending','needs-drew')",
                 ("denied: " + reason, now(), by, request_id))


def hold_request(conn: sqlite3.Connection, request_id: int, reason: str) -> None:
    conn.execute("UPDATE requests SET status='needs-drew', notes=? WHERE id=? AND status='pending'", (reason, request_id))


def mark_delivery(conn: sqlite3.Connection, request_id: int, how: str) -> None:
    conn.execute("UPDATE requests SET delivery=?, delivered=? WHERE id=?", (how, now(), request_id))


def stats(conn: sqlite3.Connection) -> dict[str, Any]:
    q = lambda sql, *a: conn.execute(sql, a).fetchone()[0]  # noqa: E731
    d = today()
    return {
        "date": d,
        "keys_active": q("SELECT COUNT(*) FROM keys WHERE status='active'"),
        "keys_revoked": q("SELECT COUNT(*) FROM keys WHERE status='revoked'"),
        "calls_total": q("SELECT COALESCE(SUM(calls),0) FROM keys"),
        "calls_today": q("SELECT COALESCE(SUM(calls),0) FROM usage WHERE day=?", d),
        "keys_used_today": q("SELECT COUNT(*) FROM usage WHERE day=? AND calls>0", d),
        "requests_pending": q("SELECT COUNT(*) FROM requests WHERE status='pending'"),
        "requests_needs_drew": q("SELECT COUNT(*) FROM requests WHERE status='needs-drew'"),
        "requests_approved": q("SELECT COUNT(*) FROM requests WHERE status='approved'"),
        "requests_denied": q("SELECT COUNT(*) FROM requests WHERE status='denied'"),
        "requests_spam": q("SELECT COUNT(*) FROM requests WHERE status='spam'"),
    }


def _print_rows(rows: list[sqlite3.Row], cols: list[str]) -> None:
    for r in rows:
        print("  " + " | ".join("%s=%s" % (c, r[c]) for c in cols if c in r.keys()))


def main(argv: Optional[list[str]] = None) -> int:
    ap = argparse.ArgumentParser(prog="gtm-mcp-directory keys", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--db", default=None, help="SQLite path; default $%s" % DB_ENV)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("init")
    p = sub.add_parser("issue"); p.add_argument("--name", required=True); p.add_argument("--email", required=True); p.add_argument("--org", default=""); p.add_argument("--note", default=""); p.add_argument("--by", default="operator")
    p = sub.add_parser("revoke"); p.add_argument("prefix_or_id"); p.add_argument("--by", default="operator")
    p = sub.add_parser("list"); p.add_argument("--status", default=None)
    p = sub.add_parser("requests"); p.add_argument("--status", default="pending")
    p = sub.add_parser("approve"); p.add_argument("request_id", type=int); p.add_argument("--by", default="operator"); p.add_argument("--note", default="")
    p = sub.add_parser("deny"); p.add_argument("request_id", type=int); p.add_argument("--reason", required=True); p.add_argument("--by", default="operator")
    sub.add_parser("stats")
    a = ap.parse_args(argv)
    conn = init(a.db) if a.cmd == "init" else connect(a.db)
    if a.cmd == "init":
        print("key store ready at %s" % (a.db or db_path()))
    elif a.cmd == "issue":
        plaintext, row = issue(conn, a.name, a.email, a.org, a.note, a.by)
        print("issued key id=%d prefix=%s for %s <%s>. Shown once:" % (row["id"], row["prefix"], row["name"], row["email"]))
        print(plaintext)
    elif a.cmd == "revoke":
        n = revoke(conn, a.prefix_or_id, a.by)
        print("revoked %d key(s)" % n)
    elif a.cmd == "list":
        rows = list_keys(conn, a.status)
        print("%d key(s) on %s" % (len(rows), today()))
        _print_rows(rows, ["id", "prefix", "status", "name", "email", "org", "created", "last_used", "calls"])
    elif a.cmd == "requests":
        rows = requests_by_status(conn, a.status)
        print("%d request(s) with status %s on %s" % (len(rows), a.status, today()))
        _print_rows(rows, ["id", "created", "name", "email", "company", "client", "status", "notes", "use_case"])
    elif a.cmd == "approve":
        plaintext, key, req = approve_request(conn, a.request_id, a.by, a.note)
        print("approved request %d: key id=%d prefix=%s for %s <%s>. Shown once:" % (req["id"], key["id"], key["prefix"], key["name"], key["email"]))
        print(plaintext)
    elif a.cmd == "deny":
        deny_request(conn, a.request_id, a.by, a.reason)
        print("denied request %d" % a.request_id)
    elif a.cmd == "stats":
        for k, v in stats(conn).items():
            print("  %s: %s" % (k, v))
    return 0


if __name__ == "__main__":
    sys.exit(main())
