# AnchoredIP: MCP server status, API access gate and what it does

> Dedicated static outbound IPv4 over WireGuard. Free 7-day trial, no card, no sales call. Community MCP, Gate unknown. Checked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Email Deliverability](../categories/email-deliverability.md) /
AnchoredIP

# AnchoredIP

[Community MCP](../mcp/community.md)
[Gate unknown](../gates/unknown.md)
[Email Deliverability](../categories/email-deliverability.md)
RESEARCHED
Checked 2026-09-12

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [https://api.anchoredip.com/api/mcp](https://api.anchoredip.com/api/mcp) · entry id 09-anchoredip · source 09-email-deliverability.md line 594

**What it does**
Dedicated static outbound IPv4 over WireGuard. Free 7-day trial, no card, no sales call.

**AI features, separated from automation with an AI label on it**
Not evidenced from fetched pages this pass; no AI feature claims recorded without a source URL.

**RevOps role**
Outbound engagement or dialer/sequencing layer used by sales teams

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: not recorded

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: not probed yet

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established on 2026-09-12 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://api.anchoredip.com/api/mcp

- [https://api.anchoredip.com/api/mcp](https://api.anchoredip.com/api/mcp)

**What this server exposes**

- **Tools named**: 8
- **Strongest evidence**: answered tools/list
- **Harvested**: 2026-09-18
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **create_tunnel** Provision a peer and return its WireGuard configuration. Three routing modes, and the right one depends on the machine. source (the default) sends only traffic from the leased address through us and leaves the default route alone - but it evidence: answered tools/list · calling it reads · required: access_token

- **lease_status** Everything about one lease: whether it is active, which addresses it holds, its tunnels and when it renews. evidence: answered tools/list · calling it reads · required: access_token

- **list_plans** The published catalogue with live prices and which payment methods each plan accepts. Prices are never hardcoded; read them here. evidence: answered tools/list · calling it spends money

- **order_lease** Place an order. The trial plan is free and activates immediately; paid plans return payment details and stay pending until settled. No account or card is needed to order. A second trial for the same billing email is refused - order a paid... evidence: answered tools/list · calling it spends money · required: plan, organization_name, country, billing_email

- **renew_lease** Raise an invoice for another term and keep the same addresses. This is how a trial becomes a paying customer: the address does not change, so whatever the customer's partner has already allowlisted goes on working. A trial cannot renew into evidence: answered tools/list · calling it reads · required: access_token

- **revoke_tunnel** Retire a peer and hand its slot back to the plan's allowance. An agent that provisions a tunnel per short-lived worker and never revokes one exhausts the allowance and then cannot bring the next machine up. Revoking the peer that holds the evidence: answered tools/list · calling it reads · required: access_token, tunnel_id

- **set_autorenew** Stop this lease charging the customer's card again, or start it again. Only a card subscription can be stopped - a bank transfer is a payment the customer sends us, so there is nothing of ours to cancel. Stopping is not a cancellation: the evidence: answered tools/list · calling it spends money · required: access_token, enabled

- **set_reverse_dns** Publish a PTR record for an address on the lease. Live within a second; an empty hostname removes it. evidence: answered tools/list · calling it reads · required: access_token, address, hostname

140 of the 741 entries that record an official or community MCP server carry a harvested tool list. The other 601 are unmeasured, which is not the same as empty. Harvest last run 2026-09-18. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-18 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Gate unknown

- **Can a solo operator reach it**: Not established

api_gate, verbatim from the file:

unknown

949 of 1252 entries carry an unknown gate. Unknown is a legal answer and it ships as unknown rather than as a guess.

**API documentation**

[https://api.anchoredip.com/api/](https://api.anchoredip.com/api/)

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

No GitHub organisation could be tied to api.anchoredip.com with evidence on 2026-09-15.

Recorded by the harvest: not checked: gh CLI missing or not logged in.

**Jobs it can do**

No job tag on this entry.

981 of 1,252 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://api.anchoredip.com/api/](https://api.anchoredip.com/api/)
- [https://api.anchoredip.com/llms.txt](https://api.anchoredip.com/llms.txt)
- [https://api.anchoredip.com/api/mcp](https://api.anchoredip.com/api/mcp)

3 source URLs. Raw sources field, verbatim:

https://api.anchoredip.com/api/, https://api.anchoredip.com/llms.txt, https://api.anchoredip.com/api/mcp

**Notes, verbatim from the file**
Homepage fetch failed (HTTPError 405); what_it_does used staging desc. API mentioned on https://api.anchoredip.com/api/; pricing/gate not inferred from presence alone. API mentioned on https://api.anchoredip.com/llms.txt; pricing/gate not inferred from presence alone. mcp_status=community from official-mcp-registry listing; not an invented official vendor MCP. mcp_url is the registry/listing or product MCP URL from staging. api_gate unknown with dated probe 2026-09-12; free/paid not inferred from HTTP status alone. Promote wave P 2026-09-12.

**Provenance**

- **Entry id**: 09-anchoredip

- **Source file**: 09-email-deliverability.md

- **Source line**: 594

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-12

- **Data baked**: 2026-09-21

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
