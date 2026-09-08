# GTM tools by GitHub repo health: not measured yet, and why

> Repo staleness for every tool with a public repo, stamped with the date it was measured. Nothing is measured in this build: 98 entries carry a github.com URL as a seed.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) / By GitHub health

**View: by GitHub health**

## Is the thing you are about to depend on still moving.

> **Nothing measured yet** github_url, github_stars, github_last_commit, github_archived and github_fetched_on are null on all 336 entries. The refresh rail in SPEC section 7.2 has not been run. A star count without the date it was taken is a lie, so no number is shown at all.

When the rail runs, every repo lands in one of five bands and every band ships with the date it was measured: active under 90 days, slowing 90 to 180, quiet 180 to 365, dormant over a year, and archived. The band is descriptive and never a verdict. A stable server genuinely may not need commits. But an agent about to write a community MCP wrapper into a workflow deserves to know the repo has been silent for eight months first, and this directory already has the receipts that the category churns.

### The seed, which is a fact and not a measurement

98 of 336 entries already carry a github.com URL somewhere in their fields, and 83 of those sit in the mcp_url field. Those repos are free to measure when the rail runs. Nothing below says anything about whether a repo is healthy.

- [Apideck](../tools/apideck.md) apideck.com A unified API that normalises 200+ SaaS connectors into single data models, exposed as one MCP endpoint covering CRM, accounting, HRIS, ATS, file storage and issue tracking. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [MCP Layer](../categories/mcp-infrastructure.md) · CLI: apideck

- [Cal.com](../tools/cal-com.md) cal.com Open-source scheduling infrastructure - booking pages, event types, and a scheduling API/platform - offered both as a free, self-hostable open-source product and as hosted SaaS. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Scheduling & Routing](../categories/scheduling-routing.md)

- [Cargo](../tools/cargo.md) getcargo.ai A GTM/RevOps engineering platform (YC S23) that lets revenue teams define, version, and automate go-to-market logic - lead sourcing, enrichment, scoring, routing, CRM sync - as code, run by AI agents. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [RevOps Infra](../categories/revops-infra.md) · CLI: cargo

- [Census (now operates as "Fivetran Activations")](../tools/census.md) getcensus.com Was a standalone reverse-ETL tool for syncing warehouse data (Snowflake, BigQuery, etc.) into GTM tools like Salesforce/HubSpot without code; the product now lives inside Fivetran as "Activations," same... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [RevOps Infra](../categories/revops-infra.md)

- [Composio](../tools/composio.md) composio.dev A hosted integration/auth platform that lets AI agents and MCP clients call actions across 1,000+ SaaS apps (HubSpot, Slack, Gmail, GitHub, Notion, Stripe, and others) through Composio-managed OAuth. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [MCP Layer](../categories/mcp-infrastructure.md) · CLI: composio

- [Diffbot](../tools/diffbot.md) diffbot.com A web-extraction and "Knowledge Graph" company that crawls the public web and structures it into an entity graph (organizations, people, articles) queryable for company/entity enrichment, plus raw... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Data & Enrichment](../categories/data-enrichment.md) · CLI: composer (community)

- [Enrow](../tools/enrow.md) enrow.io Finds and verifies work email addresses and direct phone numbers from a name plus company domain or a LinkedIn URL, charging only when it returns a verified result. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Data & Enrichment](../categories/data-enrichment.md) · CLI: enrow

- [Exa](../tools/exa.md) exa.ai A search API that returns web pages and structured results ranked by semantic/meaning similarity to a query (embeddings-based) rather than keyword matching, plus tools to fetch page contents and get... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Data & Enrichment](../categories/data-enrichment.md) · CLI: exa-cli (community)

- [Fathom](../tools/fathom.md) fathom.video Free AI meeting recorder/notetaker that transcribes calls and generates summaries, action items, and CRM sync. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Conversation Intel](../categories/conversation-intel.md)

