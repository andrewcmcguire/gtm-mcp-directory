# Which GTM jobs have no official MCP server at all? The gaps, counted

> Of 55 jobs in the vocabulary, 2 have no tool at all with a first party MCP server. The gaps in the map, and the thinly covered jobs next to them. Counted 2026-08-28.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Learn](index.md) / What the data says

**What the data says**

# Which GTM jobs can no tool do through an official MCP server?

**The short answer**

Of the 55 jobs in this directory's closed vocabulary, 2 have no tool with an official MCP server at all. These are the holes an agent builder falls into: the capability exists in the market, and nothing exposes it through a vendor maintained server.

## Jobs with zero official servers

| Job | Tools tagged | Community | Solo reachable |
|---|---|---|---|
| [run a sales roleplay practice](../jobs/run-sales-roleplay-practice.md) | 11 | 0 | 0 |
| [reverse-look-up a person from an email](../jobs/reverse-lookup-person-from-email.md) | 1 | 1 | 1 |

Counted 2026-08-28 from the per job blocks in directory.json.

## The thinnest jobs in the vocabulary

Separately from the zero official list, some jobs are barely covered by any tool at all. These are the ones where the vocabulary describes something real and the market has almost nothing tagged against it.

| Job | Entries tagged | Official |
|---|---|---|
| [reverse-look-up a person from an email](../jobs/reverse-lookup-person-from-email.md) | 1 | 0 |
| [query a data warehouse](../jobs/query-data-warehouse.md) | 2 | 2 |
| [read contract terms](../jobs/read-contract-terms.md) | 3 | 3 |
| [draft an rfp or questionnaire response](../jobs/draft-rfp-response.md) | 3 | 2 |
| [discover warm intro paths](../jobs/discover-warm-intro-paths.md) | 4 | 3 |
| [check inbox placement](../jobs/check-inbox-placement.md) | 4 | 1 |
| [scrape job postings](../jobs/scrape-job-postings.md) | 5 | 5 |
| [search across recorded calls](../jobs/search-call-library.md) | 5 | 5 |
| [generate a proposal or quote](../jobs/generate-proposal-or-quote.md) | 5 | 1 |
| [create a digital sales room](../jobs/create-digital-sales-room.md) | 5 | 2 |
| [discover mcp servers](../jobs/discover-mcp-servers.md) | 5 | 1 |

## Read these as leads, not as receipts

> **Machine pass, human review pending** The job tags behind these numbers came from a machine pass over each entry's own description text on 2026-08-25, and 28 entries were flagged by that pass as needing a human to look again. A gap in this table can mean the market has a hole, or it can mean the vocabulary drew a line the tagger read differently. Both are worth checking before anybody builds a business on one.

## Why publish the gaps at all

Because a gap is the most actionable thing in a directory. If you were going to write an MCP server for something, the top of the first table is where an agent builder is currently stuck with no vendor maintained option, and the second table is where the market itself is thin.

## Sources

- [The GTM MCP Directory, by job](../jobs/index.md) this site
- [The GTM MCP Directory, the counted data](../data.md) this site
- [The GTM MCP Directory, methodology](../methodology.md) this site

Every number on this page is generated from directory.json at build time and carries the date it was baked: 2026-08-28. Nothing is typed by hand, nothing is rounded, and nothing is estimated. The underlying data is [published in full](../data.md). Where the honest answer is a zero, the zero is printed.

## Related questions

- [How do I build an MCP server for a tool that does not have one?](how-do-i-build-an-mcp-server-for-a-tool-that-has-none.md)
- [Which GTM tools have no MCP server?](which-gtm-tools-have-no-mcp-server.md)
- [Which GTM tool categories are most usable by AI agents?](which-gtm-categories-are-most-agent-ready.md)
- [How many of these GTM tools have actually been tested?](how-many-gtm-tools-are-bench-tested.md)

## In the directory

- [Every job](../jobs/index.md)
