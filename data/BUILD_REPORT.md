# The GTM MCP Directory - phase 1+2 build report

Generated 2026-09-03 by `build_directory.py`. Zero network calls.

## Reconciliation against tools_recount.py

**PASS**

| File | Build | tools_recount | |
|---|---|---|---|
| 01-data-enrichment.md | 38 | 38 | OK |
| 02-engagement-outbound.md | 27 | 27 | OK |
| 03-conversation-intel.md | 24 | 24 | OK |
| 04-ai-sdr-agents.md | 23 | 23 | OK |
| 05-signals-intent-abm.md | 28 | 28 | OK |
| 06-revops-infra.md | 23 | 23 | OK |
| 07-mcp-infrastructure.md | 13 | 13 | OK |
| 08-video-prospecting.md | 14 | 14 | OK |
| 09-email-deliverability.md | 13 | 13 | OK |
| 10-scheduling-routing.md | 14 | 14 | OK |
| 11-enablement-coaching.md | 14 | 14 | OK |
| 12-forecasting-revenue.md | 17 | 17 | OK |
| 13-proposals-deals.md | 14 | 14 | OK |
| 14-inbound-plg-chat.md | 15 | 15 | OK |
| 15-community-dark-social.md | 16 | 16 | OK |
| **Total** | **293** | **293** | **OK** |

mcp_status, build: `{"community": 26, "n-a": 9, "none-found": 87, "official": 156, "unknown": 15}`
mcp_status, recount: `{"community": 26, "n-a": 9, "none-found": 87, "official": 156, "unknown": 15}`

api_gate, build: `{"enterprise-leaning": 4, "enterprise-only": 77, "free": 62, "n-a": 6, "paid": 112, "unknown": 32}`
api_gate, recount: `{"enterprise-leaning": 4, "enterprise-only": 77, "free": 62, "n-a": 6, "paid": 112, "unknown": 32}`

## Field coverage, all 293 entries

| Field | Present | Missing |
|---|---|---|
| name | 293 | 0 |
| vendor_url | 293 | 0 |
| category | 293 | 0 |
| what_it_does | 293 | 0 |
| ai_features | 293 | 0 |
| mcp_status | 293 | 0 |
| mcp_url | 276 | 17 |
| mcp_auth | 288 | 5 |
| api_gate | 293 | 0 |
| revops_role | 293 | 0 |
| tier | 293 | 0 |
| last_checked | 293 | 0 |
| sources | 293 | 0 |
| notes | 293 | 0 |
| docs_url | 30 | 263 |

- mcp_url non-empty: **276 of 293** (200 parse to at least one URL, 51 point at github.com)
- mcp_auth non-empty: **288 of 293**
- docs_url present: **30 of 293**
- api_gate `unknown`: **32 of 293**
- entries with at least one github.com URL anywhere (phase 6 seed): **66**
- sources: 1219 URLs total; 279 entries with 2+, 14 with exactly 1, 0 with none
- sources carrying a non-URL annotation (preserved, not dropped): **12**
- solo-reachable (official or community MCP AND gate free or paid): **132**
- BENCH-TESTED: **1**. This stays 0 until Andrew runs something.

mcp_status: `{"community": 26, "n-a": 9, "none-found": 87, "official": 156, "unknown": 15}`
api_gate: `{"enterprise-leaning": 4, "enterprise-only": 77, "free": 62, "n-a": 6, "paid": 112, "unknown": 32}`
tier: `{"BENCH-TESTED": 1, "RESEARCHED": 292}`
last_checked: `{"2026-08-24": 118, "2026-08-25": 23, "2026-09-02": 131, "2026-09-03": 21}`

### Endpoint liveness (measured by mcp_verify.py, read from ../verify_history.jsonl)

