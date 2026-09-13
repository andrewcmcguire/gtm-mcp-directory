# GTM tools by GitHub repo health: not measured yet, and why

> Repo staleness for every tool with a public repo, stamped with the date it was measured. Nothing is measured in this build: 469 entries carry a github.com URL as a seed.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) / By GitHub health

**View: by GitHub health**

## Is the thing you are about to depend on still moving.

> **Nothing measured yet** github_url, github_stars, github_last_commit, github_archived and github_fetched_on are null on all 1,251 entries. The refresh rail in SPEC section 7.2 has not been run. A star count without the date it was taken is a lie, so no number is shown at all.

When the rail runs, every repo lands in one of five bands and every band ships with the date it was measured: active under 90 days, slowing 90 to 180, quiet 180 to 365, dormant over a year, and archived. The band is descriptive and never a verdict. A stable server genuinely may not need commits. But an agent about to write a community MCP wrapper into a workflow deserves to know the repo has been silent for eight months first, and this directory already has the receipts that the category churns.

### The seed, which is a fact and not a measurement

469 of 1,251 entries already carry a github.com URL somewhere in their fields, and 431 of those sit in the mcp_url field. Those repos are free to measure when the rail runs. Nothing below says anything about whether a repo is healthy.

- [Apideck](../tools/apideck.md) apideck.com A unified API that normalises 200+ SaaS connectors into single data models, exposed as one MCP endpoint covering CRM, accounting, HRIS, ATS, file storage and issue tracking. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [MCP Layer](../categories/mcp-infrastructure.md) · CLI: apideck

- [Apify](../tools/apify.md) apify.com A cloud platform for running "Actors" (hosted scrapers and automation programs, thousands of them in a public store) that extract web data such as LinkedIn posts, Google Maps listings, company sites and social... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Data & Enrichment](../categories/data-enrichment.md) · CLI: actor

- [Browserbase](../tools/browserbase.md) browserbase.com A hosted headless-browser service (sessions, proxies, stealth, session recording) with Stagehand, its natural-language browser automation layer, so agents can navigate, act on and extract from web pages that... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Data & Enrichment](../categories/data-enrichment.md) · CLI: bb9

- [Cal.com](../tools/cal-com.md) cal.com Open-source scheduling infrastructure - booking pages, event types, and a scheduling API/platform - offered both as a free, self-hostable open-source product and as hosted SaaS. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Scheduling & Routing](../categories/scheduling-routing.md)

- [Cargo](../tools/cargo.md) getcargo.ai A GTM/RevOps engineering platform (YC S23) that lets revenue teams define, version, and automate go-to-market logic - lead sourcing, enrichment, scoring, routing, CRM sync - as code, run by AI agents. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [RevOps Infra](../categories/revops-infra.md) · CLI: cargo

- [Census (now operates as "Fivetran Activations")](../tools/census.md) getcensus.com Was a standalone reverse-ETL tool for syncing warehouse data (Snowflake, BigQuery, etc.) into GTM tools like Salesforce/HubSpot without code; the product now lives inside Fivetran as "Activations," same... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [RevOps Infra](../categories/revops-infra.md)

- [Composio](../tools/composio.md) composio.dev A hosted integration/auth platform that lets AI agents and MCP clients call actions across 1,000+ SaaS apps (HubSpot, Slack, Gmail, GitHub, Notion, Stripe, and others) through Composio-managed OAuth. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [MCP Layer](../categories/mcp-infrastructure.md) · CLI: composio

- [Diffbot](../tools/diffbot.md) diffbot.com A web-extraction and "Knowledge Graph" company that crawls the public web and structures it into an entity graph (organizations, people, articles) queryable for company/entity enrichment, plus raw... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Data & Enrichment](../categories/data-enrichment.md) · CLI: diffbot (community)

- [Enrow](../tools/enrow.md) enrow.io Finds and verifies work email addresses and direct phone numbers from a name plus company domain or a LinkedIn URL, charging only when it returns a verified result. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Exa](../tools/exa.md) exa.ai A search API that returns web pages and structured results ranked by semantic/meaning similarity to a query (embeddings-based) rather than keyword matching, plus tools to fetch page contents and get... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Data & Enrichment](../categories/data-enrichment.md) · CLI: exa-cli (community)

- [Fathom](../tools/fathom.md) fathom.video Free AI meeting recorder/notetaker that transcribes calls and generates summaries, action items, and CRM sync. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Conversation Intel](../categories/conversation-intel.md)

- [Firecrawl](../tools/firecrawl.md) firecrawl.dev A web scraping and crawling API that turns any URL or whole site into clean markdown or structured JSON for LLM pipelines, with search, map, crawl, extract, parse and browser-interaction endpoints. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Data & Enrichment](../categories/data-enrichment.md) · CLI: firecrawl

- [Fivetran](../tools/fivetran.md) fivetran.com Managed ELT pipeline platform; for GTM purposes, the relevant piece is its Salesforce/HubSpot/Marketo/Outreach/Salesloft/Gong/Zendesk connectors that land CRM and GTM-tool data in a warehouse, plus... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [RevOps Infra](../categories/revops-infra.md) · CLI: fivetran-cli (community)

- [HubSpot](../tools/hubspot.md) hubspot.com An all-in-one CRM/marketing/sales/service platform with contacts, deals, marketing automation, and a public REST API/developer platform. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [RevOps Infra](../categories/revops-infra.md) · CLI: hs

- [Hunter.io](../tools/hunter-io.md) hunter.io An email-finding and verification tool - given a name, domain, or company, it locates likely professional email addresses (via domain pattern-matching and web-crawled data) and verifies deliverability; also... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Jotform](../tools/jotform.md) jotform.com An online form builder (forms, approvals, tables, e-sign, payment collection and conversational "AI Agents") with a REST API and a hosted MCP server. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Inbound & PLG Chat](../categories/inbound-plg-chat.md)

- [Leadfeeder (product line rebranded/merged under Dealfront; dealfront.com redirects to leadfeeder.com)](../tools/leadfeeder.md) leadfeeder.com Identifies companies visiting a website via IP-to-company matching, tracks page-level visit behavior, and surfaces intent signals plus verified contact data for those companies. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Signals & Intent](../categories/signals-intent-abm.md)

- [LeadMagic](../tools/leadmagic.md) leadmagic.io A B2B contact/company data API and CLI that finds and validates work emails, mobile numbers, and social-to-email matches, plus company/job/ad-intelligence lookups, billing only for successful (valid) results. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Data & Enrichment](../categories/data-enrichment.md) · CLI: leadmagic (community)

- [Lusha](../tools/lusha.md) lusha.com A B2B contact and company database (300M+ profiles) accessed via a browser extension, web prospecting platform, and bulk CSV/API enrichment for finding direct dials, emails, and company data. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [MeetGeek](../tools/meetgeek.md) meetgeek.ai Automatic meeting recorder and transcriber that produces summaries, highlights and conversation analytics across Zoom, Teams and Meet. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Conversation Intel](../categories/conversation-intel.md) · CLI: meetgeek (community)

- [Merge Agent Handler](../tools/merge-agent-handler.md) merge.dev Merge's tool-calling platform for AI agents: it wraps hundreds of third-party SaaS applications as pre-built MCP-ready connectors, bundles them into scoped "tool packs" per agent, brokers per-end-user... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Metricool](../tools/metricool.md) metricool.com A social media management and analytics tool (scheduling, analytics, competitor tracking and ad-campaign monitoring across Instagram, Facebook, X, LinkedIn, TikTok, YouTube and Meta, Google and TikTok Ads) for... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Community & Dark Social](../categories/community-dark-social.md)

- [Model Context Protocol - official servers repo](../tools/model-context-protocol-official-servers-repo.md) github.com The official reference-implementation repository for MCP, "managed by Anthropic, but built together with the community" - ships a small set of maintained example servers (Everything, Fetch, Filesystem, Git,... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [monday.com (monday CRM)](../tools/monday-com.md) monday.com A work-management platform whose CRM product runs pipelines, contacts, accounts and deal activity as boards and items, with a first-party remote MCP server that lets an AI client read and update that data on... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [RevOps Infra](../categories/revops-infra.md) · CLI: mapps

- [n8n](../tools/n8n.md) n8n.io A node-based workflow-automation platform for connecting apps/APIs and orchestrating multi-step processes, usable self-hosted or as managed cloud. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [RevOps Infra](../categories/revops-infra.md)

- [PandaDoc](../tools/pandadoc.md) pandadoc.com Document builder/e-signature platform for proposals, quotes, and contracts, with AI-assisted content generation and CRM-linked workflows. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Proposals & Deals](../categories/proposals-deals.md) · CLI: pandadoc (community)

- [Pipeworx](../tools/pipeworx.md) pipeworx.io A single MCP gateway that fronts a stated 1,532 live data sources as 5,871 tools behind one URL, weighted toward public and regulatory data (SEC EDGAR, FDA, the Federal Reserve, ClinicalTrials, USPTO, EPA, EU... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [MCP Layer](../categories/mcp-infrastructure.md) · CLI: pipeworx

- [Prospeo](../tools/prospeo.md) prospeo.io A B2B contact database/lookup tool that finds verified work emails and mobile phone numbers for a given person or domain and returns basic firmographic data (headcount, industry, tech stack) for companies;... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Data & Enrichment](../categories/data-enrichment.md) · CLI: prospeo (community)

- [Relevance AI](../tools/relevance-ai.md) relevanceai.com A platform for building and deploying specialist AI agents (research/enrichment, outbound prospecting, meeting scheduling, deal review, proposal building) that teams configure and progress toward autonomous... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [AI SDRs](../categories/ai-sdr-agents.md) · CLI: relevanceai

- [Retool](../tools/retool.md) retool.com A low-code platform for building internal tools/dashboards/admin panels on top of databases and APIs; in a GTM context, used to build custom RevOps tooling - lead-routing consoles, deal-desk approval apps,... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [RevOps Infra](../categories/revops-infra.md) · CLI: retool (community)

- [Snowflake (Cortex AI, as GTM/RevOps warehouse layer)](../tools/snowflake.md) snowflake.com Cloud data warehouse that acts as the central store where GTM data (CRM, product usage, marketing, support) gets modeled and joined; increasingly the platform other reverse-ETL tools (Hightouch, Fivetran... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [RevOps Infra](../categories/revops-infra.md) · CLI: snowflake-cli

- [StackOne](../tools/stackone.md) stackone.com A unified-API vendor that publishes a stated 518 managed MCP servers exposing 31,928 tools across HR, CRM, IT and finance applications, reachable through one endpoint with per-account routing, plus dynamic... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [MCP Layer](../categories/mcp-infrastructure.md) · CLI: stackone

- [Tavily](../tools/tavily.md) tavily.com A web search and page-extraction API built for LLM agents that returns ranked, cleaned results and extracted page content rather than a list of links. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Data & Enrichment](../categories/data-enrichment.md) · CLI: tavily-cli

- [Tavus](../tools/tavus.md) tavus.io Developer platform for building real-time, two-way conversational AI video agents ("Conversational Video Interface") - positioned for GTM use cases like greeting website visitors and booking meetings, not... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Video Prospecting](../categories/video-prospecting.md) · CLI: tavus-cli (community)

- [Tidio](../tools/tidio.md) tidio.com Customer-service platform combining live chat, a help desk, and an AI agent ("Lyro") that resolves routine support/sales questions automatically. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Inbound & PLG Chat](../categories/inbound-plg-chat.md)

- [usefulapi.io](../tools/usefulapi-io.md) usefulapi.io A hosted catalogue of 146 single-application MCP servers, one per SaaS product, each on its own subdomain, wrapping that product's public REST API as a named tool list with per-tool read and write labels and... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Wistia](../tools/wistia.md) wistia.com A video hosting and marketing platform for business (player, channels, webinars, analytics, lead capture) with a REST API; sales and marketing teams use it for hosted demo and follow-up video with per-viewer... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Video Prospecting](../categories/video-prospecting.md) · CLI: wistia

- [Zapier](../tools/zapier.md) zapier.com A cloud automation platform connecting thousands of apps via trigger-action workflows (Zaps), plus a separate agent product. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [RevOps Infra](../categories/revops-infra.md) · CLI: zapier-platform

- [Zapier MCP](../tools/zapier-mcp.md) zapier.com Zapier's own MCP endpoint, letting Claude, ChatGPT, Cursor, and other MCP clients trigger the same 9,000+ app actions Zapier already exposes to its classic trigger-action Zaps. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [MCP Layer](../categories/mcp-infrastructure.md) · CLI: zapier-platform

- [ZoomInfo](../tools/zoominfo.md) zoominfo.com A B2B contact/company database and go-to-market platform (500M+ contacts, 100M+ companies) built from web crawling, public filings, and human researchers, used for prospecting, account research, and lead... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Data & Enrichment](../categories/data-enrichment.md) · CLI: gtm

- [Amplemarket (Duo Copilot)](../tools/amplemarket.md) amplemarket.com An all-in-one sales platform (lead gen + multichannel engagement + deliverability) with an AI agent layer ("Duo Copilot") that detects buying signals, writes and A/B-tests email copy (including AI voice-cloned... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [AI SDRs](../categories/ai-sdr-agents.md) · Cross listed, canonical home is Engagement & Outbound

- [Apollo.io](../tools/apollo-io.md) apollo.io A combined B2B contact database (265M+ contacts) and sales engagement platform in one product - prospect search/filtering, email and call sequencing, and contact/organization enrichment. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Attention](../tools/attention.md) attention.com Captures, transcribes, and analyzes sales and customer conversations, automatically syncing structured insights to the CRM. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Conversation Intel](../categories/conversation-intel.md)

- [Bright Data](../tools/bright-data.md) brightdata.com A general-purpose web-scraping/proxy infrastructure platform (residential proxies, browser automation, structured scraping APIs) that GTM engineers repurpose to pull LinkedIn, company-site, and directory data... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Data & Enrichment](../categories/data-enrichment.md) · CLI: bdata

- [CatchIntent](../tools/catchintent.md) catchintent.com A B2B intent tool that monitors social and web sources for buying signals, ranks the people behind them by warmth, enriches the profiles and drafts personalised openers, then pushes leads to a CRM or outreach... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Signals & Intent](../categories/signals-intent-abm.md)

- [Chili Piper](../tools/chili-piper.md) chilipiper.com Inbound lead-routing and instant meeting-booking platform ("Concierge") that qualifies web-form leads and books them directly onto the right rep's calendar in real time. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Scheduling & Routing](../categories/scheduling-routing.md)

- [Chili Piper](../tools/chili-piper.md) chilipiper.com Inbound lead routing and meeting-scheduling platform - converts web-form submissions and inbound leads into booked meetings in seconds, with rep-availability and fairness-rule logic. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Inbound & PLG Chat](../categories/inbound-plg-chat.md) · Cross listed, canonical home is Scheduling & Routing