- [Firecrawl](../tools/firecrawl.md) firecrawl.dev A web scraping and crawling API that turns any URL or whole site into clean markdown or structured JSON for LLM pipelines, with search, map, crawl, extract, parse and browser-interaction endpoints. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Data & Enrichment](../categories/data-enrichment.md) · CLI: firecrawl

- [Fivetran](../tools/fivetran.md) fivetran.com Managed ELT pipeline platform; for GTM purposes, the relevant piece is its Salesforce/HubSpot/Marketo/Outreach/Salesloft/Gong/Zendesk connectors that land CRM and GTM-tool data in a warehouse, plus... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [RevOps Infra](../categories/revops-infra.md) · CLI: fivetran-cli (community)

- [Hunter.io](../tools/hunter-io.md) hunter.io An email-finding and verification tool - given a name, domain, or company, it locates likely professional email addresses (via domain pattern-matching and web-crawled data) and verifies deliverability; also... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Leadfeeder (product line rebranded/merged under Dealfront; dealfront.com redirects to leadfeeder.com)](../tools/leadfeeder.md) leadfeeder.com Identifies companies visiting a website via IP-to-company matching, tracks page-level visit behavior, and surfaces intent signals plus verified contact data for those companies. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Signals & Intent](../categories/signals-intent-abm.md)

- [LeadMagic](../tools/leadmagic.md) leadmagic.io A B2B contact/company data API and CLI that finds and validates work emails, mobile numbers, and social-to-email matches, plus company/job/ad-intelligence lookups, billing only for successful (valid) results. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Data & Enrichment](../categories/data-enrichment.md) · CLI: leadmagic (community)

- [Lusha](../tools/lusha.md) lusha.com A B2B contact and company database (300M+ profiles) accessed via a browser extension, web prospecting platform, and bulk CSV/API enrichment for finding direct dials, emails, and company data. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Data & Enrichment](../categories/data-enrichment.md) · CLI (community)

- [MeetGeek](../tools/meetgeek.md) meetgeek.ai Automatic meeting recorder and transcriber that produces summaries, highlights and conversation analytics across Zoom, Teams and Meet. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Conversation Intel](../categories/conversation-intel.md) · CLI: meetgeek (community)

- [Merge Agent Handler](../tools/merge-agent-handler.md) merge.dev Merge's tool-calling platform for AI agents: it wraps hundreds of third-party SaaS applications as pre-built MCP-ready connectors, bundles them into scoped "tool packs" per agent, brokers per-end-user... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [MCP Layer](../categories/mcp-infrastructure.md) · CLI: MergePythonClient

- [Metricool](../tools/metricool.md) metricool.com A social media management and analytics tool (scheduling, analytics, competitor tracking and ad-campaign monitoring across Instagram, Facebook, X, LinkedIn, TikTok, YouTube and Meta, Google and TikTok Ads) for... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Community & Dark Social](../categories/community-dark-social.md) · CLI: metricool (community)

- [Model Context Protocol - official servers repo](../tools/model-context-protocol-official-servers-repo.md) github.com The official reference-implementation repository for MCP, "managed by Anthropic, but built together with the community" - ships a small set of maintained example servers (Everything, Fetch, Filesystem, Git,... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [monday.com (monday CRM)](../tools/monday-com.md) monday.com A work-management platform whose CRM product runs pipelines, contacts, accounts and deal activity as boards and items, with a first-party remote MCP server that lets an AI client read and update that data on... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [RevOps Infra](../categories/revops-infra.md) · CLI: mapps

- [n8n](../tools/n8n.md) n8n.io A node-based workflow-automation platform for connecting apps/APIs and orchestrating multi-step processes, usable self-hosted or as managed cloud. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [RevOps Infra](../categories/revops-infra.md)

- [PandaDoc](../tools/pandadoc.md) pandadoc.com Document builder/e-signature platform for proposals, quotes, and contracts, with AI-assisted content generation and CRM-linked workflows. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Proposals & Deals](../categories/proposals-deals.md) · CLI: pandadoc (community)

