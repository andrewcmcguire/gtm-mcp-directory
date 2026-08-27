# How every listing on the job board is verified, and what was removed on 2026-08-27

> The verification method behind The GTM Engineer job board, and the full ledger of the 60 listings the 2026-08-27 pass removed, each with the reason it failed.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[The job board](index.md) / Verification

**The verification pass, 2026-08-27**

## What was removed, and why.

A job board is a claim about the world at a moment, and the moment passes. This page is the receipt. 126 tracked reqs were checked on 2026-08-27. 66 are published. 60 are not, and every one of them is named below with the reason it failed.

### The method

- Every req in jobs.db, plus the hand-verified roles roundups and any post drops, fetched at the exact URL the board publishes.

- GET, real browser user agent, 10s timeout, 2 concurrent, 1 retry.

- Where the employer runs a public Greenhouse, Lever or Ashby board feed, the req id is also checked against that feed. A req the employer's own feed has dropped is dead even if the page still loads.

- Only status=live reaches the board. dead and unverified are published here and nowhere else.

- changed=true is a live req whose title, location, remote flag, salary or posted date moved since it was recorded. The board publishes the new value.

- $0. Free public HTTP only. No paid API, no LinkedIn, no scraping of anything behind a login.

### The three answers, and what each one means

| Answer | What it means | Published? |
|---|---|---|
| live | The apply link answered and the posting was on it. Where the employer runs a public board feed, the req id was still in that feed too. | Yes |
| dead | 404, a closed-posting message, a redirect to a careers index with no trace of the req, an empty ATS shell, or the employer's own feed has dropped it. | No |
| unverified | The check could not settle it. A JavaScript-only page that renders nothing to a plain fetch, or the page and the employer's feed disagreeing with each other. Unverified is not a softer word for live. | No |

### How the filters are derived

| Field | How it is derived |
|---|---|
| days_tracked | Days between the first time this lane saw the req and the verification date. It is not a posted date and it is not claimed to be. |
| region | Substring match over the employer's own location string. A req naming several cities appears under each of them. |
| salary | Printed only where the employer publishes it in the machine readable field of their own board feed. Never estimated, never inferred from a range seen elsewhere. |
| seniority | Ordered substring match over the title only. A title that says nothing about level is filed as not stated rather than guessed. |
| title_family | Ordered substring match over the employer's own job title. First rule that matches wins. It is a filing decision, not a judgement about the work. |

### What is not on this board

Job descriptions. Salary estimates. A count of applicants. A recruiter contact. Anything we would have had to guess. A salary appears only where the employer publishes it in the machine readable field of their own board feed, which is why 54 of 66 rows carry one and the rest are blank rather than estimated.

### The removal ledger, 2026-08-27

60 listings. These URLs are printed as text, not as links, because they no longer work. That is the point of printing them.

