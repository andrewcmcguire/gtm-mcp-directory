# Resend: MCP server status, API access gate and what it does

> The best way to reach humans instead of spam folders. Deliver transactional and marketing emails at scale. Community MCP, Gate unknown. Checked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Email Deliverability](../categories/email-deliverability.md) /
Resend

# Resend

[Community MCP](../mcp/community.md)
[Gate unknown](../gates/unknown.md)
[Email Deliverability](../categories/email-deliverability.md)
RESEARCHED
Checked 2026-09-12
CLI: resend

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [resend.com](https://resend.com) · entry id 09-resend · source 09-email-deliverability.md line 638

**What it does**
The best way to reach humans instead of spam folders. Deliver transactional and marketing emails at scale.

**AI features, separated from automation with an AI label on it**
Homepage copy mentions AI/ML-related terms; specific AI feature list not independently verified beyond that mention this pass. See sources.

**RevOps role**
MCP server/client or agent-tooling infrastructure

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: not recorded

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: not probed yet

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established on 2026-09-12 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://registry.smithery.ai/servers?page=1&pageSize=100&q=crm

- [https://registry.smithery.ai/servers?page=1&pageSize=100&q=crm](https://registry.smithery.ai/servers?page=1&pageSize=100&q=crm)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

140 of the 741 entries that record an official or community MCP server carry a harvested tool list. The other 601 are unmeasured, which is not the same as empty. Harvest last run 2026-09-18. The full roll up is on the [tools index](../tools-index.md).

**Command line**

- **Binary**: resend
- **Status**: official CLI, first party
- **Strongest evidence**: vendor-docs
- **Harvested**: 2026-09-18

Install, as the source shows it:

```
npm install -g resend-cli
```

quoted from [https://resend.com/docs/cli](https://resend.com/docs/cli) on 2026-09-18, via npm

```
brew install resend/cli/resend
```

quoted from [https://resend.com/docs/cli](https://resend.com/docs/cli) on 2026-09-18, via brew

```
curl -fsSL https://resend.com/install.sh | bash
```

quoted from [https://resend.com/docs/cli](https://resend.com/docs/cli) on 2026-09-18, via shell

Login or key hint seen on the page:

resend login

22 subcommands seen with the binary in the docs or README:
expand to read them

api-keys, auth, automations, broadcasts, completion, contact-properties, contacts, doctor, domains, emails, events, login, logout, logs, open, segments, suppressions, templates, topics, update, webhooks, whoami

Packages seen, with the version on 2026-09-18:

- [npm: resend-cli 2.21.1, third party](https://www.npmjs.com/package/resend-cli)
- [pypi: resend 2.47.0, third party](https://pypi.org/project/resend/)

Where it was documented:

- [https://resend.com/docs/cli](https://resend.com/docs/cli) (the page that documented the CLI)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-18.

**Access gate**

- **Gate bucket**: Gate unknown

- **Can a solo operator reach it**: Not established

api_gate, verbatim from the file:

unknown

949 of 1252 entries carry an unknown gate. Unknown is a legal answer and it ships as unknown rather than as a guess.

**API documentation**

[https://resend.com/docs/introduction](https://resend.com/docs/introduction)

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

No GitHub organisation could be tied to resend.com with evidence on 2026-09-15.

Recorded by the harvest: not checked: gh CLI missing or not logged in.

**Jobs it can do**

No job tag on this entry.

981 of 1,252 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://resend.com](https://resend.com)
- [https://resend.com/docs/introduction](https://resend.com/docs/introduction)
- [https://resend.com/llms.txt](https://resend.com/llms.txt)
- [https://registry.smithery.ai/servers?page=1&pageSize=100&q=crm](https://registry.smithery.ai/servers?page=1&pageSize=100&q=crm)

4 source URLs. Raw sources field, verbatim:

https://resend.com, https://resend.com/docs/introduction, https://resend.com/llms.txt, https://registry.smithery.ai/servers?page=1&pageSize=100&q=crm

**Notes, verbatim from the file**
API mentioned on https://resend.com/llms.txt; pricing/gate not inferred from presence alone. mcp_status=community from smithery listing; not an invented official vendor MCP. mcp_url is the registry/listing or product MCP URL from staging. api_gate unknown with dated probe 2026-09-12; free/paid not inferred from HTTP status alone. Promote wave U 2026-09-12.

**Provenance**

- **Entry id**: 09-resend

- **Source file**: 09-email-deliverability.md

- **Source line**: 638

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-12

- **Data baked**: 2026-09-18

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
