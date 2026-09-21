# Coordinalo: MCP server status, API access gate and what it does

> Scheduling, availability, clients, billing and CRM for appointment-based services. Community MCP, Gate unknown. Checked 2026-09-12.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Scheduling & Routing](../categories/scheduling-routing.md) /
Coordinalo

# Coordinalo

[Community MCP](../mcp/community.md)
[Gate unknown](../gates/unknown.md)
[Scheduling & Routing](../categories/scheduling-routing.md)
RESEARCHED
Checked 2026-09-12

> **RESEARCHED** Facts from public sources with URLs. No usage claims. Nobody has run this tool. The other tier is BENCH-TESTED, which means Andrew personally ran the tool on a stated date and cannot be bought at any price. Across the whole directory that count is 1.

Vendor: [https://coordinalo.com/api/mcp](https://coordinalo.com/api/mcp) · entry id 10-coordinalo · source 10-scheduling-routing.md line 451

**What it does**
Scheduling, availability, clients, billing and CRM for appointment-based services.

**AI features, separated from automation with an AI label on it**
Not evidenced from fetched pages this pass; no AI feature claims recorded without a source URL.

**RevOps role**
MCP server/client or agent-tooling infrastructure

**MCP server**

- **Status bucket**: Community MCP

- **Auth**: not recorded

- **Parsed URLs**: 1 found in the mcp_url field

- **Endpoint probe**: not probed yet

A working server exists but somebody other than the vendor built it. It can be abandoned without the vendor noticing. The status was established on 2026-09-12 and the MCP URL has not been probed live yet.

mcp_status, verbatim from the file:

community

mcp_url, verbatim from the file:

https://coordinalo.com/api/mcp

- [https://coordinalo.com/api/mcp](https://coordinalo.com/api/mcp)

**What this server exposes**

- **Tools named**: 112
- **Strongest evidence**: answered tools/list
- **Harvested**: 2026-09-18
- **Catalogue shape**: a fixed catalogue the vendor publishes

A tool below is one the server NAMES. Nobody has called it. That is the same two tier honesty rule the rest of the directory runs on: a named tool is research, and BENCH-TESTED stays the only claim that anybody ran anything.

- **admin_create_service** Add a bookable service to an organization. Use after admin_create_organization. Auto-discoverable by default. If the org has exactly one active provider, the service is auto-assigned to them. With multiple providers, use service_assign_prov evidence: answered tools/list · calling it writes · required: orgSlug, name, duration_minutes, price

- **admin_list_providers** List active providers (professionals) for an organization. Use this to get providerId before calling admin_set_availability. The org owner is auto-provisioned as a provider. Requires X-Org-Api-Key header. evidence: answered tools/list · calling it reads · required: orgSlug

- **admin_set_availability** Replace the weekly availability schedule for a provider (not additive - overwrites all existing blocks). Get providerId from admin_list_providers first. Schedule uses day names and HH:MM times. Requires X-Org-Api-Key header. evidence: answered tools/list · calling it writes · required: orgSlug, providerId, schedule

- **admin_toggle_discoverable** Toggle the LIFECYCLE flags isPublic and servicialoPublished. ⚠️ This tool does NOT grant public discovery consent - discovery in the Servicialo registry requires Organization.discoveryConsent=true, which can ONLY be set by the human owner... evidence: answered tools/list · calling it reads · required: orgSlug, discoverable

- **agendas_create** Create a public agenda - a shareable booking page where external clients can self-book appointments. Links to a specific provider and/or service. The agenda gets a public URL at /{orgSlug}/agenda/{slug}. Create this after services and... evidence: answered tools/list · calling it writes · required: orgSlug, slug

- **agendas_delete** Delete a public agenda permanently. Cascades to related sessions booked through this agenda, comments, and service configs. Requires confirm: true. Cannot be undone. evidence: answered tools/list · calling it writes · required: orgSlug, agendaId, confirm

- **agendas_get** Get complete details of a public agenda by ID. Returns all configuration including booking flow (service_first, provider_first, auto), selection modes, assignment strategy, privacy settings, linked provider/service, and session count. Use b evidence: answered tools/list · calling it reads · required: orgSlug, agendaId

- **agendas_list** List public agendas for an organization. Returns agendas with their provider, service, and session counts. evidence: answered tools/list · calling it reads · required: orgSlug

- **agendas_update** Update a public agenda’s configuration. Partial update - only provided fields are changed. Supports modifying: title, description, visibility (isPublic/isActive), booking flow order (service_first/provider_first/auto), selection modes for... evidence: answered tools/list · calling it writes · required: orgSlug, agendaId

- **availability_get_provider_schedule** Get the configured weekly availability schedule for a provider (not free slots, but the base configuration). Use admin_set_availability to modify. evidence: answered tools/list · calling it writes · required: orgSlug, providerId

- **availability_get_slots** Query available time slots within a date range. Agenda-aware: without clientId, filters by the org default public agenda - each org decides which services to expose. With clientId, resolves the client titular provider and returns their... evidence: answered tools/list · calling it reads · required: orgSlug

- **booking_cancel** Cancel an existing session. By default applies the org cancellation policy: the charge is computed from the no-charge/partial/full windows and, if the policy has autoApply, registered as a penalty transaction (money-write). Set applyCancell evidence: answered tools/list · calling it spends money · required: orgSlug, sessionId, reason, confirm

- **booking_create** Create a new session/appointment for a client. providerId is optional - if omitted, the system auto-assigns a provider using the agenda assignment strategy (round_robin, least_booked, etc.). When a client has a titular provider, that... evidence: answered tools/list · calling it spends money · required: orgSlug, clientId, serviceId, scheduledAt

- **booking_create_recurring** Create recurring sessions (e.g. weekly therapy). Generates multiple individual sessions linked by a recurrence series ID. Max 52 occurrences. evidence: answered tools/list · calling it writes · required: orgSlug, clientId, providerId, recurrence, timezone, confirm

- **booking_get** Get complete details of a session/appointment by its ID, including client, provider, service, financial, and delivery proof information. evidence: answered tools/list · calling it reads · required: orgSlug, sessionId

- **booking_list** List sessions for an organization with filters by provider, client, service, status, and date range. Supports cursor-based pagination. evidence: answered tools/list · calling it reads · required: orgSlug

- **booking_list_requests** List the reschedule requests (SessionRequest) of an organization - the org side of the bilateral coordination loop a client opens from the portal. Filter by status (pending|all|resolved, default pending), sessionId or clientId. Returns the evidence: answered tools/list · calling it reads · required: orgSlug

- **booking_reschedule** Reschedule a session to a new time. Cancels the original and creates a new one. Requires confirm: true. evidence: answered tools/list · calling it reads · required: orgSlug, sessionId, newScheduledAt, confirm

- **booking_resolve_request** Approve or reject a pending reschedule request (SessionRequest) that a client proposed from the portal - closes the bilateral coordination loop. outcome: "approved" applies the reschedule atomically (moves the session to the proposed slot... evidence: answered tools/list · calling it reads · required: orgSlug, requestId, outcome

- **booking_update_status** Advance a session through the Servicialo lifecycle: confirm, start, complete, or mark as no-show. NOTE: the "deliver" action is NOT available via MCP (ref PDC-SEC-001) - MCP authentication cannot validate actor-as-Proveedor. Delivery must... evidence: answered tools/list · calling it writes · required: orgSlug, sessionId, action

- **cierre_cerrar_org** Close the organizational period. Requires ALL active clients with historialCompleto=true to be closed first. Freezes the period. Requires confirm: true. evidence: answered tools/list · calling it reads · required: orgSlug, periodo, confirm

- **cierre_crear_cliente** Create a client monthly closing (immutable financial snapshot). Requires historialCompleto=true on the client. One closing per client per period. Requires confirm: true. evidence: answered tools/list · calling it writes · required: orgSlug, clientId, periodo, confirm

- **cierre_distribuir_utilidades** Distribute profits for a closed period. Freezes the current period and all prior open periods. Requires the period to be organizationally closed first. Requires confirm: true. evidence: answered tools/list · calling it reads · required: orgSlug, periodo, montoDistribuido, confirm

- **cierre_eliminar_cliente** Delete (reopen) a client closing. Only allowed if the organizational period is not frozen. Requires confirm: true. evidence: answered tools/list · calling it writes · required: orgSlug, cierreId, confirm

- **cierre_evaluar_org** Evaluate organizational closing readiness for a period. Returns: active clients, closed count, excluded count, pending count, completion percentage, and whether closing is possible. evidence: answered tools/list · calling it reads · required: orgSlug, periodo

- **cierre_listar_clientes** List client closings for an organization. Filter by period and/or client. evidence: answered tools/list · calling it reads · required: orgSlug

- **cierre_listar_utilidades** List retained earnings (utilidades retenidas) for an organization. Returns per-period records with accumulated totals: ingresos, costos, utilidadNeta, distribuido, retenido. evidence: answered tools/list · calling it reads · required: orgSlug

- **cierre_preview_cliente** Preview the financial snapshot for a client in a period WITHOUT creating the closing. Returns totals for ventas, cobros, pagos, sessions. evidence: answered tools/list · calling it reads · required: orgSlug, clientId, periodo

- **client_create** Create a new client in the organization. If a Person with the same email exists, it will be linked (not duplicated). evidence: answered tools/list · calling it writes · required: orgSlug, name, lastName

- **client_get** Get complete details of a client including financial summary and recent sessions. evidence: answered tools/list · calling it reads · required: orgSlug, clientId

- **client_list** List clients of an organization with search and pagination. Can filter by provider or outstanding debt. evidence: answered tools/list · calling it reads · required: orgSlug

- **client_update** Update an existing client's personal data. Email cannot be changed via MCP. evidence: answered tools/list · calling it writes · required: orgSlug, clientId

- **comms_create_campaign** Create a new email campaign with HTML body to send to a segmented audience. Supports variable substitution: {nombre}, {apellido}, {nombre_completo}, {email}, {telefono}, {organizacion}. Use audienceType "predefined" with audienceId "active" evidence: answered tools/list · calling it writes · required: orgSlug, name, emailBody, audienceType, confirm

- **comms_get_campaign** Get details of a specific campaign with optional delivery logs per recipient. evidence: answered tools/list · calling it reads · required: orgSlug, campaignId

- **comms_get_preferences** Get the communication preferences for an organization (WhatsApp, email, confirmation, reminder channels and messages). evidence: answered tools/list · calling it reads · required: orgSlug

- **comms_list_audiences** List the saved audiences/segments used for campaign targeting, each with its filter definition and campaign-usage count. Set includeCount: true to also resolve how many clients currently match each audience, and includePredefined: true to i evidence: answered tools/list · calling it reads · required: orgSlug

- **comms_list_campaigns** List communication campaigns (WhatsApp/email) for the organization. Filter by status. evidence: answered tools/list · calling it reads · required: orgSlug

- **comms_render_message** Render a communication template as a visual image (PNG). Available templates: session-confirmation, session-reminder, payment-reminder. Use action "preview" to get the image URL, "send" to render and send via WhatsApp with the image attache evidence: answered tools/list · calling it spends money · required: orgSlug, template, data

- **comms_send_campaign** Execute a draft or scheduled campaign. Sends messages to all matching recipients asynchronously, skipping recipients with email opt-out or bounced addresses (logged as "skipped"). Campaign must be in draft or scheduled status. Returns immed evidence: answered tools/list · calling it reads · required: orgSlug, campaignId, confirm

- **comms_send_message** Send a single WhatsApp or email message to a specific client. Use templateKey for predefined templates or customMessage for free text. Requires confirm: true. evidence: answered tools/list · calling it writes · required: orgSlug, clientId, channel, confirm

- **comms_update_preferences** Enable or disable communication channels and features for an organization. Partial update - only provided fields are changed. Creates preferences if none exist. evidence: answered tools/list · calling it writes · required: orgSlug

- **delivery_confirmations_list** List the delivery-confirmation ledger for an organization's sessions. Each row reflects the DeliveryProof overlay: whether the provider confirmed delivery, whether the client confirmed, and whether the system auto-confirmed after the verifi evidence: answered tools/list · calling it reads · required: orgSlug

- **disputes_list** List disputes for an organization. Filter by status or type. Returns disputes with client and provider info. evidence: answered tools/list · calling it reads · required: orgSlug

- **dunning_configure** Update dunning (payment recovery) configuration for an organization. All fields except organizationSlug are optional - only provided fields are updated, rest stays unchanged. evidence: answered tools/list · calling it spends money · required: organizationSlug

- **dunning_get_config** Get the current dunning (payment recovery) configuration for an organization. Returns whether dunning is enabled, grace period, step timings, and blocking settings. evidence: answered tools/list · calling it spends money · required: organizationSlug

- **email_domain_delete** Remove the configured email sending domain from the organization. This deletes it from both Resend and the database. The organization will revert to using the default Coordinalo sending address. Requires confirm: true. evidence: answered tools/list · calling it writes · required: orgSlug, confirm

- **email_domain_get** Get the email sending domain configured for an organization and its verification status (PENDING, VERIFIED, FAILED). Returns null if no domain is configured. Use email_domain_register to set one up. evidence: answered tools/list · calling it reads · required: orgSlug

- **email_domain_register** Register a custom email sending domain for an organization via Resend. Returns DNS records that must be configured in the domain provider before verification. Replaces any previously configured domain. After adding DNS records, call email_d evidence: answered tools/list · calling it reads · required: orgSlug, domain

- **email_domain_verify** Trigger DNS verification for the configured email domain and return updated status. Call this after the organization has added the required DNS records. Status will be VERIFIED (ready to send), PENDING (DNS not yet propagated), or FAILED. evidence: answered tools/list · calling it reads · required: orgSlug

- **finance_aging** Get accounts receivable aging report: pending charges grouped by age buckets (0-7, 7-30, 30-90, 90+ days). Use to answer "who owes money" or "old debts" questions. evidence: answered tools/list · calling it reads · required: orgSlug

- **finance_client_balance** Get the complete financial balance for a client: total sales, charges, payments, pending debt, and credits. evidence: answered tools/list · calling it reads · required: orgSlug, clientId

- **finance_create_cobro** Create a manual charge (cobro) for a client. Not linked to a sale/venta. Requires confirm: true. evidence: answered tools/list · calling it spends money · required: orgSlug, clientId, monto, descripcion, confirm

- **finance_create_venta** Create a service sale (venta) for a client. Optionally auto-creates a charge (cobro) depending on org configuration. Requires confirm: true. evidence: answered tools/list · calling it spends money · required: orgSlug, clientId, servicioId, precio, confirm

- **finance_get_cobro** Get details of a specific charge (cobro) including all associated payments. evidence: answered tools/list · calling it spends money · required: orgSlug, cobroId

- **finance_list_cobros** List charges (cobros) for an organization. Filter by client, status, or date range. Includes summary totals. evidence: answered tools/list · calling it reads · required: orgSlug

- **finance_list_confirmations** List pending charge confirmations and their status. Shows cobros in pending_confirmation state that await client verification. Filter by client or confirmation status (pending, confirmed, disputed, auto_confirmed). evidence: answered tools/list · calling it spends money · required: orgSlug

- **finance_list_gastos** List operational expenses (gastos operacionales) of an organization with their category, plus totals broken down by category type (FIJO/VARIABLE/COSTO_PRODUCTO/PROVISION). Filter by date range (dateFrom/dateTo), category id, type(s), or rec evidence: answered tools/list · calling it reads · required: orgSlug

- **finance_list_invoices** List invoices (facturas) of an organization with total, balance (saldo), status, SII status, linked-sales count and the amount already applied via payment links (with a derived payment status: pendiente/abonada/pagada). Filter by client or evidence: answered tools/list · calling it spends money · required: orgSlug

- **finance_list_payments** List payments received with filters. Includes summary by payment type. evidence: answered tools/list · calling it spends money · required: orgSlug

- **finance_list_ventas** List sales (ventas) for an organization. Filter by client, service, provider, or status. evidence: answered tools/list · calling it reads · required: orgSlug

- **finance_register_payment** Register a manual payment against an existing charge (cobro). Updates cobro status automatically. Requires confirm: true. evidence: answered tools/list · calling it spends money · required: orgSlug, cobroId, monto, tipo, confirm

- **finance_send_confirmations** Send pending confirmation digest to clients. Groups all pending_confirmation charges by client and sends a single message per client via WhatsApp or email. Creates confirmation tokens and sets a grace period for auto-confirmation. Requires evidence: answered tools/list · calling it writes · required: orgSlug, confirm

- **lifecycle_get_state** Get the current lifecycle state of a session, including available transitions, state history, and SC resolution. Returns current_state, available_transitions, verification_deadline (when state=delivered), timestamps, duration, sc_resolution evidence: answered tools/list · calling it reads · required: orgSlug, session_id

- **lifecycle_history** Get the SCEvent stream for a session - all observed transitions reconstructed from status_history. Returns events[] with discriminated union by event_type (sc.scheduled, sc.confirmed, sc.completed, sc.delivered, sc.verified, sc.cancelled,... evidence: answered tools/list · calling it reads · required: orgSlug, session_id

- **lifecycle_transition** Execute a state transition on a session. Accepts either to_state (target state name per Servicialo spec: confirmed, in_progress, completed, verified, documented, cancelled, no_show) or action (semantic verb: confirm, start, complete, verify evidence: answered tools/list · calling it reads · required: orgSlug, session_id

- **members_invite** Invite a new member to the organization by email. Sends an invitation email. Requires confirm: true. evidence: answered tools/list · calling it reads · required: orgSlug, email, role, confirm

- **members_list** List members of an organization with their roles and status. evidence: answered tools/list · calling it reads · required: orgSlug

- **org_summary** Compact organization overview (~500 tokens). Returns services, providers, schedules, active features, key counts, and an onboarding_status checklist showing what is configured vs missing (services, providers, availability, public agenda). U evidence: answered tools/list · calling it reads · required: orgSlug

- **org_update** Update organization profile fields: name, description, logo URL, or vertical. Only provided fields are updated. evidence: answered tools/list · calling it writes · required: orgSlug

- **payroll_get_summary** Get payroll summary for a period: total per provider, total cost, pending approvals. evidence: answered tools/list · calling it reads · required: orgSlug, periodo

- **payroll_list_records** List payroll records for an organization. Filter by period, provider, or status. evidence: answered tools/list · calling it reads · required: orgSlug

- **portal_cancel_reschedule_request** Cancel a pending reschedule request (SessionRequest) on behalf of the client who proposed it - the client-side withdrawal in the bilateral loop (outcome=cancelled_by_client). Idempotent: a request already cancelled_by_client returns... evidence: answered tools/list · calling it reads · required: orgSlug, requestId

- **portal_confirm_delivery** Confirm, on behalf of the client, that the service was delivered (writes DeliveryProof.clientConfirmed) - the client-side confirmation that closes dual-confirm verification. Allowed once the session is completed/delivered/documented;... evidence: answered tools/list · calling it reads · required: orgSlug, sessionId

- **portal_propose_reschedule** Propose a new time for a session on behalf of the client - opens the bilateral coordination loop by creating a pending SessionRequest (it does NOT move the session; the org resolves it with booking_resolve_request). Provide... evidence: answered tools/list · calling it reads · required: orgSlug, sessionId, requestedScheduledAt

- **portal_report_session** Report, on behalf of the client, that the professional did not show up (reason=provider_no_show) or that the session was cancelled/not delivered (reason=cancelled). Creates a Dispute(OPEN) for the org to review - it does NOT change the... evidence: answered tools/list · calling it reads · required: orgSlug, sessionId, reason

- **portal_session_cancel** Cancel a client's session on behalf of the client (client-initiated cancellation: cancelledBy=client). Allowed from scheduled/pending_confirmation/confirmed; rejects past sessions. Idempotent: a session already cancelled returns alreadyCanc evidence: answered tools/list · calling it reads · required: orgSlug, sessionId

- **portal_session_confirm** Confirm a client's attendance to their session, on behalf of the client (e.g. the client called or messaged the org to confirm). Moves scheduled/pending_confirmation → confirmed and notifies the provider. This is the client-portal confirm f evidence: answered tools/list · calling it reads · required: orgSlug, sessionId

- **provider_create** Create a new provider in the organization. Links or creates a Person record by email. evidence: answered tools/list · calling it writes · required: orgSlug, name, lastName, email

- **provider_get** Get complete details of a provider including services, schedule, and session stats. evidence: answered tools/list · calling it writes · required: orgSlug, providerId

- **provider_get_stats** Get detailed performance metrics for a provider over a date range: sessions, occupancy, no-show rate, revenue. evidence: answered tools/list · calling it reads · required: orgSlug, providerId

- **provider_update** Update provider data: status, commission, coverage areas, permissions. evidence: answered tools/list · calling it writes · required: orgSlug, providerId

- **public_availability_get_slots** Query available time slots for public booking. Does NOT require an API key. Returns slots grouped by service from the organization's public agenda. Provider details are hidden - the system auto-assigns at booking time. Use after... evidence: answered tools/list · calling it reads · required: orgSlug

- **public_booking_cancel** Cancel a public booking using the bookingToken. Only works for bookings in pending_confirmation, scheduled, or confirmed status. Optionally include a reason. Does NOT require an API key. The booking token scopes access to a single booking. evidence: answered tools/list · calling it reads · required: orgSlug, bookingToken

- **public_booking_confirm** Confirm a pending public booking using the confirmationToken returned by public_booking_create. Advances the booking from pending_confirmation to scheduled. The token expires after 30 minutes. Does NOT require an API key. Rate-limited. evidence: answered tools/list · calling it reads · required: orgSlug, confirmationToken

- **public_booking_create** Create a public booking request. Does NOT require an API key, but DOES require: (1) requester identity - fullName plus at least email or phone, (2) submission context - channel and whether an agent assisted, (3)... evidence: answered tools/list · calling it writes · required: orgSlug, serviceId, startAt, requester, submission, authorization

- **public_booking_get** Get details of a public booking using the bookingToken returned by public_booking_create. Returns status, scheduled time, service, and requester info. Does NOT require an API key - the booking token is the credential. Only returns... evidence: answered tools/list · calling it reads · required: orgSlug, bookingToken

- **public_booking_reschedule** Reschedule a public booking using the bookingToken. Cancels the original and creates a new pending_confirmation booking at the new time. Returns new confirmationToken and bookingToken. Only works for bookings in pending_confirmation, schedu evidence: answered tools/list · calling it reads · required: orgSlug, bookingToken, newStartAt

- **public_service_list** List publicly bookable services for an organization. Does NOT require an API key. Returns only active, discoverable services with assigned providers. Use this as the first step in the public booking flow to show available services to end us evidence: answered tools/list · calling it reads · required: orgSlug

- **reminders_get_config** Get the full reminder/notification configuration for an organization. Returns detailed settings for each reminder type: bookingReminder (post-booking follow-up), sessionReminder24h (24h before), sessionReminder1h (1h before), paymentReminde evidence: answered tools/list · calling it spends money · required: orgSlug

- **reminders_update_config** Update reminder/notification configuration for an organization. Partial update - only provided sections are changed. Sections: bookingReminder {enabled, daysAfter, maxReminders, interval}, sessionReminder24h {enabled, hoursBefore,... evidence: answered tools/list · calling it writes · required: orgSlug

- **report_dashboard** Executive summary of the organization: today's sessions, monthly metrics, revenue, pending charges, and alerts. evidence: answered tools/list · calling it reads · required: orgSlug

- **report_deuda_real** Real-time report of clients with genuine outstanding debt. Excludes temporal payment mismatches (prepaid clients whose global balance is covered). Shows: client name, debt amount, periods with debt, last payment date, and collection status evidence: answered tools/list · calling it spends money · required: orgSlug

- **report_evidence_gates** Adoption and switching evidence for one organization, by month and week: sessions created natively in the app vs imported (count and %), date of the last bulk import, weeks since it, switching level (0 no use / 1 activation / 2 adoption / 3 evidence: answered tools/list · calling it spends money · required: orgSlug

- **report_no_shows** Report no-show statistics for a period. Group by client, provider, service, or day. evidence: answered tools/list · calling it reads · required: orgSlug

- **report_occupancy** Calculate provider occupancy rates for a period. Group by provider, day, or week. evidence: answered tools/list · calling it reads · required: orgSlug

- **report_revenue** Calculate revenue for a period grouped by day, week, month, service, or provider. evidence: answered tools/list · calling it reads · required: orgSlug

- **report_sc_summary** Breakdown of Servicio Coordinado (SC) events by month and resolver path (backfill, cac-native, live, compensalo). Use to validate SC coverage and monitor live SC resolution growth. Key metric: sc_live shows SCs resolved in production (not b evidence: answered tools/list · calling it reads · required: orgSlug

- **resources_list** List the bookable resources of an organization (rooms, boxes, chairs, equipment) with their type, capacity, buffer minutes, location and active state. Filter by type, active state, or a name/description search. Read-only. evidence: answered tools/list · calling it reads · required: orgSlug

- **scheduling_book** Book a session (Servicialo spec). Returns confirmation_credential (opaque token, valid 30 min) and booking_id. Use scheduling_confirm with the credential to finalize. Does NOT require an API key - uses requester identity (fullName + email... evidence: answered tools/list · calling it reads · required: orgSlug, service_id, datetime, requester

- **scheduling_cancel** Cancel a session through the Servicialo protocol lane. Moves the session to cancelled and emits sc_service.cancelled.v1. It REPORTS the cancellation policy tier that applies (policy_applied: none | partial | full, with the percentage) but d evidence: answered tools/list · calling it spends money · required: orgSlug, session_id, confirm

- **scheduling_confirm** Confirm a booking (Servicialo spec). Dual-mode: (1) with credential - uses the confirmation token from scheduling_book, no API key needed; (2) with booking_id - uses API key to confirm an existing session. Returns confirmed status with... evidence: answered tools/list · calling it reads · required: orgSlug

- **scheduling_reschedule** Reschedule a session to a new time (Servicialo spec). Cancels the original session and creates a new one at the specified datetime. Requires confirm: true and X-Org-Api-Key. evidence: answered tools/list · calling it reads · required: orgSlug, session_id, new_datetime, confirm

- **service_assign_provider** Assign or unassign a provider to/from a service. Controls which providers can deliver which services. evidence: answered tools/list · calling it writes · required: orgSlug, serviceId, providerId, action

- **service_create** Create a new bookable service in an existing organization. Use this for day-to-day service management (requires X-Org-Api-Key). For initial org setup, prefer admin_create_service instead. After creating, use service_assign_provider to link evidence: answered tools/list · calling it writes · required: orgSlug, name, price, duration

- **service_list** List services of an organization. Can filter by active status, discoverability, or category. evidence: answered tools/list · calling it reads · required: orgSlug

- **service_update** Update an existing service (price, duration, status, etc.). Creates a price history entry if price changes. Delivery-verification overrides can be changed too: verificationLevel (none / default_confirm / dual_confirm / documented - see... evidence: answered tools/list · calling it writes · required: orgSlug, serviceId

- **session_note_get** Read the clinical note of a session. Non-restricted notes return full content. Notes marked dataSensitivity=restricted return metadata only (type, sensitivity, timestamps, which fields are present) with the clinical text withheld - pass... evidence: answered tools/list · calling it reads · required: orgSlug, sessionId

- **session_note_upsert** Create or update the clinical note (ficha) of a session: evolution, treatmentPerformed, nextSessionPlan, type (evaluacion/tratamiento/derivacion/cierre), progressMetrics, etc. One note per session (upsert). Sensitivity is resolved automatic evidence: answered tools/list · calling it writes · required: orgSlug, sessionId

- **settings_get** Get organization settings. THIS IS THE ENTRY POINT for anything configurable: call it with no filters first to get the full map. Settings are indexed on two axes - `group` (the sections a human sees in the settings screen: profile,... evidence: answered tools/list · calling it reads · required: orgSlug

- **settings_update** Update organization settings. Partial update - only provided keys are changed. Pass a settings object with key-value pairs (e.g. {"policies.noShowMaxStrikes": 3, "finances.clientPaymentTiming": "BEFORE"}). ALL values are validated before... evidence: answered tools/list · calling it spends money · required: orgSlug, settings

- **treatment_plans_get** Get the full detail of a single treatment/care plan by id: diagnosis, objectives, notes, status timeline, expiration, the intake session, and all plan items (service, quantity, frequency, priority, sessions booked/completed). Read-only. evidence: answered tools/list · calling it reads · required: orgSlug, planId

- **treatment_plans_list** List treatment/care plans of an organization with client, provider, status, objectives and their items (services with quantity/frequency/priority). Filter by clientId, status or proveedorId; paginated (page/limit). Read-only - plan... evidence: answered tools/list · calling it reads · required: orgSlug

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

[https://coordinalo.com/docs](https://coordinalo.com/docs)

No documentation text is reproduced anywhere on this site. Read the vendor page for the prose. The structured docs digest specced in SPEC section 3 has not been built or crawled: docs_digest is null on every entry in this build.

**GitHub health**

Not measured. github_url, github_stars, github_last_commit and github_archived are null on every entry in this build.

The refresh rail specced in SPEC section 7.2 has not been run. An unstamped star count is a lie, so nothing is shown rather than something stale.

**On GitHub**

No GitHub organisation could be tied to coordinalo.com with evidence on 2026-09-15.

Recorded by the harvest: not checked: gh CLI missing or not logged in.

**Jobs it can do**

No job tag on this entry.

981 of 1,252 entries are untagged. An empty list here means nobody has tagged this, not that the tool does nothing. The vocabulary is closed, so a tool whose job is genuinely not in it stays blank rather than being forced into the nearest tag.

**Sources**

- [https://coordinalo.com/api/mcp](https://coordinalo.com/api/mcp)
- [https://coordinalo.com/docs](https://coordinalo.com/docs)
- [https://coordinalo.com/developers](https://coordinalo.com/developers)

3 source URLs. Raw sources field, verbatim:

https://coordinalo.com/api/mcp, https://coordinalo.com/docs, https://coordinalo.com/developers

**Notes, verbatim from the file**
what_it_does used staging desc because homepage meta description was empty. API mentioned on https://coordinalo.com/developers; pricing/gate not inferred from presence alone. mcp_status=community from official-mcp-registry listing; not an invented official vendor MCP. mcp_url is the registry/listing or product MCP URL from staging. api_gate unknown with dated probe 2026-09-12; free/paid not inferred from HTTP status alone. Promote wave P 2026-09-12: canonical name Coordinalo (draft listed as Coordinalo - Service Business Operations).

**Provenance**

- **Entry id**: 10-coordinalo

- **Source file**: 10-scheduling-routing.md

- **Source line**: 451

- **Tier**: RESEARCHED

- **last_checked**: 2026-09-12

- **Data baked**: 2026-09-20

Every field above is rendered from directory.json exactly as the build produced it. Nothing is summarised and nothing is dropped. The one change made at render time is typographic and it is disclosed on the [methodology page](../methodology.md).