- [Clay](../tools/clay.md) clay.com A spreadsheet-style workflow/orchestration tool that runs lead and company records through "waterfall" lookups across 100-200+ third-party data providers (Apollo, Lusha, Clearbit, etc.) and chains automation... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Coresignal](../tools/coresignal.md) coresignal.com Sells structured B2B datasets and APIs (company, employee/people, job-posting records) scraped and normalized from public and professional-network sources, delivered as bulk datasets or pay-per-call enrichment... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [dbt (dbt platform remote MCP)](../tools/dbt.md) getdbt.com The transformation layer of the modern data stack: SQL models, tests and documentation compiled and run against a warehouse, with a hosted "dbt platform" (formerly dbt Cloud) that adds scheduling, a Semantic... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [RevOps Infra](../categories/revops-infra.md) · CLI: dbt

- [Derrick](../tools/derrick.md) derrick-app.com A credit-metered B2B enrichment engine sold primarily as a Google Sheets add-on, plus a REST API and a hosted MCP server, covering email finding, mobile phone finding, LinkedIn profile lookup, company... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Explorium](../tools/explorium.md) explorium.ai Aggregates roughly 50 third-party data sources into one API/platform for business and prospect lookup (firmographics, contacts, technographics, business events), claiming coverage of 150M+ companies and 800M+... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Fiber AI](../tools/fiber-ai.md) fiber.ai B2B search and enrichment APIs for finding companies and people by structured filters or natural language, then revealing work emails and phone numbers with live LinkedIn data. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Grain](../tools/grain.md) grain.com AI meeting notetaker that records and transcribes calls and builds a searchable, cross-meeting library synced to the CRM. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Conversation Intel](../categories/conversation-intel.md)

- [Granola](../tools/granola.md) granola.ai General-purpose AI notetaker that generates enhanced meeting notes and summaries from a local desktop app. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Conversation Intel](../categories/conversation-intel.md) · CLI: granola (community)

- [Hex](../tools/hex.md) hex.tech A collaborative data workspace (SQL and Python notebooks, published apps, a conversational "Threads" analysis mode) used by data and RevOps teams to answer questions on top of the warehouse. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [RevOps Infra](../categories/revops-infra.md)

- [Instantly](../tools/instantly.md) instantly.ai Cold email sending platform providing mailbox infrastructure, warmup, deliverability management, sequencing, and lead sourcing. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [JustCall](../tools/justcall.md) justcall.io A cloud phone, SMS and WhatsApp platform for sales and support teams built by SaaS Labs, with a sales dialer, CRM integrations and AI voice agents, plus a hosted MCP server that lets an assistant read and act... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [La Growth Machine](../tools/la-growth-machine.md) lagrowthmachine.com Multi-channel prospecting platform that sequences outreach across LinkedIn, email, Twitter/X, and voice notes/calls from one campaign builder, with built-in lead enrichment. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [Make](../tools/make.md) make.com A visual, node-based workflow automation platform ("scenarios") connecting 3,000+ apps, with newer AI-agent and natural-language-build features layered on top. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [RevOps Infra](../categories/revops-infra.md)

- [Metorial](../tools/metorial.md) metorial.com A hosted MCP gateway that gives AI agents/"AI employees" centralized, governed access to a company's SaaS tools (Google Workspace, Microsoft 365, GitHub, Jira, Slack, Teams, Stripe, Salesforce, Zendesk, and... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [MCP Layer](../categories/mcp-infrastructure.md) · CLI: metorial

- [Ocean.io](../tools/ocean-io.md) ocean.io A company-search and "lookalike" prospecting tool that finds businesses similar to a given target account based on industry, size, geography, and website content, and exports the resulting account lists. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Octave](../tools/octave.md) octavehq.com A GTM context engine that stores a company's ICP, personas, positioning, competitors, proof points, and objections as one structured model, then serves that model to sequences, scripts, and AI agents at... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [RevOps Infra](../categories/revops-infra.md)

- [Offorte](../tools/offorte.md) offorte.com Proposal software (templates, interactive web proposals, e-signature, open and read tracking, automation sets) for small businesses, with a REST API, webhooks and an MCP server published by the vendor. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Proposals & Deals](../categories/proposals-deals.md)

- [PhantomBuster](../tools/phantombuster.md) phantombuster.com General browser-automation/data-extraction platform ("Phantoms") that runs cloud scripts to scrape and act on LinkedIn and other web platforms - widely used as a LinkedIn outbound backbone rather than a... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Engagement & Outbound](../categories/engagement-outbound.md) · CLI: phantombuster (community)

- [Pipedream MCP](../tools/pipedream-mcp.md) pipedream.com Pipedream's existing workflow/integration platform re-exposed as hosted MCP servers, giving an MCP client access to 3,000+ connected apps and 10,000+ pre-built tools via Pipedream Connect. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Reply.io](../tools/reply-io.md) reply.io Multichannel sales engagement platform for email, LinkedIn, call, and SMS outreach with an AI SDR product layered on top. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Engagement & Outbound](../categories/engagement-outbound.md) · CLI: reply

- [Reply.io (Jason AI)](../tools/reply-io.md) reply.io A multichannel sales engagement platform whose AI layer ("Jason AI," per widely reported branding) generates outreach emails/follow-ups and automates sequencing across email, calls, and tasks. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [AI SDRs](../categories/ai-sdr-agents.md) · Cross listed, canonical home is Engagement & Outbound · CLI: reply

- [RingCentral App Connect MCP](../tools/ringcentral-app-connect-mcp.md) ringcentral.com One of four MCP servers RingCentral publishes through its Labs programme; this one bridges RingCentral telephony to whichever CRM the customer has linked through the App Connect browser extension, so an... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [RocketReach](../tools/rocketreach.md) rocketreach.co A large contact/company lookup database queried by name, company domain, or LinkedIn profile to find work emails, direct dials, and mobile numbers, with bulk lookup and CRM/Salesforce sync. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Salesforge](../tools/salesforge.md) salesforge.ai Multi-channel cold outreach platform (email + LinkedIn) with an AI SDR product ("Agent Frank") layered on top of standard sequencing. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Engagement & Outbound](../categories/engagement-outbound.md) · CLI: forge

- [Salesforge (Agent Frank)](../tools/salesforge.md) salesforge.ai An AI agent ("Agent Frank") that prospects, writes tailored outreach, sends across email and LinkedIn, manages follow-up sequences, and books meetings - positioned to either join a human team or fully replace... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [AI SDRs](../categories/ai-sdr-agents.md) · Cross listed, canonical home is Engagement & Outbound · CLI: forge

- [Saleshandy](../tools/saleshandy.md) saleshandy.com A cold-email outreach platform with sequences, sender rotation, email warm-up and deliverability tooling, plus a Lead Finder contact database, exposed to AI clients through an MCP server that can create... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Engagement & Outbound](../categories/engagement-outbound.md) · CLI: saleshandy

- [SalesQL](../tools/salesql.md) salesql.com A LinkedIn-first contact database and browser extension that returns verified work emails and mobile numbers, with bulk CSV enrichment, an email verifier, a REST API and an MCP server that exposes search and... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Smartlead](../tools/smartlead.md) smartlead.ai Cold email outreach platform for managing campaigns across many mailboxes, with built-in deliverability infrastructure and a unified reply inbox. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Engagement & Outbound](../categories/engagement-outbound.md) · CLI: smartlead

- [SparkToro](../tools/sparktoro.md) sparktoro.com Audience-research tool that shows what a defined audience (by keyword, website, social account, or podcast) reads, watches, listens to, and follows, by combining social-graph, search, and web-crawl data. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Community & Dark Social](../categories/community-dark-social.md)

- [Sumble](../tools/sumble.md) sumble.com Builds an account-intelligence knowledge graph by continuously scanning tens of millions of public sources (job boards, company sites, social media, regulatory filings) to map org structure, tech stack, and... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Signals & Intent](../categories/signals-intent-abm.md)

- [tl;dv](../tools/tl-dv.md) tldv.io Records and transcribes Zoom, Google Meet, and Microsoft Teams calls, layering on sales coaching (playbook monitoring, objection handling) at higher tiers. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Conversation Intel](../categories/conversation-intel.md) · CLI: tldv (community)

- [Trainual](../tools/trainual.md) trainual.com SOP and process-documentation platform for onboarding and training, positioned more broadly at operations/HR than sales-specific enablement, with AI-assisted SOP drafting. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Enablement & Coaching](../categories/enablement-coaching.md)

- [Waalaxy](../tools/waalaxy.md) waalaxy.com Chrome-extension-based LinkedIn (+ email) prospecting tool that automates invitations, messages, and multi-step campaigns, with a built-in prospect finder. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [Woodpecker](../tools/woodpecker.md) woodpecker.co Cold email and LinkedIn outreach automation tool with inbox rotation, adaptive sending, and centralized reply management. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Engagement & Outbound](../categories/engagement-outbound.md) · CLI: woodpecker