- Senior / AI Agent Engineer, Brand Concierge Adobe 200 but the page carries no trace of this req (js-only shell or wrong page) https://adobe.wd5.myworkdayjobs.com/en-US/external_experienced/job/San-Jose/AI-Agent-Engineer_R158282 unverified checked 2026-08-27 HTTP 200
- GTM Engineer Anthropic redirected to https://job-boards.greenhouse.io/anthropic?error=true with no trace of this req https://job-boards.greenhouse.io/anthropic/jobs/5211222008 dead checked 2026-08-27 HTTP 200
- Program Manager, GTM Systems Anthropic redirected to https://job-boards.greenhouse.io/anthropic?error=true with no trace of this req https://job-boards.greenhouse.io/anthropic/jobs/5363352008 dead checked 2026-08-27 HTTP 200
- Account Executive (GTME - High Velocity) Clay req id is gone from the employer board feed https://jobs.ashbyhq.com/claylabs/6a716895-54fb-41f7-9cd5-13ff6a4085a4 dead checked 2026-08-27 HTTP 200
- Account Executive (GTME - New Business) Clay req id is gone from the employer board feed https://jobs.ashbyhq.com/claylabs/84212160-462f-42a1-a9c2-b9b6428e945f dead checked 2026-08-27 HTTP 200
- Account Executive (GTME) - SMB/High Velocity Clay req id is gone from the employer board feed https://jobs.ashbyhq.com/claylabs/7bd35c48-c394-46c8-98a1-f809fed007d8 dead checked 2026-08-27 HTTP 200
- Forward Deployed GTME Clay req id is gone from the employer board feed https://jobs.ashbyhq.com/claylabs/26c9a251-b616-49f7-a489-4d393a02ea5f dead checked 2026-08-27 HTTP 200
- Go-To-Market Engineering (GTME) Ecosystems - Cohorts Clay req id is gone from the employer board feed https://jobs.ashbyhq.com/claylabs/f50ce265-afa3-4da7-9d1b-f0b02256282c dead checked 2026-08-27 HTTP 200
- GTM Enablement Program Manager, EMEA Clay req id is gone from the employer board feed https://jobs.ashbyhq.com/claylabs/454725ed-81e8-4252-992d-e16ee48621b9 dead checked 2026-08-27 HTTP 200
- GTME (Sales) Enablement Clay req id is gone from the employer board feed https://jobs.ashbyhq.com/claylabs/0944c931-d792-45f9-9d5f-eab2dacad4d8 dead checked 2026-08-27 HTTP 200
- GTME Ecosystem - Community Strategy & Ops Clay req id is gone from the employer board feed https://jobs.ashbyhq.com/claylabs/b996c889-9985-4ff1-98c3-ebf6b60b8790 dead checked 2026-08-27 HTTP 200
- GTME Ecosystem - Create Your Own Role Clay req id is gone from the employer board feed https://jobs.ashbyhq.com/claylabs/45fbd224-6a30-4b8e-8938-139ae0a0127f dead checked 2026-08-27 HTTP 200
- GTME Ecosystem - Ecosystem Programs Lead Clay req id is gone from the employer board feed https://jobs.ashbyhq.com/claylabs/05d88dd4-372c-40b5-85c1-8fb8a53fb133 dead checked 2026-08-27 HTTP 200
- GTME Ecosystem - GTME Talent Lead Clay req id is gone from the employer board feed https://jobs.ashbyhq.com/claylabs/9c58e923-3034-4d25-b820-2102769a77e1 dead checked 2026-08-27 HTTP 200
- GTME Ecosystem - GTME University Lead Clay req id is gone from the employer board feed https://jobs.ashbyhq.com/claylabs/0532ee84-60a2-4998-a461-eabc555ee4c8 dead checked 2026-08-27 HTTP 200
- GTME Ecosystem - Startup Programs Lead Clay req id is gone from the employer board feed https://jobs.ashbyhq.com/claylabs/3115a0f7-0978-44ff-9ee7-b9bb82afacc2 dead checked 2026-08-27 HTTP 200
- Product Marketing (GTM) Clay req id is gone from the employer board feed https://jobs.ashbyhq.com/claylabs/6579de6f-b5df-46df-bb73-e8d82955f293 dead checked 2026-08-27 HTTP 200
- Trainer, GTM Enablement Clay req id is gone from the employer board feed https://jobs.ashbyhq.com/claylabs/a4cd530e-a99b-4c24-a2b7-f609ce3f59c1 dead checked 2026-08-27 HTTP 200
- GTM Engineer, Growth Programs Cursor req id is gone from the employer board feed https://jobs.ashbyhq.com/cursor/044a003e-d6cc-43b6-806a-833d9399c3d4 dead checked 2026-08-27 HTTP 200
- Senior Staff GTM Systems Engineer Cursor req id is gone from the employer board feed https://jobs.ashbyhq.com/cursor/47df1e88-54af-42e1-a813-444b523b1a4d dead checked 2026-08-27 HTTP 200
- Global GTM Strategy and Scale Architect Databricks redirected to https://www.databricks.com/company/careers/open-positions with no trace of this req https://databricks.com/company/careers/open-positions/job?gh_jid=8463173002 dead checked 2026-08-27 HTTP 200
- Manager, GTM Commissions Design Databricks redirected to https://www.databricks.com/company/careers/open-positions with no trace of this req https://databricks.com/company/careers/open-positions/job?gh_jid=8461584002 dead checked 2026-08-27 HTTP 200
- Strategy & Execution Manager - GTM Planning Databricks redirected to https://www.databricks.com/company/careers/open-positions with no trace of this req https://databricks.com/company/careers/open-positions/job?gh_jid=8468678002 dead checked 2026-08-27 HTTP 200
- GTM Engineer Fundraise Up redirected to https://fundraiseup.com/careers/ with no trace of this req https://job-boards.greenhouse.io/fundraiseup/jobs/4705061005 dead checked 2026-08-27 HTTP 200
- GTM Enablement Manager, EMEA Harvey req id is gone from the employer board feed https://jobs.ashbyhq.com/harvey/430a45ad-f66d-48cc-aa75-da657aeb827f dead checked 2026-08-27 HTTP 200
- GTM Recruiter Harvey req id is gone from the employer board feed https://jobs.ashbyhq.com/harvey/cda9ac50-83bd-4965-8afa-feeca25bad4f dead checked 2026-08-27 HTTP 200
- GTM Systems Admin (Support) Harvey req id is gone from the employer board feed https://jobs.ashbyhq.com/harvey/22a3e192-e8ab-41f0-bfc3-1586587ab182 dead checked 2026-08-27 HTTP 200
- GTM Systems Admin, Growth Harvey req id is gone from the employer board feed https://jobs.ashbyhq.com/harvey/beaeadde-22b3-4917-ba7c-d9c1a62f2d38 dead checked 2026-08-27 HTTP 200
- Principal Engineer - Go-To-Market Intercom redirected to https://job-boards.greenhouse.io/intercom?error=true with no trace of this req https://job-boards.greenhouse.io/intercom/jobs/7811880 dead checked 2026-08-27 HTTP 200
- Senior GTM Product Enablement Manager Intercom redirected to https://job-boards.greenhouse.io/intercom?error=true with no trace of this req https://job-boards.greenhouse.io/intercom/jobs/7441074 dead checked 2026-08-27 HTTP 200
- GTM Engineer Meesho (AI Services) conflict: the page still renders this req but the employer's own board feed has dropped it https://jobs.lever.co/meesho/c49e13f6-f027-42f3-98b5-745d83997cbf unverified checked 2026-08-27 HTTP 200
- Talent Acquisition (Engineering/Product/GTM/ Science) - EMEA Mistral AI 200 but the page carries no trace of this req (js-only shell or wrong page) https://jobs.ashbyhq.com/mistral/c0968784-8292-425a-b0a6-ac144decdf21 unverified checked 2026-08-27 HTTP 200
- Data Engineer, Go-To-Market Notion req id is gone from the employer board feed https://jobs.ashbyhq.com/notion/655b047b-5e58-4b0c-82f0-8c16b2c03318 dead checked 2026-08-27 HTTP 200
- Enterprise Product Marketing, GTM Notion req id is gone from the employer board feed https://jobs.ashbyhq.com/notion/5f986e92-f668-4c9b-8b13-3de9cfe737e2 dead checked 2026-08-27 HTTP 200
- Forward Deployed Engineer, GTM - Korea Notion req id is gone from the employer board feed https://jobs.ashbyhq.com/notion/1cd3f44f-aa30-44a6-a64b-c7bfc813eeb9 dead checked 2026-08-27 HTTP 200
- Forward Deployed Engineer, GTM, DACH Notion req id is gone from the employer board feed https://jobs.ashbyhq.com/notion/b50c884e-1170-46d2-ae4c-3f559d2c98c4 dead checked 2026-08-27 HTTP 200
- Forward Deployed Engineer, GTM, France Notion req id is gone from the employer board feed https://jobs.ashbyhq.com/notion/2ca618b4-2223-47ca-b1f0-84ac101fcd90 dead checked 2026-08-27 HTTP 200
- GTM AI + Innovation Manager Notion req id is gone from the employer board feed https://jobs.ashbyhq.com/notion/3336e944-0970-48ef-9a97-4ebd6656d0c2 dead checked 2026-08-27 HTTP 200
- GTM Recruiter, Tokyo Notion req id is gone from the employer board feed https://jobs.ashbyhq.com/notion/6b702ebf-0829-4b0a-b103-fe9271708881 dead checked 2026-08-27 HTTP 200
- People Partner, GTM Notion req id is gone from the employer board feed https://jobs.ashbyhq.com/notion/2a1bd4d8-fd02-486e-a1ac-d98c59e57ae5 dead checked 2026-08-27 HTTP 200
- Full Stack Software Engineer, GTM Innovation OpenAI req id is gone from the employer board feed https://jobs.ashbyhq.com/openai/a2c9f105-b41a-41db-afd8-e70a54b3f21c dead checked 2026-08-27 HTTP 200
- GTM Business Operations & Strategy Lead, Codex OpenAI req id is gone from the employer board feed https://jobs.ashbyhq.com/openai/ffbd26ce-25fe-44af-931f-8939cb8a731b dead checked 2026-08-27 HTTP 200
- GTM Business Operations & Strategy Lead, Platform OpenAI req id is gone from the employer board feed https://jobs.ashbyhq.com/openai/76d44b19-7586-446e-a21a-a073af1f0a00 dead checked 2026-08-27 HTTP 200
- GTM Enablement Manager OpenAI req id is gone from the employer board feed https://jobs.ashbyhq.com/openai/f266cb79-dc62-42e9-a2f1-efc083c94457 dead checked 2026-08-27 HTTP 200
- GTM Partnerships Enablement Lead OpenAI req id is gone from the employer board feed https://jobs.ashbyhq.com/openai/b75f6b5b-8a84-4796-9093-588cc9334c04 dead checked 2026-08-27 HTTP 200
- GTM Strategy & Operations Lead - BDR OpenAI req id is gone from the employer board feed https://jobs.ashbyhq.com/openai/c3029025-9f6e-429c-98da-01efc387b621 dead checked 2026-08-27 HTTP 200
- GTM Strategy & Operations Lead, Enterprise OpenAI req id is gone from the employer board feed https://jobs.ashbyhq.com/openai/d9b8a8fb-838f-4851-b61c-b80a89319a5f dead checked 2026-08-27 HTTP 200
- GTM Strategy & Operations, Strategic Programs OpenAI req id is gone from the employer board feed https://jobs.ashbyhq.com/openai/75f10cd2-22f4-4dae-8c67-3d51b9c2ec4a dead checked 2026-08-27 HTTP 200
- GTM Strategy & Planning OpenAI req id is gone from the employer board feed https://jobs.ashbyhq.com/openai/bd3a367f-aa91-4b6f-b74e-451fb7fc3151 dead checked 2026-08-27 HTTP 200
- Product Engineer, GTM Innovation OpenAI req id is gone from the employer board feed https://jobs.ashbyhq.com/openai/3bb3c9f8-78d1-4df5-b47e-235f8ed5cbf9 dead checked 2026-08-27 HTTP 200
- Strategic Finance, GTM OpenAI req id is gone from the employer board feed https://jobs.ashbyhq.com/openai/4f1870f0-b0a8-44fb-b6fe-28638b45ae47 dead checked 2026-08-27 HTTP 200
- Principal GTM Systems Manager Outreach http 404 https://jobs.lever.co/outreach/38ac7a54-e7d2-4a5d-bd56-ddee7b85bea4 dead checked 2026-08-27 HTTP 404
- Associate, GTM Finance & Operations Ramp req id is gone from the employer board feed https://jobs.ashbyhq.com/ramp/bd9e9159-6c35-4755-9a48-02cc96d5379d dead checked 2026-08-27 HTTP 200
- GTM Associate - Europe Ramp req id is gone from the employer board feed https://jobs.ashbyhq.com/ramp/20331539-c49c-4bf7-a719-a7e1b6e55537 dead checked 2026-08-27 HTTP 200
- Senior Program Analyst - GTM Ops Spotify http 404 https://jobs.lever.co/spotify/1f0ccb2c-bf5f-49ee-936d-4a22e8725c2b dead checked 2026-08-27 HTTP 404
- Senior Analyst, GTM Analytics Vanta req id is gone from the employer board feed https://jobs.ashbyhq.com/vanta/4d9672a3-3e60-44b2-b992-21dd06f0d172 dead checked 2026-08-27 HTTP 200
- Senior Manager, Enablement GTM Programs Vanta req id is gone from the employer board feed https://jobs.ashbyhq.com/vanta/02750249-acde-4518-816c-1717f315f32e dead checked 2026-08-27 HTTP 200
- Full Stack Engineer, Go-to-Market Systems Verkada redirected to https://job-boards.greenhouse.io/verkada?error=true with no trace of this req https://job-boards.greenhouse.io/verkada/jobs/5101666007 dead checked 2026-08-27 HTTP 200
- GTM operations, customer Watershed req id is gone from the employer board feed https://jobs.ashbyhq.com/watershed/ee822cb3-56c1-43aa-9150-4529f8053080 dead checked 2026-08-27 HTTP 200
- Head of GTM - Systems & Agents xAI redirected to https://job-boards.greenhouse.io/xai?error=true with no trace of this req https://job-boards.greenhouse.io/xai/jobs/5005154007 dead checked 2026-08-27 HTTP 200
