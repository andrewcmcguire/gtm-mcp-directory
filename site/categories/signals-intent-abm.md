# Signals & Intent: 52 tools, 20 with an official MCP server

> Tools that try to answer "who is about to buy, and how do you know." The category splits cleanly... 52 tools counted, 20 with an official MCP server and 6 free to start.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[By category](index.md) / Signals & Intent

**05 · signals-intent-abm**

## Signals & Intent

Tools that try to answer "who is about to buy, and how do you know." The category splits cleanly into two eras: the legacy enterprise intent-data incumbents (6sense, Demandbase, Bombora, HG Insights) sold on annual contracts with no self-serve path, and a newer wave of visitor-ID/job-change/ API-first tools (RB2B, Warmly, Crustdata, TheirStack, PredictLeads) built for solo operators with free tiers and documented MCP servers.

- **entries in this file**: 52

- **Official MCP**: 20
- **Community MCP**: 2
- **MCP unknown**: 2
- **MCP not applicable**: 1
- **No MCP found**: 27

- **ship a CLI (official) as of 2026-09-12**: 2

- **Free to start**: 6
- **Paid, self-serve**: 13
- **Enterprise only**: 10
- **Gate unknown**: 23

Source file: 05-signals-intent-abm.md · content sha256 9d71ea93b6580d73... · counts reconciled against tools_recount.py at build time.

- [The 22 with an MCP server](../lists/mcp-signals-intent-abm.md)

- [Fetch buyer intent signals](../jobs/fetch-buyer-intent-signals.md)
- [Identify an anonymous website visitor](../jobs/identify-anonymous-website-visitor.md)
- [Enrich a company from a domain](../jobs/enrich-company-from-domain.md)
- [Detect a company's tech stack](../jobs/detect-technographics.md)

- [Crustdata](../tools/crustdata.md) crustdata.com Aggregates real-time company and people data (250+ data points per company from 15+ sources - funding, headcount, web signals, social, reviews) plus a "Watcher API" for near-real-time hiring/funding/event... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md) · Cross listed, canonical home is Data & Enrichment

- [Leadfeeder (product line rebranded/merged under Dealfront; dealfront.com redirects to leadfeeder.com)](../tools/leadfeeder.md) leadfeeder.com Identifies companies visiting a website via IP-to-company matching, tracks page-level visit behavior, and surfaces intent signals plus verified contact data for those companies. [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)

- [PredictLeads](../tools/predictleads.md) predictleads.com Aggregates five signal categories (job openings, technology detections, news events, business connections, firmographics) across 129M companies in 195 countries by scraping public web sources - company sites,... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)

- [TheirStack](../tools/theirstack.md) theirstack.com Tracks 233M+ job postings across 195+ countries and 33,000+ technologies to detect hiring signals, technographic footprint, and buying-intent signals (job-posting keywords implying a company has or needs a... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)

- [Warmly (Warmly.ai)](../tools/warmly.md) warmly.ai De-anonymizes website visitors at the person and company level from site traffic, and aggregates first-party (web/product/CRM), second-party (social/job-change), and third-party (Bombora intent, keyword... [Official MCP](../mcp/official.md) · [Free to start](../gates/free.md)

- [CatchIntent](../tools/catchintent.md) catchintent.com A B2B intent tool that monitors social and web sources for buying signals, ranks the people behind them by warmth, enriches the profiles and drafts personalised openers, then pushes leads to a CRM or outreach... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md)

- [Factors.ai](../tools/factors-ai.md) factors.ai De-anonymizes website visitors and tracks named-account behavior (page visits, LinkedIn/Google ad engagement, email/content engagement, third-party intent research signals) to identify in-market accounts and... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md)

- [Keyplay](../tools/keyplay.md) keyplay.io Builds a mathematical ICP model from a company's existing best customers, then scores and ranks a universe of target accounts against that model using 750+ pre-built "signals" (hiring velocity, tech stack,... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md)

- [RB2B](../tools/rb2b.md) rb2b.com Deanonymizes B2B website traffic by matching visitor IP/device identifiers and first/third-party data against a contact database to reveal the specific US-based person (name, LinkedIn, email) browsing the... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md)

