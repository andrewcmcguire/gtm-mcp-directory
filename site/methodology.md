# Methodology: how an entry is made and where this build is thin

> The five laws an entry survives, the two honesty tiers (1 bench tested of 1,251), the counting authority, and every thin spot named rather than padded.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](llms.txt). The whole dataset: [directory.json](data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](index.md) / Methodology

**Methodology**

## The verification is the product.

The list is not the moat. Anyone can copy 1,251 rows. What is hard to copy is that every answer carries its honesty tier and the date it was measured, and that the awkward numbers are on the page instead of in a drawer.

**The two tiers**

**RESEARCHED.** Facts from public sources with URLs. No usage claims. Nobody has run this tool. All 1,250 entries in this build are RESEARCHED.

**BENCH-TESTED.** Andrew personally ran it on a stated date. Cannot be bought. There are 1 of them. That number is on the front page. It stays at 1 until Andrew actually runs something, and a vendor offering access buys a test, never a verdict.

**The five laws an entry has to survive**

1. An MCP claim needs a URL. A claim without one is not accepted.

2. Unknown is a legal answer. 948 entries carry an unknown access gate and they are published as unknown rather than guessed into a bucket.

3. Vendor copy is a source for what the vendor says, not for what the tool can do. Every what_it_does on this site was rewritten in plain language.

4. Enterprise gated with no public docs is itself the most useful fact in the directory, so it is surfaced rather than hidden. 79 entries are enterprise only.

5. Official means first party. A Zapier, viaSocket or Composio wrapper is not an official MCP server no matter how well it works.

**What none-found does and does not mean**

487 entries are none-found. That is a statement about the search, made on the date in the entry, and it is not a promise that no server exists. A vendor who shipped one the week after the check is recorded as none-found until the next pass, which is exactly why the weekly diff exists and why every entry ships its last_checked date.

**The counting authority**

tools_recount.py is the counter, not this site and not the build script. The build reconciles against it file by file and fails rather than publish a drifted number. This build: 1,251 against 1,251, 0 failures, 0 parser warnings. The site generator re-checks the same numbers before it writes a single file.

Data baked 2026-09-12 by build_directory.py (phase 1). Network calls made during the build: 0. Content sha256 ead8e7fc6cfac593aa6f0a86...

**The duplicates, and why two counts exist**

1,251 entries, 1,235 unique products. The difference is 16 products that are deliberately listed in two category files because a reader browsing either one should find them. The canonical home for each is declared in INDEX.md and not chosen by the parser. Category and status views count all 1,251 entries, because that is what the source files hold. Tool pages count 1,235, because that is how many products there are.

- [Amplemarket](tools/amplemarket.md) 02-amplemarket + 04-amplemarket
- [Chili Piper](tools/chili-piper.md) 10-chili-piper + 14-chili-piper
- [Clari](tools/clari.md) 03-clari + 04-clari
- [Common Room](tools/common-room.md) 05-common-room + 15-common-room
- [Crustdata](tools/crustdata.md) 01-crustdata + 05-crustdata
- [Default](tools/default.md) 06-default + 10-default
- [HubSpot](tools/hubspot.md) 06-hubspot + 12-hubspot
- [Klenty](tools/klenty.md) 02-klenty + 04-klenty
- [Pipedrive](tools/pipedrive.md) 06-pipedrive + 12-pipedrive
- [Qualified](tools/qualified.md) 14-qualified + 04-qualified
- [Reply.io](tools/reply-io.md) 02-reply-io + 04-reply-io
- [Salesforce (core CRM/platform) + Agentforce](tools/salesforce-agentforce.md) 06-salesforce-agentforce + 04-salesforce-agentforce
- [Salesforge](tools/salesforge.md) 02-salesforge + 04-salesforge
- [TheirStack](tools/theirstack.md) 05-theirstack + 01-theirstack
- [Trumpet (sendtrumpet.com)](tools/trumpet.md) 13-trumpet + 08-trumpet
- [Warmly (Warmly.ai)](tools/warmly.md) 05-warmly + 01-warmly

**Where this build is thin, named rather than padded**

**1 entry claims an MCP with no parseable URL.** SCHEMA law 1: an MCP claim requires a URL. These entries claim official or community but their mcp_url field contains no parseable URL.

- [Arphie](tools/arphie.md) 13-arphie