- [Pipeworx](../tools/pipeworx.md) pipeworx.io A single MCP gateway that fronts a stated 1,532 live data sources as 5,871 tools behind one URL, weighted toward public and regulatory data (SEC EDGAR, FDA, the Federal Reserve, ClinicalTrials, USPTO, EPA, EU... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [MCP Layer](../categories/mcp-infrastructure.md) · CLI: pipeworx

- [Prospeo](../tools/prospeo.md) prospeo.io A B2B contact database/lookup tool that finds verified work emails and mobile phone numbers for a given person or domain and returns basic firmographic data (headcount, industry, tech stack) for companies;... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Data & Enrichment](../categories/data-enrichment.md) · CLI: prospeo (community)

- [Snowflake (Cortex AI, as GTM/RevOps warehouse layer)](../tools/snowflake.md) snowflake.com Cloud data warehouse that acts as the central store where GTM data (CRM, product usage, marketing, support) gets modeled and joined; increasingly the platform other reverse-ETL tools (Hightouch, Fivetran... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [RevOps Infra](../categories/revops-infra.md) · CLI: snowflake-cli

- [Tavus](../tools/tavus.md) tavus.io Developer platform for building real-time, two-way conversational AI video agents ("Conversational Video Interface") - positioned for GTM use cases like greeting website visitors and booking meetings, not... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Video Prospecting](../categories/video-prospecting.md) · CLI: tavus

- [Tidio](../tools/tidio.md) tidio.com Customer-service platform combining live chat, a help desk, and an AI agent ("Lyro") that resolves routine support/sales questions automatically. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Inbound & PLG Chat](../categories/inbound-plg-chat.md) · CLI (community)

- [usefulapi.io](../tools/usefulapi-io.md) usefulapi.io A hosted catalogue of 146 single-application MCP servers, one per SaaS product, each on its own subdomain, wrapping that product's public REST API as a named tool list with per-tool read and write labels and... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Zapier](../tools/zapier.md) zapier.com A cloud automation platform connecting thousands of apps via trigger-action workflows (Zaps), plus a separate agent product. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [RevOps Infra](../categories/revops-infra.md) · CLI: zapier-platform

- [Zapier MCP](../tools/zapier-mcp.md) zapier.com Zapier's own MCP endpoint, letting Claude, ChatGPT, Cursor, and other MCP clients trigger the same 9,000+ app actions Zapier already exposes to its classic trigger-action Zaps. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [MCP Layer](../categories/mcp-infrastructure.md) · CLI: zapier-platform

- [ZoomInfo](../tools/zoominfo.md) zoominfo.com A B2B contact/company database and go-to-market platform (500M+ contacts, 100M+ companies) built from web crawling, public filings, and human researchers, used for prospecting, account research, and lead... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · [Data & Enrichment](../categories/data-enrichment.md) · CLI: gtm

- [Apollo.io](../tools/apollo-io.md) apollo.io A combined B2B contact database (265M+ contacts) and sales engagement platform in one product - prospect search/filtering, email and call sequencing, and contact/organization enrichment. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Attention](../tools/attention.md) attention.com Captures, transcribes, and analyzes sales and customer conversations, automatically syncing structured insights to the CRM. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Conversation Intel](../categories/conversation-intel.md) · CLI (community)

- [Bright Data](../tools/bright-data.md) brightdata.com A general-purpose web-scraping/proxy infrastructure platform (residential proxies, browser automation, structured scraping APIs) that GTM engineers repurpose to pull LinkedIn, company-site, and directory data... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Data & Enrichment](../categories/data-enrichment.md) · CLI: bdata

- [Chili Piper](../tools/chili-piper.md) chilipiper.com Inbound lead-routing and instant meeting-booking platform ("Concierge") that qualifies web-form leads and books them directly onto the right rep's calendar in real time. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Scheduling & Routing](../categories/scheduling-routing.md)

- [Chili Piper](../tools/chili-piper.md) chilipiper.com Inbound lead routing and meeting-scheduling platform - converts web-form submissions and inbound leads into booked meetings in seconds, with rep-availability and fairness-rule logic. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Inbound & PLG Chat](../categories/inbound-plg-chat.md) · Cross listed, canonical home is Scheduling & Routing