- [Amplemarket](../tools/amplemarket.md) amplemarket.com An all-in-one sales engagement platform that finds leads, runs multichannel outbound sequences (email/social/phone/voice), and optimizes email deliverability. [Official MCP](../mcp/official.md) · [Enterprise leaning](../gates/enterprise-leaning.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [Paragon (ActionKit MCP)](../tools/paragon.md) useparagon.com An embedded integration platform for SaaS products, whose ActionKit product exposes a stated 1,000-plus actions across 130-plus third-party applications through one API and one MCP server, with Paragon... [Official MCP](../mcp/official.md) · [Enterprise leaning](../gates/enterprise-leaning.md) · [MCP Layer](../categories/mcp-infrastructure.md) · CLI: para

- [Ada](../tools/ada.md) ada.cx Enterprise AI customer-experience platform (voice, chat, email) that automates inbound support and sales conversations end-to-end. [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md) · [Inbound & PLG Chat](../categories/inbound-plg-chat.md)

- [Anaplan (PlanIQ / Anaplan Forecaster)](../tools/anaplan.md) anaplan.com Connected-planning platform whose AI forecasting engine - originally branded PlanIQ, now superseded by "Anaplan Forecaster" (launched October 2025) - generates time-series demand/sales/revenue forecasts that... [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md) · [Forecasting & Revenue](../categories/forecasting-revenue.md)

- [Apollo.io Sequences (Emailer Campaigns)](../tools/apollo-io-sequences.md) apollo.io Apollo's outbound-sequencing feature - multi-step, multi-channel (email/call/task) cadences that enroll contacts pulled from Apollo's prospecting database and track send/reply state. [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [Common Room](../tools/common-room.md) commonroom.io Aggregates buyer/community engagement signals - Slack, Discord, GitHub activity (stars, PRs, issues), product usage, and third-party intent data (Bombora integration) - across a company's community/product... [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md) · [Signals & Intent](../categories/signals-intent-abm.md) · CLI: cr

- [Common Room](../tools/common-room.md) commonroom.io See the full RESEARCHED entry in 05-signals-intent-abm.md (Common Room is filed there as its canonical home in this directory) - aggregates Slack, Discord, GitHub, product-usage, and third-party intent signals... [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md) · [Community & Dark Social](../categories/community-dark-social.md) · Cross listed, canonical home is Signals & Intent · CLI: cr

- [Gong](../tools/gong.md) gong.io Records, transcribes, and analyzes sales calls and emails, then rolls the signals into deal-risk scores, coaching data, and revenue forecasts. [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md) · [Conversation Intel](../categories/conversation-intel.md)

- [Ironclad](../tools/ironclad.md) ironcladapp.com Contract lifecycle management (CLM) platform for drafting, negotiating, and managing contracts with workflow automation across legal, sales, and procurement teams - sales-adjacent rather than a sales tool... [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md) · [Proposals & Deals](../categories/proposals-deals.md)

- [Looker](../tools/looker.md) cloud.google.com Google Cloud's governed BI platform (LookML semantic model, explores, Looks, dashboards, embedded analytics) that sits on top of a warehouse; two first-party MCP routes exist, a local MCP Toolbox prebuilt... [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md) · [RevOps Infra](../categories/revops-infra.md)

- [mcp.run / TurboMCP](../tools/mcp-run-turbomcp.md) turbomcp.ai An enterprise self-hosted MCP gateway and management platform - a trusted, admin-curated registry plus RBAC-controlled deployment of MCP servers across a team's own infrastructure (K8s, PaaS, VMs). [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Meltwater](../tools/meltwater.md) meltwater.com Media-intelligence and social-listening platform that consolidates news coverage, social conversations, and AI-generated content into prioritized alerts and workflows for PR, comms, and marketing teams. [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md) · [Community & Dark Social](../categories/community-dark-social.md) · CLI: generateJwk

- [Nooks](../tools/nooks.md) nooks.ai AI parallel dialer and "virtual salesfloor" combining multi-line dialing, live manager coaching, and prospecting assistance for SDR teams. [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [Pigment](../tools/pigment.md) pigment.com AI-native enterprise business-planning (EPM) platform used across finance, sales, HR, and supply chain; GTM-relevant use cases include capacity, territory, and quota planning and revenue-growth-management... [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md) · [Forecasting & Revenue](../categories/forecasting-revenue.md)

- [Salesforce (core CRM/platform) + Agentforce](../tools/salesforce-agentforce.md) salesforce.com A cloud CRM/platform for managing sales, service, and marketing records via a database, APIs, and a low-code app layer, with Agentforce as a layer on top for configuring autonomous AI agents that read... [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md) · [RevOps Infra](../categories/revops-infra.md) · CLI: sf

- [Klavis AI](../tools/klavis-ai.md) klavis.ai Primarily an AI-agent training-data company - it builds "live environments for training AI agents" (long-horizon coding tasks and agentic tool-use scenarios), and separately mentions "production MCP servers"... [Official MCP](../mcp/official.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Reclaim.ai](../tools/reclaim-ai.md) reclaim.ai AI calendar app that auto-schedules tasks, habits, and focus time around a user's existing meetings, dynamically defending and rebalancing the calendar as things change. [Official MCP](../mcp/official.md) · [Gate unknown](../gates/unknown.md) · [Scheduling & Routing](../categories/scheduling-routing.md) · CLI: reclaim-cli (community)

- [RevenueHero](../tools/revenuehero.md) revenuehero.io Instant meeting-scheduling and inbound-lead-routing tool that qualifies web-form leads against CRM data and books them directly onto the right rep's calendar without a redirect. [Official MCP](../mcp/official.md) · [Gate unknown](../gates/unknown.md) · [Scheduling & Routing](../categories/scheduling-routing.md)

- [Zoom Revenue Accelerator](../tools/zoom-revenue-accelerator.md) zoom.com Zoom's built-in conversation/revenue-intelligence layer that analyzes Zoom Meetings and Phone calls for deal insights, scorecards, and account activity. [Official MCP](../mcp/official.md) · [Gate unknown](../gates/unknown.md) · [Conversation Intel](../categories/conversation-intel.md)

- [Loom](../tools/loom.md) loom.com Async video-messaging platform; in its sales use case, reps record personalized video messages with name/company variables, track prospect views, and embed CTAs/booking links directly in the video. [Community MCP](../mcp/community.md) · [Free to start](../gates/free.md) · [Video Prospecting](../categories/video-prospecting.md)

- [People Data Labs](../tools/people-data-labs.md) peopledatalabs.com A raw person/company data API that returns profile records (name, job history, education, skills, social handles, contact fields) matched by identifiers like email, name, or LinkedIn URL, plus SQL-style bulk... [Community MCP](../mcp/community.md) · [Free to start](../gates/free.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Aircall](../tools/aircall.md) aircall.io A cloud phone system and call centre for sales and support teams (numbers, dialer campaigns, call recording, SMS, CRM integrations) with a public REST API and webhooks. [Community MCP](../mcp/community.md) · [Paid, self-serve](../gates/paid.md) · [Engagement & Outbound](../categories/engagement-outbound.md) · CLI: aircall (community)

- [Mention](../tools/mention.md) mention.com Monitors web and social mentions across a claimed 1 billion+ sources in real time, layering sentiment/reach analytics and a unified social inbox on top of the monitoring feed. [Community MCP](../mcp/community.md) · [Paid, self-serve](../gates/paid.md) · [Community & Dark Social](../categories/community-dark-social.md)

- [Motion](../tools/motion.md) usemotion.com AI-driven work-management app that auto-schedules a user's tasks, projects, and meetings onto their calendar around priorities and deadlines, bundled with note-taking and document tools. [Community MCP](../mcp/community.md) · [Paid, self-serve](../gates/paid.md) · [Scheduling & Routing](../categories/scheduling-routing.md)

- [Overloop](../tools/overloop.md) overloop.com Sales engagement and lead-gen platform for finding, verifying, and contacting B2B prospects via automated email and LinkedIn campaigns. [Community MCP](../mcp/community.md) · [Paid, self-serve](../gates/paid.md) · [Engagement & Outbound](../categories/engagement-outbound.md) · CLI: overloop (community)

- [SavvyCal](../tools/savvycal.md) savvycal.com Prospect-facing scheduling/booking-page tool (Calendly competitor) built around letting invitees overlay their own calendar on the organizer's availability, with Collective/Round-Robin/Group team-scheduling... [Community MCP](../mcp/community.md) · [Paid, self-serve](../gates/paid.md) · [Scheduling & Routing](../categories/scheduling-routing.md)

- [Syften](../tools/syften.md) syften.com Monitors Reddit, Hacker News, X/Twitter, Bluesky, Mastodon, GitHub, YouTube, Slack communities, and general web/forum sources for keyword mentions, delivering alerts via email, Slack, RSS, webhook, or API. [Community MCP](../mcp/community.md) · [Paid, self-serve](../gates/paid.md) · [Community & Dark Social](../categories/community-dark-social.md)

- [Trigify (Trigify.io)](../tools/trigify.md) trigify.io Monitors LinkedIn, X/Twitter, Reddit, YouTube, and podcasts for keyword mentions and engagement (likes, comments, shares, job changes), mapping who engaged with that content into an "engagement graph" filtered... [Community MCP](../mcp/community.md) · [Paid, self-serve](../gates/paid.md) · [Signals & Intent](../categories/signals-intent-abm.md) · CLI: trigify

- [Unify](../tools/unify.md) unifygtm.com A hybrid signals-plus-agent platform: AI agents build targeted account/prospect lists from 40+ data sources, write personalized outbound copy, and run multi-channel sequences triggered by intent signals... [Community MCP](../mcp/community.md) · [Paid, self-serve](../gates/paid.md) · [AI SDRs](../categories/ai-sdr-agents.md) · CLI: unify-cli (community)

- [Brandwatch](../tools/brandwatch.md) brandwatch.com Enterprise consumer-intelligence and social-listening suite spanning social media management, influencer marketing, search/GenAI-mention monitoring, and analyst-backed media intelligence. [Community MCP](../mcp/community.md) · [Enterprise only](../gates/enterprise-only.md) · [Community & Dark Social](../categories/community-dark-social.md)

- [Chorus](../tools/chorus.md) zoominfo.com Records, transcribes, and analyzes sales calls, meetings, and emails, and syncs the resulting insights into the CRM. [Community MCP](../mcp/community.md) · [Enterprise only](../gates/enterprise-only.md) · [Conversation Intel](../categories/conversation-intel.md) · CLI: gtm

- [Copy.ai (GTM AI Platform)](../tools/copy-ai.md) copy.ai Pivoted from an AI copywriting tool to a workflow-building platform ("Copy Agents") that automates GTM tasks - prospecting/lead research, inbound enrichment, content generation, deal analysis - via user-built... [Community MCP](../mcp/community.md) · [Enterprise only](../gates/enterprise-only.md) · [AI SDRs](../categories/ai-sdr-agents.md)

- [Jiminny](../tools/jiminny.md) jiminny.com Records, transcribes, and scores sales calls, syncing action items and summaries into the CRM. [Community MCP](../mcp/community.md) · [Enterprise only](../gates/enterprise-only.md) · [Conversation Intel](../categories/conversation-intel.md)

- [Loopio](../tools/loopio.md) loopio.com RFP/RFI response-management platform with a searchable content library, AI-assisted answer drafting, and collaborative proposal workflows for larger bid teams. [Community MCP](../mcp/community.md) · [Enterprise only](../gates/enterprise-only.md) · [Proposals & Deals](../categories/proposals-deals.md)

- [WorkRamp](../tools/workramp.md) workramp.com Corporate learning and training platform ("Business Academy") for employee onboarding, sales enablement, and customer education content, with AI-assisted content creation. [Community MCP](../mcp/community.md) · [Enterprise only](../gates/enterprise-only.md) · [Enablement & Coaching](../categories/enablement-coaching.md)

- [ACA Automated Client Acquisition](../tools/aca-automated-client-acquisition.md) automatedclientacquisition.com AI content generation, lead management, and multi-channel outreach campaigns. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [Accelo MCP by Selerity](../tools/accelo-mcp-by-selerity.md) github.com Unofficial MCP server for the Accelo CRM platform. Contribute to Selerity/accelo-mcp development by creating an account on GitHub. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Accordo Agent CRM MCP](../tools/accordo-agent-crm-mcp.md) accordo.dev The open-source framework your coding agent - Claude Code, Codex, Gemini CLI - uses to build a custom CRM as code you own, with deterministic policy and audit. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [ActiveCampaign MCP by pipeworx](../tools/activecampaign-mcp-by-pipeworx.md) github.com ActiveCampaign MCP Pack - email marketing + CRM (API v3). - pipeworx-io/mcp-activecampaign [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Acuris Geo MCP](../tools/acuris-geo-mcp.md) api.acuris-geo.com Address validation & geocoding for AI agents: 240+ countries, UK PAF, free US/CA enrichment [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Agent Cold Email MCP (Coldrig)](../tools/agent-cold-email-mcp.md) coldrig.dev Coldrig gives Codex, Claude Code, Cursor, and other AI agents one API and MCP surface for cold-email domains, mailboxes, warmup, campaigns, replies, and enforced sending guardrails. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [AlphaAI](../tools/alphaai.md) alphai.io Financial news MCP server for ChatGPT, Claude, Gemini, Cursor, VS Code, Windsurf and any spec-compliant client. Relevance-scored feed, OAuth 2.1, 13 tools. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [amoCRM MCP by theYahia](../tools/amocrm-mcp-by-theyahia.md) github.com MCP server for amoCRM - leads, contacts, pipelines, tasks (Russia) - theYahia/amocrm-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [AmpUp GTM Chat](../tools/ampup-gtm-chat.md) chat.ampup.ai Chat over your CRM, meetings, and knowledge base. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Andru Revenue Intelligence](../tools/andru-revenue-intelligence.md) andru.ai Revenue intelligence for SaaS founders: ICP scoring, persona profiling, competitive positioning. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Forecasting & Revenue](../categories/forecasting-revenue.md)

- [Anyquery](../tools/anyquery.md) anyquery.dev Run SQL on GitHub, Notion, Spotify, Gmail, Airtable, Google Sheets, CSVs, Parquet, logs - and 40+ more. One binary, one dialect. Then hand it to an LLM over MCP. Open source, AGPL-3.0. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Apex Log MCP by Certinia](../tools/apex-log-mcp-by-certinia.md) npmjs.com Apex Log MCP Server - AI-powered Salesforce Apex debug log analysis. Find performance bottlenecks, slow methods, SOQL bottlenecks, and governor limit issues. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Apex MCP SDK by bfmvsa](../tools/apex-mcp-sdk-by-bfmvsa.md) github.com Apex SDK for building Model Context Protocol (MCP) servers natively in Salesforce - bfmvsa/mcp-apex-sdk [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Apollo Agent CLI by bcharleson](../tools/apollo-agent-cli-by-bcharleson.md) github.com Agent-native CLI and MCP server for Apollo.io REST API - bcharleson/apollo-agent-cli [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Apollo MCP by adelaidasofia](../tools/apollo-mcp-by-adelaidasofia.md) github.com FastMCP server for Apollo.io - 22 tools: sequences, campaign health, mailbox warmup, enrichment, CRM, credits. Includes Cloudflare bypass and undocumented API discoveries. - adelaidasofia/apollo-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Apollo MCP by AgenTeam](../tools/apollo-mcp-by-agenteam.md) github.com An open-source, MIT Licensed, custom MCP server for Apollo.io - AgenTeam-AI-2026/mcp-apollo [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Apollo MCP by BlockchainRev](../tools/apollo-mcp-by-blockchainrev.md) github.com MCP server for Apollo.io sales engagement platform - 34+ tools for prospecting, outreach automation, and pipeline management - BlockchainRev/apollo-mcp-server [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Apollo MCP by Eden-Anthony](../tools/apollo-mcp-by-eden-anthony.md) github.com Quick little MCP for those that use Apollo.io for prospecting - Eden-Anthony/apollo-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Apollo MCP by fuzzylabs](../tools/apollo-mcp-by-fuzzylabs.md) github.com MCP server for Apollo.io integration - enables AI assistants to search accounts, enrich contacts, and access sales intelligence data through natural language. - fuzzylabs/apollo-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Apollo MCP by Inferensys](../tools/apollo-mcp-by-inferensys.md) github.com MCP server for Apollo.io, search leads, enrich contacts, manage sequences & CRM from Claude Code, Cursor, or any MCP client. 27 tools covering the full Apollo.io API. - Inferensys/apollo-io-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Apollo MCP by kingler](../tools/apollo-mcp-by-kingler.md) github.com MCP server for Apollo.io sales intelligence integration with 9 tools for lead generation - kingler/apollo-io-mcp-server [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Apollo MCP by louis030195](../tools/apollo-mcp-by-louis030195.md) github.com let AGI print dollars for you. Contribute to louis030195/apollo-io-mcp development by creating an account on GitHub. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Apollo MCP by maxmulvey](../tools/apollo-mcp-by-maxmulvey.md) github.com MCP server for Apollo.io integration - enables AI assistants to search accounts, enrich contacts, and access sales intelligence data through natural language. - maxmulvey/apollo-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Apollo MCP by mayanksingh09](../tools/apollo-mcp-by-mayanksingh09.md) github.com MCP server that enables AI assistants to draft personalized sales emails through Apollo.io. Search prospects, enrich contact data, and automatically generate tailored outreach messages based on recipient... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Apollo MCP by shariqriazz](../tools/apollo-mcp-by-shariqriazz.md) github.com MCP server for Apollo.io lead search, contact enrichment, account data, sequences, and engagement reporting. - shariqriazz/apollo-io-mcp-server [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Apollo MCP by wmarceau](../tools/apollo-mcp-by-wmarceau.md) github.com Apollo.io lead enrichment and prospecting via MCP [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Apollo MCP Plugin (apolloio)](../tools/apollo-mcp-plugin.md) github.com Connect Claude Code + Cowork to Apollo MCP via this plugin - apolloio/apollo-mcp-plugin [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Apollo MCP Plugin by apolloio](../tools/apollo-mcp-plugin-by-apolloio.md) github.com Connect Claude Code + Cowork to Apollo MCP via this plugin - apolloio/apollo-mcp-plugin [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Apollo.io CLI by dipankar](../tools/apollo-io-cli-by-dipankar.md) github.com A powerful command-line interface for the Apollo.io API, designed for both humans and AI agents. - dipankar/apollo-io-cli [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Artefact MCP](../tools/artefact-mcp.md) github.com Revenue intelligence MCP server: RFM analysis, 14.5-point ICP scoring, pipeline health scoring. Embeds Artefact Formula methodology. HubSpot integration. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Artefact Revenue Intelligence MCP](../tools/artefact-revenue-intelligence-mcp.md) github.com Revenue intelligence MCP server: RFM analysis, 14.5-point ICP scoring, pipeline health scoring. Embeds Artefact Formula methodology. HubSpot integration. - artefactventures/artefact-mcp-server [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Forecasting & Revenue](../categories/forecasting-revenue.md)

- [Ascend GTM Gateway](../tools/ascend-gtm-gateway.md) ascend-gateway-v5.ascendgtm.workers.dev 34-tool GTM gateway: CRMs, ad platforms, analytics, Google Workspace, AWS, and LLM orchestration. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [AstroFabric MCP](../tools/astrofabric-mcp.md) astrofabric.ai Build with AstroFabric's autonomous intelligence platform using REST, MCP and CLI across datasets, enrichment, signals, audiences and governed delivery. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Attio MCP by Arkel-ai](../tools/attio-mcp-by-arkel-ai.md) github.com Community MCP server for Attio CRM so agents can work pipeline and account data. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Attio MCP by hmk](../tools/attio-mcp-by-hmk.md) github.com Contribute to hmk/attio-mcp-server development by creating an account on GitHub. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [AU BizIntel MCP](../tools/au-bizintel-mcp.md) github.com Australian Business Intelligence MCP Server - ABN lookup, business search, AI prospect intelligence for AI agents - ljdigital/au-bizintel-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Autostackup Sales MCP](../tools/autostackup-sales-mcp.md) github.com Contribute to Autostackup/autostackup development by creating an account on GitHub. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [B2B Enrichment MCP by Aleksey-Panf](../tools/b2b-enrichment-mcp-by-aleksey-panf.md) github.com Unified MCP server combining Hunter.io and Apollo for B2B lead enrichment - Aleksey-Panf/b2b-enrichment-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [B2B Lead Enrichment MCP](../tools/b2b-lead-enrichment-mcp.md) lead-enrichment-mcp.agent-infra.workers.dev Remote MCP server to enrich company profiles with structured B2B data and confidence scores. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Backengine MCP](../tools/backengine-mcp.md) mcp.backengine.ai Surface customer & prospect context from Slack, email, transcripts and tickets in any MCP client. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Conversation Intel](../categories/conversation-intel.md)