**100 entries carry fewer than two source URLs.** SPEC 6.3 item 8: at least two independent sources. These entries carry fewer than two source URLs. They are listed rather than quietly padded.

- [Agent Utility API](tools/agent-utility-api.md) 01-agent-utility-api
- [Compelling](tools/compelling.md) 01-compelling
- [DataMerge MCP](tools/datamerge-mcp.md) 01-datamerge-mcp
- [Eesier AI Lead Prospecting](tools/eesier-ai-lead-prospecting.md) 01-eesier-ai-lead-prospecting
- [Enginy MCP](tools/enginy-mcp.md) 01-enginy-mcp
- [Enrich Company Domain Intelligence](tools/enrich-company-domain-intelligence.md) 01-enrich-company-domain-intelligence
- [Generect MCP](tools/generect-mcp.md) 01-generect-mcp
- [Interzoid MCP](tools/interzoid-mcp.md) 01-interzoid-mcp
- [Leadgen ONRC Romania](tools/leadgen-onrc-romania.md) 01-leadgen-onrc-romania
- [LeadScout MCP](tools/leadscout-mcp.md) 01-leadscout-mcp
- [MineWorks Lead Generation MCP](tools/mineworks-lead-generation-mcp.md) 01-mineworks-lead-generation-mcp
- [Outscraper MCP Server](tools/outscraper-mcp-server.md) 01-outscraper-mcp-server
- [SalesSift](tools/salessift.md) 01-salessift
- [StackLead](tools/stacklead.md) 01-stacklead
- [Theona Person Enrichment](tools/theona-person-enrichment.md) 01-theona-person-enrichment
- [Unhaze](tools/unhaze.md) 01-unhaze
- [Alyce](tools/alyce.md) 02-alyce
- [Blaze](tools/blaze.md) 02-blaze
- [Bluebirds](tools/bluebirds.md) 02-bluebirds
- [CoffeeAI](tools/coffeeai.md) 02-coffeeai
- [LeadSmarts](tools/leadsmarts.md) 02-leadsmarts
- [Linkly](tools/linkly.md) 02-linkly
- [Locent](tools/locent.md) 02-locent
- [MuntuAI MCP](tools/muntuai-mcp.md) 02-muntuai-mcp
- [Onsa](tools/onsa.md) 02-onsa
- [OpenHelm Email Outreach MCP](tools/openhelm-email-outreach-mcp.md) 02-openhelm-email-outreach-mcp
- [PhoneSys](tools/phonesys.md) 02-phonesys
- [Phos Sales Engine](tools/phos-sales-engine.md) 02-phos-sales-engine
- [Phos Sales Engine MCP](tools/phos-sales-engine-mcp.md) 02-phos-sales-engine-mcp
- [Popsy](tools/popsy.md) 02-popsy
- [Slik](tools/slik.md) 02-slik
- [Backengine MCP](tools/backengine-mcp.md) 03-backengine-mcp
- [Fabius](tools/fabius.md) 03-fabius
- [AiSDR](tools/aisdr.md) 04-aisdr
- [Conversica](tools/conversica.md) 04-conversica
- [PropelAgent Studio](tools/propelagent-studio.md) 04-propelagent-studio
- [Salesforce Agentforce (SDR Agent)](tools/salesforce-agentforce.md) 04-salesforce-agentforce
- [Saleswhale](tools/saleswhale.md) 04-saleswhale
- [Soff](tools/soff.md) 04-soff
- [Struct](tools/struct.md) 04-struct
- [Truva](tools/truva.md) 04-truva
- [ClearBrain](tools/clearbrain.md) 05-clearbrain
- [Intently (getintently.com)](tools/intently.md) 05-intently
- [Klarix Intelligence Engine](tools/klarix-intelligence-engine.md) 05-klarix-intelligence-engine
- [Lead Intelligence by Saifs](tools/lead-intelligence-by-saifs.md) 05-lead-intelligence-by-saifs
- [crmCopilot](tools/crmcopilot.md) 06-crmcopilot
- [Kenva](tools/kenva.md) 06-kenva
- [Apex Log MCP by Certinia](tools/apex-log-mcp-by-certinia.md) 07-apex-log-mcp-by-certinia
- [Apollo-Salesforce Mapper MCP](tools/apollo-salesforce-mapper-mcp.md) 07-apollo-salesforce-mapper-mcp
- [Ascend GTM Gateway](tools/ascend-gtm-gateway.md) 07-ascend-gtm-gateway
- [Cavyro](tools/cavyro.md) 07-cavyro
- [Cirra AI Salesforce Admin MCP](tools/cirra-ai-salesforce-admin-mcp.md) 07-cirra-ai-salesforce-admin-mcp
- [CRM Bridge MCP](tools/crm-bridge-mcp.md) 07-crm-bridge-mcp
- [Eutexa CRM](tools/eutexa-crm.md) 07-eutexa-crm
- [Flipfactory CRM MCP](tools/flipfactory-crm-mcp.md) 07-flipfactory-crm-mcp
- [GTM Tools MCP](tools/gtm-tools-mcp.md) 07-gtm-tools-mcp
- [Guapu](tools/guapu.md) 07-guapu
- [HubSpot MCP by rfoxes](tools/hubspot-mcp-by-rfoxes.md) 07-hubspot-mcp-by-rfoxes
- [JackTrade CRM](tools/jacktrade-crm.md) 07-jacktrade-crm
- [Kommo MCP](tools/kommo-mcp.md) 07-kommo-mcp
- [LeadDelta MCP](tools/leaddelta-mcp.md) 07-leaddelta-mcp
- [Maasy](tools/maasy.md) 07-maasy
- [ManyContacts npm MCP](tools/manycontacts-npm-mcp.md) 07-manycontacts-npm-mcp
- [MCPCloud CLI](tools/mcpcloud-cli.md) 07-mcpcloud-cli
- [Model Context Protocol - official servers repo](tools/model-context-protocol-official-servers-repo.md) 07-model-context-protocol-official-servers-repo
- [PulseMCP](tools/pulsemcp.md) 07-pulsemcp
- [RevOrbit CRM](tools/revorbit-crm.md) 07-revorbit-crm
- [Sales Intelligence MCP by Aria Agentworks](tools/sales-intelligence-mcp-by-aria-agentworks.md) 07-sales-intelligence-mcp-by-aria-agentworks
- [Salesforce MCP by rohithvemulapally](tools/salesforce-mcp-by-rohithvemulapally.md) 07-salesforce-mcp-by-rohithvemulapally
- [Salesforce MCP by starcatmeow](tools/salesforce-mcp-by-starcatmeow.md) 07-salesforce-mcp-by-starcatmeow
- [Serpent Salesforce DevOps MCP](tools/serpent-salesforce-devops-mcp.md) 07-serpent-salesforce-devops-mcp
- [Siftable](tools/siftable.md) 07-siftable
- [Smithery](tools/smithery.md) 07-smithery
- [Vesxo Connect](tools/vesxo-connect.md) 07-vesxo-connect
- [Zevari](tools/zevari.md) 07-zevari
- [ClearMix](tools/clearmix.md) 08-clearmix
- [Milk Video](tools/milk-video.md) 08-milk-video
- [Mailcannon](tools/mailcannon.md) 09-mailcannon
- [Criya](tools/criya.md) 11-criya
- [Gluetrail](tools/gluetrail.md) 11-gluetrail
- [Prelay](tools/prelay.md) 11-prelay
- [Resonance](tools/resonance.md) 11-resonance
- [StoriesOnBoard](tools/storiesonboard.md) 11-storiesonboard
- [Compgun](tools/compgun.md) 12-compgun
- [Data Parrot AI Revenue Analyst](tools/data-parrot-ai-revenue-analyst.md) 12-data-parrot-ai-revenue-analyst
- [HubSpot (AI Forecasting)](tools/hubspot.md) 12-hubspot
- [Phos Analytics Engine](tools/phos-analytics-engine.md) 12-phos-analytics-engine
- [Phos Analytics Engine MCP](tools/phos-analytics-engine-mcp.md) 12-phos-analytics-engine-mcp
- [Salesforce Einstein Forecasting](tools/salesforce-einstein-forecasting.md) 12-salesforce-einstein-forecasting
- [DocSend](tools/docsend.md) 13-docsend
- [Manatee](tools/manatee.md) 13-manatee
- [Sameplan](tools/sameplan.md) 13-sameplan
- [Abbot](tools/abbot.md) 14-abbot
- [Crisp MCP](tools/crisp-mcp.md) 14-crisp-mcp
- [Laudspeaker](tools/laudspeaker.md) 14-laudspeaker
- [Nara](tools/nara.md) 14-nara
- [Pocus](tools/pocus.md) 14-pocus
- [Ultimate.ai (Ultimate)](tools/ultimate-ai.md) 14-ultimate-ai
- [BuzzSumo](tools/buzzsumo.md) 15-buzzsumo
- [F5Bot](tools/f5bot.md) 15-f5bot

