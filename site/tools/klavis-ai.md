# Klavis AI: MCP server status, API access gate and what it does

> Primarily an AI-agent training-data company - it builds "live environments for training AI agents"... Official MCP, Gate unknown. Checked 2026-09-02.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[MCP Layer](../categories/mcp-infrastructure.md) /
Klavis AI

# Klavis AI

[Official MCP](../mcp/official.md)
[Gate unknown](../gates/unknown.md)
[MCP Layer](../categories/mcp-infrastructure.md)
RESEARCHED
Checked 2026-09-02

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [klavis.ai](https://klavis.ai) · entry id 07-klavis-ai · source 07-mcp-infrastructure.md line 225

**What it does**
Primarily an AI-agent training-data company - it builds "live environments for training AI agents" (long-horizon coding tasks and agentic tool-use scenarios), and separately mentions "production MCP servers" and "600+ real tools and SaaS apps" as part of that training-data infrastructure.

**AI features, separated from automation with an AI label on it**
The product itself generates training/eval data for frontier model development (dockerized coding environments, programmatic verification, reward signals) - it is not positioned, in what was found, as a live GTM connector layer the way Composio/Pipedream/Metorial are.

**RevOps role**
Unclear fit for a solo GTM operator based on what's public - reads as an AI-lab infrastructure vendor (agent training data) rather than a connector service a RevOps team would wire into a live workflow. Flagging this mismatch explicitly rather than assuming it belongs alongside Composio/Pipedream.

**MCP server**

- **Status bucket**: Official MCP

- **Auth**: Klavis API key as an HTTP Bearer token on the management API that creates a per-user Strata server (https://www.klavis.ai/docs/api-reference/strata/create.md); the response returns a strataServerUrl to connect to plus per-integration OAuth and API-key setup URLs for the downstream apps. The hosted endpoint answered 401 to an unauthenticated request today.

- **Parsed URLs**: 3 found in the mcp_url field

- **Endpoint probe**: docs page, not an endpoint
- **Docs URL**: [https://www.klavis.ai/docs/concepts/strata.md](https://www.klavis.ai/docs/concepts/strata.md)
- **Probed**: 2026-09-04, HTTP 200

The vendor ships and maintains the server itself. A wrapper built by Zapier, Composio or a similar third party does not count as official. The status was established by hand on 2026-09-02. On 2026-09-04 the recorded URL served a documentation page, not an MCP endpoint. That is where to read about the server, not where to connect to it. An agent needs the second.

mcp_status, verbatim from the file:

official

mcp_url, verbatim from the file:

https://www.klavis.ai/docs/concepts/strata.md (first-party docs for the hosted Strata server; endpoint https://strata.klavis.ai/mcp/ per the official registry entry ai.klavis/strata; source at https://github.com/Klavis-AI/klavis, Apache-2.0)

- [https://www.klavis.ai/docs/concepts/strata.md](https://www.klavis.ai/docs/concepts/strata.md)
- [https://strata.klavis.ai/mcp/](https://strata.klavis.ai/mcp/)
- [https://github.com/Klavis-AI/klavis](https://github.com/Klavis-AI/klavis)

**What this server exposes**

- **Tools named**: 25
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-12
- **Repo read**: Klavis-AI/klavis
- **Whose repo**: first-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **shopify_adjust_inventory** Adjust the inventory quantity for an item at a specific location. Use this to add or remove stock after receiving shipments, cycle counts, damaged goods, or other inventory adjustments. Provide a positive number to increase stock or negativ evidence: in the server source · calling it writes

- **shopify_create_collection** Create a new product collection in your Shopify store. Collections help organize products for easier browsing. Custom collections require you to manually add products later. Smart collections automatically include products based on rules yo evidence: in the server source · calling it writes

- **shopify_create_discount** Create a new discount/price rule in your Shopify store. Discounts can be percentage-based (e.g., 20% off) or fixed amount (e.g., $10 off). They can apply to line items (products) or shipping. Configure target selection (all products or spec evidence: in the server source · calling it writes

- **shopify_create_draft_order** Create a new draft order in your Shopify store. Draft orders are perfect for processing orders over the phone, via email, or for custom quotes. They allow you to create an order, potentially apply custom pricing or discounts, and send an in evidence: in the server source · calling it spends money

- **shopify_create_fulfillment** Create a new fulfillment (shipment) for an order. Use this when you evidence: in the server source · calling it writes

- **shopify_create_order** Create a new order in the Shopify store programmatically. Useful for creating orders from external systems, processing phone orders, or creating manual orders for customers. Requires line items with product variant IDs and quantities. Can o evidence: in the server source · calling it writes

- **shopify_create_product** Create a new product in the Shopify store with full configuration. Allows setting title, HTML description, vendor, product type, tags, status (active/draft/archived), and variants. Each variant can have its own price, SKU, inventory quantit evidence: in the server source · calling it writes

- **shopify_get_collection** Get detailed information about a specific collection by ID. Returns complete collection details including title, description (body_html), handle (URL slug), publication date and scope, sort order for products, collection type (custom or sma evidence: in the server source · calling it reads

- **shopify_get_customer** Get comprehensive details about a specific customer by ID. Returns complete customer profile including personal information (name, email, phone), order history (total orders, total spent), addresses (default and additional), marketing prefe evidence: in the server source · calling it reads

- **shopify_get_discount** Get detailed information about a specific discount/price rule by ID. Returns complete discount configuration including title, value type and amount, what it targets (products or shipping), how it evidence: in the server source · calling it reads

- **shopify_get_draft_order** Get comprehensive details about a specific draft order by ID. Returns complete draft order information including order name, status, customer details, all line items with pricing, subtotal/taxes/total, shipping and billing addresses, notes, evidence: in the server source · calling it spends money

- **shopify_get_inventory_levels** Get current stock levels for inventory items across your locations. Inventory levels show how much stock is available for each product variant at each location. Returns inventory item ID, location ID, available quantity, and last updated ti evidence: in the server source · calling it reads

- **shopify_get_location** Get detailed information about a specific location by ID. Returns complete location details including name, full address components, contact phone, active status, legacy flag, localized country/province names, and location capabilities. Use evidence: in the server source · calling it reads

- **shopify_get_order** Get complete details about a specific order by ID. Returns comprehensive order information including order number, customer information (name, email, phone), all line items with product details and quantities, pricing breakdown (subtotal, t evidence: in the server source · calling it reads

- **shopify_get_product** Get comprehensive details about a specific product by ID. Returns complete product information including title, description, body HTML, vendor, product type, tags, status, all variants with pricing and inventory, product options (size, colo evidence: in the server source · calling it reads

- **shopify_list_collections** List all product collections in your Shopify store, including both custom collections (manually curated) and smart collections (automatically populated based on rules). Returns collection details including title, handle, description, public evidence: in the server source · calling it reads

- **shopify_list_customers** List and browse all customers in your Shopify store with pagination. Returns customer information including name, email, phone number, total orders count, total amount spent, customer tags, marketing preferences, account status, default add evidence: in the server source · calling it reads

- **shopify_list_discounts** List all discount codes and automatic discounts (price rules) in your Shopify store. Price rules define the discount logic and can have multiple discount codes associated with them. Returns discount details including title, value type (perc evidence: in the server source · calling it reads

- **shopify_list_draft_orders** List draft orders in your Shopify store with optional filtering. Draft orders are orders created by merchants that haven evidence: in the server source · calling it reads

- **shopify_list_fulfillments** List all fulfillments (shipments) for a specific order. Fulfillments represent shipments sent to customers and track which items were shipped, tracking information, and shipment status. Returns fulfillment ID, status (pending, open, success evidence: in the server source · calling it reads

- **shopify_list_inventory_items** List inventory items in your Shopify store with optional filtering. Each product variant has an associated inventory item that tracks stock across locations. Returns inventory item details including SKU, cost, tracked status, shipping requi evidence: in the server source · calling it reads

- **shopify_list_locations** List all physical and virtual locations/warehouses configured in your Shopify store. Locations represent places where you stock and ship inventory from (warehouses, retail stores, pop-up shops, etc.). Returns location details including name evidence: in the server source · calling it reads

- **shopify_list_orders** List and search orders in your Shopify store with filtering by status. Returns comprehensive order information including order number, customer details, line items with products and quantities, pricing (subtotal, taxes, discounts, total), p evidence: in the server source · calling it spends money

- **shopify_list_products** Search and list products in your Shopify store with advanced filtering. Returns comprehensive product details including title, description, vendor, pricing, product type, variants, images, and inventory status. Use this to find products by evidence: in the server source · calling it reads

- **shopify_update_product** Update an existing product evidence: in the server source · calling it writes

119 of the 225 entries that record an official or community MCP server carry a harvested tool list. The other 106 are unmeasured, which is not the same as empty. Harvest last run 2026-09-12. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-12 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Gate unknown

- **Can a solo operator reach it**: Not established

api_gate, verbatim from the file:

unknown - pricing page referenced but not disclosed in the fetched content

33 of 336 entries carry an unknown gate. Unknown is a legal answer and it ships as unknown rather than as a guess.

**API documentation**

No documentation URL recorded.

307 of 336 entries are in the same position. Blank is legal and it is published as blank.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/Klavis-AI/klavis](https://github.com/Klavis-AI/klavis)

**On GitHub**

[github.com/Klavis-AI](https://github.com/Klavis-AI) tied to the vendor by rule 1, account website www.klavis.ai has the vendor's domain, confidence strong

- **Public repositories**: 6, forks excluded, as read on 2026-09-08
- **Mention MCP**: 1 of them
- **Look like CLIs**: 0 of them
- **Latest push**: 2026-08-04

The five most recently pushed, on 2026-09-08:

| Repository | Kind | Description | Stars | Pushed | Latest release |
|---|---|---|---|---|---|
| [deep-swe](https://github.com/Klavis-AI/deep-swe) | other | | 0 | 2026-08-04 | |
| [Toolathlon-mvp](https://github.com/Klavis-AI/Toolathlon-mvp) | other | | 0 | 2026-06-02 | |
| [klavis](https://github.com/Klavis-AI/klavis) | MCP server | Klavis AI: MCP integration platforms that let AI agents use tools reliably at any scale | 5,801 | 2026-06-01 | ts-v2.20.0 |
| [python-sdk](https://github.com/Klavis-AI/python-sdk) | SDK | | 4 | 2026-01-29 | 2.20.0 |
| [typescript-sdk](https://github.com/Klavis-AI/typescript-sdk) | SDK | | 0 | 2026-01-29 | 2.20.0 |

Kind is a heuristic guessed from the repository name, topics and description, not a fact the vendor stated. A repository count is activity, not a verdict. Read 2026-09-08.

**Jobs it can do**

No job tag on this entry.

Reason recorded by the tagging pass: unclear. The entry states the product is agent-training-data infrastructure and explicitly flags the mismatch with Composio/Pipedream. proxy-tool-calls-to-saas is plausible from the "600+ real tools" line and unsupported by everything else on the page.

65 of 336 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://www.klavis.ai](https://www.klavis.ai)
- [https://klavis.ai/pricing](https://klavis.ai/pricing)
- [https://www.klavis.ai/docs/quickstart.md](https://www.klavis.ai/docs/quickstart.md)
- [https://www.klavis.ai/docs/concepts/strata.md](https://www.klavis.ai/docs/concepts/strata.md)
- [https://www.klavis.ai/docs/api-reference/strata/create.md](https://www.klavis.ai/docs/api-reference/strata/create.md)
- [https://github.com/Klavis-AI/klavis](https://github.com/Klavis-AI/klavis)
- [https://registry.modelcontextprotocol.io/v0/servers?search=klavis](https://registry.modelcontextprotocol.io/v0/servers?search=klavis)
- (fetched; no pricing figures returned)

7 source URLs. Raw sources field, verbatim:

https://www.klavis.ai, https://klavis.ai/pricing (fetched; no pricing figures returned), https://www.klavis.ai/docs/quickstart.md, https://www.klavis.ai/docs/concepts/strata.md, https://www.klavis.ai/docs/api-reference/strata/create.md, https://github.com/Klavis-AI/klavis, https://registry.modelcontextprotocol.io/v0/servers?search=klavis

**Notes, verbatim from the file**
Included per the research brief's seed list, but the public-facing material found positions Klavis as an AI-agent training/eval company first, not a GTM-facing hosted-MCP aggregator - treat any "GTM connector" framing of Klavis with caution until a clearer product page is found. [api_gate 2026-08-25] Re-checked and left unknown, honestly: the quickstart says to create an account and get the API key from klavis.ai/home/api-keys, so keys are self-serve with no sales call and an open-source self-hosted path exists - but klavis.ai/pricing is client-rendered and returned only nav and footer to a plain fetch, so whether a free tier or a paid plan backs those keys is unverified and the free-versus-paid split stays unknown. Checked against https://www.klavis.ai/docs/quickstart.md. 2026-09-02: mcp_status none-found -> official. Klavis publishes a hosted MCP server, Strata, documented at https://www.klavis.ai/docs/concepts/strata.md ("One MCP server for AI agents to use tools progressively at any scale") with a create endpoint at https://www.klavis.ai/docs/api-reference/strata/create.md; the official MCP registry lists ai.klavis/strata with the remote https://strata.klavis.ai/mcp/ (401 today, alive and auth-gated); and the GitHub repo https://github.com/Klavis-AI/klavis describes "MCP integration platforms that let AI agents use tools reliably at any scale" with 100+ prebuilt integrations with OAuth support, cloud-hosted or self-hosted. That softens the caution above: Klavis is a usable MCP integration layer as well as a training-data vendor. Pricing is still unpublished to a plain fetch, so api_gate stays unknown.

**Provenance**

- **Entry id**: 07-klavis-ai

- **Source file**: 07-mcp-infrastructure.md

- **Source line**: 225

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-02

- **Data baked**: 2026-09-12

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
