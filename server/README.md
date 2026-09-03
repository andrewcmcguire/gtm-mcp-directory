# The GTM MCP Directory, as an MCP server

<!-- mcp-name: io.github.andrewcmcguire/gtm-mcp-directory -->

Part of **Agent Operator**.

293 go-to-market tools, scored on the one axis nobody else publishes: **can an
agent actually call this, and what does it cost to get in.**

This server is local. It loads a baked JSON directory once at startup and
answers everything from memory. It makes **zero outbound requests**, at
startup or at query time. It cannot be slow, cannot cost anything, cannot
rate-limit you, cannot leak your query to a vendor, and cannot break because a
vendor's site is down. Everything network-shaped happens in the weekly build,
never in your session.

```
> which tools can enrich a person from a LinkedIn profile URL, and which can I
  actually get a key for today?

Resolved to the job enrich-person-from-linkedin-url.

12 tools carry this job. 8 have an official MCP server, 1 community, 3 none
found. On access: 3 free, 7 paid, 2 enterprise-only. 8 are solo-reachable.
None have been bench-tested, and every one of those tags means the vendor
says the tool does this.
```

---

## The honesty model, before anything else

The honesty tier is the product. It is on every single response and it is
never optional.

**Two tiers, and only two.**

| Tier | What it means |
|---|---|
| `RESEARCHED` | Facts from public sources with URLs. No usage claims. Nobody has run this tool. |
| `BENCH-TESTED` | Andrew personally ran it on a stated date. Cannot be bought. |

Right now **all 293 entries are RESEARCHED and 0 are BENCH-TESTED**. That zero
is printed in the stats tool rather than hidden, and it stays zero until
somebody actually runs something and says so with a date.

**A job tag means the vendor says the tool does this.** It is not a test
result, not a benchmark, and not an endorsement. That sentence rides on every
capability answer in the `honesty.job_tag_meaning` and `honesty.jobs_meaning`
fields, the second one quoted verbatim from the build itself so the server and
the data can never say two different things about the same claim. If you take
one thing from this README, take that one.

**Tag provenance is published too.** 271 of the 293 entries carry job tags,
and all 271 were tagged by a machine pass over the entry's own description
text rather than read by a human. Every response says so, and every entry
carries `jobs_tagged_by` and `jobs_tagged_on` so you can see which pass
produced a tag rather than having to assume.

**Unmeasured is not the same as missing.** A field that has never been
measured says so in a sentence. An agent reading `github_stars: null` learns
nothing; an agent reading "no public repo was found for this vendor, and many
GTM SaaS vendors have none" learns the right thing.

**Anything that rots ships with the date it was measured.** `last_checked` is
on every entry and every response. `github_fetched_on` and `docs_last_crawled`
are mandatory the moment the fields they stamp become non-null. An unstamped
number is a lie.

**Ordering is computed, disclosed, and not purchasable.** Every list-shaped
response carries a `sort` field spelling out the exact rule that produced it.
There is no `featured` field and no `recommended` field anywhere in the
schema, because a field that exists is a field somebody will eventually try to
buy.

---

## Install

Nothing to sign up for. No account, no API key, no telemetry.

> **Status note, in the spirit of the rest of this file:** the `uvx` blocks
> below are the shipping shape and they are what the config will say, but the
> package is **not on PyPI yet**. Until it is, use the clone instructions
> further down. This README does not pretend a publish happened.

### Claude Desktop

Edit `claude_desktop_config.json`:

- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "gtm-directory": {
      "command": "uvx",
      "args": ["gtm-mcp-directory"]
    }
  }
}
```

Restart Claude Desktop. The seven tools appear under the tools menu.

### Claude Code

```bash
claude mcp add gtm-directory -- uvx gtm-mcp-directory
```

Or commit a `.mcp.json` at the root of a repo so the whole team gets it:

```json
{
  "mcpServers": {
    "gtm-directory": {
      "command": "uvx",
      "args": ["gtm-mcp-directory"]
    }
  }
}
```

### From a clone (what you want if you are working on the directory itself)

```bash
git clone https://github.com/andrewcmcguire/gtm-mcp-directory
cd gtm-mcp-directory/server
python -m gtm_mcp_directory        # stdio, blocks, speaks MCP
```

Config block for a clone:

```json
{
  "mcpServers": {
    "gtm-directory": {
      "command": "python",
      "args": ["-m", "gtm_mcp_directory"],
      "cwd": "/absolute/path/to/gtm-mcp-directory/server"
    }
  }
}
```

Run from a clone and the server reads the live `data/directory.json` in the
repo. Install from PyPI and it reads the copy baked into the wheel at release
time.

### Requirements

Python 3.10 or newer, `fastmcp`, `pyyaml`. That is the whole dependency list.

---

## The tools

Seven read-only tools. No write tools, no submission tool, no telemetry.

### `find_tools(job_or_query, ...)`

The main one. "Which tools can do X, and can my agent actually reach them."

```python
find_tools(job_or_query="enrich a linkedin profile url", limit=8)
find_tools(category="data-enrichment", mcp_status="official", gate="free")
find_tools(job_or_query="find-work-email", gate="free")
```

| Argument | Values |
|---|---|
| `job_or_query` | a job slug from `list_jobs`, or plain natural language |
| `category` | one of the 15 category slugs |
| `mcp_status` | `official`, `community`, `none-found`, `unknown`, `n-a` |
| `gate` | `free`, `paid`, `enterprise-leaning`, `enterprise-only`, `unknown`, `n-a` |
| `tier` | `RESEARCHED`, `BENCH-TESTED` |
| `has_github` | measured `github_url` only |
| `has_github_candidate` | the unverified lead list parsed out of `mcp_url` and `sources` |
| `canonical_only` | drop the 16 cross-listed second entries |
| `limit` | default 20, max 100 |

**Two match paths, and the response always names the one it used.**

1. **Job tags.** Your query resolves against the 55-job vocabulary (slugs,
   labels, phrasings and aliases). The best match, plus anything within 5
   percent of it, filters the results. Weaker candidates come back in
   `also_considered` so you can re-ask precisely instead of being handed a
   quietly widened answer.
2. **Text search.** If the query resolves to nothing, or resolves to a job no
   entry carries yet, the server falls back to a literal text match over each
   vendor's own description of itself and says so in `query_resolved.fallback`
   and in the honesty caveats. A text match is a weaker claim than a tag and
   is never dressed up as one.

The response always states what your query resolved to and how, in
`query_resolved`. It never returns a silent empty list: a query that resolves
to nothing says so and hands back the vocabulary instead.

Ordering: with a free-text query, relevance first (how many distinct query
terms matched, then a weighted field score), ties broken by the published
display rule. With filters only, the published display rule alone: official
MCP first, then community, then unknown, then n/a, then none-found; within
each band the gate order is free, paid, enterprise-leaning, enterprise-only,
unknown; then alphabetical.

### `get_tool(name)`

One tool's full entry: all 50 fields, every source URL, the honesty envelope,
the docs digest if one exists, and the cross-listing block for the 16 products
that legitimately appear in two categories.

```python
get_tool(name="Lusha")
get_tool(name="clay")
```

Fuzzy-matches the name. On genuine ambiguity it returns the candidates instead
of picking one for you.

### `list_categories()`

The 15 categories with entry counts, official/community/none-found splits,
access gates, solo-reachable counts, and top jobs per category once tagging
has run.

### `whats_mcpd(category=None, job=None)`

The stats tool. The one that gets screenshotted.

```python
whats_mcpd()
whats_mcpd(category="ai-sdr-agents")
whats_mcpd(job="find-work-email")
```

Returns the official/community/none-found/unknown split, the gate breakdown,
`solo_reachable`, `bench_tested`, the most and least MCP-covered categories,
and a headline built from live numbers:

> RevOps Infra is 22 of 23 MCP-reachable. Enablement and Coaching is 2 of 14.
> The tools sold AS agents, the AI SDRs, are 6 of 23. Across all 293 entries,
> 144 have an official MCP server (49.1 percent) and 117 are solo-reachable.

### `find_by_gate(gate, category=None, mcp_status=None, limit=25)`

The access axis on its own. An MCP server you cannot get a key for is not
reachable, whatever the marketing says.

```python
find_by_gate(gate="free")
find_by_gate(gate="enterprise-only", category="forecasting-revenue")
```

Each result carries `api_gate` (the bucket) and `api_gate_raw` (the verbatim
sentence from the research pass). Where a vendor changed its gate the sentence
says so, and the sentence is the truth while the bucket is only the index. An
unrecognised gate returns the closed vocabulary rather than an empty list.

### `get_docs_digest(name)`

Structured facts from a vendor's public API documentation: auth model,
endpoint count, capabilities, rate limits, pricing model, webhooks, SDKs,
OpenAPI spec URL. Never mirrored prose, never a paraphrase of the docs body.

```python
get_docs_digest(name="Anymail Finder")
```

The docs intel layer has not run yet, so today every call returns
`digest: null` with an honest status: `not yet digested` plus the URL for the
30 entries that have one, or `no docs_url on file` for the rest. It never
fabricates a digest.

### `list_jobs(family=None)`

The closed capability vocabulary an agent should ask with: 55 jobs in 10
families, plus the supply behind each one. An agent cannot guess a closed
vocabulary. Read the menu once, then ask `find_tools` precisely.

Each job carries how many tools claim it and how many of those have an
official MCP server, which is where the directory's whole argument lives:

```
draft-personalized-outreach     50 tools claim it, 22 agent-callable
score-rep-performance           25 tools claim it,  5 agent-callable
run-sales-roleplay-practice     11 tools claim it,  0 agent-callable
```

A job with almost no agent-callable supply is a finding, not a gap to paper
over.

### Resource: `gtm-directory://integrity`

