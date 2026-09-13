# Tavus: MCP server status, API access gate and what it does

> Developer platform for building real-time, two-way conversational AI video agents ("Conversational Video... Official MCP, Free to start. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Video Prospecting](../categories/video-prospecting.md) /
Tavus

# Tavus

[Official MCP](../mcp/official.md)
[Free to start](../gates/free.md)
[Video Prospecting](../categories/video-prospecting.md)
RESEARCHED
Checked 2026-08-24
CLI: tavus-cli (community)

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [tavus.io](https://tavus.io) · entry id 08-tavus · source 08-video-prospecting.md line 128

**What it does**
Developer platform for building real-time, two-way conversational AI video agents ("Conversational Video Interface") - positioned for GTM use cases like greeting website visitors and booking meetings, not primarily batch personalized-outbound video.

**AI features, separated from automation with an AI label on it**
Vendor states AI voice/face replicas ("Replica"), persona-driven real-time conversational agents, and a no-code agent builder ("PAL Maker"). This is a genuine real-time conversational-AI product per vendor's own architecture description (perception, understanding, voice, rendering components), not just a templated video swap - but capability claims are vendor-stated and not independently benchmarked here.

**RevOps role**
Conversational AI-agent layer for GTM (an AI rep that greets/qualifies a site visitor and books a meeting live) rather than a classic async 1:many personalized-outbound-video tool.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: OAuth 2.0 browser-based flow; the exchange mints a per-user API key server-side, nothing stored in client config.

- **Parsed URLs**: 4 found in the mcp_url field

- **Endpoint probe**: answered, asking for a key
- **Endpoint URL**: [https://mcp.tavus.io/mcp](https://mcp.tavus.io/mcp)
- **Probed**: 2026-09-04, HTTP 401

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-08-24. On 2026-09-04 the recorded URL answered an MCP initialize as a server, which is liveness and nothing more: nobody has run its tools.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://mcp.tavus.io/mcp (docs: https://docs.tavus.io/sections/agent-tools/mcp-server.md, https://docs.tavus.io/sections/agent-tools/mcp-tools-reference.md); community alternative at https://github.com/rakeshdavid/Tavus-MCP

- [https://mcp.tavus.io/mcp](https://mcp.tavus.io/mcp)
- [https://docs.tavus.io/sections/agent-tools/mcp-server.md](https://docs.tavus.io/sections/agent-tools/mcp-server.md)
- [https://docs.tavus.io/sections/agent-tools/mcp-tools-reference.md](https://docs.tavus.io/sections/agent-tools/mcp-tools-reference.md)
- [https://github.com/rakeshdavid/Tavus-MCP](https://github.com/rakeshdavid/Tavus-MCP)

**What this server exposes**

- **Tools named**: 29
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-12
- **Repo read**: rakeshdavid/Tavus-MCP
- **Whose repo**: third-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

This list came from a repo the vendor does not own. Those are that author's tools for the vendor's API, not the vendor's own published surface, and the two must not be read as the same thing.

- **create_conversation** Create a new conversational video interface evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_lipsync** Create a lipsync video by synchronizing audio with video evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_persona** Create a new persona for conversational AI evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_replica** Create a new AI replica from a training video evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **delete_conversation** Delete a conversation permanently evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **delete_lipsync** Delete a lipsync permanently evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **delete_persona** Delete a persona permanently evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **delete_replica** Delete a replica permanently evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **delete_speech** Delete a speech permanently evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **delete_video** Delete a video permanently evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **end_conversation** End an active conversation evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **generate_speech** Generate speech audio from text using a replica evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **generate_video** Generate a video using a replica and script or audio evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_conversation** Get details of a specific conversation evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_lipsync** Get details of a specific lipsync evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_persona** Get details of a specific persona evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_replica** Get details of a specific replica evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_speech** Get details of a specific speech evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_video** Get details of a specific video evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_conversations** List all conversations in your account evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_lipsyncs** List all lipsyncs in your account evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_personas** List all personas in your account evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_replicas** List all replicas in your account evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_speeches** List all speeches in your account evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_videos** List all videos in your account evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **patch_persona** Update a persona using JSON patch format evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **rename_replica** Rename an existing replica evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **rename_speech** Rename an existing speech evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **rename_video** Rename an existing video evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

119 of the 437 entries that record an official or community MCP server carry a harvested tool list. The other 318 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

This is a third party's CLI. It was published by somebody other than the vendor, so it is that author's surface for the vendor's API and not the vendor's published surface. The two must not be read as the same thing.

- **Binary**: tavus-cli
- **Status**: community CLI, third party
- **Strongest evidence**: pypi
- **Harvested**: 2026-09-12

Install, as the source shows it:

```
pip install tavus-cli
```

quoted from [https://pypi.org/project/tavus-cli/](https://pypi.org/project/tavus-cli/) on 2026-09-12, via pypi, a third party source

```
pip install tavus
```

quoted from [https://pypi.org/project/tavus/](https://pypi.org/project/tavus/) on 2026-09-12, via pypi, a third party source

Packages seen, with the version on 2026-09-12:

- [pypi: tavus-cli 0.4.3, third party](https://pypi.org/project/tavus-cli/)
- [pypi: tavus 0.4.3, third party](https://pypi.org/project/tavus/)
- [pypi: tavus-cli 0.4.3, third party](https://pypi.org/project/tavus-cli/)

A CLI being listed means the harvest found an install command or a package on a stated date. Nobody has run it. Every command is quoted verbatim from the URL beneath it. Harvest date 2026-09-12.

**Access gate**

- **Gate bucket**: Free to start

- **Can a solo operator reach it**: Yes, without talking to anyone

api_gate, verbatim from the file:

free tier available. Free plan includes 25 minutes of conversational video/month; Starter/solo-developer tier is $59/mo (100 min + 3 custom replicas); Growth $397/mo (1,250 min); Enterprise custom. Overage billed per-minute.

**API documentation**

No documentation URL recorded.

604 of 934 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/rakeshdavid/Tavus-MCP](https://github.com/rakeshdavid/Tavus-MCP)

**On GitHub**

[github.com/Tavus-Engineering](https://github.com/Tavus-Engineering) tied to the vendor by rule 3, account website tavus.io has the vendor's domain, confidence strong

- **Public repositories**: 10, forks excluded, as read on 2026-09-08
- **Mention MCP**: 0 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-09-07

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [tavus-intake](https://github.com/Tavus-Engineering/tavus-intake) | other | | 4 | 2026-09-07 | |
| [tavus-interviewer](https://github.com/Tavus-Engineering/tavus-interviewer) | other | | 3 | 2026-09-07 | |
| [dj_charlie](https://github.com/Tavus-Engineering/dj_charlie) | other | | 1 | 2026-06-23 | |
| [tavus-audio-passthrough-demo](https://github.com/Tavus-Engineering/tavus-audio-passthrough-demo) | docs or examples | | 1 | 2026-04-09 | |
| [tavus-examples](https://github.com/Tavus-Engineering/tavus-examples) | docs or examples | Examples and guides for using Tavus's Conversational Video Interface (CVI) & Video Gen APIs | 86 | 2026-04-06 | |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

- [Book a meeting](../jobs/book-a-meeting.md)
- [Answer an inbound chat or call](../jobs/answer-inbound-chat.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 56 job vocabulary. 271 of 934 entries carry at least one tag; 849 tags are assigned in total.

**Sources**

- [https://www.tavus.io/](https://www.tavus.io/)
- [https://www.tavus.io/pricing](https://www.tavus.io/pricing)
- [https://docs.tavus.io/llms.txt](https://docs.tavus.io/llms.txt)
- [https://docs.tavus.io/sections/agent-tools/mcp-server.md](https://docs.tavus.io/sections/agent-tools/mcp-server.md)
- [https://github.com/rakeshdavid/Tavus-MCP](https://github.com/rakeshdavid/Tavus-MCP)
- [https://coldiq.com/blog/tavus-video-prospecting](https://coldiq.com/blog/tavus-video-prospecting)

6 source URLs. Raw sources field, verbatim:

https://www.tavus.io/, https://www.tavus.io/pricing, https://docs.tavus.io/llms.txt, https://docs.tavus.io/sections/agent-tools/mcp-server.md, https://github.com/rakeshdavid/Tavus-MCP, https://coldiq.com/blog/tavus-video-prospecting

**Notes, verbatim from the file**
Third-party blogs (e.g. ColdIQ) frame Tavus as a "video prospecting" tool via its replica/clone capability, but Tavus's own current marketing emphasizes real-time conversational agents over the "record once, blast personalized clips" model most other entries in this file use - worth noting the mechanism differs from Vidyard/Sendspark/Potion even though the sales use case is real.

**Provenance**

- **Entry id**: 08-tavus

- **Source file**: 08-video-prospecting.md

- **Source line**: 128

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
