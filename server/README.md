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

Restart Claude Desktop. The eleven tools appear under the tools menu.

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

Eleven read-only tools. No write tools, no submission tool, no telemetry.

| Tool | Question it answers |
|---|---|
| `find_tools` | which tools claim a job, and by which interface (MCP, CLI) can an agent reach them |
| `get_tool` | one entry, every field, every source URL |
| `list_categories` | the 15 categories with counts and gates |
| `whats_mcpd` | how much of GTM an agent can reach, in numbers |
| `find_by_gate` | the access axis on its own |
| `get_docs_digest` | structured facts from vendor API docs, when crawled |
| `get_server_tools` | what one MCP server actually exposes |
| `get_install` | both routes into one tool: the MCP endpoint and the CLI install commands |
| `whats_building` | what vendors ship in public on GitHub, dated |
| `plan_stack` | a step-by-step shortlist for a multi-step GTM job |
| `list_jobs` | the closed capability vocabulary |

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
| `live_endpoint_only` | keep only entries whose recorded MCP URL answered an `initialize` as a server on the last probe (`endpoint_status` live or live-auth-gated). Liveness, not a test of the tools |
| `tool_query` | match against the actual tool names and descriptions a server exposes, not the vendor's blurb. Only harvested servers can match |
| `interface` | `mcp` (official or community MCP server on record), `cli` (`cli_status` official or community), `either` (at least one). An entry dropped by `cli` has `cli_status` none-found or not-checked, and neither is proof the vendor ships no CLI |
| `cli_status` | `official`, `community`, `none-found`, `not-checked`, the direct filter on the command-line layer |
| `limit` | default 20, max 100 |

Every result row carries its CLI fields (`cli_status`, `cli_party`,
`cli_binary`, the first two `cli_install` commands with the `source_url` and
`fetched_on` each was quoted from, `cli_checked_on`) and its vendor
organisation fields (`github_org`, `github_org_repos`,
`github_org_latest_activity`, `github_org_checked_on`). `get_install` returns
every install command for one tool.

**Two match paths, and the response always names the one it used.**

