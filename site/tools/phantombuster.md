# PhantomBuster: MCP server status, API access gate and what it does

> General browser-automation/data-extraction platform ("Phantoms") that runs cloud scripts to scrape and act on... Official MCP, Paid, self-serve. Checked 2026-09-03.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Engagement & Outbound](../categories/engagement-outbound.md) /
PhantomBuster

# PhantomBuster

[Official MCP](../mcp/official.md)
[Paid, self-serve](../gates/paid.md)
[Engagement & Outbound](../categories/engagement-outbound.md)
RESEARCHED
Checked 2026-09-03
CLI: phantombuster (community)

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [phantombuster.com](https://phantombuster.com) · entry id 02-phantombuster · source 02-engagement-outbound.md line 407

**What it does**
General browser-automation/data-extraction platform ("Phantoms") that runs cloud scripts to scrape and act on LinkedIn and other web platforms - widely used as a LinkedIn outbound backbone rather than a purpose-built sequencer.

**AI features, separated from automation with an AI label on it**
Vendor-stated AI add-ons: an "AI LinkedIn Message Writer" (GPT-based drafting), an "AI LinkedIn Profile Enricher" (structures scraped data), and an "AI LinkedIn Post Responder" (comment suggestions) - metered AI-credit features layered on a core scraping/automation engine that is itself not AI.

**RevOps role**
Data-extraction/scraping and light-automation backbone many other engagement tools (and Clay) sit on top of; general-purpose rather than LinkedIn-native.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth - first connection redirects to PhantomBuster sign-in/authorization, then workspace selection.

- **Parsed URLs**: 2 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://hub.phantombuster.com/docs/mcp-server](https://hub.phantombuster.com/docs/mcp-server)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-03. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://hub.phantombuster.com/docs/mcp-server (hosted at mcp.phantombuster.com); community alternative at https://github.com/globodai-group/mcp-phantombuster

- [https://hub.phantombuster.com/docs/mcp-server](https://hub.phantombuster.com/docs/mcp-server)
- [https://github.com/globodai-group/mcp-phantombuster](https://github.com/globodai-group/mcp-phantombuster)

**What this server exposes**

- **Tools named**: 9
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-13
- **Repo read**: globodai-group/mcp-phantombuster
- **Whose repo**: third-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

This list came from a repo the vendor does not own. Those are that author's tools for the vendor's API, not the vendor's own published surface, and the two must not be read as the same thing.

- **phantombuster_delete_agent** Delete a PhantomBuster agent permanently evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **phantombuster_get_agent** Get details of a specific PhantomBuster agent by ID evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **phantombuster_get_agent_output** Get the console output of the most recent container of a PhantomBuster agent. Useful for monitoring execution progress and debugging. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **phantombuster_get_container** Get details of a specific container (execution run) by ID evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **phantombuster_get_container_result** Get the result object (structured data output) from a specific container execution evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **phantombuster_launch_agent** Launch a PhantomBuster agent. Adds it to the launch queue. Optionally pass arguments to override the agent evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **phantombuster_list_agents** List all PhantomBuster agents (phantoms) in your organization evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **phantombuster_list_containers** List all containers (execution runs) for a specific PhantomBuster agent evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **phantombuster_stop_agent** Stop a running PhantomBuster agent evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

121 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 104 are unmeasured, which is not the same as empty. Harvest last run 2026-09-13. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

This is a third party's CLI. It was published by somebody other than the vendor, so it is that author's surface for the vendor's API and not the vendor's published surface. The two must not be read as the same thing.

- **Binary**: phantombuster
- **Status**: community CLI, third party
- **Strongest evidence**: pypi
- **Harvested**: 2026-09-13

Install, as the source shows it:

```
pip install phantombuster
```

quoted from [https://pypi.org/project/phantombuster/](https://pypi.org/project/phantombuster/) on 2026-09-13, via pypi, a third party source

Packages seen, with the version on 2026-09-13:

- [pypi: phantombuster 0.20.5, third party](https://pypi.org/project/phantombuster/)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-13.

**Access gate**

- **Gate bucket**: Paid, self-serve

- **Can a solo operator reach it**: Yes, by paying, no sales call

api_gate, verbatim from the file:

paid

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/globodai-group/mcp-phantombuster](https://github.com/globodai-group/mcp-phantombuster)

**On GitHub**

[github.com/phantombuster](https://github.com/phantombuster) tied to the vendor by rule 3, account website https://phantombuster.com has the vendor's domain, confidence strong

- **Public repositories**: 13, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-09-08

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [public-gists](https://github.com/phantombuster/public-gists) | other | Because you can't create gists as a GitHub org | 2 | 2026-09-08 | |
| [.github](https://github.com/phantombuster/.github) | other | Special repository for default files available throughout the organization. | 1 | 2025-12-03 | |
| [sdk](https://github.com/phantombuster/sdk) | SDK | Phantombuster's SDK | 15 | 2024-10-16 | |
| [dyn53](https://github.com/phantombuster/dyn53) | other | A Lambda that updates a Route53 A record with the requester's IP address | 2 | 2021-11-16 | |
| [nickjs](https://github.com/phantombuster/nickjs) | other | Web scraping library made by the Phantombuster team. Modern, simple & works on all websites. (Deprecated) | 495 | 2020-06-19 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Enrich a person from a LinkedIn URL](../jobs/enrich-person-from-linkedin-url.md)
- [Find a person's LinkedIn URL from a name and company](../jobs/find-linkedin-url-from-name-and-company.md)
- [Scrape a web page for facts](../jobs/scrape-web-page-for-facts.md)
- [Send a LinkedIn message or connection request](../jobs/send-linkedin-message.md)
- [Draft personalized outreach](../jobs/draft-personalized-outreach.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 336 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://hub.phantombuster.com/docs/mcp-server](https://hub.phantombuster.com/docs/mcp-server)
- [https://lagrowthmachine.com/phantombuster-pricing/](https://lagrowthmachine.com/phantombuster-pricing/)
- [https://github.com/globodai-group/mcp-phantombuster](https://github.com/globodai-group/mcp-phantombuster)
- [https://phantombuster.com/automations/linkedin/4015/linkedin-profile-url-finder](https://phantombuster.com/automations/linkedin/4015/linkedin-profile-url-finder)
- [https://support.phantombuster.com/hc/en-us/articles/26971028103826-How-to-Use-the-LinkedIn-Profile-URL-Finder](https://support.phantombuster.com/hc/en-us/articles/26971028103826-How-to-Use-the-LinkedIn-Profile-URL-Finder)

5 source URLs. Raw sources field, verbatim:

https://hub.phantombuster.com/docs/mcp-server, https://lagrowthmachine.com/phantombuster-pricing/, https://github.com/globodai-group/mcp-phantombuster, https://phantombuster.com/automations/linkedin/4015/linkedin-profile-url-finder, https://support.phantombuster.com/hc/en-us/articles/26971028103826-How-to-Use-the-LinkedIn-Profile-URL-Finder

**Notes, verbatim from the file**
Documented REST API available starting on the entry paid plan (~$56/mo Starter, 20 execution hours/mo); no enterprise-only gate found. Because it operates via scraping/headless browser automation, it sits squarely inside activity LinkedIn's User Agreement prohibits. 2026-09-03: PhantomBuster's catalog lists a Phantom titled "LinkedIn Profile URL Finder" (https://phantombuster.com/automations/linkedin/4015/linkedin-profile-url-finder) with a support article "How to Use the LinkedIn Profile URL Finder" (https://support.phantombuster.com/hc/en-us/articles/26971028103826-How-to-Use-the-LinkedIn-Profile-URL-Finder); both pages are client-rendered and did not render for the fetcher, and the search index's rendering of them says the Phantom takes first and last name (or a full name) plus a company name or professional email and returns LinkedIn profile URLs at one URL finder credit per lookup; the MCP docs do not name it as a tool.

**Provenance**

- **Entry id**: 02-phantombuster

- **Source file**: 02-engagement-outbound.md

- **Source line**: 407

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-03

- **Data baked**: 2026-09-13

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