- [Bavlio](../tools/bavlio.md) bavlio.com Bavlio is an AI-powered sales outreach platform that researches every lead and writes personalized cold email and LinkedIn campaigns for your team. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [BD Desk MCP by iaj6](../tools/bd-desk-mcp-by-iaj6.md) github.com An end-to-end BD pipeline on Claude Managed Agents - lead sourcing, research, outreach drafting, and a deployable CRM. The system researches and drafts; a human always sends. - iaj6/bd-desk [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Beacon MCP by enrichgateagent](../tools/beacon-mcp-by-enrichgateagent.md) github.com Search engine for open-source AI agents, as an MCP server. Find 3,800+ agents by capability from Claude/Cursor/Cline. npx -y beacon-mcp - enrichgateagent-png/beacon-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [BigDataCorp MCP](../tools/bigdatacorp-mcp.md) github.com Open-source MCP servers for Latin American commerce - Pix, NF-e, banking, fiscal, logistics, and messaging across Brazil, Mexico, Argentina, Colombia, Chile, and Peru. MIT, on npm. - codespar/mcp-dev-latam [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Bird MCP by UsefulAPI](../tools/bird-mcp-by-usefulapi.md) bird.usefulapi.io Read SMS, WhatsApp, email, contacts and audiences from your Bird workspace, plus safe CRM writes. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [Bitrix24 MCP by john7ross](../tools/bitrix24-mcp-by-john7ross.md) github.com Universal, full-featured, portable MCP server for the Bitrix24 REST API (CRM, tasks, scrum, calendar, disk, users, messaging) - read and write. - john7ross/BitrixMCP [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Bitrix24 MCP by theYahia](../tools/bitrix24-mcp-by-theyahia.md) github.com MCP server for Bitrix24 - CRM, deals, contacts, tasks (Russia) - theYahia/bitrix24-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Blitz API Open Source](../tools/blitz-api-open-source.md) github.com Open-source Apollo.io-style lead-sourcing UI powered by the Blitz API - malharlakdawala/blitzapi-opensource [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [BNI MCP by alexaltovate](../tools/bni-mcp-by-alexaltovate.md) github.com MCP server for BNI member search in Germany & Austria - find members, analyze chapter gaps, prepare 1:1 outreach - alexaltovate/bni-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Brand Intel MCP](../tools/brand-intel-mcp.md) github.com Domain & brand intelligence for AI agents - company enrichment, domain intelligence, tech stack detection, brand research. MCP + x402. - FoundryNet/brand-intel-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Buildforce Agentic Ops](../tools/buildforce-agentic-ops.md) buildforce.io AI platform manager that automates Salesforce, HubSpot, and ServiceNow operations. 200+ continuous health checks, AI consulting in your stack, and CI/CD automation - replacing $7K/month managed-services... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Bytemine MCP](../tools/bytemine-mcp.md) github.com Bytemine MCP Server - Search 130M+ B2B contacts and enrich profiles with verified emails & phone numbers directly from Claude, Cursor, and other AI assistants via the Model Context Protocol. -... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Capsule CRM MCP by MonadsAG](../tools/capsule-crm-mcp-by-monadsag.md) github.com Contribute to MonadsAG/capsulecrm-mcp development by creating an account on GitHub. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Capsule CRM MCP by soil-dev](../tools/capsule-crm-mcp-by-soil-dev.md) github.com Capsule CRM tools for Claude. Local install via npx, org-wide via Custom Connectors. - soil-dev/capsulemcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Chatflow](../tools/chatflow.md) chatflow.biz WhatsApp CRM for AI agents: search contacts, read chats, manage the sales pipeline, send messages. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Cirra AI Salesforce Admin MCP](../tools/cirra-ai-salesforce-admin-mcp.md) mcp.cirra.ai Comprehensive Salesforce administration and data management capabilities [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [CiviCRM MCP by YogiAdhik](../tools/civicrm-mcp-by-yogiadhik.md) github.com Model Context Protocol server for CiviCRM - AuthX-first, schema-introspected, write-gated. - YogiAdhik/civicrm-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Clay MCP by bpw-civic](../tools/clay-mcp-by-bpw-civic.md) github.com MCP server for Clay.com API - people and company enrichment - bpw-civic/clay-mcp-server [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Clay MCP by shanefirek](../tools/clay-mcp-by-shanefirek.md) github.com 73-tool MCP server for Clay. 1,100+ enrichment providers, waterfall sequences, CRM sync. - shanefirek/clay-mcp-public [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Clay to Instantly/Smartlead MCP](../tools/clay-to-instantly-smartlead-mcp.md) github.com MCP server for the Mamba Labs Sequencer Lead Push actor on Apify. Push enriched leads into an Instantly or Smartlead campaign. - mambalabsdev/mcp-clay-to-instantly-smartlead-push [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Clay-CXD by xprooket](../tools/clay-cxd-by-xprooket.md) github.com Contextual Memory Intelligence for AI Systems - Persistent memory, cognitive tools, and adaptive reasoning capabilities for LLMs Experimental memory system for LLMs (see MemMimic for optimized version) -... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Clint CRM MCP by Franky-Neto](../tools/clint-crm-mcp-by-franky-neto.md) github.com Clint CRM MCP Server. This is a non oficial MCP Server for Clint CRM. - Franky-Neto/mcp-clint-crm [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Close CRM MCP by pipeworx](../tools/close-crm-mcp-by-pipeworx.md) github.com Close CRM MCP Pack - wraps the Close (close.com) API v1. - pipeworx-io/mcp-close-crm [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Codex Data MCP](../tools/codex-data-mcp.md) github.com A Model Context Protocol server for the Codex API. Contribute to Codex-Data/codex-mcp development by creating an account on GitHub. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Cognis Coldforge MCP](../tools/cognis-coldforge-mcp.md) github.com Render personalized cold-outreach sequences from Markdown templates plus a contacts CSV, with spam-score linting. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Cognis CRM Sync MCP](../tools/cognis-crm-sync-mcp.md) github.com MCP tooling to sync CRM records for Cognis Digital GTM workflows. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Cognis Dealflow MCP](../tools/cognis-dealflow-mcp.md) github.com Model a sales pipeline as a YAML state machine and compute conversion rates, stage velocity, and weighted forecasts. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Cognis Enrichr MCP](../tools/cognis-enrichr-mcp.md) cognis.digital Enrich a leads CSV with firmographic data via Cognis Digital tooling. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Cognis Leadforge MCP](../tools/cognis-leadforge-mcp.md) github.com Lightweight MCP-native CRM pipeline with email sequences. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Coherence MCP](../tools/coherence-mcp.md) getcoherence.io Coherence is the agentic customer operations platform that connects CRM data, email, campaigns, websites, workflows, and AI agents in one shared context. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Coldforge](../tools/coldforge.md) github.com Honest, local-first cold outreach toolkit: research, personalize, sequence, send, follow. CLI + MCP server, no SaaS, no required API keys. - Makeph/coldforge [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Company Enrichment API by Br0ski777](../tools/company-enrichment-api-by-br0ski777.md) github.com Company enrichment from any domain. Firmographics, socials, tech stack, contact info, address. Built for sales prospecting and CRM. -- x402 micropayment API + MCP server for AI agents -... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Company Enrichment MCP by sercanmetalore](../tools/company-enrichment-mcp-by-sercanmetalore.md) github.com Firmographic profile, NACE/NAICS categorization, and contact extraction from a company domain. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [CompCode MCP](../tools/compcode-mcp.md) compcode.ai The first commission platform where plans are created, modified, and versioned via API. Statements your team trusts. Plan changes in minutes, not weeks. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Forecasting & Revenue](../categories/forecasting-revenue.md)

- [Craft GTM MCP](../tools/craft-gtm-mcp.md) github.com 8 strategic GTM execution tools - PMF, Launch, Retention, Partners, Crisis, Competitive Intel - shashwatgtm/craft-gtm-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Crevideo Reach](../tools/crevideo-reach.md) crevideo.com Scale TikTok Shop affiliate outreach with Crevideo Reach. Find affiliate creators, automate outreach, track ROI, and manage TikTok Shop creator partnerships from one platform. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [Crisp MCP](../tools/crisp-mcp.md) api.mcp.ai Customer support, live chat, CRM and helpdesk on Crisp with the full official REST API v1 (api.crisp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Inbound & PLG Chat](../categories/inbound-plg-chat.md)

- [CrispHive MCP](../tools/crisphive-mcp.md) docs.crisphive.com The scheduling & dispatch API for field-service teams. Create bookings, preview emergency cascades, and map technicians to service boundaries. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Scheduling & Routing](../categories/scheduling-routing.md)

- [CRM AI MCP by MEOK](../tools/crm-ai-mcp-by-meok.md) meok.ai ≡ƒöî Exposes Customer relationship management toolkit: lead scoring, deal stage prediction, follow-up scheduling, customer health scoring, and churn prediction. By MEOK AI Labs. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Curtis LinkedIn MCP](../tools/curtis-linkedin-mcp.md) github.com Curtis runs your LinkedIn outreach from your own machine, at the pace you would run it yourself - an MCP server for Claude Code and Codex that keeps going after you have stopped paying attention. -... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Customer Intelligence Hub](../tools/customer-intelligence-hub.md) github.com Customer Intelligence Hub: AI Agents for CRM Analytics, Slack & Marketing Automation | LangGraph & MCP - Gabrielm3/customer-intelligence-hub [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [DataLayer.sh MCP](../tools/datalayer-sh-mcp.md) datalayer.sh B2B enrichment API with 60M companies and 300M verified contacts. Enrich by domain or email - get intent signals, technographics, funding data, and verified contacts in one API call. MCP-native for AI agents. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [DealMachine](../tools/dealmachine.md) mcp.dealmachine.com Search and enrich US property, owner, people, and company data for sales and lead generation. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Decern CRM MCP](../tools/decern-crm-mcp.md) github.com MCP server for Decern CRM: contacts, deals, pipelines, tasks, and approvals. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Diffbot MCP by pipeworx](../tools/diffbot-mcp-by-pipeworx.md) github.com Diffbot MCP - Knowledge Graph company enrichment + web content extraction (diffbot.com) - pipeworx-io/mcp-diffbot [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [DingDawg Sales Agent MCP](../tools/dingdawg-sales-agent-mcp.md) github.com DingDawg Agent 1 - Governance receipts for AI agents. Deploy governed AI agents with signed audit trails. EU AI Act + Colorado AI Act compliant. Open-core platform. - dingdawg/dingdawg-agent-1 [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [AI SDRs](../categories/ai-sdr-agents.md)

- [Dolibarr MCP by sachitha7](../tools/dolibarr-mcp-by-sachitha7.md) github.com MCP server for Dolibarr ERP/CRM - manage thirdparties, proposals, contracts and invoices from Claude or any MCP client - sachitha7/mcp-server-dolibarr [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Elizabeth AI Agent](../tools/elizabeth-ai-agent.md) github.com Fully autonomous AI sales agent on WhatsApp Business API. Groq LLM · Firebase Cloud Functions · Firestore · Google Sheets ETL · MCP server · finite-state lead pipeline from cold outreach to qualified handoff -... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [AI SDRs](../categories/ai-sdr-agents.md)

- [Emelia](../tools/emelia.md) emelia.io Emelia simplifies LinkedIn and email prospecting, helping you find future clients with an easy-to-use platform and advanced technology. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [Enrich Company Domain Intelligence](../tools/enrich-company-domain-intelligence.md) tradego.ai Domain → company name, country, contacts, social profiles. Enterprise enrichment via Elasticsearch. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Entity Enricher MCP](../tools/entity-enricher-mcp.md) entityenricher.ai Use Entity Enricher directly from claude.ai, Claude Desktop, Claude Code, Cursor, and other MCP clients. Embedded Model Context Protocol server with 29 tools, 2 resources, OAuth 2.1 or X-API-Key auth, and... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Everything Civi MCP](../tools/everything-civi-mcp.md) github.com MCP server for complete CiviCRM operations ΓÇö 28 tools for contacts, contributions, memberships, events, cases, SearchKit, bulk import, and all 150+ entities [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [EZ@Work MCP](../tools/ez-work-mcp.md) ezatwork.com Connect EZ@Work to Claude (Claude.ai, Claude Desktop, Claude Code). Manage clients, projects, invoices, and time entries through natural conversation. OAuth 2.1, scoped tokens, full audit log. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Fintalio LinkedIn MCP](../tools/fintalio-linkedin-mcp.md) fintalio.com LinkedIn outreach MCP server - 19 tools for AI agents to prospect, sequence, and manage contacts. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [FirstTouch](../tools/firsttouch.md) firsttouch.com One MCP connection gives Claude, Cursor, Codex, and ChatGPT real hands in FirstTouch: build audiences, launch flows, discover prospects, and track pipeline. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [Fluent MCP Servers](../tools/fluent-mcp-servers.md) github.com Connect AI agents to the Fluent WordPress ecosystem using standardized MCP servers for CRM, support, boards, community, and affiliate management. - Dominotypist3077/fluent-mcp-servers [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Follow Up Boss MCP](../tools/follow-up-boss-mcp.md) github.com Connect the Follow Up Boss real estate CRM to ChatGPT, Claude, Cursor, and other AI assistants with one hosted MCP URL. OAuth-enabled server and typed Python SDK. - theperrygroup/Follow-Up-Boss-MCP [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Forency](../tools/forency.md) forency.io Investigate any website's tech stack. Forency detects the CMS, frameworks, analytics, payments, CRM and 100+ technologies that matter - via REST API and MCP server, built for AI agents first. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [FounderStack CRM](../tools/founderstack-crm.md) crm-landing-three.vercel.app FounderStack keeps your sales conversations, follow-ups, and client context in one place-without pipelines, setup, or CRM overhead. Built for founders who sell via WhatsApp, email, and DMs. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [RevOps Infra](../categories/revops-infra.md)

- [FullEnrich Skills](../tools/fullenrich-skills.md) github.com List of skills.md for Claude. Usage for Claude, MCP and Plugin - FullEnrich/fullenrich-skills [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Fundz Agent Examples](../tools/fundz-agent-examples.md) github.com Working examples for the Fundz Agent API - buying signals, SEC 8-K and Form D funding evidence for GTM agents and AI SDRs. - Fund-z/agent-examples [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [GenPark B2B Lead Waterfall Skill](../tools/genpark-b2b-lead-waterfall-skill.md) genpark.ai B2B lead waterfall enrichment cascade skill for AI agents. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [GenPark Deal Velocity Skill](../tools/genpark-deal-velocity-skill.md) genpark.ai Conversational B2B deal velocity scoring engine skill for AI agents. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Forecasting & Revenue](../categories/forecasting-revenue.md)

