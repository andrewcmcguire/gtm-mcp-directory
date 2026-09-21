# BigDataCorp MCP: MCP server status, API access gate and what it does

> Open-source MCP servers for Latin American commerce - Pix, NF-e, banking, fiscal, logistics, and messaging... Community MCP, Gate unknown. Checked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Data & Enrichment](../categories/data-enrichment.md) /
BigDataCorp MCP

# BigDataCorp MCP

[Community MCP](../mcp/community.md)
[Gate unknown](../gates/unknown.md)
[Data & Enrichment](../categories/data-enrichment.md)
RESEARCHED
Checked 2026-09-12

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [https://github.com/codespar/mcp-dev-latam](https://github.com/codespar/mcp-dev-latam) · entry id 01-bigdatacorp-mcp · source 01-data-enrichment.md line 4438

**What it does**
Open-source MCP servers for Latin American commerce - Pix, NF-e, banking, fiscal, logistics, and messaging across Brazil, Mexico, Argentina, Colombia, Chile, and Peru. MIT, on npm. - codespar/mcp-dev-latam

**AI features, separated from automation with an AI label on it**
Homepage copy mentions AI/ML-related terms; specific AI feature list not independently verified beyond that mention this pass. See sources.

**RevOps role**
Upstream contact/company data or enrichment utility feeding CRM and outbound tooling

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: not recorded

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: not probed yet

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established on 2026-09-12 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://github.com/codespar/mcp-dev-latam

- [https://github.com/codespar/mcp-dev-latam](https://github.com/codespar/mcp-dev-latam)

**What this server exposes**

- **Tools named**: 223
- **Strongest evidence**: in the server source
- **Harvested**: 2026-09-18
- **Repo read**: codespar/mcp-dev-latam
- **Whose repo**: third-party
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

This list came from a repo the vendor does not own. Those are that author's tools for the vendor's API, not the vendor's own published surface, and the two must not be read as the same thing.

- **add_opt_out** Add a phone number to the opt-out list (suppresses future messages) evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **address_validation** Address normalization + validation against CORREIOS + IBGE - canonical address, CEP, neighborhood, city, state, geocode. POST /v1/datasets/addresses. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **antifraud_score** Compute Certta evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **authorize_transaction** Authorize a purchase (POST /api.authorization/v3/authorization/ecommerce/{merchantId}). Pass the transactionToken the Niubiz checkout form returned after the customer entered the card, plus your purchaseNumber and the amount. evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **biometrics_face_match** Compare a selfie against a document photo (RG / CNH front). Returns match_score (0..1) and liveness verdict. POST /v1/biometrics/face-match. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **biometrics_liveness** Passive liveness check on a selfie (no document). Returns liveness_score (0..1) + spoofing_indicators. POST /v1/biometrics/liveness. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **calculate_freight** Calculate shipping rates across multiple carriers (PAC, SEDEX, JadLog, Loggi, Mini Envios). Returns pricing, delivery time, and carrier details for each available service. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **cancel_all_orders** Cancel all open orders for a symbol evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **cancel_freight** Cancel a freight order. Provide the order ID and a reason for cancellation. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **cancel_order** Cancel an open order evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **cancel_payment** Attempt to cancel a payment that has not yet settled. Iniciador endpoint: POST /payments/{id}/cancel. evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **cancel_subscription** Cancel a subscription (DELETE /card/v1/subscriptions/{subscriptionId}, private merchant id). Stops all future charges. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **cancel_transaction** Cancel a transaction. Only valid while status is evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **capture_preauthorization** Two-step charge, step 2: capture a previous preauthorization (POST /card/v1/capture, private merchant id). Amount may be lower than the preauth (partial capture). evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **charge_card** Charge a tokenized card (POST /payment/v1/charge/create). Amounts in COP unless currency says otherwise. Test mode is controlled by EPAYCO_TEST. evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **checkout_freight** Purchase/checkout freight orders. Pays for the orders and generates shipping labels. Returns tracking numbers and label print URLs. evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **companies_lookup** CNPJ lookup - razão social, fantasia, founding date, paid-in capital, partners, address, CNAE. POST /v1/datasets/companies. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **company_check** KYB - validate a CNPJ, return corporate profile, QSA, regularity, sanctions. POST /v1/checks/company. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **confirm_payment** Confirm (capture) a previously authorized payment in the two-step auth + capture flow (PUT /payments/{id}). Uses the PRIVATE apikey. evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_account** Create an account in a ledger (POST /v1/organizations/{org}/ledgers/{ledger}/accounts). Accounts hold balances per asset code (e.g. BRL, USD, USDC). evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_card** Issue a card for a user (POST /cards/v1). card_type VIRTUAL is usable immediately; PHYSICAL enters embossing/shipping and must be activated on receipt. affinity_group_id selects the card program (BIN, art, limits) configured with Pomelo. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_card_payment_link** Convenience wrapper: create a Bold payment link restricted to cards (payment_methods=[\ evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_cash_charge** Cash payment reference (POST /cash/v1/charges, private merchant id). Generates a voucher/reference the customer pays at a cash network (OXXO-style). Returns reference + expiry. evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_cash_payment** Create a cash payment voucher on a Colombian cash network (POST /restpagos/v2/efectivo/{network} on secure.payco.co). The payer takes the voucher code to a physical point to pay. evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_charge** One-step card charge (POST /card/v1/charges, private merchant id). Pass the token from tokenize_card plus the amount object. Supports metadata, months (MX installments) and deferred (installment plans). evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_connect_token** Mint a connect token for embedding the Pluggy Connect widget on the client. Pluggy endpoint: POST /connect_token. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_consent** Create a payment consent that the payer will authorize at their bank. Iniciador endpoint: POST /consents. evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_contact** Create a contact in the contact base evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_counterparty** Register a counterparty (beneficiary) to pay out to (POST /v1/counterparties). Pass the counterparty object in Cobre evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_customer** Create an individual or business customer (KYC mother). Business customers require date_of_incorporation; both types use 3-letter ISO country codes (BRA/USA/MEX). Returns { id, status: evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_external_account** Register a fiat receiver account (BRL Pix, USD wire, EUR SEPA, MXN SPEI). Skippable for BRL Pix payouts - pass pix_key + document directly on /payout instead. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_freight** Create a freight/label order. Returns the order ID, price, protocol, and tracking code. For commercial shipments, invoice details are required. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_item** Create a new bank connection (item) for a connector. Pluggy endpoint: POST /items. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_money_movement** Create an outbound money movement (POST /v1/money_movements): source account/balance, destination counterparty, amount and currency. Runs over Colombia evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_order** Create an order / request a payment (POST /order/add, form-urlencoded). payment_type selects the method (pix | boleto | creditcard). Returns XML: for Pix it carries pix_code (copy-paste) and pix_image; for boleto, the bar code and PDF URL. evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_payin** Create a fiat → stablecoin pay-in referencing a quote_id. Sandbox min: 150 BRL / payout-side equivalents. Response carries { id, status: evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_payment** Initiate a Pix transfer once a consent has been authorized. Iniciador endpoint: POST /payments. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_payment_by_email** Create a collection order Flow emails to the customer (POST /payment/createEmail). Same shape as create_payment but Flow delivers the payment link by email - no checkout redirect needed. evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_payment_intent** Create a payment intent for Pluggy Payments (PISP). Pluggy endpoint: POST /payments/intents. evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_payment_link** Create a hosted checkout / payment link (POST /v2/checkout). The buyer opens the returned payment_request_url and pays with card, Clip account or other enabled MX methods. Amount is in MXN pesos (decimal, e.g. 150.00). evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_payment_source_using_token** Attach a payment source to a customer using a gateway token (e.g. from Chargebee JS / Stripe.js / Adyen tokenization) evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_payout** Create a stablecoin → fiat payout referencing a quote_id. customer_id is REQUIRED at the top level (404 evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_paywall** Create a x402 paywall configuration for an endpoint. When requests hit this endpoint, they receive HTTP 402 with payment instructions. evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_preauthorization** Two-step charge, step 1: hold funds on the card (POST /card/v1/preAuthorization, private merchant id). Returns a ticketNumber to capture later. evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_pse_payment** Create a PSE bank-debit payment (POST /restpagos/pagos/debitos.json on secure.payco.co). Returns a bank redirect URL the payer must open to authorize the debit. evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_pse_payment_link** Convenience wrapper: create a Bold payment link restricted to PSE bank debit (payment_methods=[\ evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_quote** Lock an FX + fee quote for a 5-minute TTL. Same endpoint for both on_ramp (fiat → stablecoin) and off_ramp (stablecoin → fiat). Pass amount on EITHER sender or receiver, not both. Response carries { id, expires_at, commercial_quotation, fee evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_refund** Create a refund order (POST /refund/create). Refund a received payment fully or partially; Flow notifies urlCallBack when the refund resolves. evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_session_token** Create a checkout session (POST /api.ecommerce/v2/ecommerce/token/session/{merchantId}). Returns the sessionKey the Niubiz checkout form needs. Send the purchase amount and the customer evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_subscription** Create a webhook subscription for message events evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_token** Tokenize sensitive card data (PAN, expiry, CVV, cardholder, document) into a single-use payment token (POST /tokens). Uses the PUBLIC apikey. Returns a token id consumed by create_payment, plus the card bin. evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_transaction** Post a balanced double-entry transaction (POST /v1/organizations/{org}/ledgers/{ledger}/transactions/json). The send block debits source accounts and credits distribute targets; amounts must balance. Accounts are referenced by id or @alias. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_transfer_charge** Bank transfer-in charge with a transfer token (POST /transfer/v1/init, private merchant id). Returns the bank redirect URL the customer authorizes at. evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_transfer_token** Token for a bank-transfer-in (POST /transfer/v1/tokens, public merchant id). PSE in Colombia, SPEI in Mexico, bank transfer in Chile/Peru. Feeds create_transfer_charge. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_user** Create a card-holder identity (POST /users/v1). The user is the person or business the card is issued to. Pass the Pomelo user shape for the target country (name, surname, identification_type/value, birthdate, address, email, phone). evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_wallet** Create a stablecoin wallet under an APPROVED customer. blockchain selects the network (solana → USDC; ethereum/polygon → USDC/USDT; tron → USDT). Customer must be evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **create_webhook** Create a new webhook to receive notifications about order events. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **delete_contact** Delete a contact by ID evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **delete_item** Delete a bank connection (revokes credentials, removes accounts/transactions). Pluggy endpoint: DELETE /items/{id}. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **delete_payment_source** Delete a payment source evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **delete_paywall** Remove a x402 paywall from an endpoint evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **delete_subscription** Delete a webhook subscription by ID evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **delete_webhook** Delete a webhook by ID. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **document_check** Document validation - OCR + authenticity check on RG / CNH / passport / proof of residence. Returns structured fields + authenticity_score. POST /v1/checks/document. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **documents_ocr** OCR a Brazilian ID document (RG / CNH / CRLV / proof of residence / passport). Returns extracted structured fields per document type. POST /v1/documents/ocr. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **employment_data** Employment profile for a CPF - current employer, history, monthly income, professional category. POST /v1/datasets/persons. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **face_authentication** Face authentication against a base image (typically the document photo). Returns match_score + liveness verdict + spoofing indicators. POST /v1/biometrics/face. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **financial_data** Credit + financial profile for a CPF/CNPJ - income, score, declared assets, banking, default history. POST /v1/datasets/persons. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **generate_checkout_signature** Generate the SHA-256 integrity signature Bold evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_account** Get a single account by id. Pluggy endpoint: GET /accounts/{id}. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_authorization_url** Build the URL where the payer authorizes a consent at their bank. This is a helper - it does not call Iniciador. Returns the standard OFB authorization URL using the consent id + redirect URI. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_badlar_rate** Get BADLAR rate (tasa de plazos fijos >1M ARS, bancos privados) - used as benchmark for many financial products evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_balance** Read an account evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_banks** List all Brazilian banks with codes and names evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_candles** Get candlestick/OHLCV data for a trading pair evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_card** Fetch a card by id (GET /cards/v1/{id}). Returns masked PAN, status, type and program data - never full card credentials. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_cep** Look up address by CEP (Brazilian postal code) evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_cep_v1** Look up address by CEP using BrasilAPI v1 (single-provider, often faster than v2) evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_check_result** Retrieve a previously-run check by ID (person, company, or document). Useful for replay + auditing without re-querying datasources. GET /v1/checks/{check_id}. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_cnpj** Look up company information by CNPJ evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_connector** Get a single connector definition by id. Pluggy endpoint: GET /connectors/{id}. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_consent** Fetch a payment consent and its current authorization status. Iniciador endpoint: GET /consents/{id}. evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_corretora** Look up a single CVM-registered brokerage by CNPJ evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_corretoras** List all CVM-registered Brazilian brokerages (corretoras) evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_counterparty** Get one counterparty by id (GET /v1/counterparties/{id}). evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_cptec_airport_weather** Get current airport weather (METAR) by ICAO code from CPTEC/INPE evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_cptec_capitals_weather** Get current weather conditions for all Brazilian state capitals evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_cptec_cities** Search CPTEC/INPE cities by name for weather forecasts evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_cptec_ocean_forecast** Get ocean/wave forecast for a coastal city (CPTEC/INPE) evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_cptec_weather** Get weather forecast for a city (CPTEC/INPE) evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_currency_history** Get historical quotes for a currency over a date range evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_ddd** Get state and cities for a DDD (area code) evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_domain_info** Look up .br domain registration info evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_exchange_rates** Get official exchange rates snapshot for a date (USD, EUR, BRL, etc.) evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_fees** Query trading fees (maker/taker) for a symbol evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_fipe_brands** List vehicle brands by type from FIPE table evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_fipe_price** Get vehicle price from FIPE table by code evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_fipe_tables** List FIPE reference tables (months/years available for FIPE queries) evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_fipe_vehicles** List vehicle models for a given FIPE brand code and vehicle type evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_freight** Get detailed information about a freight order including status, tracking, addresses, pricing, and label print URL. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_holidays** List national holidays for a given year evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_ibge_municipalities** List all municipalities for a Brazilian state (IBGE data) evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_ibge_states** List all Brazilian states/UFs with IBGE codes and metadata evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_inflation** Get inflation data (IPC nivel general - variación mensual) evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_interest_rates** Get reference interest rates (tasas de interés de referencia) evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_isbn** Look up book information by ISBN evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_item** Fetch a single bank connection by id. Pluggy endpoint: GET /items/{id}. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_leliq_rate** Get monetary policy rate (ex-LELIQ / tasa de política monetaria) evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_message_status** Get message delivery status by ID evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_monetary_base** Get monetary base data (base monetaria) evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_money_movement** Get a money movement and its status by id (GET /v1/money_movements/{id}). evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_ncm** Look up NCM tax classification code evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_official_rate** Get the official BCRA quote for a single currency on a specific date evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_order** Request information about an order (POST /order/get). Returns the same XML order shape as create_order, including current payment status - poll this to detect Pix/boleto settlement. evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_payment** Fetch a payment by id (status, E2E id, error reason if rejected). Iniciador endpoint: GET /payments/{id}. evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_payment_intent** Fetch the current status of a payment intent. Pluggy endpoint: GET /payments/intents/{id}. evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_payment_link** Fetch a checkout / payment link by id (GET /v2/checkout/{id}) - status, amount, payment outcome. evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_payment_status** Get a payment order evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_payment_status_by_commerce_id** Get a payment order evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_payment_status_by_flow_order** Get a payment order evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_paywall** Get paywall configuration for a specific URL evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_pix_participants** List Pix participant institutions (PSPs/banks enrolled in Pix) evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_pse_transaction** Get a PSE transaction evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_refund_status** Get a refund order evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_report_entries** Get message report entries within a date range evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_reserves** Get international reserves data (reservas internacionales) evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_security_token** Fetch the Niubiz API bearer token (POST /api.security/v1/security, Basic auth). Other tools fetch and cache this automatically - call it explicitly only to verify credentials or force a refresh. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_services** Get available shipping services with detailed restrictions (min/max weight, dimensions) and carrier information. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_supported_networks** List supported blockchain networks, tokens, and facilitators for x402 payments evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_tax_rates** Get current Brazilian tax/economic rates (Selic, CDI, IPCA) evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_ticker** Get ticker data for a trading pair (price, volume, etc.) evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_tm20_rate** Get TM20 rate (tasa de plazos fijos >20M ARS, bancos privados) evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_transaction** Fetch a transaction with its operations (GET /v1/organizations/{org}/ledgers/{ledger}/transactions/{id}). evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_user** Fetch a user by id (GET /users/v1/{id}). evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_user_addresses** List all saved addresses for the authenticated user. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_user_info** Get authenticated user information including name, email, document (CPF/CNPJ), account balance, and shipment limits. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_uva_value** Get UVA (Unidad de Valor Adquisitivo) - used for inflation-adjusted mortgage calculations evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_variable_history** Get the historical series for any monetary variable by id, with optional date range. Use list_variables to discover ids. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_verification_details** Poll the KYC verification state for a customer. Returns { customer_status: evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **get_withdrawal** Get withdrawal details by ID evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **kyb_lookup_cnpj** Validate a CNPJ and return company profile - corporate name, fantasia, address, partners (QSA), CNAE, share capital, regularity status. POST /v1/kyb/cnpj. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **kyc_lookup_cpf** Validate a CPF against Receita Federal + SPC / Serasa. Returns name, DOB, regularity status, restrictions, risk score. POST /v1/kyc/cpf. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_account_trades** List authenticated account fills/trades for a symbol evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_accounts** List a ledger evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_assets** List supported assets/coins on the exchange evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_balances** List the balances of every account visible to this credential (GET /v1/balances). evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_cards** List cards (GET /cards/v1), filterable by user and status. Paginated. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_categories** List Pluggy evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_channels** List available messaging channels evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_cheque_entities** List the catalog of financial entities with their cheque codes - use the código to validate cheques evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_connectors** Lists supported Brazilian banks (connectors). Pluggy endpoint: GET /connectors. Optional filters: name, types (e.g. PERSONAL_BANK, BUSINESS_BANK), countries (BR), sandbox. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_contacts** List contacts from the contact base evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_counterparties** List registered counterparties (GET /v1/counterparties). evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_currencies** List the master catalog of currencies (divisas) tracked by BCRA evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_customers** List customers under the operator evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_datasources** List the datasources available to your Caf account (varies per subscription tier). GET /v1/datasources. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_deposits** List deposits (crypto + fiat) for the authenticated account evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_events** List webhook events. Useful for auditing or backfilling missed webhooks. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_external_accounts** List external accounts under the operator evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_identities** Fetch identity data (legal name, document, address) for an item. Pluggy endpoint: GET /identity?itemId=... evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_institutions** List Brazilian banks supported for Pix payment initiation. Iniciador endpoint: GET /institutions. evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_invoices** List invoices with optional filters evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_items** List bank connections (items) owned by the application. Pluggy endpoint: GET /items. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_money_movements** List money movements (GET /v1/money_movements). evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_networks** List supported blockchain networks for a given asset evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_orderbook** Get order book (bids and asks) for a trading pair evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_orders** List orders with optional filters evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_payment_methods** List the payment methods enabled for this merchant (GET /online/link/v1/payment_methods). evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_payments** List payments in a date range with optional filters. Iniciador endpoint: GET /payments. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_paywalls** List all configured x402 paywalls evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_positions** List open margin/futures positions (if applicable to the account) evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_pse_banks** List PSE banks available for bank debit (GET /restpagos/pse/bancos.json on secure.payco.co). evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_subscriptions** List all webhook subscriptions evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_symbols** List available trading symbols (pairs) on the exchange evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_templates** List approved message templates (WhatsApp/SMS/RCS) evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_trades** List executed trades for a trading pair evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_transactions** List transactions for an account in a date range. Pluggy endpoint: GET /transactions?accountId=&from=&to=. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_variables** List the catalog of monetary variables (id, descripción, categoría) - use this to discover variable ids for get_variable_history evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_wallets** List wallets under the operator evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_webhooks** List all configured webhooks for the account. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **list_withdrawals** List withdrawals (crypto + fiat) for the authenticated account evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **liveness_check** Passive liveness on a selfie (no comparison image). Returns liveness_score + spoofing signals. POST /v1/biometrics/liveness. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **onboarding_process_create** Kick off an orchestrated onboarding pipeline that chains KYC + biometrics + signature in one call. Returns process_id; track via onboarding_process_get. POST /v1/onboarding/processes. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **onboarding_process_get** Get status + results of an onboarding process. Each step (KYC, biometrics, signature) reports its own verdict. GET /v1/onboarding/processes/{process_id}. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **pay_request** Pay for a 402-protected resource. Sends USDC payment via x402 protocol and returns the resource content. The agent automatically handles the 402 handshake. evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **person_check** KYC - validate a CPF, return name + DOB + restrictions + risk indicators. POST /v1/checks/person. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **persons_lookup** CPF lookup - name, DOB, mother evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **properties_lookup** Real-estate lookup by address or registration - property type, area, owner history, market value estimate. POST /v1/datasets/properties. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **reactivate_subscription** Reactivate a cancelled or paused subscription evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **refund_order** Request a refund for a settled order (POST /order/refund). Pass amount_brl for a partial refund; omit for a full refund. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **refund_payment** Refund a payment (POST /payments/{id}/refund). Omit amount for a full refund; pass it for a partial refund in MXN. evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **retrieve_customer** Retrieve a customer by ID evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **retrieve_invoice** Retrieve an invoice by ID evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **retrieve_subscription** Retrieve a subscription by ID evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **reverse_transaction** Reverse (void) an authorization (POST /api.authorization/v3/reverse/ecommerce/{merchantId}). Same-day undo of an authorized transaction by transactionId or purchaseNumber. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **revoke_consent** Revoke a payment consent before it is exercised. Iniciador endpoint: DELETE /consents/{id}. evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **sanctions_check** Sanctions + PEP screening (OFAC / UN / EU / BR PEP / CNJ / INSS / IBAMA) for a CPF or CNPJ. POST /v1/datasets/persons. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **send_email** Send a transactional email evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **send_facebook_message** Send a Facebook Messenger message evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **send_rcs** Send an RCS (Rich Communication Services) message evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **send_sms** Send an SMS message evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **send_template** Send a WhatsApp template message (pre-approved) evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **send_voice** Send a voice message via TTS or pre-recorded audio URL evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **send_whatsapp** Send a WhatsApp message evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **signature_electronic_create** Create a GoCertta electronic signature envelope (e-signature without ICP-Brasil cert - lower legal weight, faster UX). POST /v1/signature/electronic/envelopes. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **signature_get_envelope** Get status + signer responses for a signature envelope. GET /v1/signature/envelopes/{envelope_id}. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **signature_icp_create** Create an ICP-Brasil digital signature envelope for one or more documents. Returns envelope_id + signers evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **social_signals** Social-presence enrichment for a CPF (Instagram / LinkedIn / Twitter / Facebook handles + follower counts). POST /v1/datasets/persons. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **tokenize_card** Exchange raw card data for a single-use token (POST /card/v1/tokens, public merchant id). The token feeds create_charge / create_preauthorization / create_subscription. Card data never touches your backend. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **trust_platform_get** Get the status + step-by-step verdicts of a Trust Platform flow. GET /v1/trust/flows/{flow_id}. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **trust_platform_start** Start a Trust Platform onboarding flow - orchestrated pipeline chaining person/company checks + biometrics + document validation per a dashboard template. Returns flow_id + hosted onboarding URL. POST /v1/trust/flows. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **update_card_status** Change a card evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **update_customer** Update a customer. Accepts any customer fields. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **update_item** Refresh / update credentials for an existing bank connection. Pluggy endpoint: PATCH /items/{id}. evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **update_subscription** Update a subscription. Accepts any Chargebee subscription fields (plan_id, plan_quantity, coupon_ids, addons, billing_cycles, etc.) evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

- **update_user** Patch a user (PATCH /users/v1/{id}). Pass only the fields to change (e.g. status ACTIVE | BLOCKED, email, phone, address). evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **validate_cheque** Check whether a cheque has been reported as stolen/lost (denunciado) by entity code and cheque number evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **validate_webhook_signature** Verify the HMAC-SHA256 signature of a Bold webhook notification against BOLD_SECRET_KEY. Pass the raw request body string and the signature header value. Accepts hex or base64 encodings. Runs locally. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **vehicles_lookup** Vehicle lookup by plate / chassis / RENAVAM - make, model, year, color, fuel, FIPE price, ownership history, restrictions. POST /v1/datasets/vehicles. evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **verify_customer** Trigger the KYC verification check for a customer. Sandbox auto-progresses business customers through the hosted KYC flow once documents are uploaded. Idempotent - returns 422 evidence: in the server source · calling it reads · from a third party repo, so these are that author's tools, not the vendor's published surface

- **verify_payment** Verify if a x402 payment was received and settled on-chain evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **void_charge** Void / refund a card charge (DELETE /card/v1/charges/{ticketNumber}, private merchant id). Same-day = void; settled = refund. Optional partial amount where the acquirer supports it. evidence: in the server source · calling it spends money · from a third party repo, so these are that author's tools, not the vendor's published surface

- **withdraw** Create a withdrawal request evidence: in the server source · calling it writes · from a third party repo, so these are that author's tools, not the vendor's published surface

140 of the 741 entries that record an official or community MCP server carry a harvested tool list. The other 601 are unmeasured, which is not the same as empty. Harvest last run 2026-09-18. Every name across every server is on the [tools index](../tools-index.md).

**Command line**

No CLI found by the 2026-09-18 harvest across vendor docs, npm, PyPI, Homebrew and GitHub. That is a probe result, not proof of absence.

**Access gate**

- **Gate bucket**: Gate unknown

- **Can a solo operator reach it**: Not established

api_gate, verbatim from the file:

unknown

949 of 1252 entries carry an unknown gate. Unknown is a legal answer and it ships as unknown rather than as a guess.

**API documentation**

[https://github.com/docs](https://github.com/docs)

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

A github.com URL already appears somewhere in this entry, which is a seed for that rail and not a measurement of repo health:

- [https://github.com/codespar/mcp-dev-latam](https://github.com/codespar/mcp-dev-latam)
- [https://github.com/developers](https://github.com/developers)
- [https://github.com/docs](https://github.com/docs)

**On GitHub**

No GitHub organisation could be tied to github.com with evidence on 2026-09-15.

Recorded by the harvest: not checked: gh CLI missing or not logged in.

**Jobs it can do**

No job tag on this entry.

981 of 1,252 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://github.com/codespar/mcp-dev-latam](https://github.com/codespar/mcp-dev-latam)
- [https://github.com/docs](https://github.com/docs)
- [https://github.com/developers](https://github.com/developers)

3 source URLs. Raw sources field, verbatim:

https://github.com/codespar/mcp-dev-latam, https://github.com/docs, https://github.com/developers

**Notes, verbatim from the file**
mcp_status=community from official-mcp-registry listing; not an invented official vendor MCP. mcp_url is the registry/listing or product MCP URL from staging. api_gate unknown with dated probe 2026-09-12; free/paid not inferred from HTTP status alone. Promote wave R 2026-09-12: canonical name BigDataCorp MCP (draft listed as io.github.codespar/mcp-bigdatacorp).

**Provenance**

- **Entry id**: 01-bigdatacorp-mcp

- **Source file**: 01-data-enrichment.md

- **Source line**: 4438

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-12

- **Data baked**: 2026-09-20

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