1. **Job tags.** Your query resolves against the 56-job vocabulary (slugs,
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

### Endpoint versus docs, measured (added 2026-09-03)

About half of the official `mcp_url` values are documentation pages, not
endpoints. Every official and community entry now carries four derived,
dated fields, filled from the weekly `mcp_verify.py` run and never hand-edited:

| Field | Meaning |
|---|---|
| `endpoint_status` | `live` (answered an MCP initialize), `live-auth-gated` (401/402/407: alive, wants a key), `repo-local` (a repo or package you install and run locally over stdio), `docs-only` (a page about the server, not the server), `unreachable`, `not-probed`, `not-applicable` |
| `mcp_endpoint` | the URL that answered as a server, or null |
| `mcp_docs_url` | the URL that served a page or a repo, or null |
| `endpoint_last_probed` | the date of the run that produced the three values above |

`docs-only` is not a downgrade of `mcp_status`. It is the gap between where to
read and where to connect, and an agent needs the second. `whats_mcpd` reports
the split as `official_with_live_endpoint` and `official_docs_only`.

### Command line and vendor GitHub, measured (added 2026-09-08)

Agents reach for a CLI as readily as for an MCP server (Claude Code, Codex and
Gemini CLI all run shell commands), so the directory asks the same question of
the command line, and it asks what each vendor is shipping in public. Two more
machine-measured layers, same rules: dated, never hand-edited, and "none found"
is a statement about the instrument on that date.

| Field | Meaning |
|---|---|
| `cli_status` | `official` (a first-party source: the vendor's own docs page showing an install command, or a registry package the vendor publishes), `community` (only third-party packages or repositories name this vendor), `none-found` (every probe empty on `cli_checked_on`), `not-checked` (the harvest did not reach the entry) |
| `cli_binary` | the command users type, as seen in usage lines |
| `cli_install[]` | `{cmd, manager, source_url, party, fetched_on}`: every command quoted verbatim from `source_url` on `fetched_on`. Never run here |
| `cli_login`, `cli_commands_seen`, `cli_docs_url`, `cli_repo`, `cli_packages[]` | the auth command seen, the subcommands seen, the page and repository that documented it, the npm/PyPI/Homebrew records |
| `cli_checked_on` | the date of the harvest that produced the values above |
| `github_org` | the GitHub organisation tied to the vendor by domain evidence, or null |
| `github_org_status` | `resolved`, `unresolved` (accounts seen, none passed the evidence rules), `no-github-signal`, `not-checked` |
| `github_org_repos`, `github_org_repos_mcp`, `github_org_repos_cli` | public non-fork repositories on `github_org_checked_on`, and how many mention MCP or look like CLIs |
| `github_org_latest_activity`, `github_org_recent_repos[]` | the most recent push, and the five most recently pushed repositories with kind, description, stars, pushed date and latest release |
| `github_org_checked_on` | the date of the harvest that produced the values above |

Three honesty rules ride on both layers, in every response:

- **A community CLI is a third party's work.** It wraps the vendor's API, the
  vendor did not publish it and may not support it. The server says so on the
  entry and on every install answer.
- **An install command is a quotation, not a test.** Each one carries the URL
  it was read from and the date. Nobody ran it for this directory; read the
  page before pasting it.
- **Unmeasured is null, not zero.** `none-found` means not found on that date.
  `not-checked` means the harvest did not reach the entry. A null organisation
  is a resolution miss on a date, not proof the vendor has no GitHub. When a
  layer has not run at all, every count comes back as `null` with a sentence
  ("the CLI layer has not been measured on this build") rather than as 0.
  Repository `kind` is a heuristic from name, topics and description, not a
  statement by the vendor.

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

### `get_install(name)`

Everything an agent needs to start using one tool, both routes in one answer.

```python
get_install(name="ZoomInfo")
```

`mcp` carries the MCP route: `mcp_endpoint` or the repository to install,
`endpoint_status`, `mcp_auth`, the access gate, and `hosted_or_local` (a live
endpoint is hosted and needs no install; a `repo-local` server is installed and
run over stdio; a `docs-only` URL is a page to read, not a place to connect).
`cli` carries the CLI route: `cli_status`, `cli_binary`, every `cli_install`
command with its `source_url` and `fetched_on`, `cli_login`,
`cli_commands_seen`, `cli_docs_url`, `cli_repo` and `cli_packages`.

`recommendation` is one line that says which routes exist and are reachable,
in the same shape every time. The MCP half comes from the liveness probe, the
CLI half from the harvest, and each carries its date. On a build where the CLI
harvest has not run it reads:

> MCP: a live endpoint at https://mcp.zoominfo.com/mcp that asks for a key
> (probed 2026-09-04). CLI: the CLI layer has not been measured on this build.

On a build where it has, the CLI half becomes "CLI: official, <install
command>, quoted from <source_url> on <date>", or "community (a third party's
work, not the vendor's), ...", or "none found on <date>".

It describes routes. It does not rank vendors, and it never says "best".
`caveats` carries the three rules above for this entry: a community CLI is a
third party's work, an install command was quoted from a page on a date and
not run, and none-found means not found on that date. A name that matches
nothing says "not researched yet"; a name that matches several returns the
candidates instead of guessing.

### `whats_building(name=None, category=None, days=90, limit=20)`

What vendors are shipping in public on GitHub, from organisations tied to
them with domain evidence (never a name match alone).

```python
whats_building(name="Apify")
whats_building(category="data-enrichment", days=30)
```

With a name: the vendor's `github_org`, its status and the evidence rule that
tied it, public repository counts, and the five most recently pushed
repositories with description, kind, stars, pushed date and latest release.

Without a name: across the directory or one category, the vendors whose
organisation pushed within `days` of the measurement date, most recent first,
each with its most recently pushed repositories. The window is measured back
from `github_org_checked_on`, not from today, because the server has no clock
it trusts over its data. `counts` carries resolved, unresolved, no-signal and
not-checked totals with their date, and `silence_note` spells out how many
vendors are silent here so that silence is never read as inactivity. If the
layer has not been measured on the build, `status` is `not measured` and every
count is `null`.

### `list_jobs(family=None)`

The closed capability vocabulary an agent should ask with: 56 jobs in 10
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
| Job vocabulary | 56 jobs in 10 families |
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
speaks MCP over stdio, calls all eleven tools with real queries, asserts the
honesty envelope on every response, rebuilds three degraded copies of the
directory in a temp folder (one with the tags stripped, one with the tags
stripped but the vocabulary kept, one with the CLI and organisation layers
reset to not-checked) to prove the fallbacks still answer honestly, checks
that `find_tools(interface="cli")` counts what the data counts and that
`plan_stack(prefer_interface="cli")` reorders without removing, and proves
the startup gate by feeding the server a hand-edited file, a short file and a
broken file and checking it refuses all three. Every expected count is read
from `directory.json`, never typed into the test, and it prints every answer
so you can read them rather than trust them.

---

## Not doing, on purpose

- **No write tools.** Nothing here mutates the directory.
- **No submission tool.** A vendor submitting through an agent cannot be
  verified as a human at a company. The review queue is deliberately human.
- **No telemetry of any kind.** Not usage counts, not query logs, not a ping.
- **No `featured` or `recommended` field**, in the schema or anywhere else.
- **No query log at the hosted endpoint.** A hosted copy exists since 2026-09-08 at
  `https://andrewcmcguire.com/gtm-directory/api/mcp` (streamable HTTP; put that URL in your client's `mcpServers` entry). It runs
  this same read-only package with zero outbound requests, keeps no request log of its
  own, and the local install stays the reference: nothing is available remotely that is
  not in the repo.

## Submitting a tool or a correction

Open an issue on
[gtm-mcp-directory](https://github.com/andrewcmcguire/gtm-mcp-directory). The
standing rule, published on the site and repeated here: a vendor can correct a
fact and can supply a source. A vendor cannot buy a tier, a position, a badge
or a phrasing. Corrections that come with a public URL are made and credited.
Corrections that come with an argument are made if the URL supports them.
