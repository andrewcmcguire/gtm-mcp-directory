# Intercom (Fin): MCP server status, API access gate and what it does

> Customer service/helpdesk platform whose "Fin" AI agent resolves support and pre-sales chat conversations... Official MCP, Paid, self-serve. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Inbound & PLG Chat](../categories/inbound-plg-chat.md) /
Intercom (Fin)

# Intercom (Fin)

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Inbound & PLG Chat](../categories/inbound-plg-chat.md)
RESEARCHED
Checked 2026-08-24
CLI: fin

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [intercom.com](https://intercom.com) · entry id 14-intercom · source 14-inbound-plg-chat.md line 46

**What it does**
Customer service/helpdesk platform whose "Fin" AI agent resolves support and pre-sales chat conversations autonomously across a website widget, email, and other channels.

**AI features, separated from automation with an AI label on it**
Fin is a genuine LLM-based conversational agent (originally built on OpenAI GPT-4, moved to Anthropic Claude for "Fin 2" in 2024) that can both answer questions and take actions on a customer's behalf. "Fin Apex 1.0" (March 2026) is described as a purpose-built, post-trained model for customer support, and "Fin Operator" (May 2026) is an agent that monitors and improves Fin's own performance - sourced from Wikipedia's company history rather than vendor copy alone, so more substantiated than most AI claims in this category, though still worth a second source.

**RevOps role**
Inbound support-and-sales chat system of record, one of the more technically credible "AI agent" implementations in this category with a real, documented MCP server.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth (browser-based, recommended) or a Bearer token using an Intercom API token; Streamable HTTP transport, 13 exposed tools covering conversations, contacts, companies, and Help Center articles.

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: answered, asking for a key
- **Endpoint URL**: [https://mcp.intercom.com/mcp](https://mcp.intercom.com/mcp)
- **Probed**: 2026-09-04, HTTP 401

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL answered an MCP initialize as a server, which is liveness and nothing more: nobody has run its tools.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.intercom.com/mcp (EU: https://mcp.eu.intercom.com/mcp); listing: https://www.pulsemcp.com/servers/intercom

- [https://mcp.intercom.com/mcp](https://mcp.intercom.com/mcp)
- [https://mcp.eu.intercom.com/mcp](https://mcp.eu.intercom.com/mcp)
- [https://www.pulsemcp.com/servers/intercom](https://www.pulsemcp.com/servers/intercom)

**What this server exposes**

Not harvested yet. Unmeasured, not empty: nobody has read this server's tool list, so this page says nothing about what it exposes.

120 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 105 are unmeasured, which is not the same as empty. Harvest last run 2026-09-11. The full roll up is on the [tools index](../tools-index.md).

**Command line**

- **Binary**: fin
- **Status**: official CLI, first party
- **Strongest evidence**: npm
- **Harvested**: 2026-09-11

Install, as the source shows it:

```
npm install -g @intercom/cli
```

quoted from [https://www.npmjs.com/package/@intercom/cli](https://www.npmjs.com/package/@intercom/cli) on 2026-09-11, via npm

Packages seen, with the version on 2026-09-11:

- [npm: @intercom/cli 0.13.0](https://www.npmjs.com/package/@intercom/cli)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-11.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid - API/MCP access requires an Intercom account; specific plan-level gating for API access specifically was not confirmed in the sources reviewed.

**API documentation**

No documentation URL recorded.

328 of 374 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

[github.com/intercom](https://github.com/intercom) tied to the vendor by rule 3, account website https://www.intercom.com has the vendor's domain, confidence strong

- **Public repositories**: 30, forks excluded, as read on 2026-09-08
- **Mention MCP**: 1 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [intercom-react-native](https://github.com/intercom/intercom-react-native) | SDK | React Native wrapper to bridge our iOS and Android SDK | 167 | 2026-09-08 | 10.7.0 |
| [Intercom-OpenAPI](https://github.com/intercom/Intercom-OpenAPI) | API client | An OpenAPI description for Intercom's REST API | 15 | 2026-09-08 | |
| [intercom-android](https://github.com/intercom/intercom-android) | SDK | Intercom for Android, for integrating Intercom into your Android application. | 289 | 2026-09-04 | 18.9.3 |
| [intercom-ios-sp](https://github.com/intercom/intercom-ios-sp) | SDK | The Official Swift Package for Intercom's iOS SDK | 9 | 2026-09-04 | 19.8.1 |
| [intercom-ios](https://github.com/intercom/intercom-ios) | SDK | :iphone: Intercom for iOS, for integrating Intercom into your iOS application. | 386 | 2026-09-04 | 19.8.1 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Answer an inbound chat or call](../jobs/answer-inbound-chat.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 374 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.intercom.com](https://www.intercom.com)
- [https://en.wikipedia.org/wiki/Intercom_(company](https://en.wikipedia.org/wiki/Intercom_(company)
- [https://developers.intercom.com/docs/guides/mcp](https://developers.intercom.com/docs/guides/mcp)
- [https://www.pulsemcp.com/servers/intercom](https://www.pulsemcp.com/servers/intercom)
- [https://fin.ai](https://fin.ai)

5 source URLs. Raw sources field, verbatim:

https://www.intercom.com, https://en.wikipedia.org/wiki/Intercom_(company), https://developers.intercom.com/docs/guides/mcp, https://www.pulsemcp.com/servers/intercom, https://fin.ai

**Notes, verbatim from the file**
STATUS FLAG - corporate identity is in flux and needs a second source. Per Wikipedia, Intercom Inc. formally renamed itself "Fin" in May 2026, and in June 2026 agreed to be acquired by Salesforce for roughly $3.6B (deal expected to close Q4 of Salesforce's FY2027) - this was sourced from a single tertiary reference in this pass and was not independently corroborated via a press release, so treat the acquisition specifics as unconfirmed pending a direct check. Consumer-facing branding (intercom.com, fin.ai) still presents "Intercom" as the helpdesk and "Fin" as its AI agent as of this research date, not yet reflecting a full rename.

**Provenance**

- **Entry id**: 14-intercom

- **Source file**: 14-inbound-plg-chat.md

- **Source line**: 46

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