- [Clay](../tools/clay.md) clay.com A spreadsheet-style workflow/orchestration tool that runs lead and company records through "waterfall" lookups across 100-200+ third-party data providers (Apollo, Lusha, Clearbit, etc.) and chains automation... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Coresignal](../tools/coresignal.md) coresignal.com Sells structured B2B datasets and APIs (company, employee/people, job-posting records) scraped and normalized from public and professional-network sources, delivered as bulk datasets or pay-per-call enrichment... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [dbt (dbt platform remote MCP)](../tools/dbt.md) getdbt.com The transformation layer of the modern data stack: SQL models, tests and documentation compiled and run against a warehouse, with a hosted "dbt platform" (formerly dbt Cloud) that adds scheduling, a Semantic... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [RevOps Infra](../categories/revops-infra.md) · CLI: dbt

- [Derrick](../tools/derrick.md) derrick-app.com A credit-metered B2B enrichment engine sold primarily as a Google Sheets add-on, plus a REST API and a hosted MCP server, covering email finding, mobile phone finding, LinkedIn profile lookup, company... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Explorium](../tools/explorium.md) explorium.ai Aggregates roughly 50 third-party data sources into one API/platform for business and prospect lookup (firmographics, contacts, technographics, business events), claiming coverage of 150M+ companies and 800M+... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Data & Enrichment](../categories/data-enrichment.md) · CLI: explorium (community)

- [Fiber AI](../tools/fiber-ai.md) fiber.ai B2B search and enrichment APIs for finding companies and people by structured filters or natural language, then revealing work emails and phone numbers with live LinkedIn data. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Granola](../tools/granola.md) granola.ai General-purpose AI notetaker that generates enhanced meeting notes and summaries from a local desktop app. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Conversation Intel](../categories/conversation-intel.md) · CLI: granola (community)

- [Instantly](../tools/instantly.md) instantly.ai Cold email sending platform providing mailbox infrastructure, warmup, deliverability management, sequencing, and lead sourcing. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Engagement & Outbound](../categories/engagement-outbound.md) · CLI: instantly (community)

- [JustCall](../tools/justcall.md) justcall.io A cloud phone, SMS and WhatsApp platform for sales and support teams built by SaaS Labs, with a sales dialer, CRM integrations and AI voice agents, plus a hosted MCP server that lets an assistant read and act... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [La Growth Machine](../tools/la-growth-machine.md) lagrowthmachine.com Multi-channel prospecting platform that sequences outreach across LinkedIn, email, Twitter/X, and voice notes/calls from one campaign builder, with built-in lead enrichment. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [Make](../tools/make.md) make.com A visual, node-based workflow automation platform ("scenarios") connecting 3,000+ apps, with newer AI-agent and natural-language-build features layered on top. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [RevOps Infra](../categories/revops-infra.md)

- [Metorial](../tools/metorial.md) metorial.com A hosted MCP gateway that gives AI agents/"AI employees" centralized, governed access to a company's SaaS tools (Google Workspace, Microsoft 365, GitHub, Jira, Slack, Teams, Stripe, Salesforce, Zendesk, and... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [MCP Layer](../categories/mcp-infrastructure.md) · CLI: metorial

- [Ocean.io](../tools/ocean-io.md) ocean.io A company-search and "lookalike" prospecting tool that finds businesses similar to a given target account based on industry, size, geography, and website content, and exports the resulting account lists. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Octave](../tools/octave.md) octavehq.com A GTM context engine that stores a company's ICP, personas, positioning, competitors, proof points, and objections as one structured model, then serves that model to sequences, scripts, and AI agents at... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [RevOps Infra](../categories/revops-infra.md)

- [Offorte](../tools/offorte.md) offorte.com Proposal software (templates, interactive web proposals, e-signature, open and read tracking, automation sets) for small businesses, with a REST API, webhooks and an MCP server published by the vendor. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Proposals & Deals](../categories/proposals-deals.md)