- probe run used: `2026-09-03`
- endpoint_status: `{"live": 1, "live-auth-gated": 34, "repo-local": 34, "docs-only": 97, "unreachable": 15, "not-probed": 1, "not-applicable": 111}`
- official entries whose recorded URL answered as an MCP server (live or auth-gated): **35**
- official entries whose recorded URL is a docs page, not an endpoint: **86**
- docs-only is not wrong under SCHEMA law 1; it records where to read, not where to connect. Agents need the second.

### SPEC 2.3 fields present in the shape, unmeasured everywhere

- `github_url`: null or empty on all 293 entries
- `github_stars`: null or empty on all 293 entries
- `github_last_commit`: null or empty on all 293 entries
- `github_archived`: null or empty on all 293 entries
- `github_fetched_on`: null or empty on all 293 entries
- `docs_digest`: null or empty on all 293 entries
- `docs_last_crawled`: null or empty on all 293 entries
- `submission`: null or empty on all 293 entries

## Job tagging (phase 2)

Source files: `data/jobs.yaml` (the closed vocabulary) and `data/tags.yaml` (the tags). `directory.json` is generated output and is never the place a tag lives.

**What a tag means: the vendor says the tool does this.** Tags are derived from each entry's own what_it_does / ai_features / revops_role text, which is RESEARCHED tier. A tag is not a test result and bench_tested is still 1.

- vocabulary: **56 jobs** in **10 families**, status `closed`
- tags.yaml keys (products): **255**, tagged on 2026-08-25 by `machine-pass`
- entries tagged: **271 of 293**; untagged: **22**
- canonical products tagged: **255**; untagged: **22**
- total tag assignments: **849**, mean **3.13** per tagged entry, max **9**
- flagged needs-review in tags.yaml: **49**

Tags per entry: `{"0": 22, "1": 71, "2": 54, "3": 52, "4": 26, "5": 30, "6": 18, "7": 10, "8": 8, "9": 2}`

### Supply per job, as computed

A job with almost no supply is a finding, not a hole. These counts ship exactly as computed.

