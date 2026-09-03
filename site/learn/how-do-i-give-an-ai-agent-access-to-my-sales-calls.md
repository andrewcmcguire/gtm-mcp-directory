# How do I give an AI agent access to sales call transcripts? The routes

> 20 tools here are tagged with fetching a call transcript and 15 have an official MCP server. The routes, and the consent question first.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Learn](index.md) / How to actually do it

**How to actually do it**

# How do I give an AI agent access to my sales calls?

**The short answer**

Most call recording platforms expose transcripts through an API, and 15 of the 20 entries tagged with that job ship an official MCP server. The technical part is straightforward. The consent language you recorded under is the part to settle first.

## Start with consent, not with the API

A transcript contains other people's words, captured under a notice that almost certainly did not mention an autonomous agent retrieving them later. Before you widen who or what can read them, check what your recording notice actually says, what your retention policy is, and whether any of those calls are in jurisdictions with stricter rules. Nothing here is legal advice and this directory records no compliance claims about any tool.

## The three routes

- **The recorder's own MCP server.** Cleanest, and the most common: 15 of the tagged entries have one.

- **The recorder's REST API with a thin wrapper.** Fine, and about an afternoon of work if the API is documented. 30 of 293 entries in this directory record a documentation URL.

- **A proxy platform.** 9 entries are tagged [proxy tool calls to saas apps](../jobs/proxy-tool-calls-to-saas.md). Fastest, and it puts a third party between your agent and your recordings, which for call data is a bigger decision than it is for firmographics.

## The tools an agent can call

- [Fathom](../tools/fathom.md) Official MCP · Free to start
Free AI meeting recorder/notetaker that transcribes calls and generates summaries, action items, and CRM sync.
- [Fireflies.ai](../tools/fireflies-ai.md) Official MCP · Free to start
Records and transcribes meetings and exposes the data through an open GraphQL API and an in-app AI assistant ("AskFred") for summaries, search, and...
- [MeetGeek](../tools/meetgeek.md) Official MCP · Free to start
Automatic meeting recorder and transcriber that produces summaries, highlights and conversation analytics across Zoom, Teams and Meet.
- [Affinity](../tools/affinity.md) Official MCP · Paid, self-serve
A relationship-intelligence CRM for deal teams that auto-builds the contact graph from email and calendar activity and scores relationship strength,...
- [Attention](../tools/attention.md) Official MCP · Paid, self-serve
Captures, transcribes, and analyzes sales and customer conversations, automatically syncing structured insights to the CRM.
- [Avoma](../tools/avoma.md) Official MCP · Paid, self-serve
AI meeting platform combining scheduling, note-taking, and conversation intelligence (deal insights, coaching) for sales teams.
- [Fellow](../tools/fellow.md) Official MCP · Paid, self-serve
A meeting assistant that records, transcribes and summarises calls, then turns them into action items and decisions tied to the calendar event they...
- [Grain](../tools/grain.md) Official MCP · Paid, self-serve
AI meeting notetaker that records and transcribes calls and builds a searchable, cross-meeting library synced to the CRM.
- [Granola](../tools/granola.md) Official MCP · Paid, self-serve
General-purpose AI notetaker that generates enhanced meeting notes and summaries from a local desktop app.
- [tl;dv](../tools/tl-dv.md) Official MCP · Paid, self-serve
Records and transcribes Zoom, Google Meet, and Microsoft Teams calls, layering on sales coaching (playbook monitoring, objection handling) at higher...

8 more are on the linked page. The cut is the display limit, not a ranking.

## What to do with them once you can read them

| Step | The job | Tools tagged | Official MCP | Free tier |
|---|---|---|---|---|
| Fetch the transcript | [fetch a call transcript](../jobs/fetch-call-transcript.md) | 20 | 15 | 3 |
| Search across the library | [search across recorded calls](../jobs/search-call-library.md) | 5 | 5 | 1 |
| Summarize the meeting | [summarize a meeting](../jobs/summarize-meeting.md) | 22 | 17 | 3 |
| Extract deal signals | [extract deal signals from calls](../jobs/extract-deal-signals-from-calls.md) | 21 | 11 | 0 |
| Research the account before the next call | [research an account before a call](../jobs/research-account-for-call-prep.md) | 17 | 10 | 3 |

The read only chain above is the highest value, lowest risk agent work in the whole GTM stack. Nothing in it sends, spends or writes, and the raw material is the most information dense asset a revenue team owns and the least used.

## Sources

- [The GTM MCP Directory, Conversation Intel](../categories/conversation-intel.md) this site
- [The GTM MCP Directory, fetch a call transcript](../jobs/fetch-call-transcript.md) this site

Every number on this page is generated from directory.json at build time and carries the date it was baked: 2026-09-02. Nothing is typed by hand, nothing is rounded, and nothing is estimated. The underlying data is [published in full](../data.md). Where the honest answer is a zero, the zero is printed.

## Related questions

- [Which tools can give an AI agent access to sales call transcripts?](which-tools-can-fetch-a-call-transcript.md)
- [Which conversation intelligence tools have MCP servers?](which-conversation-intel-tools-have-mcp-servers.md)
- [What are the security risks of connecting an AI agent to my GTM stack?](what-are-the-security-risks-of-connecting-an-agent-to-my-gtm-stack.md)
- [Which scheduling tools can an AI agent use to book a meeting?](which-tools-can-book-a-meeting.md)

## In the directory

- [Conversations and meetings](../jobs/family-conversations-and-meetings.md)
- [Conversation Intel](../categories/conversation-intel.md)