- [GenPark Lead Scoring Skill](../tools/genpark-lead-scoring-skill.md) genpark.ai B2B lead scoring and buyer intent data enricher skill for AI agents. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [GenPark Leads Enrichment Skill](../tools/genpark-leads-enrichment-skill.md) github.com Automated Leads Enrichment Agent Skill. Performs lookups on corporate attributes and drafts targeted B2B sales development emails. - alphaparkinc/genpark-automated-leads-enrichment-skill [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [GenPark Sales Agent MCP](../tools/genpark-sales-agent-mcp.md) github.com Autonomous outbound B2B sales development representative. - alphaparkinc/genpark-sales-agent [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [AI SDRs](../categories/ai-sdr-agents.md)

- [GenPark Waterfall Intent Scoring Skill](../tools/genpark-waterfall-intent-scoring-skill.md) genpark.ai Waterfall B2B lead enrichment with intent scoring skill for AI agents. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [GlobalSearchData Enrich MCP](../tools/globalsearchdata-enrich-mcp.md) github.com Free -> no API key required. Domain or company name -> company intelligence for AI agents. Look up company name, country, contacts, and social profiles from any MCP-compatible client. -... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Gmail Outreach MCP by brandononchain](../tools/gmail-outreach-mcp-by-brandononchain.md) github.com MCP Agent for Gmail outreach and lead nurturing. . Contribute to brandononchain/gmail-mcp-agent development by creating an account on GitHub. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [GoHighLevel MCP by NightSquawk](../tools/gohighlevel-mcp-by-nightsquawk.md) github.com We handle all your technical problems so you can focus on growing your business. Managed IT services including help desk, cybersecurity, cloud services, and network monitoring. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [GoHighLevel MCP by northrosetech](../tools/gohighlevel-mcp-by-northrosetech.md) github.com A comprehensive Model Context Protocol (MCP) server that connects AI assistants directly to your GoHighLevel CRM. Supports **60+ tools** across contacts, conversations, calendars, pipelines, payments,... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [GoHighLevel MCP by rockurbusinesscs](../tools/gohighlevel-mcp-by-rockurbusinesscs.md) github.com A small, readable MCP server for GoHighLevel API v2. Six tools, dry-run writes, and the API gotchas documented. MIT. - rockurbusinesscs-ship-it/gohighlevel-mcp-starter [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Gong.io MCP by JustinBeckwith](../tools/gong-io-mcp-by-justinbeckwith.md) github.com MCP server for Gong.io - access calls, transcripts, and users - JustinBeckwith/gongio-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Conversation Intel](../categories/conversation-intel.md)

- [Google Maps Email Extractor MCP](../tools/google-maps-email-extractor-mcp.md) github.com Google Maps businesses to leads with a verified contact email. Search by keyword or enrich a website list. No proxy. - the-ai-entrepreneur-ai-hub/google-maps-email-extractor [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Google Maps Extractor MCP by dppalukuri](../tools/google-maps-extractor-mcp-by-dppalukuri.md) github.com MCP server for Google Maps lead generation - search businesses, enrich with emails/phones/socials, score leads, export CSV. Free, no API keys needed. - dppalukuri/mcp-google-maps-extractor [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [GramClaw](../tools/gramclaw.md) gramclaw.com Connect Telegram to Claude, Cursor, and any MCP client with the GramClaw Telegram MCP server. Search chats, send messages, run broadcasts, and launch campaigns in natural language. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [GTM Alpha Consultant](../tools/gtm-alpha-consultant.md) github.com Structured data for Shashwat Ghosh - GTM Expert. Contribute to shashwatgtm/gtm-expert-schema development by creating an account on GitHub. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [GTM Alpha MCP Server](../tools/gtm-alpha-mcp-server.md) github.com Structured data for Shashwat Ghosh - GTM Expert. Contribute to shashwatgtm/gtm-expert-schema development by creating an account on GitHub. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [GTM Copilot by archanakrishnan](../tools/gtm-copilot-by-archanakrishnan.md) github.com AI-powered GTM intelligence, lead scoring, personalized outreach, and HubSpot CRM automation built with n8n, Apollo MCP, Firecrawl, and Groq AI. -... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [GTM MCP by aleprieto790](../tools/gtm-mcp-by-aleprieto790.md) github.com Run B2B cold outreach in Claude Code: find companies, verify fit, extract contacts, write sequences, and launch campaigns locally - aleprieto790-alt/gtm-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [GTMos MCP by Kai8karma](../tools/gtmos-mcp-by-kai8karma.md) kai8karma.github.io Recover the revenue trapped in your broken CRM. A tested, deterministic GTM engine, run on your data, in your environment. No new vendor touches your data. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Hecher CRM](../tools/hecher-crm.md) hecher.app Hecher by Grow Gelt is the donor management platform built for Chabad Shluchim. Part of the Grow Gelt Solutions family. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [RevOps Infra](../categories/revops-infra.md)

- [HeyLead - Autonomous LinkedIn SDR](../tools/heylead-autonomous-linkedin-sdr.md) github.com AI-powered LinkedIn SDR: voice-matched outreach, ICP generation, drip sequences, and analytics. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [HireSignal MCP](../tools/hiresignal-mcp.md) github.com Hiring-intent signals for B2B sales/GTM - an MCP server that turns live job postings into buying signals your AI agent can act on. Free demo key inside. - iusmuchandra/hiresignal-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Holded MCP](../tools/holded-mcp.md) github.com MCP server for Holded - invoicing, accounting, CRM, projects, and team [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [HubSpot MCP by amin-ale](../tools/hubspot-mcp-by-amin-ale.md) github.com HubSpot MCP server for contacts, deals, and pipelines with idempotent writes and a PII-redacted audit trail. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [HubSpot MCP by baryhuang](../tools/hubspot-mcp-by-baryhuang.md) github.com A Model Context Protocol (MCP) server that enables AI assistants to interact with HubSpot CRM data, providing built-in vector storage and caching mechanisms help overcome HubSpot API limitations while... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [HubSpot MCP by Devart](../tools/hubspot-mcp-by-devart.md) github.com Self-hosted MCP server for secure AI access to HubSpot CRM and marketing data. - devart-ai-connectivity/devart-mcp-server-hubspot [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [HubSpot MCP by djmoore-projects](../tools/hubspot-mcp-by-djmoore-projects.md) github.com MCP server exposing HubSpot CRM data and actions as tools for AI agents (Claude, Cursor). - djmoore-projects/hubspot-mcp-server [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [HubSpot MCP by mindstone-engineering](../tools/hubspot-mcp-by-mindstone-engineering.md) github.com Production-ready MCP connectors for popular SaaS tools. Works with Claude Desktop, Cursor, Rebel, and any MCP host. - mcp-servers/connectors/hubspot at main · mindstone/mcp-servers [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [HubSpot MCP by pipeworx](../tools/hubspot-mcp-by-pipeworx.md) github.com HubSpot MCP Pack. Contribute to pipeworx-io/mcp-hubspot development by creating an account on GitHub. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [HumanHours](../tools/humanhours.md) humanhours.dev HumanHours runs a hosted [Model Context Protocol](https://modelcontextprotocol.io) server, so any MCP client can log agent ROI and ask about a workspace in p... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Hunter MCP by scalably](../tools/hunter-mcp-by-scalably.md) scalably.io Hunter.io MCP: domain search, email finder and verifier, enrichment, discovery, leads. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [ICT Contact MCP](../tools/ict-contact-mcp.md) ictcontact.com ICTContact is AI-powered contact center software with builtin CRM, Omnichannel support, WhatsApp integration, progressive dialer, preview dialer, IVR studio, and CRM buisness automation. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [ICT CRM MCP](../tools/ict-crm-mcp.md) ictcrm.com ICTCRM is a CRM with a full contact center inside: auto dialer, campaigns, AI voice agent, and a timeline that logs every call, text and email automatically. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [ICT Dialer MCP](../tools/ict-dialer-mcp.md) ictdialer.com ICTDialer is a cloud-based call center and contact center platform that supports Voice, SMS, and Fax communications technologies. You need internet and a web [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [IN2 Agent MCP](../tools/in2-agent-mcp.md) github.com IN2 MCP stdio server: turns Campfire Salesforce requirements into verified org changes, driven by a Claude Code supervisor. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Infosys AI CRM by ffred1962](../tools/infosys-ai-crm-by-ffred1962.md) github.com AI based CRM system for small business . Contribute to ffred1962/infosys development by creating an account on GitHub. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Insaight](../tools/insaight.md) github.com LinkedIn prospect intelligence inside Claude - MCP server + 8 skills that research people, companies and comment threads, draft outreach, and learn what gets replies. - spirosbax/insaight [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Intelagent Enrichment MCP](../tools/intelagent-enrichment-mcp.md) github.com Open-source MCP servers for entity enrichment, file processing, web research, and more - usable with Claude Code, Claude Desktop, Cursor, and any MCP-compatible client. - Opafex/opafex-mcps [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Intelligence Aeternum](../tools/intelligence-aeternum.md) iaeternum.ai High-fidelity, provenance-verified training data for the next generation of AI. 4,000+ tokens per image. C2PA certified. Available now on HuggingFace. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Intent Engineering MCP by seanwinslow](../tools/intent-engineering-mcp-by-seanwinslow.md) github.com This repo contains the MCP server for agentic intent engineering workflows - GitHub - seanwinslow28/sw-mcp-intent-engineering: This repo contains the MCP server for agentic intent engineering workflows [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Intent Outreach](../tools/intent-outreach.md) demos.intentsolutions.io Intent Outreach runs outbound prospecting inside Claude Code: research, enrichment, and drafted outreach over your own provider accounts, with a typed validation gate in front of storage and a per-campaign... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [IntentLink](../tools/intentlink.md) intentlink.io IntentLink is the commercial intent network for the AI agent era - developers monetize conversations via MCP and Skills; advertisers reach high-intent buyers. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Signals & Intent](../categories/signals-intent-abm.md)

- [Interzoid MCP](../tools/interzoid-mcp.md) mcp.interzoid.com 58 AI data quality, data matching, and data enrichment APIs for better data ROI [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Investor Relations MCP by adelaidasofia](../tools/investor-relations-mcp-by-adelaidasofia.md) github.com FastMCP seed raise pipeline tracker - syncs from Obsidian CRM, generates meeting prep, tracks follow-up compliance - adelaidasofia/investor-relations-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Iridium LinkedIn Agent](../tools/iridium-linkedin-agent.md) iridiumhqmcp.com An MCP server that gives AI agents live LinkedIn data and the ability to act: commenting, outreach, messaging, with every action logged and human approval before anything posts. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [JackTrade CRM](../tools/jacktrade-crm.md) frostsa2.ed1.jacktrade.xyz Search customers, manage quotes, work orders, action items, and calendar events for your business [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [JobDataLake MCP](../tools/jobdatalake-mcp.md) github.com MCP server for JobDataLake - search 1M+ enriched job listings from AI tools - echojobsio/jdl-mcp-server [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Keepsake MCP by nicolascroce](../tools/keepsake-mcp-by-nicolascroce.md) github.com MCP server for Keepsake personal CRM - connect your AI agent to your contacts, tasks, notes, and more - nicolascroce/keepsake-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Keyword Research API by Br0ski777](../tools/keyword-research-api-by-br0ski777.md) github.com SEO keyword research via Google Suggest with intent scoring and long-tail discovery. -- x402 micropayment API + MCP server for AI agents - Br0ski777/keyword-research-x402 [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Kommo MCP](../tools/kommo-mcp.md) api.mcp.ai Kommo CRM (formerly amoCRM), the conversation-first sales CRM (WhatsApp, Instagram, Telegram) used b [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Kordic CRM](../tools/kordic-crm.md) kordic.io A sales CRM for teams of 5 to 50. Visual pipeline, WhatsApp and Gmail in one place, invoicing and payment tracking. From $4.99 a user. 3-month free trial. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [RevOps Infra](../categories/revops-infra.md)

- [Kylas CRM MCP](../tools/kylas-crm-mcp.md) github.com Contribute to akshaykylas94/MCP development by creating an account on GitHub. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Lead Enrich MCP by carsonlabs](../tools/lead-enrich-mcp-by-carsonlabs.md) github.com MCP server for waterfall lead enrichment - cascades Apollo, Clearbit, and Hunter for maximum data coverage - carsonlabs/leadenrich-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Lead Enrich MCP by carsonroell-debug](../tools/lead-enrich-mcp-by-carsonroell-debug.md) github.com MCP server for waterfall lead enrichment - cascades Apollo, Clearbit, and Hunter for maximum data coverage - carsonlabs/leadenrich-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [LeadConnector MCP by pipeworx](../tools/leadconnector-mcp-by-pipeworx.md) github.com LeadConnector / GoHighLevel MCP Pack - wraps the GoHighLevel CRM for AI agents. - pipeworx-io/mcp-leadconnector [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Leadcraft MCP](../tools/leadcraft-mcp.md) github.com Turn your AI coding agent into a sales copilot. Find clients on the open web, draft personalized cold email, track the pipeline all from slash commands. - Lakshya330-sudo/leadcraft [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [LeadDelta MCP](../tools/leaddelta-mcp.md) mcp.leaddelta.com MCP server for LeadDelta - manage LinkedIn connections and CRM data via AI assistants. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Leadgen MCP by koolninad](../tools/leadgen-mcp-by-koolninad.md) github.com MCP Server for AI-powered lead generation - scans websites, crawls platforms, and sends personalized outreach emails - koolninad/leadgen-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Leadgen ONRC Romania](../tools/leadgen-onrc-romania.md) leadgen-mcp.adrianhomelab.com Romania company registry: search 4.2M businesses by name/CUI, directors, financials. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [LeadMagic MCP](../tools/leadmagic-mcp.md) leadmagic.io Local TypeScript MCP server for the LeadMagic API: email finder, email validation, company enrichment, and research tools over stdio. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [LeadOracle MCP](../tools/leadoracle-mcp.md) tooloracle.io LeadOracle ΓÇö B2B Lead Intelligence MCP Server | 7 tools | Company lookup, domain enrichment, email finder | Part of ToolOracle [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Leadpipe MCP](../tools/leadpipe-mcp.md) github.com AI-powered lead qualification engine for MCP. Ingest, enrich, score, and export leads to your CRM. - automatiabcn/leadpipe-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Leadpipe MCP by enzoemir1](../tools/leadpipe-mcp-by-enzoemir1.md) github.com AI-powered lead qualification engine for MCP. Ingest, enrich, score, and export leads to your CRM. - automatiabcn/leadpipe-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [LeadScout MCP](../tools/leadscout-mcp.md) chenagent.dev MCP server for LeadScout Spanish B2B lead generation for PyMEs. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [LeadSleuth MCP](../tools/leadsleuth-mcp.md) leads.zalize.com Connect AI agents to your LeadSleuth leads via the Model Context Protocol: step-by-step setup for Claude Desktop, Claude Code, ChatGPT and Cursor with copy-paste configs. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [Leadzaar](../tools/leadzaar.md) github.com Local-first, single-user sales CRM in one self-contained Go binary - tview TUI + MCP stdio server over an embedded bbolt store - Techthos/leadzaar [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [LinkDeal](../tools/linkdeal.md) app.linkdeal.ai Find B2B leads from LinkedIn engagement, enrich contacts and deliver to Slack. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [LinkedGrow](../tools/linkedgrow.md) linkedgrow.ai Lead generation on LinkedIn, run by an agent that finds your leads, sends the invitation and opens the conversation, inside limits that keep your account safe. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [LinkedIn ICP Discovery MCP](../tools/linkedin-icp-discovery-mcp.md) github.com ICP lookalike discovery for Claude Code. Seed from your best customers → Apollo firmographic candidates → Zevari behavioral lookalike scoring → live-confirmed top-tier list. The list-build that converts. -... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [LinkedIn Job Change MCP by jpeslar1](../tools/linkedin-job-change-mcp-by-jpeslar1.md) github.com Daily job-change trigger for Claude Code. Detects changes the day they happen via LinkedIn MCP (Zevari) - not 30-90 days later like Apollo/Clay. Pipedrive + Instantly + Slack. -... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Signals & Intent](../categories/signals-intent-abm.md)

