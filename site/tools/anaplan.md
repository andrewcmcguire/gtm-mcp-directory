# Anaplan (PlanIQ / Anaplan Forecaster): MCP server status, API access gate and what it does

> Connected-planning platform whose AI forecasting engine  - originally branded PlanIQ, now superseded by... Official MCP, Gate unknown. Checked 2026-08-24.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Forecasting & Revenue](../categories/forecasting-revenue.md) /
Anaplan (PlanIQ / Anaplan Forecaster)

# Anaplan (PlanIQ / Anaplan Forecaster)

[Official MCP](../mcp/official.md)
[Gate unknown](../gates/unknown.md)
[Forecasting & Revenue](../categories/forecasting-revenue.md)
RESEARCHED
Checked 2026-08-24

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 0.

Vendor: [anaplan.com](https://anaplan.com) · entry id 12-anaplan · source 12-forecasting-revenue.md line 283

**What it does**
Connected-planning platform whose AI forecasting engine - originally branded PlanIQ, now superseded by "Anaplan Forecaster" (launched October 2025) - generates time-series demand/sales/revenue forecasts that feed directly into a customer's broader Anaplan models.

**AI features, separated from automation with an AI label on it**
Genuinely ML-based: the vendor names specific algorithms (DeepAR+, Prophet) combining statistical and machine-learning techniques on internal plus enriched external data to uncover patterns and correlations; Anaplan Forecaster is described as the next generation of PlanIQ with expanded ML algorithms and improved explainability. Separately, "CoModeler" (natural-language model building) and role-based AI agents are LLM-workflow features, not the forecasting engine itself.

**RevOps role**
Enterprise connected-planning platform where sales/demand forecasting is one module among many (finance, supply chain, workforce); the AI Gateway/MCP layer is Anaplan's play to make that planning data agent-accessible.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: unknown - described only as a "governed MCP connection" with permission/audit controls; the specific credential mechanism (API key vs. OAuth) is not disclosed on the page found.

- **Parsed URLs**: 1 found in the mcp_url field

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established on 2026-08-24 and has not been re-fetched since.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://www.anaplan.com/platform/intelligence/ - the "Anaplan AI Gateway" feature page states: "Securely connect any LLM interface or enterprise agent to Anaplan through a governed MCP connection, with controls for permissions, auditability, consumption management, and rate limiting." No separate dedicated MCP docs/repo page was found beyond this feature description.

- [https://www.anaplan.com/platform/intelligence/](https://www.anaplan.com/platform/intelligence/)

**Access gate**

- **Gate bucket**: Gate unknown

- **Can a solo operator reach it**: Not established

api_gate, verbatim from the file:

unknown/enterprise-leaning. No pricing or plan-gating information is disclosed on the pages reviewed; Anaplan is sold via enterprise contract in every other context researched for this directory, and nothing found here contradicts that pattern.

83 of 293 entries carry an unknown gate. Unknown is a legal answer and it ships as unknown rather than as a guess.

**API documentation**

No documentation URL recorded.

263 of 293 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**Jobs it can do**

- [Read the pipeline forecast](../jobs/read-pipeline-forecast.md)
- [Model a revenue plan](../jobs/model-revenue-plan.md)

A job tag means the vendor says the tool does this. It is not a test result, not proof the capability is reachable through the tool's MCP server, and not proof it is available on the gate this entry records.

Tagged by machine-pass on 2026-08-25 against the closed 55 job vocabulary. 271 of 293 entries carry at least one tag; 827 tags are assigned in total.

**Sources**

- [https://www.anaplan.com/platform/anaplan-planiq/](https://www.anaplan.com/platform/anaplan-planiq/)
- [https://www.anaplan.com/platform/intelligence/](https://www.anaplan.com/platform/intelligence/)
- [https://help.anaplan.com/drive-intelligent-forecasting-with-planiq-7333fab4-7118-45d9-8504-4137bc114e04](https://help.anaplan.com/drive-intelligent-forecasting-with-planiq-7333fab4-7118-45d9-8504-4137bc114e04)
- [https://www.globenewswire.com/news-release/2025/12/09/3202449/0/en/Anaplan-Introduces-Role-Based-AI-Agents-to-Advance-Industry-Leading-Enterprise-Scenario-Planning-and-Analysis-Platform.html](https://www.globenewswire.com/news-release/2025/12/09/3202449/0/en/Anaplan-Introduces-Role-Based-AI-Agents-to-Advance-Industry-Leading-Enterprise-Scenario-Planning-and-Analysis-Platform.html)
- [https://www.pulsemcp.com/servers?q=anaplan](https://www.pulsemcp.com/servers?q=anaplan)

5 source URLs. Raw sources field, verbatim:

https://www.anaplan.com/platform/anaplan-planiq/, https://www.anaplan.com/platform/intelligence/, https://help.anaplan.com/drive-intelligent-forecasting-with-planiq-7333fab4-7118-45d9-8504-4137bc114e04, https://www.globenewswire.com/news-release/2025/12/09/3202449/0/en/Anaplan-Introduces-Role-Based-AI-Agents-to-Advance-Industry-Leading-Enterprise-Scenario-Planning-and-Analysis-Platform.html, https://www.pulsemcp.com/servers?q=anaplan

**Notes, verbatim from the file**
Marked official rather than none-found because Anaplan's own product page explicitly names MCP with a linkable URL, satisfying the schema's "URL required" law - the same judgment call made for the Default entry in 06-revops-infra.md - even though no dedicated MCP docs/repo page exists yet. Re-check as this matures; it currently reads as an early/generic capability statement rather than a documented integration.

**Provenance**

- **Entry id**: 12-anaplan

- **Source file**: 12-forecasting-revenue.md

- **Source line**: 283

- **Tier**: RESEARCHED

- **last_checked**: 2026-08-24

- **Data baked**: 2026-08-25

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