- [Snitcher](../tools/snitcher.md) snitcher.com Identifies anonymous website visitor companies via IP-to-company database matching, tracks on-site behavior (pages viewed, session length, return visits) via an embedded tracking script, and surfaces "hot... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md)

- [Sumble](../tools/sumble.md) sumble.com Builds an account-intelligence knowledge graph by continuously scanning tens of millions of public sources (job boards, company sites, social media, regulatory filings) to map org structure, tech stack, and... [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md)

- [6sense](../tools/6sense.md) 6sense.com Detects B2B buying intent by combining IP-based website deanonymization, a proprietary third-party intent/content-consumption network ("Signalverse"), and first-party CRM/MAP/product data to flag in-market... [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md)

- [Common Room](../tools/common-room.md) commonroom.io Aggregates buyer/community engagement signals - Slack, Discord, GitHub activity (stars, PRs, issues), product usage, and third-party intent data (Bombora integration) - across a company's community/product... [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md) · CLI: cr

- [Crossbeam](../tools/crossbeam.md) crossbeam.com Compares your account list against your partners' account lists to surface overlaps, partner-shared contacts, and warm introduction paths for co-selling. [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md) · CLI: crossbeam (community)

- [Demandbase (Demandbase One)](../tools/demandbase.md) demandbase.com Identifies and scores in-market B2B accounts by combining IP/website deanonymization, a global firmographic/technographic database, and intent-signal ingestion, rolling this into "Buying Group" and... [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md)

- [G2 Buyer Intent](../tools/g2-buyer-intent.md) g2.com Surfaces which companies are researching your product and your competitors on G2's review marketplace, plus the review and category data behind those signals. [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md)