- [LinkedIn Marketing MCP by 1036007003-wq](../tools/linkedin-marketing-mcp-by-1036007003-wq.md) github.com LinkedIn B2B marketing MCP Server - profile search, company analysis, outreach message drafting. - 1036007003-wq/linkedin-marketing-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [LinkedIn Outreach MCP by hfarazul](../tools/linkedin-outreach-mcp-by-hfarazul.md) github.com LinkedIn outreach automation MCP server for Claude Code - search, connect, and message prospects with rate limiting - hfarazul/linkedin-outreach-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [LinkedIn Outreach MCP by MEOK](../tools/linkedin-outreach-mcp-by-meok.md) meok.ai ≡ƒöî Exposes linkedin outreach tools over MCP (MEOK AI Labs) [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [LinkedNav](../tools/linkednav.md) linkednav.com LinkedNav detects LinkedIn buying signals and sends personalized outreach you approve. Built for founders and lead-gen agencies. Free 7-day trial. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [LinkMCP](../tools/linkmcp.md) app.linkmcp.io The LinkedIn access layer for AI agents. Search, message, and enrich LinkedIn from Claude, ChatGPT, Cursor, n8n, or your own agent - 31 tools over MCP. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [LinkupAPI LinkedIn Skills](../tools/linkupapi-linkedin-skills.md) linkupapi.com Claude Skills for LinkedIn outreach, high-intent leads, feed engagement, and profile enrichment via LinkupAPI MCP. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [ListSignal MCP](../tools/listsignal-mcp.md) listsignal.com Query 14M+ online businesses by tech stack, revenue, and hiring signals. REST API + MCP server for AI agents. Free tier: 1,000 lookups/month, no card required. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Little Green Light MCP](../tools/little-green-light-mcp.md) github.com A direct, secure, and high-fidelity Model Context Protocol (MCP) Server for the Little Green Light CRM database. - WillHeadlee/Little-Green-Light-MCP-Server [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Livespace CRM MCP](../tools/livespace-crm-mcp.md) github.com Unofficial MCP server for Livespace CRM with safe, intent-shaped read and write tools. - proAutomator/livespace-crm-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Local MCP CRM](../tools/local-mcp-crm.md) github.com Local-first CRM built on the Model Context Protocol (MCP) - customer/project management exposed as MCP tools, usable from a custom LlamaIndex agent or directly in Claude Code or any other applications... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [LocalTry AI CRM](../tools/localtry-ai-crm.md) localtry.com We built LocalTry after years of CRM hopping and a $20,000-plus custom-build estimate. Start with a complete CRM, then shape the workspace around your business. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Lookaberry GTM MCP](../tools/lookaberry-gtm-mcp.md) github.com Autonomous, headless AI Go-to-Market (GTM) outbound engine & MCP Server powered by PostgreSQL 16 + pgvector. - lucasmartins-ai/lookaberry [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Maasy](../tools/maasy.md) maasy.co AI marketing copilot: brand intelligence, campaigns, content, CRM, SEO, and skills for Claude. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Magellan MCP by sorrek](../tools/magellan-mcp-by-sorrek.md) magellandata.io Parent companies, PE ownership, corporate families, and portfolio siblings - delivered as a hosted MCP server your AI agent calls mid-task. No login, no CSV, no tabs. Prefer a file? Spotlight, our web app,... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Magpipe](../tools/magpipe.md) magpipe.ai Omni-channel AI communications platform. Voice, SMS, email, and chat - handled by intelligent AI agents 24/7. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Mailcannon](../tools/mailcannon.md) thinkandautomate.dev AI-powered email outreach platform - send campaigns with deliverability tracking. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Email Deliverability](../categories/email-deliverability.md)

- [MailerLite MCP by UsefulAPI](../tools/mailerlite-mcp-by-usefulapi.md) mailerlite.usefulapi.io Read subscribers, groups, campaigns, fields, segments, automations, webhooks; safe additive writes. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [Mailrith](../tools/mailrith.md) mailrith.com Connect Mailrith from Claude [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [Mamba B2B Prospect Engine MCP](../tools/mamba-b2b-prospect-engine-mcp.md) github.com MCP server for the Mamba Labs Prospect Engine actor on Apify - mambalabsdev/mcp-b2b-prospect-engine [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Mamba Clay to Instantly/Smartlead Push MCP](../tools/mamba-clay-to-instantly-smartlead-push-mcp.md) github.com MCP server for the Mamba Labs Sequencer Lead Push actor on Apify. Push enriched leads into an Instantly or Smartlead campaign. - mambalabsdev/mcp-clay-to-instantly-smartlead-push [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [Mamba Domain Deliverability MCP](../tools/mamba-domain-deliverability-mcp.md) github.com MCP server for the Mamba Labs Domain Deliverability Checker actor: SPF, DKIM, DMARC, MX, blacklist, catch-all, domain age. Clay-ready. - mambalabsdev/mcp-domain-deliverability-checker [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Email Deliverability](../categories/email-deliverability.md)

- [Mamba Firmographic Enricher MCP](../tools/mamba-firmographic-enricher-mcp.md) github.com MCP server for the Mamba Labs Company Firmographic Enricher actor: employees, industry, HQ, founded, revenue, logo from a domain. Clay-ready. - mambalabsdev/mcp-company-firmographic-enricher [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Mamba GTM Hiring Signal MCP](../tools/mamba-gtm-hiring-signal-mcp.md) github.com MCP server for GTM Hiring Signal Scraper. Detects GTM hiring activity from company career pages via Apify. Clay-ready output. - mambalabsdev/mcp-gtm-hiring-signal-scraper [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Signals & Intent](../categories/signals-intent-abm.md)

- [Mamba GTM Signals Aggregator MCP](../tools/mamba-gtm-signals-aggregator-mcp.md) github.com MCP server for GTM Signals Aggregator. Combines hiring and tech stack detection into one composite GTM score via Apify. Clay-ready output. - mambalabsdev/mcp-gtm-signals-aggregator [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Signals & Intent](../categories/signals-intent-abm.md)

- [Mamba GTM Suite MCP](../tools/mamba-gtm-suite-mcp.md) github.com MCP server for the full Mamba Labs GTM Suite. All six GTM actors as tools in one server via Apify. Clay-ready output. - mambalabsdev/mcp-gtm-suite [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Mamba Job Board Keyword Signal Scanner MCP](../tools/mamba-job-board-keyword-signal-scanner-mcp.md) github.com MCP server for Job Board Keyword Signal Scanner. Scans Greenhouse, Lever, Ashby, Workday, and Rippling for roles in any category via Apify. Clay-ready output. - mambalabsdev/mcp-job-board-keyword-signal-scanner [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Signals & Intent](../categories/signals-intent-abm.md)

- [Mamba Public Company Reporting Window MCP](../tools/mamba-public-company-reporting-window-mcp.md) github.com Contribute to mambalabsdev/mcp-public-company-reporting-window-finder development by creating an account on GitHub. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Signals & Intent](../categories/signals-intent-abm.md)

- [Mamba Review Reputation Enricher MCP](../tools/mamba-review-reputation-enricher-mcp.md) github.com Resolve a company domain to its Trustpilot rating, review count and claimed status. - mambalabsdev/mcp-review-platform-reputation-enricher [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Mamba Tech Stack Signal MCP](../tools/mamba-tech-stack-signal-mcp.md) github.com MCP server for GTM Tech Stack Signal Enrichment. Detects CRM, sequencer, and marketing automation tools from a company's public website via Apify. Clay-ready output. -... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [ManyContacts WhatsApp Business CRM MCP](../tools/manycontacts-whatsapp-business-crm-mcp.md) github.com ManyContacts MCP. Contribute to ManyContacts/mcp development by creating an account on GitHub. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Marvenn MCP](../tools/marvenn-mcp.md) github.com Connect AI agents to Marvenn for outbound growth via email, voice, and LinkedIn. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [Max MCP by Digital Crew](../tools/max-mcp-by-digital-crew.md) max-mcp-server.vercel.app Model Context Protocol (MCP) server for Max, Digital Crew's AI sales agent. Exposes workspace profile tools via Streamable HTTP for Digital Crew integrations. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [MCP Force by RapidoCloud](../tools/mcp-force-by-rapidocloud.md) github.com An MCP server to expose Salesforce APIs as tools for AI Agents - RapidoCloud/mcp-force [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [MCP Lead Gen by FlipFactory](../tools/mcp-lead-gen-by-flipfactory.md) github.com Could not fully document product behavior from a live vendor homepage this pass (fetch status=404 error=HTTPError 404). [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [MCP-Salesforce by smn2gnt](../tools/mcp-salesforce-by-smn2gnt.md) github.com MCP Salesforce connector. Contribute to smn2gnt/MCP-Salesforce development by creating an account on GitHub. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [MentionAgent](../tools/mentionagent.md) mentionagent.ai Link building outreach from your agent: review drafts, send the batch, answer publisher replies. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [Mesh](../tools/mesh.md) me.sh Mesh is a beautiful rolodex and CRM for iPhone, Mac, Windows, and web, built automatically to help you manage your personal and professional relationships. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Method CRM MCP](../tools/method-crm-mcp.md) github.com MCP server for Method CRM on Cloudflare Workers - 22 tools, OAuth 2.1, multi-tenant - avisangle/method-crm-mcp-workers [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [MineWorks Lead Generation MCP](../tools/mineworks-lead-generation-mcp.md) themineworks--lead-generation-mcp.apify.actor B2B and local lead gen: verified emails, site contacts, Maps and Yellow Pages leads. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Moltlines Studio Outbound](../tools/moltlines-studio-outbound.md) moltlinestudio.com 138 production AI agent skills, persona bundles, and 22 MCP servers with free tiers. One $19 All-Access license unlocks every premium tool. Pay with crypto. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Munin](../tools/munin.md) getmunin.com The customer platform for the agentic era. MCP-first, open source, self-hostable. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [MuntuAI MCP](../tools/muntuai-mcp.md) api.muntuai.com Hosted MCP server for MuntuAI outreach campaigns, leads, senders, domains, and analytics. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [myOPC](../tools/myopc.md) myopc.io All-in-one AI business platform with 28+ modules: CRM, inventory, accounting, sales orders, quotations, HR, payroll, tax compliance & e-invoicing. Bring your own AI key (BYOK) from 13 providers and connect AI... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [n47vc MCP Suite](../tools/n47vc-mcp-suite.md) github.com Deploy MCP servers to Vercel in minutes. Includes Gmail, Google Drive, and Apollo.io servers with pluggable OAuth authentication. - n47vc/mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Nevent MCP](../tools/nevent-mcp.md) nevent.ai Connect Nevent to Claude, ChatGPT and other LLMs via MCP. Ask, analyze, segment and launch event campaigns from chat, using real data from your CRM. Age... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Nex MCP](../tools/nex-mcp.md) github.com Organizational context and memory for AI agents; connect 100+ tools into one knowledge graph. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Nimbus](../tools/nimbus.md) testnimbus.dev Run real Salesforce Apex locally - no org, no Docker - then ship through the same tool: gated deploys, Salesforce validation, release receipts. A typical test runs in tens of milliseconds. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [NirmahGTM](../tools/nirmahgtm.md) github.com AI reasoning engine for Clay: auto-detects 5 GTM buying signals, scores with calibrated LLMs, outputs evidence-backed openers/hooks/CRM sync governed, cached, evaluated. - AnjaliPPal/NirmahGTM [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Signals & Intent](../categories/signals-intent-abm.md)

- [Nuph](../tools/nuph.md) github.com Official MCP server for nuph.ai - LinkedIn outreach, lead search, AI messages, and pipeline management from Claude, Cursor, and any MCP-compatible AI agent - teslaeas/nuph-mcp-server [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Nynch MCP](../tools/nynch-mcp.md) nynch.com Nynch developer resources for AI agents. Nynch API docs, Nynch OpenAPI specification, Nynch MCP server, authentication, and example requests for the Nynch AI CRM. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Obriym CRM MCP](../tools/obriym-crm-mcp.md) obriym-crm.com Підключіть Obriym CRM до Claude, ChatGPT, Gemini чи Cursor через OAuth із явним підтвердженням акаунта або scoped API-токен. Асистент знаходить застійні ліди, угоди й замовлення та виконує лише дозволені дії. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Ocean.io Agent CLI](../tools/ocean-io-agent-cli.md) ocean.io CLI and MCP server for the Ocean.io API ΓÇö search companies & people, enrich profiles, reveal emails/phones. Built for humans and AI agents. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Odoo MCP by pipeworx](../tools/odoo-mcp-by-pipeworx.md) github.com Odoo MCP Pack - ERP/CRM via Odoo's external JSON-RPC API. - pipeworx-io/mcp-odoo [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Oisha OS](../tools/oisha-os.md) github.com Autonomous Multi-Agent Operating System for Modern Agency Operations, CRM & Financial Intelligence [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Opafex MCP Suite](../tools/opafex-mcp-suite.md) github.com Open-source MCP servers for entity enrichment, file processing, web research, and more - usable with Claude Code, Claude Desktop, Cursor, and any MCP-compatible client. - Opafex/opafex-mcps [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Open Sales Stack MCP by ekas](../tools/open-sales-stack-mcp-by-ekas.md) github.com MCP and tools for various tasks related to ekas. Contribute to ekas-io/open-sales-stack development by creating an account on GitHub. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [OpenDirectories MCP](../tools/opendirectories-mcp.md) github.com MCP server for 12M+ verified businesses across 10 countries. Government-sourced, Google Maps enriched. 6 tools for search, verification, competitor analysis, and market research. - BigJai/opendirectories-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [OpsDoctor](../tools/opsdoctor.md) opsdoctor.app Get a free AI-powered diagnostic of your CRM and operational workflows, scored across four dimensions with a branded PDF report. 38 CRM platforms. 8 industry verticals. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [RevOps Infra](../categories/revops-infra.md)

- [Outbound Engine MCP by closermethod](../tools/outbound-engine-mcp-by-closermethod.md) github.com Outbound Engine MCP for AI agents and creators. One cold-outreach engine, any target: brand deals, UGC, newsletter sponsorships, jobs, podcasts. HOOK/BRIDGE/SOFT-ASK structuring, message auditing, follow-up... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Outreach Deliverability MCP by closermethod](../tools/outreach-deliverability-mcp-by-closermethod.md) github.com Outreach Deliverability MCP for AI agents. Channel-safety layer for cold outreach on email, LinkedIn, Instagram DM, X DM: volume limits, SPF/DKIM/DMARC sender setup, spam-trigger auditing, benchmark... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Email Deliverability](../categories/email-deliverability.md)