**948 entries have an unknown access gate** and **727 have no documentation URL.** Both are legal and both are published as blank. Every one of them is visible on its own tool page.

**What has not been measured at all**

The following fields exist in the schema, are present on every entry, and are empty on every entry. Nothing about them is inferred anywhere on this site.

- docs_digest: empty on 1,251 of 1,251 entries
- docs_last_crawled: empty on 1,251 of 1,251 entries
- github_archived: empty on 1,251 of 1,251 entries
- github_fetched_on: empty on 1,251 of 1,251 entries
- github_last_commit: empty on 1,251 of 1,251 entries
- github_stars: empty on 1,251 of 1,251 entries
- github_url: empty on 1,251 of 1,251 entries
- submission: empty on 1,251 of 1,251 entries

That is why the GitHub view shows seeds instead of star counts. An empty field is published as empty.

**The jobs field, which is now measured**

jobs[] used to be on the list above. It is not any more. As of 2026-08-25 the vocabulary is closed at 56 jobs in 10 families, and 849 tags are assigned across 271 of 1,251 entries. 980 entries carry no tag at all, each one for a recorded reason that is printed on its own tool page.

**What a tag means, exactly.** A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records. It was derived from the entry's own what_it_does, ai_features and revops_role text, which is itself RESEARCHED tier. Tagged by machine-pass, tier RESEARCHED, and bench_tested is still 1. 49 entries were flagged for human review by that pass and are the first thing a second reader should look at.

