# Forecasting & Revenue: 17 tools, 3 with an official MCP server

> Tools that try to answer "how much will we actually close this quarter" - CRM-native ML forecast... 17 tools counted, 3 with an official MCP server and 1 free to start.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[By category](index.md) / Forecasting & Revenue

**12 · forecasting-revenue**

## Forecasting & Revenue

Tools that try to answer "how much will we actually close this quarter" - CRM-native ML forecast engines (BoostUp/Terret, Aviso, Kluster) sold sales-led and quote-only, incentive-comp platforms that tie forecast risk to rep behavior (Xactly, Varicent), FP&A tools that model revenue top-down as one planning use case among several (Vareto, Cube Software, Pigment, Anaplan), and forecasting bolted onto core CRMs for free (Salesforce, HubSpot). The tension: almost every vendor in this category quotes a specific forecast-accuracy percentage with no published methodology behind a demo-request wall, and a real, self-serve MCP server is the exception rather than the rule - Pigment and Cube Software are the only two found here with one.

- **entries in this file**: 17

- **Official MCP**: 3
- **No MCP found**: 14

- **Free to start**: 1
- **Paid, self-serve**: 3
- **Enterprise only**: 13

Source file: 12-forecasting-revenue.md · content sha256 45fa59f2494342e7... · counts reconciled against tools_recount.py at build time.

- [The 3 with an MCP server](../lists/mcp-forecasting-revenue.md)

- [Read the pipeline forecast](../jobs/read-pipeline-forecast.md)
- [Model a revenue plan](../jobs/model-revenue-plan.md)
- [Extract deal signals from calls](../jobs/extract-deal-signals-from-calls.md)
- [Write CRM records](../jobs/write-crm-records.md)

- [Cube Software](../tools/cube-software.md) cubesoftware.com Spreadsheet-native FP&A planning and reporting platform for finance teams; revenue-scenario modeling is one supported use case rather than a dedicated CRM-native sales-forecasting product. [Official MCP](../mcp/official.md) · [Paid, self-serve](../gates/paid.md)

- [Anaplan (PlanIQ / Anaplan Forecaster)](../tools/anaplan.md) anaplan.com Connected-planning platform whose AI forecasting engine - originally branded PlanIQ, now superseded by "Anaplan Forecaster" (launched October 2025) - generates time-series demand/sales/revenue forecasts that... [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md)

- [Pigment](../tools/pigment.md) pigment.com AI-native enterprise business-planning (EPM) platform used across finance, sales, HR, and supply chain; GTM-relevant use cases include capacity, territory, and quota planning and revenue-growth-management... [Official MCP](../mcp/official.md) · [Enterprise only](../gates/enterprise-only.md)

- [Pipedrive (AI Sales Assistant / forecasting)](../tools/pipedrive.md) pipedrive.com Pipedrive's built-in AI-driven forecasting layer - not a separately branded "Insights" product, but the CRM's AI Sales Assistant plus probability-weighted pipeline forecasting math. See 06-revops-infra.md for... [No MCP found](../mcp/none-found.md) · [Free to start](../gates/free.md) · Cross listed, canonical home is RevOps Infra

- [Forecastio](../tools/forecastio.md) forecastio.ai AI sales-forecasting and pipeline-intelligence platform built for HubSpot and Salesforce users, applying machine learning, time-series models, and weighted-pipeline methods to predict a forecast range (best... [No MCP found](../mcp/none-found.md) · [Paid, self-serve](../gates/paid.md)

- [HubSpot (AI Forecasting)](../tools/hubspot.md) hubspot.com HubSpot's forecasting tool inside Sales Hub/Service Hub, turning pipeline data into revenue predictions via weighted-pipeline calculations plus an "AI forecasting" layer shown in-product. See... [No MCP found](../mcp/none-found.md) · [Paid, self-serve](../gates/paid.md) · Cross listed, canonical home is RevOps Infra

- [Aviso](../tools/aviso.md) aviso.com AI revenue operations platform combining pipeline forecasting, conversation/deal intelligence, and agentic workflow automation for sales, RevOps, and customer success teams. [No MCP found](../mcp/none-found.md) · [Enterprise only](../gates/enterprise-only.md)

- [BoostUp (rebranded: Terret)](../tools/boostup.md) terret.ai AI revenue-intelligence and pipeline-forecasting platform that ingests CRM, email, call, and calendar data to produce forecasts and deal-risk scores, plus (post-rebrand) automated GTM workflow agents. [No MCP found](../mcp/none-found.md) · [Enterprise only](../gates/enterprise-only.md)

- [Ebsta](../tools/ebsta.md) ebsta.com Revenue-intelligence add-on for Salesforce/HubSpot that syncs email and calendar activity into the CRM and layers on relationship scoring, conversation capture, and pipeline forecasting. [No MCP found](../mcp/none-found.md) · [Enterprise only](../gates/enterprise-only.md)

- [Gong Forecast](../tools/gong-forecast.md) gong.io A licensed add-on module (separate from the base Gong Foundation license, with a lighter "Forecast Essentials" tier bundled into Gong's Deal Execution package) that turns Gong's conversation-intelligence... [No MCP found](../mcp/none-found.md) · [Enterprise only](../gates/enterprise-only.md)

- [Kluster](../tools/kluster.md) kluster.com AI-native revenue forecasting and revenue-analytics platform for mid-market to enterprise SaaS companies - plugs into the CRM, ingests historical performance and activity data, and produces AI/statistical... [No MCP found](../mcp/none-found.md) · [Enterprise only](../gates/enterprise-only.md)

- [Mediafly (Intelligence360, formerly InsightSquared)](../tools/mediafly.md) mediafly.com Combined revenue-enablement and revenue-intelligence platform; the InsightSquared product (acquired January 2022) is now folded into "Mediafly Intelligence360," providing deal inspection, pipeline forecasting,... [No MCP found](../mcp/none-found.md) · [Enterprise only](../gates/enterprise-only.md)

- [Revenue.io](../tools/revenue-io.md) revenue.io Salesforce-native AI-guided-selling platform whose forecasting product reads live Salesforce opportunity data to produce automatic rep/manager/VP forecast roll-ups without CSV exports or manual sync. [No MCP found](../mcp/none-found.md) · [Enterprise only](../gates/enterprise-only.md)

- [Salesforce Einstein Forecasting](../tools/salesforce-einstein-forecasting.md) salesforce.com Sales Cloud's AI forecasting feature, analyzing past opportunities, account history, and activities plus rep win-rates to generate revenue predictions with confidence ranges. See 06-revops-infra.md for... [No MCP found](../mcp/none-found.md) · [Enterprise only](../gates/enterprise-only.md)

- [Vareto](../tools/vareto.md) vareto.com FP&A / financial-planning platform for finance teams (budgeting, headcount planning, driver-based modeling, cash-flow forecasting) that lists "Sales Revenue Forecasting" and "Capacity Planning" as one of... [No MCP found](../mcp/none-found.md) · [Enterprise only](../gates/enterprise-only.md)

- [Varicent](../tools/varicent.md) varicent.com Enterprise sales-performance-management (SPM) platform covering incentive compensation, quota setting, territory design, pipeline management, and revenue forecasting in one suite. [No MCP found](../mcp/none-found.md) · [Enterprise only](../gates/enterprise-only.md)

- [Xactly](../tools/xactly.md) xactlycorp.com Revenue platform combining incentive-compensation management (Xactly Incent) with pipeline/revenue forecasting (Xactly Forecast), using compensation-plan and rep-behavior data as a forecasting input. [No MCP found](../mcp/none-found.md) · [Enterprise only](../gates/enterprise-only.md)