| Job | Family | Entries | Products | Official MCP | Solo-reachable |
|---|---|---|---|---|---|
| search-people-by-criteria | find-people-and-companies | 24 | 22 | 17 | 17 |
| search-companies-by-firmographics | find-people-and-companies | 15 | 14 | 12 | 13 |
| enrich-person-from-linkedin-url | find-people-and-companies | 12 | 12 | 8 | 8 |
| enrich-company-from-domain | find-people-and-companies | 34 | 31 | 24 | 23 |
| reverse-lookup-person-from-email | find-people-and-companies | 1 | 1 | 0 | 1 |
| build-target-account-list | find-people-and-companies | 7 | 7 | 5 | 4 |
| discover-warm-intro-paths | find-people-and-companies | 4 | 4 | 3 | 2 |
| find-linkedin-url-from-name-and-company | find-people-and-companies | 22 | 21 | 18 | 19 |
| find-work-email | get-contact-data | 29 | 29 | 22 | 22 |
| find-phone-number | get-contact-data | 19 | 19 | 13 | 11 |
| verify-email-deliverable | get-contact-data | 15 | 15 | 12 | 14 |
| identify-anonymous-website-visitor | signals-and-research | 11 | 10 | 8 | 6 |
| fetch-buyer-intent-signals | signals-and-research | 30 | 26 | 20 | 13 |
| track-job-changes | signals-and-research | 10 | 9 | 5 | 5 |
| scrape-job-postings | signals-and-research | 5 | 4 | 5 | 5 |
| detect-technographics | signals-and-research | 14 | 12 | 11 | 11 |
| detect-funding-or-news-event | signals-and-research | 12 | 11 | 10 | 9 |
| scrape-web-page-for-facts | signals-and-research | 6 | 6 | 5 | 5 |
| monitor-social-mentions | signals-and-research | 12 | 11 | 5 | 4 |
| research-account-for-call-prep | signals-and-research | 17 | 16 | 10 | 8 |
| run-email-sequence | outreach-and-engagement | 45 | 38 | 26 | 23 |
| send-linkedin-message | outreach-and-engagement | 22 | 19 | 14 | 13 |
| draft-personalized-outreach | outreach-and-engagement | 51 | 45 | 28 | 25 |
| place-outbound-call | outreach-and-engagement | 22 | 19 | 12 | 8 |
| create-and-send-prospecting-video | outreach-and-engagement | 14 | 13 | 3 | 7 |
| read-outreach-performance | outreach-and-engagement | 14 | 13 | 7 | 6 |
| run-autonomous-sdr-agent | outreach-and-engagement | 16 | 12 | 6 | 4 |
| fetch-call-transcript | conversations-and-meetings | 20 | 20 | 15 | 11 |
| search-call-library | conversations-and-meetings | 5 | 5 | 5 | 3 |
| summarize-meeting | conversations-and-meetings | 22 | 22 | 18 | 14 |
| extract-deal-signals-from-calls | conversations-and-meetings | 21 | 21 | 11 | 4 |
| book-a-meeting | conversations-and-meetings | 26 | 23 | 10 | 10 |
| read-calendar-availability | conversations-and-meetings | 12 | 11 | 6 | 6 |
| answer-inbound-chat | conversations-and-meetings | 21 | 16 | 12 | 11 |
| read-crm-records | systems-of-record | 13 | 10 | 10 | 8 |
| write-crm-records | systems-of-record | 28 | 25 | 18 | 14 |
| query-data-warehouse | systems-of-record | 2 | 2 | 2 | 2 |
| sync-records-between-systems | systems-of-record | 9 | 9 | 8 | 7 |
| run-automation-workflow | systems-of-record | 18 | 15 | 10 | 9 |
| route-inbound-lead | systems-of-record | 9 | 7 | 4 | 3 |
| generate-proposal-or-quote | deals-and-documents | 5 | 5 | 1 | 1 |
| send-document-for-signature | deals-and-documents | 6 | 6 | 3 | 3 |
| read-contract-terms | deals-and-documents | 3 | 3 | 3 | 2 |
| create-digital-sales-room | deals-and-documents | 5 | 4 | 2 | 1 |
| retrieve-sales-content | deals-and-documents | 9 | 9 | 4 | 1 |
| draft-rfp-response | deals-and-documents | 3 | 3 | 2 | 2 |
| read-pipeline-forecast | planning-scoring-coaching | 22 | 19 | 8 | 2 |
| model-revenue-plan | planning-scoring-coaching | 7 | 7 | 3 | 1 |
| score-and-prioritize-leads | planning-scoring-coaching | 24 | 21 | 15 | 9 |
| score-rep-performance | planning-scoring-coaching | 25 | 24 | 7 | 4 |
| run-sales-roleplay-practice | planning-scoring-coaching | 11 | 10 | 2 | 1 |
| warm-up-inbox | sending-infrastructure | 13 | 12 | 9 | 9 |
| provision-sending-infrastructure | sending-infrastructure | 9 | 9 | 6 | 6 |
| check-inbox-placement | sending-infrastructure | 4 | 4 | 1 | 1 |
| discover-mcp-servers | mcp-plumbing | 5 | 5 | 1 | 0 |
| proxy-tool-calls-to-saas | mcp-plumbing | 9 | 9 | 9 | 8 |

- jobs with zero tagged supply: **0**

### Needs review