What the server verified about its data before it agreed to serve anything.
Read it if you want to audit your install.

---

## What is actually in the data today

Live numbers from the current build, not the spec's prose.

| | |
|---|---|
| Entries | 293 across 15 categories |
| Unique products | 277 (16 are deliberately cross-listed in two categories) |
| Official MCP | 144 |
| Community MCP | 21 |
| No MCP found | 117 |
| MCP status unknown | 7 |
| Not applicable | 4 |
| Access gate | 57 free, 101 paid, 45 enterprise-only, 1 enterprise-leaning, 83 unknown, 6 n/a |
| Solo-reachable | 117 (an MCP server plus a gate you can pass without a sales call) |
| BENCH-TESTED | 0 |
| Entries with a docs URL | 30 |
| Job vocabulary | 55 jobs in 10 families |
| Entries with job tags | 271 of 293, all from a machine pass, none human-reviewed |

Two things to know about the shape:

- **`mcp_url` is prose on 98 entries.** 272 entries carry the field; 174 parse
  to at least one real URL. The other 98 are a sentence about where the server
  lives. Those are returned verbatim as `mcp_url_raw` rather than being
  dropped or invented, and `mcp_urls[]` is the parsed list. Read both.
- **`api_gate` is `unknown` on 83 entries.** That is the directory's biggest
  open quality problem and it is published rather than rounded away.

The unbuilt layers are visible rather than invisible: every `github_*` field
and `docs_digest` are empty on the current build, 22 entries carry no job tag
at all, and every response says so instead of letting you read an unmeasured
null as a measured zero.

The vocabulary is read from `jobs_vocabulary` inside `directory.json`, where
the build bakes it, so the vocabulary and the tags can never drift apart. A
`jobs.yaml` on disk is only a fallback for older builds. If you point the
server at a build that predates the tagging pass it degrades to text search
and says so on every capability answer, which the smoke test exercises rather
than assumes.

---

## Data, integrity and the startup gate

The server refuses to start on drifted data. At startup it:

1. resolves `directory.json` (env var, then the bundled copy, then the repo);
2. reads the **expected entry count from `build_report.json`**, never from a
   constant in the code;
3. checks the entry count, the file's agreement with itself, the category
   totals, and id uniqueness;
4. recomputes the content SHA-256 exactly the way the builder computes it and
   compares it to the stamped value.

Any failure is fatal and loud on stderr with a non-zero exit. A directory that
quietly serves edited data is worse than a directory that refuses to start.

| Environment variable | Effect |
|---|---|
| `GTM_DIRECTORY_DATA` | path to `directory.json`, or the directory holding it |
| `GTM_DIRECTORY_JOBS` | path to `jobs.yaml`, or the directory holding it |
| `GTM_DIRECTORY_ALLOW_CHECKSUM_DRIFT=1` | development only. Starts on a checksum mismatch and then carries a permanent "DATA NOT VERIFIED" caveat on every single response. |

The server never writes to `data/`. It opens it read-only, once.

---

## Testing

```bash
cd server
python qa_stdio.py
```

The smoke test spawns `python -m gtm_mcp_directory` as a real subprocess,
speaks MCP over stdio, calls all seven tools with real queries, asserts the
honesty envelope on every response, rebuilds two degraded copies of the
directory in a temp folder (one with the tags stripped, one with the tags
stripped but the vocabulary kept) to prove the fallbacks still answer
honestly, and proves the startup gate by feeding the server a hand-edited
file, a short file and a broken file and checking it refuses all three. 99
checks, and it prints every answer so you can read them rather than trust
them.

---

## Not doing, on purpose

- **No write tools.** Nothing here mutates the directory.
- **No submission tool.** A vendor submitting through an agent cannot be
  verified as a human at a company. The review queue is deliberately human.
- **No telemetry of any kind.** Not usage counts, not query logs, not a ping.
- **No `featured` or `recommended` field**, in the schema or anywhere else.
- **No hosted remote endpoint**, yet. That introduces a host, a bill, a log of
  other people's queries, and an availability promise. None of it is needed to
  be useful.

## Submitting a tool or a correction

Open an issue on
[gtm-mcp-directory](https://github.com/andrewcmcguire/gtm-mcp-directory). The
standing rule, published on the site and repeated here: a vendor can correct a
fact and can supply a source. A vendor cannot buy a tier, a position, a badge
or a phrasing. Corrections that come with a public URL are made and credited.
Corrections that come with an argument are made if the URL supports them.