- [PhantomBuster](../tools/phantombuster.md) phantombuster.com General browser-automation/data-extraction platform ("Phantoms") that runs cloud scripts to scrape and act on LinkedIn and other web platforms - widely used as a LinkedIn outbound backbone rather than a... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Engagement & Outbound](../categories/engagement-outbound.md) · CLI: phantombuster (community)

- [Reply.io](../tools/reply-io.md) reply.io Multichannel sales engagement platform for email, LinkedIn, call, and SMS outreach with an AI SDR product layered on top. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Engagement & Outbound](../categories/engagement-outbound.md) · CLI: reply

- [Reply.io (Jason AI)](../tools/reply-io.md) reply.io A multichannel sales engagement platform whose AI layer ("Jason AI," per widely reported branding) generates outreach emails/follow-ups and automates sequencing across email, calls, and tasks. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [AI SDRs](../categories/ai-sdr-agents.md) · Cross listed, canonical home is Engagement & Outbound · CLI: reply

- [RingCentral App Connect MCP](../tools/ringcentral-app-connect-mcp.md) ringcentral.com One of four MCP servers RingCentral publishes through its Labs programme; this one bridges RingCentral telephony to whichever CRM the customer has linked through the App Connect browser extension, so an... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [RocketReach](../tools/rocketreach.md) rocketreach.co A large contact/company lookup database queried by name, company domain, or LinkedIn profile to find work emails, direct dials, and mobile numbers, with bulk lookup and CRM/Salesforce sync. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Salesforge](../tools/salesforge.md) salesforge.ai Multi-channel cold outreach platform (email + LinkedIn) with an AI SDR product ("Agent Frank") layered on top of standard sequencing. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Engagement & Outbound](../categories/engagement-outbound.md) · CLI: forge

- [Salesforge (Agent Frank)](../tools/salesforge.md) salesforge.ai An AI agent ("Agent Frank") that prospects, writes tailored outreach, sends across email and LinkedIn, manages follow-up sequences, and books meetings - positioned to either join a human team or fully replace... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [AI SDRs](../categories/ai-sdr-agents.md) · Cross listed, canonical home is Engagement & Outbound · CLI: forge

- [Smartlead](../tools/smartlead.md) smartlead.ai Cold email outreach platform for managing campaigns across many mailboxes, with built-in deliverability infrastructure and a unified reply inbox. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Engagement & Outbound](../categories/engagement-outbound.md) · CLI: smartlead

- [SparkToro](../tools/sparktoro.md) sparktoro.com Audience-research tool that shows what a defined audience (by keyword, website, social account, or podcast) reads, watches, listens to, and follows, by combining social-graph, search, and web-crawl data. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Community & Dark Social](../categories/community-dark-social.md)

- [tl;dv](../tools/tl-dv.md) tldv.io Records and transcribes Zoom, Google Meet, and Microsoft Teams calls, layering on sales coaching (playbook monitoring, objection handling) at higher tiers. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Conversation Intel](../categories/conversation-intel.md) · CLI: tldv (community)

- [Trainual](../tools/trainual.md) trainual.com SOP and process-documentation platform for onboarding and training, positioned more broadly at operations/HR than sales-specific enablement, with AI-assisted SOP drafting. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Enablement & Coaching](../categories/enablement-coaching.md)

- [Waalaxy](../tools/waalaxy.md) waalaxy.com Chrome-extension-based LinkedIn (+ email) prospecting tool that automates invitations, messages, and multi-step campaigns, with a built-in prospect finder. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [Woodpecker](../tools/woodpecker.md) woodpecker.co Cold email and LinkedIn outreach automation tool with inbox rotation, adaptive sending, and centralized reply management. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md) · [Engagement & Outbound](../categories/engagement-outbound.md) · CLI: woodpecker

- [Paragon (ActionKit MCP)](../tools/paragon.md) useparagon.com An embedded integration platform for SaaS products, whose ActionKit product exposes a stated 1,000-plus actions across 130-plus third-party applications through one API and one MCP server, with Paragon... [Official MCP](../mcp/official.md) · [Enterprise leaning](../gates/enterprise-leaning.md) · [MCP Layer](../categories/mcp-infrastructure.md) · CLI: whiskers