- [Outreach MCP by CData](../tools/outreach-mcp-by-cdata.md) github.com This read-only MCP Server allows you to connect to Outreach data from Claude Desktop through CData JDBC Drivers. For full CRUD support, check out the first managed MCP platform: CData Connect AI... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Outreach MCP by mindstone-engineering](../tools/outreach-mcp-by-mindstone-engineering.md) github.com Production-ready MCP connectors for popular SaaS tools. Works with Claude Desktop, Cursor, Rebel, and any MCP host. - mcp-servers/connectors/outreach at main · mindstone/mcp-servers [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Outreacher](../tools/outreacher.md) github.com Boilerplate AI MCP+SaaS LLM foundation with use-case as an AI-powered lead management CRM system with an MCP server for Claude Desktop and a Next.js SaaS frontend. - technicallypete/outreacher [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Outscraper MCP Server](../tools/outscraper-mcp-server.md) mcp.outscraper.com Outscraper MCP business discovery, Maps intelligence, enrichment, reviews, and contact data. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [PaidSync MCP](../tools/paidsync-mcp.md) paidsync.ai The MCP server that runs Google, Meta, LinkedIn, TikTok ads from Claude, ChatGPT, and Gemini. 470+ tools, 14 platforms, approval-gated. Free to start. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Parsley](../tools/parsley.md) parsley.id Query buyer intent signals, MEDDIC qualifications, and lead scores from Parsley. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Signals & Intent](../categories/signals-intent-abm.md)

- [People Data Labs MCP by pipeworx](../tools/people-data-labs-mcp-by-pipeworx.md) github.com People Data Labs MCP - wraps the PDL person/company enrichment API - pipeworx-io/mcp-peopledatalabs [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [People Data Labs MCP by UsefulAPI](../tools/people-data-labs-mcp-by-usefulapi.md) peopledatalabs.usefulapi.io Enrich and search people and companies, resolve identities, and enrich IP addresses. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Perfex CRM MCP](../tools/perfex-crm-mcp.md) themesic.com Connect Perfex CRM to AI agents, automation platforms and any third-party app with a flexible, fully-documented REST API and a built-in MCP server. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Person Enrichment from Email (x402)](../tools/person-enrichment-from-email.md) github.com Person enrichment from email. Full name, job title, company, LinkedIn, GitHub, Twitter, avatar, location. Ideal for lead research. -- x402 micropayment API + MCP server for AI agents -... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [PersuadioAI](../tools/persuadioai.md) persuadioai.com Turn more seller leads into real conversations. PersuadioAI follows up by text, email, and AI voice calls, handles replies, and alerts your acquisitions team when someone is ready to talk. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [Phos Analytics Engine MCP](../tools/phos-analytics-engine-mcp.md) analytics.phos.nz AI analytics - sales analysis, ML forecasting, customer segmentation. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Forecasting & Revenue](../categories/forecasting-revenue.md)

- [Phos Sales Engine MCP](../tools/phos-sales-engine-mcp.md) sales.phos.nz AI sales - prospect discovery, ICP scoring, outreach generation. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [PILLAR GTM OS](../tools/pillar-gtm-os.md) app.pillargtm.com AI-native GTM OS for B2B SaaS - account health, pipeline, renewals, territories, and benchmarks. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [RevOps Infra](../categories/revops-infra.md)

- [Pipedrive MCP by comma-compliance](../tools/pipedrive-mcp-by-comma-compliance.md) github.com Pipedrive CRM server for the Model Context Protocol (MCP). 75 tools covering full CRUD, custom field resolution, and shortcut tools for common CRM workflows. - comma-compliance/pipedrive-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Pipedrive MCP by Teapot-Agency](../tools/pipedrive-mcp-by-teapot-agency.md) github.com MCP server for Pipedrive CRM - Full CRUD operations (36 tools) for deals, persons, organizations, activities, notes & leads. Built-in rate limiting, safety confirmations, and soft delete recovery. -... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Pipedrive MCP by UsefulAPI](../tools/pipedrive-mcp-by-usefulapi.md) pipedrive.usefulapi.io Read deals, persons, organizations, activities and pipelines; create and update CRM records. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [PitchIQ MCP](../tools/pitchiq-mcp.md) chuhching.com Chuhching is the agent-native business platform: CRM, outreach, scheduling, community, and automation that you and your AI agents run together. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Enablement & Coaching](../categories/enablement-coaching.md)

- [Planhat MCP by da-troll](../tools/planhat-mcp-by-da-troll.md) github.com Unofficial local MCP server for Planhat CRM: 60 tools for Claude Desktop and any MCP client. - da-troll/Planhat-MCP [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Ploomes MCP by victorbenazzi](../tools/ploomes-mcp-by-victorbenazzi.md) github.com Unofficial Model Context Protocol server that connects AI agents to the Ploomes CRM REST API - victorbenazzi/ploomes-mcp-server [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Podcast Guest CRM](../tools/podcast-guest-crm.md) github.com AI-native CRM for podcast guest booking: lifecycle pipeline, AI outreach drafting, and a real CLI - RudrenduPaul/podcast-guest-crm [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [Potarix Enricher](../tools/potarix-enricher.md) github.com MCP server for Potarix Enricher company and email lookup tools - Potarix/potarix-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [PropelAgent Studio](../tools/propelagent-studio.md) propelagent.studio AI agent platform: manage leads, conversations, bots, calendar and CRM via MCP. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [AI SDRs](../categories/ai-sdr-agents.md)

- [Prospecting Agent by B-Kirb](../tools/prospecting-agent-by-b-kirb.md) github.com Stateless, cost-capped prospecting agent that turns an intent-data signal into one qualified contact per account. Python - focused on agent reliability: determinism, hard cost caps, no guessing. -... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Prospector MCP by dremnik](../tools/prospector-mcp-by-dremnik.md) github.com Clay-as-an-MCP-server - B2B sales intelligence. Contribute to dremnik/prospector development by creating an account on GitHub. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Prospeo MCP](../tools/prospeo-mcp.md) mcp.prospeo.io Prospeo: Find, search, and enrich people and companies with verified emails and mobile numbers. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Provar MCP](../tools/provar-mcp.md) github.com Provar DX CLI. Contribute to ProvarTesting/provardx-cli development by creating an account on GitHub. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [PulseAgent MCP](../tools/pulseagent-mcp.md) github.com MCP server for PulseAgent - let Claude Code, Cursor, and Codex interact with your AI digital workers, CRM, and pipeline - iPythoning/pulseagent-mcp-server [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [RadiusOS CRM](../tools/radiusos-crm.md) radiusos.ai 34-tool CRM server - contacts, pipeline, quotes, invoices, scheduling, email, and AI scoring. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [RapidStart CRM MCP](../tools/rapidstart-crm-mcp.md) github.com MCP server for RapidStart CRM - enables AI assistants to discover and recommend RapidStart CRM - forceworks/rapidstart-mcp-server [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [RD Station CRM MCP](../tools/rd-station-crm-mcp.md) github.com Contribute to fernandoludvig/rdstation-crm-mcp development by creating an account on GitHub. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [RetailCRM MCP](../tools/retailcrm-mcp.md) github.com MCP server for RetailCRM - orders, customers, e-commerce analytics (Russia) - theYahia/retailcrm-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [RevenueOS by unempyd](../tools/revenueos-by-unempyd.md) unempyd.github.io RevenueOS finds opportunities, executes approved revenue work, and measures what happened. Self-hosted, MIT-licensed, and proven on a real business run - see the evidence. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Forecasting & Revenue](../categories/forecasting-revenue.md)

- [RevOps Eval](../tools/revops-eval.md) revopseval.com An evaluation benchmark for AI agents on Revenue Operations tasks. Public leaderboard. Open methodology. Real workflows. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Sales Enablement Plugin by jbalbu01](../tools/sales-enablement-plugin-by-jbalbu01.md) github.com A compounding GTM enablement engine for Claude - 18 skills, 7 commands, 16 MCP tools, self-healing content, and persistent memory that learns from every deal. - jbalbu01/sales-enablement-plugin [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Sales Intelligence MCP by Aria Agentworks](../tools/sales-intelligence-mcp-by-aria-agentworks.md) github.com Open-source MCP toolkit for company research, lead scoring, outreach automation, and CRM sync. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Salesbot LinkedIn MCP](../tools/salesbot-linkedin-mcp.md) salesbot.cz LinkedIn automatizace s AI personalizací a MCP serverem. 590 Kč měsíčně nebo 500 Kč/měsíc při roční platbě 6 000 Kč. Bez DPH, 14 dní zdarma. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [SalesBuildr MCP by WYRE-AI](../tools/salesbuildr-mcp-by-wyre-ai.md) conduit.wyre.ai Manage quotes, proposals, and sales workflows in SalesBuildr. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Proposals & Deals](../categories/proposals-deals.md)

- [SalesEQ Plugins](../tools/saleseq-plugins.md) github.com Official SalesEQ plugin for Claude Code, Cursor, and Codex - your meetings as agent context. - SalesEQ/plugins [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [Salesforce CLI MCP](../tools/salesforce-cli-mcp.md) github.com MCP Server for interacting with Salesforce instances - salesforcecli/mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Salesforce Cloud MCP by aaronsb](../tools/salesforce-cloud-mcp-by-aaronsb.md) github.com MCP server providing AI-powered Salesforce tools for opportunity intelligence, conversation analysis, business case generation, and CRUD operations with natural language interaction. - aaronsb/salesforce-cloud [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Salesforce Commerce Cloud MCP by brinzl](../tools/salesforce-commerce-cloud-mcp-by-brinzl.md) github.com 🤖 An MCP server that helps connect your AI applications with your Salesforce Commerce Cloud instance - brinzl/commercecloud-mcp-server [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Salesforce Commerce Cloud MCP by vinkius-labs](../tools/salesforce-commerce-cloud-mcp-by-vinkius-labs.md) vinkius.com Vinkius Edge enterprise Model Context Protocol (MCP) server for Salesforce B2C Commerce Cloud integration. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Salesforce Data Cloud MCP by rishiganesh25](../tools/salesforce-data-cloud-mcp-by-rishiganesh25.md) github.com A Model Context Protocol (MCP) server for Salesforce Data Cloud - 60+ tools for SQL queries, data streams, segments, calculated insights, and more. - rishiganesh25/data360-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Salesforce Docs MCP by Sanket](../tools/salesforce-docs-mcp-by-sanket.md) github.com A local-first MCP server for searching Salesforce Developer Documentation. Search 360+ official Salesforce PDF docs from VS Code or Claude Desktop. - SalesforceDiariesBySanket/salesforce-docs-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Salesforce Hosted Custom MCP by Sanket](../tools/salesforce-hosted-custom-mcp-by-sanket.md) github.com Salesforce Hosted Custom MCP Server - MCP Server Definitions, External Service Registrations, and Related Apex Classes - SalesforceDiariesBySanket/Salesforce-Hosted-Custom-Mcp-Server [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Salesforce Intelligence MCP](../tools/salesforce-intelligence-mcp.md) github.com Salesforce Org Intelligence for AI agents - a read-only, offline, source-available MCP server and CLI answering metadata, dependency, permission, Apex and Flow questions grounded in real retrieved org... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Salesforce Marketing Cloud MCP by Devart](../tools/salesforce-marketing-cloud-mcp-by-devart.md) github.com Self-hosted MCP server for secure AI access to Salesforce Marketing Cloud. - devart-ai-connectivity/devart-mcp-server-salesforce-marketing-cloud [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Salesforce Marketing Cloud MCP by Inefavel](../tools/salesforce-marketing-cloud-mcp-by-inefavel.md) github.com MCP Server para Salesforce Marketing Cloud - valide queries do Automation Studio antes de rodar, explore Data Extensions e consulte registros direto do Claude. - Inefavel/sfmc-mcp-server [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Salesforce Marketing Cloud MCP by salesforcebob](../tools/salesforce-marketing-cloud-mcp-by-salesforcebob.md) github.com MCP Server for SF MCE, supporting REST & SOAP. Contribute to salesforcebob/Salesforce-Marketing-Cloud-Engagement-MCP development by creating an account on GitHub. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Salesforce Marketing Cloud MCP by vinkius-labs](../tools/salesforce-marketing-cloud-mcp-by-vinkius-labs.md) vinkius.com Vinkius Edge enterprise Model Context Protocol (MCP) server for Salesforce Marketing Cloud API operations. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Salesforce MCP Auto Auth by kugamon](../tools/salesforce-mcp-auto-auth-by-kugamon.md) pypi.org Fastest to Enable Salesforce MCP server for Claude Desktop with automatic session refresh from your Chrome browser ΓÇö no External App needed [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Salesforce MCP by aaron-pienza](../tools/salesforce-mcp-by-aaron-pienza.md) github.com Salesforce MCP Server. Contribute to aaron-pienza/mcp-server-salesforce development by creating an account on GitHub. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Salesforce MCP by advancedcommunities](../tools/salesforce-mcp-by-advancedcommunities.md) github.com MCP server that enables AI assistants to interact with Salesforce orgs through the Salesforce CLI, providing tools for Apex execution, SOQL queries, metadata management, code analysis, and development... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Salesforce MCP by AiondaDotCom](../tools/salesforce-mcp-by-aiondadotcom.md) github.com 🚀 Complete MCP (Model Context Protocol) server for Salesforce integration with Claude Desktop. Provides seamless OAuth authentication, universal CRUD operations on any Salesforce object. -... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Salesforce MCP by boejucci](../tools/salesforce-mcp-by-boejucci.md) github.com Salesforce MCP Server. Contribute to boejucci/mcp-server-salesforce development by creating an account on GitHub. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Salesforce MCP by Devart](../tools/salesforce-mcp-by-devart.md) github.com Self-hosted MCP server for secure AI access to Salesforce CRM data. - devart-ai-connectivity/devart-mcp-server-salesforce [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Salesforce MCP by imazhar101](../tools/salesforce-mcp-by-imazhar101.md) github.com A lite, single-org Salesforce MCP server on jsforce. Bring-your-own OAuth token, stdio or streamable-HTTP. - imazhar101/salesforce-mcp-jsforce [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Salesforce MCP by jaworjar95](../tools/salesforce-mcp-by-jaworjar95.md) github.com A comprehensive Model Context Protocol (MCP) server that provides seamless Salesforce integration for AI development tools like Claude Desktop, Cline, and other MCP-compatible clients. -... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Salesforce MCP by kablewy](../tools/salesforce-mcp-by-kablewy.md) github.com Model Context Protocol server for Salesforce REST API integration - kablewy/salesforce-mcp-server [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Salesforce MCP by LokiMCPUniverse](../tools/salesforce-mcp-by-lokimcpuniverse.md) github.com 24 Enterprise MCP Servers for GenAI: AWS, Salesforce, HubSpot, Jenkins, Power BI + more. Production-ready AI agent integrations. - asklokesh/mcp-servers [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Salesforce MCP by mindstone](../tools/salesforce-mcp-by-mindstone.md) github.com Production-ready MCP connectors for popular SaaS tools. Works with Claude Desktop, Cursor, Rebel, and any MCP host. - mcp-servers/connectors/salesforce at main · mindstone/mcp-servers [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Salesforce MCP by pipeworx](../tools/salesforce-mcp-by-pipeworx.md) github.com Salesforce MCP Pack. Contribute to pipeworx-io/mcp-salesforce development by creating an account on GitHub. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Salesforce MCP by suraj20028](../tools/salesforce-mcp-by-suraj20028.md) github.com MCP Server for Salesforce Operations. Contribute to suraj20028/Salesforce-MCP development by creating an account on GitHub. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Salesforce MCP by SurajAdsul](../tools/salesforce-mcp-by-surajadsul.md) github.com An MCP (Model Context Protocol) server implementation that integrates Claude with Salesforce, enabling natural language interactions with your Salesforce data and metadata. This server allows Claude to query,... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Salesforce MCP by timescale](../tools/salesforce-mcp-by-timescale.md) github.com API wrapped around our salesforce database. Contribute to timescale/tiger-salesforce-mcp-server development by creating an account on GitHub. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Salesforce MCP by tomnagengast](../tools/salesforce-mcp-by-tomnagengast.md) github.com Model Context Protocol server for Salesforce integration - enables AI agents to securely access Salesforce data - tomnagengast/mcp-server-salesforce [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Salesforce MCP by tsmztech](../tools/salesforce-mcp-by-tsmztech.md) github.com Salesforce MCP Server. Contribute to tsmztech/mcp-server-salesforce development by creating an account on GitHub. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Salesforce MCP by vinkius-labs](../tools/salesforce-mcp-by-vinkius-labs.md) vinkius.com Vinkius Edge enterprise Model Context Protocol (MCP) server for Salesforce CRM standard objects and SOQL. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Salesforce MCP Lib by Damecek](../tools/salesforce-mcp-lib-by-damecek.md) context7.com Salesforce MCP Library is a local stdio bridge for Salesforce MCP endpoints using OAuth client credentials, featuring a reusable Apex MCP library and JSON-RPC 2.0 core. - Latest version [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Salesforce MCP Security Toolkit](../tools/salesforce-mcp-security-toolkit.md) github.com **Adversarial MCP integration testing toolkit for Salesforce ΓÇö seeds ~270 records across Account, Contact, Case, and Outreach Log with 14 attack payload categories including prom [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Salesforce Metadata MCP by semwalajay83](../tools/salesforce-metadata-mcp-by-semwalajay83.md) github.com MCP server with 228 tools for Salesforce: metadata, flows, Apex, LWC, Agentforce, OmniStudio, reports, permissions, impact analysis and more. Manage your org from Claude in natural language. -... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Salesforce Pardot MCP by DaniilMai](../tools/salesforce-pardot-mcp-by-daniilmai.md) github.com MCP server for Salesforce CRM and Pardot (Marketing Cloud Account Engagement) - DaniilMai/salesforce-pardot-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Salesforce Remote MCP by tsmztech](../tools/salesforce-remote-mcp-by-tsmztech.md) github.com Self-hosted remote MCP server for Salesforce on Cloudflare Workers - use as a Claude custom connector with OAuth login, exposing 15 Salesforce tools (SOQL, DML, Apex, metadata) -... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Samarth GTM MCP](../tools/samarth-gtm-mcp.md) github.com MCP server for Samarth Analytics Google Tag Manager operations - samarthanalytics-sj/samarth-analytics-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Say Ur Intent MCP](../tools/say-ur-intent-mcp.md) github.com Local-first MCP toolkit for Sui DeFi intents: turn a natural-language ask into verified on-chain evidence and a human-reviewable transaction you sign in your own wallet. No custody, no autonomous execution. -... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Signals & Intent](../categories/signals-intent-abm.md)