The vocabulary is closed on purpose. A tool whose job genuinely is not in the list stays blank rather than being forced into the nearest tag, because a wrong job tag is the class of quiet lie the two tier honesty law exists to prevent. Vocabulary source data/jobs.yaml sha256 bb07dcb51e730f83..., tags source data/tags.yaml sha256 7039a400c1c46643...

[Browse the 56 jobs](jobs/index.md)

**The canonical URL and the base this site is published at**

Every internal link on this site is relative, so the same files serve correctly from a Pages subdomain, from a path on andrewcmcguire.com, or from a file:// path with no network at all. The canonical tags, the sitemap and llms.txt need an absolute base, and that base is https://andrewcmcguire.com/gtm-directory. That is also where the site actually serves from: the route was applied on 2026-08-27 and this build is live at andrewcmcguire.com/gtm-directory, with the Cloudflare Pages subdomain as its origin. If that route is ever unwound, the one constant changes and the site is rebuilt. It is stated here so the canonical base is never a URL you have to take on trust.

**The markdown twins and what they are for**

Every HTML page on this site has a markdown twin at the same path with a .md extension, and the twin is generated from the rendered page rather than written by hand, so it cannot drift. It carries the same content with the chrome removed: no masthead, no footer, no theme toggle, no styling. Links inside a twin point at the other twins, so an agent that lands on one can crawl the whole site in markdown without ever parsing HTML. [llms.txt](llms.txt) is the map, and [the data page](data.md) serves the whole directory as JSON.

Schema.org JSON-LD ships inline on every page: Dataset on the front page and the data page, ItemList on every listing, FAQPage on every learn answer, BreadcrumbList everywhere. It is a data block rather than executable script, so the Content-Security-Policy that forbids inline script still holds and the site still makes zero external requests.

**The one thing this site changes about the source text**

Em dashes in source prose are rendered as a spaced hyphen. That is a house typography rule and it is the only alteration made at render time. No word, number, URL, date or field value is changed, summarised, reordered or dropped anywhere on this site. Notes ship verbatim including the awkward ones, and the raw sources string is printed alongside the parsed links so you can check the parse.

**The ordering rule**

official MCP first, then community, then unknown, then n/a, then none-found; within each band gate order is free, paid, enterprise-leaning, enterprise-only, unknown; then alphabetical by name. Computed, never curated, never purchasable.

It is computed, it is printed on every view that uses it, and there is no featured field anywhere in the schema, because a field that exists is a field somebody will eventually try to buy.

**No gate on this page**

No email is required to read anything here. No comment keyword, no DM funnel, no download wall. It is free because it is more useful when other operators correct it.