- [HG Insights (Phoenix platform)](../tools/hg-insights.md) hginsights.com Aggregates B2B technographic data (software/tech a company runs, sourced from job postings, web crawling, public filings, partner feeds), firmographics, IT spend estimates, and third-party intent (via... [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md)

- [Similarweb](../tools/similarweb.md) similarweb.com Web, app and market intelligence platform that estimates traffic, audience, keyword and competitive metrics for any domain, used in sales as an account-prioritisation and account-research signal. [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md) · CLI: similarweb (community)

- [UserGems](../tools/usergems.md) usergems.com Tracks job changes of known contacts (past customers/champions moving to new companies) plus 30+ other native signals (new hires, promotions, funding, website visits, M&A) sourced from LinkedIn-style data... [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md)

- [Actively](../tools/actively.md) actively.ai A sales platform that runs an always-on "per-account agent" for every account in a seller's book, synthesising CRM data, call transcripts and external signals into account research, risk flags and recommended... [Official MCP](../mcp/official.md) · [Gate unknown](../gates/unknown.md)

- [Trigify (Trigify.io)](../tools/trigify.md) trigify.io Monitors LinkedIn, X/Twitter, Reddit, YouTube, and podcasts for keyword mentions and engagement (likes, comments, shares, job changes), mapping who engaged with that content into an "engagement graph" filtered... [Community MCP](../mcp/community.md) · [Paid, self-serve](../gates/paid.md) · CLI: trigify

- [abm.dev](../tools/abm-dev.md) abm.dev The account-based marketing API for AI agents: Search, Enrich, and Create across B2B people and companies, every field cited with a source and a confidence score. [Community MCP](../mcp/community.md) · [Gate unknown](../gates/unknown.md)

- [Centralize](../tools/centralize.md) usecentralize.com A relationship-intelligence and account-mapping tool that builds org charts and buying-committee maps for a rep's accounts automatically from their own CRM, email, calendar, and call data, then flags coverage... [MCP unknown](../mcp/unknown.md) · [Free to start](../gates/free.md) · CLI: cm-i (community)

- [Vector (vector.co)](../tools/vector.md) vector.co Identifies named individual buyers (not just companies) by resolving anonymous website visitors and ad-click engagement to real contacts, then tracks their behavior (job changes, CRM activity, ad engagement)... [MCP unknown](../mcp/unknown.md) · [Paid, self-serve](../gates/paid.md) · CLI: vector_cli (community)

- [Koala](../tools/koala.md) getkoala.com Identified and scored anonymous B2B website visitors by matching visitor IPs/first-party signals against 30+ data sources, then triggered configurable AI-agent workflows (enrichment, research, alerting) on... [MCP not applicable](../mcp/n-a.md) · [Paid, self-serve](../gates/paid.md)

- [Albacross](../tools/albacross.md) albacross.com Identifies which companies visit a website via IP-to-company matching, tracks on-site and off-site behavioral/intent signals, and enriches identified companies with firmographic data and optional verified... [No MCP found](../mcp/none-found.md) · [Paid, self-serve](../gates/paid.md)

- [Clearbit Reveal (rebranded: HubSpot Breeze Intelligence)](../tools/clearbit-reveal.md) clearbit.com Identifies companies visiting a website via IP-to-company matching, then enriches contact/company CRM records with firmographic data (employee count, revenue, tech stack, location) and surfaces buying-intent... [No MCP found](../mcp/none-found.md) · [Paid, self-serve](../gates/paid.md)

- [Intently (getintently.com)](../tools/intently.md) getintently.com Scrapes LinkedIn in real time (without an official API or user accounts) to extract profile/company data, competitor followers, and post reactions/comments as engagement signals. [No MCP found](../mcp/none-found.md) · [Paid, self-serve](../gates/paid.md)

- [Live Data Technologies](../tools/live-data-technologies.md) livedatatechnologies.com Tracks real-time job changes and employment history for ~80M white-collar professionals by continuously re-verifying identities against open-web and public professional data sources, surfaced via API or the... [No MCP found](../mcp/none-found.md) · [Paid, self-serve](../gates/paid.md)

- [Bombora (Company Surge)](../tools/bombora.md) bombora.com Detects which companies are actively researching specific B2B topics by aggregating content-consumption data (article reads, downloads) across a co-op of 5,000+ B2B publisher sites, then measures spikes in a... [No MCP found](../mcp/none-found.md) · [Enterprise only](../gates/enterprise-only.md)

- [Champify](../tools/champify.md) champify.io Tracks job changes of a company's past customers and champions as they move to new roles/companies, and flags closed-lost opportunities for re-engagement, integrated directly into Salesforce. [No MCP found](../mcp/none-found.md) · [Enterprise only](../gates/enterprise-only.md)

- [Avina](../tools/avina.md) avina.io Avina is an AI-powered go-to-market platform that helps B2B sales teams find, prioritize, and engage high-intent prospects using real-time buying signals. [No MCP found](../mcp/none-found.md) · [Gate unknown](../gates/unknown.md)

- [Channel99](../tools/channel99.md) channel99.com B2B marketing attribution software that uses AI to recommend ways to improve campaign ROI and increase pipeline [No MCP found](../mcp/none-found.md) · [Gate unknown](../gates/unknown.md)

- [DemandSphere](../tools/demandsphere.md) demandsphere.com Global SERP and AI search analytics platform for in-house and agency teams. Track AI Overviews, AI Mode, ChatGPT, Perplexity, Gemini, and more. [No MCP found](../mcp/none-found.md) · [Gate unknown](../gates/unknown.md)

- [eBrandValue](../tools/ebrandvalue.md) ebrandvalue.com eBrandValue enables you to track the value of your brand in real-time. Social Media Analytics, Sales Prediction, Influencer Studies, Crisis & Reputation Support 24/7. [No MCP found](../mcp/none-found.md) · [Gate unknown](../gates/unknown.md)

- [HockeyStack](../tools/hockeystack.md) hockeystack.com HockeyStack is an AI powered B2B Revenue Data Platform unifying marketing, product, and sales data, bridging PLG and sales led with attribution and AI predictive insights. [No MCP found](../mcp/none-found.md) · [Gate unknown](../gates/unknown.md)

- [Influ2](../tools/influ2.md) influ2.com Reach named buyers at every stage of the buying journey. Revenue follows focus. [No MCP found](../mcp/none-found.md) · [Gate unknown](../gates/unknown.md)

- [Leadinfo](../tools/leadinfo.md) leadinfo.com Grow your sales funnel and generate better leads. Start identifying B2B website visitors and reach out to them within Leadinfo's all-in-one platform. [No MCP found](../mcp/none-found.md) · [Gate unknown](../gates/unknown.md)

- [Lift AI](../tools/lift-ai.md) lift-ai.com Lift AI scores the behavioral context of every website visitor - anonymous or identified - with a real-time buyer probability score. 85%+ accuracy. One score feeds your entire GTM. [No MCP found](../mcp/none-found.md) · [Gate unknown](../gates/unknown.md)

- [MiQ](../tools/miq.md) wearemiq.com Do more with your data to reach new customers, in new ways, wherever they are. [No MCP found](../mcp/none-found.md) · [Gate unknown](../gates/unknown.md)

- [Modash](../tools/modash.md) modash.io High performing marketing teams use Modash to find, analyze and monitor influencers at scale all over the world. Join them today. [No MCP found](../mcp/none-found.md) · [Gate unknown](../gates/unknown.md)

- [NetLine](../tools/netline.md) netline.com Promote your B2B content with the largest B2B-specific content syndication lead generation network, using performance-based lead generation solutions to meet your demand generation goals. Identify and capture... [No MCP found](../mcp/none-found.md) · [Gate unknown](../gates/unknown.md)

- [Octane11](../tools/octane11.md) octane11.com Octane11 connects B2B marketing signals to real accounts and pipeline. Account-level analytics powered by AI. Set up in minutes. [No MCP found](../mcp/none-found.md) · [Gate unknown](../gates/unknown.md)

- [Propensity](../tools/propensity.md) propensity.com Run ABM, contextual, and geofencing campaigns to identify real buyers, generate contact-level insights, and send high-intent leads to sales. [No MCP found](../mcp/none-found.md) · [Gate unknown](../gates/unknown.md)

- [Pubrio](../tools/pubrio.md) pubrio.com Pubrio turns expansion signals across 200+ markets into one live graph, so revenue teams see which companies are entering new markets, and act on the timing. [No MCP found](../mcp/none-found.md) · [Gate unknown](../gates/unknown.md)

- [RollWorks](../tools/rollworks.md) rollworks.com AdRoll ABM: Precision B2B targeting meets multi-channel advertising. Drive pipeline & revenue with intelligent campaigns that reach the right buyers, every time. [No MCP found](../mcp/none-found.md) · [Gate unknown](../gates/unknown.md)

- [SE Ranking](../tools/se-ranking.md) seranking.com SE Ranking is a trusted AI SEO tool that pays for itself. Get accurate data, actionable insights, and automated reports. Powerful tools, simple execution. [No MCP found](../mcp/none-found.md) · [Gate unknown](../gates/unknown.md)

- [Semrush](../tools/semrush.md) semrush.com Semrush is the leading platform to grow and measure brand visibility across AI search, SEO, PPC, social, and more. [No MCP found](../mcp/none-found.md) · [Gate unknown](../gates/unknown.md)

- [Sitefire](../tools/sitefire.md) sitefire.ai Sitefire helps brands market their products to AI agents. Track AI visibility, identify what gets cited, and ship brand-aware content that ranks in generative answers. [No MCP found](../mcp/none-found.md) · [Gate unknown](../gates/unknown.md)

- [TechniQ ABM](../tools/techniq-abm.md) techniqabm.com TechniQ helps B2B teams uncover the best way into their most important accounts and turns that intelligence into messaging and ready-to-use Sales & Marketing assets. [No MCP found](../mcp/none-found.md) · [Gate unknown](../gates/unknown.md)

- [Terminus](../tools/terminus.md) terminus.com DemandScience helps B2B teams identify winnable accounts and activate them across channels-generating more pipeline without legacy ABM platform complexity. [No MCP found](../mcp/none-found.md) · [Gate unknown](../gates/unknown.md)

- [ZINFI](../tools/zinfi.md) zinfi.com ZINFI's Unified Partner Management (UPM) platform automates partner onboarding, MDF, co-sell, incentives, and channel marketing for enterprise technology and manufacturing leaders. G2 Leader. 24 modules.... [No MCP found](../mcp/none-found.md) · [Gate unknown](../gates/unknown.md)