| Entry | Ids | Tagged | Reason |
|---|---|---|---|
| Bevy | 15-bevy | no | no-job-fits. Community-event infrastructure (chapters, meetups, gamification). Real product, no job in the vocabulary describes running an events programme. Either a new job or an honest permanent blank. |
| Census | 06-census | no | dead. Entry states the standalone product no longer operates and now lives inside Fivetran as Activations. Tags belong on Fivetran, which has sync-records-between-systems. |
| Champion | 15-champion | 1 job(s) | thin. Tagged score-and-prioritize-leads only. Its champion-to-deal-context matching for references and case studies is close to discover-warm-intro-paths but is matching inside existing accounts, not finding a path into a new one. Drew's call. |
| Clockwise | 10-clockwise | no | dead. Entry says THE PRODUCT IS SHUT DOWN. It did book-a-meeting and read-calendar-availability; tagging a dead endpoint as supply is exactly the failure INDEX.md finding 5 warns about. |
| Commsor | 15-commsor | no | dead. Folded into The Swarm's Go-to-Network line. The Swarm carries discover-warm-intro-paths. |
| Continu | 11-continu | no | no-job-fits. Corporate LMS. retrieve-sales-content is about approved sales collateral, not training courses. A learning-content job may be worth adding once file 11 is looked at as a set. |
| Correlated | 14-correlated | no | dead. Entry records the current form as unknown, with no live product surface to evaluate. |
| Drift | 14-drift | no | dead. Folded into Salesloft, and the entry states the conversational-AI engine is now a third party (1mind). Tagging answer-inbound-chat would point an agent at a product that no longer exists standalone. |
| Exploding Topics | 15-exploding-topics | no | no-job-fits. Trend and topic velocity detection. It is not mention monitoring and it is not an account signal, so monitor-social-mentions would be wrong. Candidate new job: detect-emerging-topic. |
| GummySearch | 15-gummysearch | no | dead. Shut down per the entry's notes. |
| Klavis AI | 07-klavis-ai | no | unclear. The entry states the product is agent-training-data infrastructure and explicitly flags the mismatch with Composio/Pipedream. proxy-tool-calls-to-saas is plausible from the "600+ real tools" line and unsupported by everything else on the page. |
| Koala | 05-koala | no | dead. The entry is written in the past tense throughout. It did identify-anonymous-website-visitor and score-and-prioritize-leads. |
| MadKudu | 04-madkudu | 1 job(s) | thin. Tagged score-and-prioritize-leads only. The domain redirects to HG Insights and the entry says the standalone product no longer appears to exist, so the HG Sales Copilot claims (account research, outreach sequences) were not carried over. |
| mcp.so | 07-mcp-so | no | unclear. The entry could not verify current content. discover-mcp-servers is the obvious tag and there is no fetched evidence for it. |
| Model Context Protocol - official servers repo | 07-model-context-protocol-official-servers-repo | no | no-job-fits. The official reference-servers repo. It is the spec's canonical reference, not a registry an agent queries and not a SaaS proxy. |
| Orbit | 15-orbit | no | dead. Community analytics platform, past tense in the entry. |
| Pocus | 14-pocus | no | dead. Absorbed into a competitor; the entry says features could not be meaningfully evaluated post-acquisition. |
| Relevance AI | 04-relevance-ai | no | thin. Tagged nothing. It is a build-your-own-agent platform and the entry says the agentic depth depends entirely on what the operator configures. Its listed specialist agents (prospecting, scheduling, deal review, proposal building) would each be a tag, but tagging a builder with its example templates would inflate the supply count for six jobs at once. |
| SparkToro | 15-sparktoro | no | no-job-fits. Audience attention mapping. Not account research, not mention monitoring. Candidate new job: map-audience-attention. |
| Superblocks | 06-superblocks | no | no-job-fits. Internal-app building and AI-app governance. run-automation-workflow is not what it does and there is no app-builder job. |
| Toplyne | 14-toplyne | no | dead. Entry records the current form as unknown. |
| Trainual | 11-trainual | no | no-job-fits. SOP and process documentation, explicitly described as not sales-specific. |
| Ultimate.ai | 14-ultimate-ai | no | dead. Presumed folded into Zendesk AI Agents; no standalone surface to evaluate. |
| WorkRamp | 11-workramp | no | no-job-fits. Corporate LMS, same call as Continu. |
| Attio | 06-attio | 2 job(s) | thin. Tagged read-crm-records and write-crm-records. The entry mentions automatic data enrichment and meeting-intelligence tooling in the MCP surface but calls the AI surface unconfirmed, so enrich-company-from-domain and summarize-meeting were left off. |
| Syncari | 06-syncari | 1 job(s) | thin. Tagged sync-records-between-systems. Its Master MCP Server exposes governed unified data to agents, which is close to query-data-warehouse, but Syncari is an MDM layer over other systems rather than a warehouse. |
| Versium REACH | 01-versium-reach | 1 job(s) | thin. Tagged verify-email-deliverable only. Identity-graph append on partial contact records is real but the entry does not say what identifiers go in or what comes out, so no enrich or reverse-lookup tag could be justified. |
| Airbyte | 06-airbyte | 1 job(s) | thin. Tagged sync-records-between-systems. The hosted Context Store and the Agents product line let agents query connected data, which reads close to query-data-warehouse, but Airbyte lands data rather than serving analytical queries over it. |
| People Data Labs | 01-people-data-labs | 6 job(s) | close-call, tagged. find-linkedin-url-from-name-and-company was added 2026-09-03 by human-pass on the entry's own what_it_does line, which says it returns profile records (name, job history, education, skills, social handles, contact fields) matched by identifiers like email, name, or LinkedIn URL. A LinkedIn URL is a social handle and name is a stated input; the entry does not say name plus company in so many words. Strike the tag if that reading is too generous. |
| Datagma | 01-datagma | 6 job(s) | close-call, tagged. find-linkedin-url-from-name-and-company was added 2026-09-03 by human-pass on the entry's revops_role, which lists find profile among its Clay waterfall actions (enrich person, enrich company, find email, find mobile, find profile, find employees) in a tool described as pulling prospect data directly from LinkedIn. The entry says profile, not LinkedIn URL; the tag reads that as the LinkedIn profile. Strike it if that reading is too generous. |
| Prospeo | 01-prospeo | 8 job(s) | tagged 2026-09-03 by human-pass on a sourced sentence appended to the entry's notes the same day: the Enrich Person API accepts first name + last name + a company identifier and returns linkedin_url, "The person's public LinkedIn URL" (https://prospeo.io/api-docs/enrich-person). The MCP docs describe enrich_person as returning email and/or mobile, so the MCP surface may not expose the URL. |
| Lusha | 01-lusha | 8 job(s) | tagged 2026-09-03 by human-pass on a sourced sentence appended to the entry's notes the same day: Search Contacts looks up contacts by "firstName + lastName + companyName or companyDomain" and returns a preview that includes linkedinUrl (https://docs.lusha.com/apis/openapi/person-api); MCP tool contacts_search. |
| RocketReach | 01-rocketreach | 4 job(s) | tagged 2026-09-03 by human-pass on a sourced sentence appended to the entry's notes the same day: People Lookup takes name ("Must specify along with current_employer") plus current_employer and returns linkedin_url (https://docs.rocketreach.co/reference/people-lookup-api.md); MCP tool person_lookup. |
| Apollo.io | 01-apollo-io | 9 job(s) | tagged 2026-09-03 by human-pass on a sourced sentence appended to the entry's notes the same day: People Enrichment accepts first_name and last_name with organization_name or domain and returns linkedin_url, "The URL for the person's LinkedIn profile" (https://docs.apollo.io/reference/people-enrichment); MCP tool apollo_people_match. |
| Wiza | 01-wiza | 6 job(s) | close-call, tagged. Tagged 2026-09-03 by human-pass on a sourced sentence appended to the entry's notes the same day: an individual reveal takes "a name, company, and domain" and returns the Profile Details fields, which include Profile URL (https://docs.wiza.co/overview/data-dictionary.md). The vendor field is named Profile URL, not LinkedIn URL; MCP tool enrich_contact says "profile data". Strike the tag if that reading is too generous. |
| FullEnrich | 01-fullenrich | 3 job(s) | tagged 2026-09-03 by human-pass on a sourced sentence appended to the entry's notes the same day: Look Up People takes "full name combined with a company identifier" and returns social_profiles.professional_network.url with a linkedin.com/in/ example (https://docs.fullenrich.com/api/v2/people/lookup/post.md). The vendor says professional network, not LinkedIn, in the field name. |
| Hunter.io | 01-hunter-io | 3 job(s) | tagged 2026-09-03 by human-pass on a sourced sentence appended to the entry's notes the same day: the Email Finder takes a domain name, a first name and a last name and its response includes linkedin_url (https://hunter.io/api-documentation/v2). The LinkedIn URL rides along with an email lookup; it is not a standalone finder. |
| UpLead | 01-uplead | 8 job(s) | tagged 2026-09-03 by human-pass on a sourced sentence appended to the entry's notes the same day: the Person API takes first_name, last_name and domain and returns linkedin_url, one credit per record received (https://docs.uplead.com/). |
| ZoomInfo | 01-zoominfo | 9 job(s) | tagged 2026-09-03 by human-pass on a sourced sentence appended to the entry's notes the same day: MCP tool Enrich Contacts accepts "a name paired with company context" and returns a LinkedIn URL among its fields, one bulk data credit per new contact (https://gtm.ai/content/docs/mcp/tools/enrich-contacts.md). |
| Clay | 01-clay | 7 job(s) | close-call, tagged. Tagged 2026-09-03 by human-pass on a sourced sentence appended to the entry's notes the same day: Clay's catalog action "Find a Person's LinkedIn via Name and Company with SMARTe" is described as "This action enables users to find a person's LinkedIn profile using their name and company" (https://www.clay.com/integrations/action/find-a-persons-linkedin-via-name-and-company-smarte). The data comes from a third-party provider inside Clay, and the Clay MCP names no such tool. Strike the tag if that reading is too generous. |
| Coresignal | 01-coresignal | 5 job(s) | close-call, tagged. Tagged 2026-09-03 by human-pass on a sourced sentence appended to the entry's notes the same day: the Base Employee search filter takes full_name and experience_company_name and its example records carry a professional-network profile url (https://docs.coresignal.com/employee-api/base-employee-api/endpoints/search-filters.md). The vendor never writes LinkedIn; the tag reads professional network as LinkedIn. Strike it if that reading is too generous. |
| Crustdata | 01-crustdata, 05-crustdata | 6 job(s) | tagged 2026-09-03 by human-pass on a sourced sentence appended to the entry's notes the same day: Person Search accepts basic_profile.name and experience.employment_details.company_name filters and returns social_handles.professional_network_identifier.profile_url with a linkedin.com/in/ value, "0.03 credits per result returned" (https://docs.crustdata.com/person-docs/search/introduction). |
| Dropcontact | 01-dropcontact | 5 job(s) | tagged 2026-09-03 by human-pass on a sourced sentence appended to the entry's notes the same day: the enrich endpoint accepts "first_name + last_name + company (or full_name + company)" and its response includes a linkedin field with a linkedin.com/in/ example (https://developer.dropcontact.com/). |
| BetterContact | 01-bettercontact | 3 job(s) | close-call, tagged. Tagged 2026-09-03 by human-pass on a sourced sentence appended to the entry's notes the same day: the enrichment endpoint takes first_name, last_name and company or company_domain and the results carry contact_linkedin_profile_url (https://doc.bettercontact.rocks/api-reference/endpoint/get). The docs do not say the URL is found when it was not supplied; the field is simply in the documented output. Strike the tag if that reading is too generous. |
| PhantomBuster | 02-phantombuster | 5 job(s) | close-call, tagged. Tagged 2026-09-03 by human-pass on a sourced sentence appended to the entry's notes the same day: the vendor catalog page is titled "LinkedIn Profile URL Finder" (https://phantombuster.com/automations/linkedin/4015/linkedin-profile-url-finder). The page body did not render for the fetcher; the input and credit statements come from the search index's rendering of the vendor pages, not a fetched sentence. Strike the tag if that is too thin. |
| lemlist | 02-lemlist | 8 job(s) | tagged 2026-09-03 by human-pass on a sourced sentence appended to the entry's notes the same day: Enrich Data accepts firstName, lastName and companyName or companyDomain with a linkedinEnrichment flag and its sample response returns linkedinUrl (https://developer.lemlist.com/api-reference/endpoints/enrich/enrich-data.md). |
| Surfe | 01-surfe | 8 job(s) | close-call, tagged. Tagged 2026-09-03 by human-pass on a sourced sentence appended to the entry's notes the same day: Enrich People accepts firstName, lastName and companyName or companyDomain and "Set include.linkedInUrl to return additional profile data" (https://developers.surfe.com/public-015-create-people-bulk-enrichment). The docs name an include flag, not a response field. Strike the tag if that reading is too generous. |
| CUFinder | 01-cufinder | 5 job(s) | tagged 2026-09-03 by human-pass on a sourced sentence appended to the entry's notes the same day: Person Enrichment takes full_name and company and returns social.linkedin_url, "Credit usage is 10 credits per request" (https://apidoc.cufinder.io/apis/person-enrichment.md). |
| Explorium | 01-explorium | 6 job(s) | tagged 2026-09-03 by human-pass on a sourced sentence appended to the entry's notes the same day: Match Prospects accepts full_name and company_name and returns prospect_id, and the profile enrichment returns linkedin_url_array, a list of LinkedIn profile URLs (https://developers.explorium.ai/reference/prospects/enrichments/professional_profile_contact_and_workplace.md). Two calls, not one; MCP tools match-prospects and enrich-prospects. |

## Duplicates resolved

16 cross-file duplicate groups, 16 with a canonical home declared in INDEX.md, 0 defaulted by the parser.

| Normalized name | Canonical | Cross-references |
|---|---|---|
| amplemarket | 02-amplemarket | 04-amplemarket |
| chili piper | 10-chili-piper | 14-chili-piper |
| clari | 03-clari | 04-clari |
| common room | 05-common-room | 15-common-room |
| crustdata | 01-crustdata | 05-crustdata |
| default | 06-default | 10-default |
| hubspot | 06-hubspot | 12-hubspot |
| klenty | 02-klenty | 04-klenty |
| pipedrive | 06-pipedrive | 12-pipedrive |
| qualified | 14-qualified | 04-qualified |
| reply io | 02-reply-io | 04-reply-io |
| salesforce agentforce | 06-salesforce-agentforce | 04-salesforce-agentforce |
| salesforge | 02-salesforge | 04-salesforge |
| theirstack | 05-theirstack | 01-theirstack |
| trumpet | 13-trumpet | 08-trumpet |
| warmly | 05-warmly | 01-warmly |

## Data quality findings

Editorial, not build failures. The markdown is the source of truth; the build reports these and ships.

- SCHEMA law 1 risk (official or community with no parseable mcp_url): **1** 13-arphie
- Thin sourcing (fewer than 2 source URLs): **14**
- api_gate unknown: **32**
- docs_url missing: **263**

## Source file fixes made by this build

None. No source category file was edited.

## Parser warnings

None.

## Integrity

- content sha256: `84e4e93b3c09e2f9230d71a6305cb656ef4a30c7ab8a4a306a557f22dcb5541f`
- source sha256: `7cb9ac376dc5b5600f4782dcb145eac0bfac0f8b37e4a1d47772eb1817ed2f7e`
- jobs.yaml sha256: `bb07dcb51e730f83a7e7f2c8a59669b29197c141c7bd3fe497dccd7477615922`
- tags.yaml sha256: `7039a400c1c4664347ef4617fb709a3beeec4d989742af51bd274691ffb3e3da`
- network calls made: 0 (the socket module is disarmed at import)