- [ScraperCity](../tools/scrapercity.md) github.com ScraperCity CLI & MCP Server - B2B lead generation for AI agents. 20+ scrapers accessible via CLI, MCP, or direct API. - scrapercity/scrapercity-cli [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [SeldonFrame MCP](../tools/seldonframe-mcp.md) seldonframe.com SeldonFrame is the agent-native, open-source alternative to GoHighLevel for agencies selling AI front offices to local businesses. Build a branded website, booking flow, CRM, intake, and AI agent for every... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [SendPulse](../tools/sendpulse.md) sendpulse.com Bring MCP into your SendPulse workflows and let an AI agent handle your email marketing, chatbots, and CRM. Courses, students, and assignment grading... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [Sequenzy MCP](../tools/sequenzy-mcp.md) github.com MCP server for AI agents to operate Sequenzy lifecycle, campaign, and transactional email workflows. - Sequenzy/mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [Setu Email MCP by gitmanhimanshu](../tools/setu-email-mcp-by-gitmanhimanshu.md) setu.mimanasa.online Setu is an AI-powered Model Context Protocol (MCP) server that lets Claude, ChatGPT, and Cursor automate email outreach and follow-ups directly from your Gmail. Built for job seekers, recruiters, and... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [SFCC Dev MCP by taurgis](../tools/sfcc-dev-mcp-by-taurgis.md) github.com Supercharge your Salesforce B2C Commerce Cloud development with AI-powered documentation access, real-time log analysis, and intelligent best practices guidance - taurgis/sfcc-dev-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Signal Found Reddit MCP](../tools/signal-found-reddit-mcp.md) github.com Arm your agent with the ability to send 1000s of dm's on Reddit a day, selling while you sleep. - signal-found/sf-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [Snov.io MCP by narkov](../tools/snov-io-mcp-by-narkov.md) github.com MCP server for Snov.io API - 43 tools for email finder, verifier, drip campaigns, prospect management, and LinkedIn enrichment - narkov/snov-io-mcp-server [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Social Profile Enrichment API](../tools/social-profile-enrichment-api.md) github.com Enrich social profiles from handle or URL -- Twitter/X, GitHub, LinkedIn, YouTube. Followers, bio, verification. -- x402 micropayment API + MCP server for AI agents - Br0ski777/social-profile-x402 [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [SpiderIQ Leads MCP](../tools/spideriq-leads-mcp.md) github.com SpiderIQ Leads: lead-gen MCP (jobs, campaigns, IDAP, Maps, People, Verify, company intel, spiderPR) [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Stacks AI](../tools/stacks-ai.md) github.com The universal board for AI agents - one Kanban for tasks, bugs, support, CRM & roadmap, operated by humans and agents via a built-in MCP server. Open-source, self-hostable (Next.js 16, Prisma 7, Auth.js v5). -... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [StratoForce AI Revenue Intelligence](../tools/stratoforce-ai-revenue-intelligence.md) stratoforce-mcp.stratoforce.workers.dev 15 AI revenue intelligence tools for Salesforce - pipeline, deals, coaching, competitors. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Forecasting & Revenue](../categories/forecasting-revenue.md)

- [Studiomeyer CRM](../tools/studiomeyer-crm.md) studiomeyer.io AI-native CRM with 37 MCP tools. Companies, deals, pipeline, leads, follow-ups, managed by AI. Connect in 30 seconds. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [SuiteCRM MCP by Anirudhx7](../tools/suitecrm-mcp-by-anirudhx7.md) anirudh.social Open-source MCP server for SuiteCRM. Connect Claude, Cursor, or any AI agent to your CRM in 5 minutes. 24 tools, OAuth2, Prometheus. MIT licensed. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Summit53 CRM](../tools/summit53-crm.md) summit53.io Summit53 LLM control center [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [RevOps Infra](../categories/revops-infra.md)

- [Synapse CRM MCP by NimbleBrain](../tools/synapse-crm-mcp-by-nimblebrain.md) github.com Lightweight CRM with contact management, deal pipeline, and agent-driven follow-ups ΓÇö Synapse app for NimbleBrain [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Teamleader MCP by BoostU](../tools/teamleader-mcp-by-boostu.md) teamleader-mcp.boostu.be De Teamleader MCP van BoostU brengt Teamleader Focus in Claude. Werk via je AI-assistent met de Teamleader Claude-koppeling op basis van het Model Context Protocol. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Technology Stack Detection API](../tools/technology-stack-detection-api.md) github.com Detect 50+ technologies on any website. CMS, JS frameworks, analytics, hosting, CDN, payments. Confidence scores and evidence. -- x402 micropayment API + MCP server for AI agents -... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Techtenstein LinkedIn MCP](../tools/techtenstein-linkedin-mcp.md) github.com Enrich LinkedIn profiles, companies, and prospect searches for sales, recruiting, and B2B. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [TeloSignal](../tools/telosignal.md) telosignal.com TeloSignal tracks demand signals across 11,909 n8n templates - AI adoption, complexity trends, weekly intelligence. Know what to build. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Signals & Intent](../categories/signals-intent-abm.md)

- [Toflow](../tools/toflow.md) toflow.ai toflow.ai is a LinkedIn automation tool for sales teams, agencies, and GTM experts. Run automated LinkedIn outreach, enrich contacts, and sequence across email and WhatsApp, just by chatting with AI. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [Tomba](../tools/tomba.md) tomba.io Find verified B2B email addresses from any company. 280M+ contacts, 81% coverage, 98% delivery rate. Trusted by 150,000+ sales teams. Start free today. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Twenty CRM MCP](../tools/twenty-crm-mcp.md) github.com A Model Context Protocol (MCP) server for Twenty CRM integration. Enables natural language interactions with your CRM data through Claude and other AI assistants. Supports CRUD operations, dynamic schema... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Twenty MCP by UsefulAPI](../tools/twenty-mcp-by-usefulapi.md) twenty.usefulapi.io Read people, companies, opportunities, notes and tasks; create and update records in Twenty CRM. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Twenty MCP Suite](../tools/twenty-mcp-suite.md) andrewmarconi.github.io Version-resilient MCP server suite for self-hosted Twenty CRM. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [UGC VZ MCP](../tools/ugc-vz-mcp.md) github.com MCP server for the UGC VZ creator directory (DACH): search real UGC creators, profiles, brand outreach. Streamable HTTP, no API key. - ugcvz/ugc-vz-mcp [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Vibe Prospecting MCP](../tools/vibe-prospecting-mcp.md) vibeprospecting.ai Professional prospecting inside the chat you already use. 50+ B2B data sources to build lead lists, research accounts, and find decision makers. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Vinkius Lead Gen Agents](../tools/vinkius-lead-gen-agents.md) vinkius.com Vinkius connects your AI to 8,239+ apps and real-world capabilities. One link works in ChatGPT, Claude, Gemini and more, with your connections managed in one place. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Wazion MCP Server](../tools/wazion-mcp-server.md) github.com WAzion MCP Server - Connect AI agents to WhatsApp via WAzion API. Smart copilot, 24/7 automation, mass marketing. - wazionapps/mcp-server [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Wokelo](../tools/wokelo.md) wokelo.ai Company and market intelligence, news, enrichment, and agentic workflows for dealmakers. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [x402 Data Gateway MCP](../tools/x402-data-gateway-mcp.md) x402-url-extractor-production.up.railway.app 25 deterministic pay-per-call tools accepting x402 and native MPP with Base USDC settlement. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [xaffinity MCP](../tools/xaffinity-mcp.md) github.com Unofficial strongly-typed Python SDK for the Affinity CRM API - full read/write coverage, Pydantic v2, MCP server included. For when you need more than Affinity's official MCP - affinity-sdk/mcp at main ·... [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [xpay Lead Gen](../tools/xpay-lead-gen.md) lead-gen.mcp.xpay.sh 50+ lead gen tools. Apollo, Hunter, Nyne, Tomba, Sixtyfour, Fiber, Exa. Pay-per-use via x402. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Yandex Audience MCP](../tools/yandex-audience-mcp.md) github.com MCP-сервер для Яндекс Аудиторий - создавать CRM- и LAL-сегменты, управлять пикселями и доступами из AI-приложения - A1-x-Tech/mcp-yandex-audience [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Signals & Intent](../categories/signals-intent-abm.md)

- [YG3](../tools/yg3.md) yg3.ai Provision a YG3 marketing workspace from any autonomous agent - no signup. Bearer-token MCP with 200+ tools for content, SEO, outbound, LinkedIn, and paid ads. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [YourICP MCP](../tools/youricp-mcp.md) app.youricp.com Official open-source MCP server for YourICP contact enrichment & B2B data cleaning. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Zavora Sales Operations Skill](../tools/zavora-sales-operations-skill.md) github.com Enterprise sales skill - proposals, CPQ, sequences, e-signatures, forecasting via mcp-sales (PandaDoc, Apollo, Calendly, Stripe) - zavora-ai/skill-sales-operations [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Zoho CRM MCP by Devart](../tools/zoho-crm-mcp-by-devart.md) github.com Self-hosted MCP server for secure AI access to Zoho CRM data. - devart-ai-connectivity/devart-mcp-server-zoho-crm [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [ZoomInfo MCP Plugin](../tools/zoominfo-mcp-plugin.md) github.com ZoomInfo MCP plugin. Contribute to Zoominfo/zoominfo-mcp-plugin development by creating an account on GitHub. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Albacross](../tools/albacross.md) albacross.com Identifies which companies visit a website via IP-to-company matching, tracks on-site and off-site behavioral/intent signals, and enriches identified companies with firmographic data and optional verified... [No MCP found](../mcp/none-found.md) · [Paid, self-serve](../gates/paid.md) · [Signals & Intent](../categories/signals-intent-abm.md)

- [ApexGTM](../tools/apexgtm.md) github.com 🚀 Autonomous GTM Engineer AI Platform - Multi-agent system that replaces 80-90% of manual GTM work. Combines Clay + Apollo + ZoomInfo + HubSpot + n8n into one AI-powered platform. Built with n8n workflows,... [No MCP found](../mcp/none-found.md) · [Gate unknown](../gates/unknown.md) · [AI SDRs](../categories/ai-sdr-agents.md)

- [Clay Workbench](../tools/clay-workbench.md) github.com Build, debug, and run Clay.com workbooks end-to-end via Claude Code. Hybrid router skill with 6 sub-skills: ABM lists, enrichment waterfalls, ICP scoring, outbound, inbound routing, troubleshooting. MCP-first... [No MCP found](../mcp/none-found.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Orbit](../tools/orbit.md) orbit.love Was a community-analytics platform that aggregated activity across Discord, Slack, GitHub, and social channels into a unified per-person engagement score ("Orbit Level") to identify a community's most valuable... [No MCP found](../mcp/none-found.md) · [Gate unknown](../gates/unknown.md) · [Community & Dark Social](../categories/community-dark-social.md)

- [Sendoff](../tools/sendoff.md) github.com Self-hosted AI that writes and sends your sales outreach in your voice. Not a CRM. Mountable Rails engine: LLM drafter with voice + hallucination critics, send-safety, Gmail, and an MCP server. Data plugs in... [No MCP found](../mcp/none-found.md) · [Gate unknown](../gates/unknown.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [Signal Prospector](../tools/signal-prospector.md) github.com A signal-based B2B prospecting engine on free infra: 8 buying-signal detectors, an explainable ICP scorer, free MX-validated email enrichment and AI outreach - via CLI, Flask and an MCP server. -... [No MCP found](../mcp/none-found.md) · [Gate unknown](../gates/unknown.md) · [Data & Enrichment](../categories/data-enrichment.md)