- [Anaplan (PlanIQ / Anaplan Forecaster)](../tools/anaplan.md) anaplan.com Connected-planning platform whose AI forecasting engine - originally branded PlanIQ, now superseded by "Anaplan Forecaster" (launched October 2025) - generates time-series demand/sales/revenue forecasts that... [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md) · [Forecasting & Revenue](../categories/forecasting-revenue.md) · CLI (community)

- [Apollo.io Sequences (Emailer Campaigns)](../tools/apollo-io-sequences.md) apollo.io Apollo's outbound-sequencing feature - multi-step, multi-channel (email/call/task) cadences that enroll contacts pulled from Apollo's prospecting database and track send/reply state. [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [Common Room](../tools/common-room.md) commonroom.io Aggregates buyer/community engagement signals - Slack, Discord, GitHub activity (stars, PRs, issues), product usage, and third-party intent data (Bombora integration) - across a company's community/product... [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md) · [Signals & Intent](../categories/signals-intent-abm.md) · CLI: cr

- [Common Room](../tools/common-room.md) commonroom.io See the full RESEARCHED entry in 05-signals-intent-abm.md (Common Room is filed there as its canonical home in this directory) - aggregates Slack, Discord, GitHub, product-usage, and third-party intent signals... [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md) · [Community & Dark Social](../categories/community-dark-social.md) · Cross listed, canonical home is Signals & Intent · CLI: cr

- [Gong](../tools/gong.md) gong.io Records, transcribes, and analyzes sales calls and emails, then rolls the signals into deal-risk scores, coaching data, and revenue forecasts. [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md) · [Conversation Intel](../categories/conversation-intel.md)

- [Ironclad](../tools/ironclad.md) ironcladapp.com Contract lifecycle management (CLM) platform for drafting, negotiating, and managing contracts with workflow automation across legal, sales, and procurement teams - sales-adjacent rather than a sales tool... [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md) · [Proposals & Deals](../categories/proposals-deals.md) · CLI: rivet

- [Looker](../tools/looker.md) cloud.google.com Google Cloud's governed BI platform (LookML semantic model, explores, Looks, dashboards, embedded analytics) that sits on top of a warehouse; two first-party MCP routes exist, a local MCP Toolbox prebuilt... [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md) · [RevOps Infra](../categories/revops-infra.md)

- [mcp.run / TurboMCP](../tools/mcp-run-turbomcp.md) turbomcp.ai An enterprise self-hosted MCP gateway and management platform - a trusted, admin-curated registry plus RBAC-controlled deployment of MCP servers across a team's own infrastructure (K8s, PaaS, VMs). [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Meltwater](../tools/meltwater.md) meltwater.com Media-intelligence and social-listening platform that consolidates news coverage, social conversations, and AI-generated content into prioritized alerts and workflows for PR, comms, and marketing teams. [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md) · [Community & Dark Social](../categories/community-dark-social.md) · CLI: generateJwk

- [Nooks](../tools/nooks.md) nooks.ai AI parallel dialer and "virtual salesfloor" combining multi-line dialing, live manager coaching, and prospecting assistance for SDR teams. [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md) · [Engagement & Outbound](../categories/engagement-outbound.md)

- [Salesforce (core CRM/platform) + Agentforce](../tools/salesforce-agentforce.md) salesforce.com A cloud CRM/platform for managing sales, service, and marketing records via a database, APIs, and a low-code app layer, with Agentforce as a layer on top for configuring autonomous AI agents that read... [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md) · [RevOps Infra](../categories/revops-infra.md) · CLI: sf

- [Klavis AI](../tools/klavis-ai.md) klavis.ai Primarily an AI-agent training-data company - it builds "live environments for training AI agents" (long-horizon coding tasks and agentic tool-use scenarios), and separately mentions "production MCP servers"... [Official MCP](../mcp/official.md) · [Gate unknown](../gates/unknown.md) · [MCP Layer](../categories/mcp-infrastructure.md)

- [Reclaim.ai](../tools/reclaim-ai.md) reclaim.ai AI calendar app that auto-schedules tasks, habits, and focus time around a user's existing meetings, dynamically defending and rebalancing the calendar as things change. [Official MCP](../mcp/official.md) · [Gate unknown](../gates/unknown.md) · [Scheduling & Routing](../categories/scheduling-routing.md) · CLI: reclaim (community)

- [RevenueHero](../tools/revenuehero.md) revenuehero.io Instant meeting-scheduling and inbound-lead-routing tool that qualifies web-form leads against CRM data and books them directly onto the right rep's calendar without a redirect. [Official MCP](../mcp/official.md) · [Gate unknown](../gates/unknown.md) · [Scheduling & Routing](../categories/scheduling-routing.md)

- [Zoom Revenue Accelerator](../tools/zoom-revenue-accelerator.md) zoom.com Zoom's built-in conversation/revenue-intelligence layer that analyzes Zoom Meetings and Phone calls for deal insights, scorecards, and account activity. [Official MCP](../mcp/official.md) · [Gate unknown](../gates/unknown.md) · [Conversation Intel](../categories/conversation-intel.md)

- [Loom](../tools/loom.md) loom.com Async video-messaging platform; in its sales use case, reps record personalized video messages with name/company variables, track prospect views, and embed CTAs/booking links directly in the video. [Community MCP](../mcp/community.md) · [Free to start](../gates/free.md) · [Video Prospecting](../categories/video-prospecting.md)

- [People Data Labs](../tools/people-data-labs.md) peopledatalabs.com A raw person/company data API that returns profile records (name, job history, education, skills, social handles, contact fields) matched by identifiers like email, name, or LinkedIn URL, plus SQL-style bulk... [Community MCP](../mcp/community.md) · [Free to start](../gates/free.md) · [Data & Enrichment](../categories/data-enrichment.md)

- [Aircall](../tools/aircall.md) aircall.io A cloud phone system and call centre for sales and support teams (numbers, dialer campaigns, call recording, SMS, CRM integrations) with a public REST API and webhooks. [Community MCP](../mcp/community.md) · [Paid, self-serve](../gates/paid.md) · [Engagement & Outbound](../categories/engagement-outbound.md) · CLI: aircall (community)

- [Mention](../tools/mention.md) mention.com Monitors web and social mentions across a claimed 1 billion+ sources in real time, layering sentiment/reach analytics and a unified social inbox on top of the monitoring feed. [Community MCP](../mcp/community.md) · [Paid, self-serve](../gates/paid.md) · [Community & Dark Social](../categories/community-dark-social.md) · CLI (community)

- [Motion](../tools/motion.md) usemotion.com AI-driven work-management app that auto-schedules a user's tasks, projects, and meetings onto their calendar around priorities and deadlines, bundled with note-taking and document tools. [Community MCP](../mcp/community.md) · [Paid, self-serve](../gates/paid.md) · [Scheduling & Routing](../categories/scheduling-routing.md)

- [Overloop](../tools/overloop.md) overloop.com Sales engagement and lead-gen platform for finding, verifying, and contacting B2B prospects via automated email and LinkedIn campaigns. [Community MCP](../mcp/community.md) · [Paid, self-serve](../gates/paid.md) · [Engagement & Outbound](../categories/engagement-outbound.md) · CLI: overloop (community)

- [SavvyCal](../tools/savvycal.md) savvycal.com Prospect-facing scheduling/booking-page tool (Calendly competitor) built around letting invitees overlay their own calendar on the organizer's availability, with Collective/Round-Robin/Group team-scheduling... [Community MCP](../mcp/community.md) · [Paid, self-serve](../gates/paid.md) · [Scheduling & Routing](../categories/scheduling-routing.md)

- [Syften](../tools/syften.md) syften.com Monitors Reddit, Hacker News, X/Twitter, Bluesky, Mastodon, GitHub, YouTube, Slack communities, and general web/forum sources for keyword mentions, delivering alerts via email, Slack, RSS, webhook, or API. [Community MCP](../mcp/community.md) · [Paid, self-serve](../gates/paid.md) · [Community & Dark Social](../categories/community-dark-social.md)

- [Trigify (Trigify.io)](../tools/trigify.md) trigify.io Monitors LinkedIn, X/Twitter, Reddit, YouTube, and podcasts for keyword mentions and engagement (likes, comments, shares, job changes), mapping who engaged with that content into an "engagement graph" filtered... [Community MCP](../mcp/community.md) · [Paid, self-serve](../gates/paid.md) · [Signals & Intent](../categories/signals-intent-abm.md) · CLI: trigify

- [Unify](../tools/unify.md) unifygtm.com A hybrid signals-plus-agent platform: AI agents build targeted account/prospect lists from 40+ data sources, write personalized outbound copy, and run multi-channel sequences triggered by intent signals... [Community MCP](../mcp/community.md) · [Paid, self-serve](../gates/paid.md) · [AI SDRs](../categories/ai-sdr-agents.md) · CLI: unify-cli (community)

- [Brandwatch](../tools/brandwatch.md) brandwatch.com Enterprise consumer-intelligence and social-listening suite spanning social media management, influencer marketing, search/GenAI-mention monitoring, and analyst-backed media intelligence. [Community MCP](../mcp/community.md) · [Enterprise only](../gates/enterprise-only.md) · [Community & Dark Social](../categories/community-dark-social.md) · CLI (community)

- [Chorus](../tools/chorus.md) zoominfo.com Records, transcribes, and analyzes sales calls, meetings, and emails, and syncs the resulting insights into the CRM. [Community MCP](../mcp/community.md) · [Enterprise only](../gates/enterprise-only.md) · [Conversation Intel](../categories/conversation-intel.md) · CLI: gtm

- [Copy.ai (GTM AI Platform)](../tools/copy-ai.md) copy.ai Pivoted from an AI copywriting tool to a workflow-building platform ("Copy Agents") that automates GTM tasks - prospecting/lead research, inbound enrichment, content generation, deal analysis - via user-built... [Community MCP](../mcp/community.md) · [Enterprise only](../gates/enterprise-only.md) · [AI SDRs](../categories/ai-sdr-agents.md)

- [Jiminny](../tools/jiminny.md) jiminny.com Records, transcribes, and scores sales calls, syncing action items and summaries into the CRM. [Community MCP](../mcp/community.md) · [Enterprise only](../gates/enterprise-only.md) · [Conversation Intel](../categories/conversation-intel.md)

- [Loopio](../tools/loopio.md) loopio.com RFP/RFI response-management platform with a searchable content library, AI-assisted answer drafting, and collaborative proposal workflows for larger bid teams. [Community MCP](../mcp/community.md) · [Enterprise only](../gates/enterprise-only.md) · [Proposals & Deals](../categories/proposals-deals.md)

- [WorkRamp](../tools/workramp.md) workramp.com Corporate learning and training platform ("Business Academy") for employee onboarding, sales enablement, and customer education content, with AI-assisted content creation. [Community MCP](../mcp/community.md) · [Enterprise only](../gates/enterprise-only.md) · [Enablement & Coaching](../categories/enablement-coaching.md)

- [Albacross](../tools/albacross.md) albacross.com Identifies which companies visit a website via IP-to-company matching, tracks on-site and off-site behavioral/intent signals, and enriches identified companies with firmographic data and optional verified... [No MCP found](../mcp/none-found.md) · [Paid, self-serve](../gates/paid.md) · [Signals & Intent](../categories/signals-intent-abm.md)

- [Orbit](../tools/orbit.md) orbit.love Was a community-analytics platform that aggregated activity across Discord, Slack, GitHub, and social channels into a unified per-person engagement score ("Orbit Level") to identify a community's most valuable... [No MCP found](../mcp/none-found.md) · [Gate unknown](../gates/unknown.md) · [Community & Dark Social](../categories/community-dark-social.md)
