# How every listing on the job board is verified, and what was removed on 2026-09-14

> The verification method behind The GTM Engineer job board, and the full ledger of the 29 listings the 2026-09-14 pass removed, each with the reason it failed.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[The job board](index.md) / Verification

**The verification pass, 2026-09-14**

## What was removed, and why.

A job board is a claim about the world at a moment, and the moment passes. This page is the receipt. 158 tracked reqs were checked on 2026-09-14. 129 are published. 29 are not, and every one of them is named below with the reason it failed.

### The method

- Every GTM-engineering req found on the public ATS feeds of 152 watched employers, plus every req on the previous board, fetched at the exact URL the board publishes.

- GET, real browser user agent, 10s timeout, 4 concurrent, 1 retry.

- Where the employer runs a public Greenhouse, Lever or Ashby board feed, the req id is also checked against that feed. A req the employer's own feed has dropped is dead even if the page still loads.

- Only status=live reaches the board. dead and unverified are published here and nowhere else.

- changed=true is a live req whose title, location, remote flag or salary moved since it was recorded. The board publishes the new value.

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
| salary | Printed only where the employer publishes it: the machine readable pay field of their own board feed first, else the first range printed in their own posting text. Never estimated, never inferred from a range seen elsewhere. |
| seniority | Ordered substring match over the title only. A title that says nothing about level is filed as not stated rather than guessed. |
| title_family | Ordered substring match over the employer's own job title. First rule that matches wins. It is a filing decision, not a judgement about the work. |

### What is not on this board

Job descriptions. Salary estimates. A count of applicants. A recruiter contact. Anything we would have had to guess. A salary appears only where the employer publishes it in the machine readable field of their own board feed, which is why 95 of 129 rows carry one and the rest are blank rather than estimated.

### The removal ledger, 2026-09-14

29 listings. These URLs are printed as text, not as links, because they no longer work. That is the point of printing them.

- Director, Forward Deployed Engineering & AI GTM Lead Aircall http 404 https://jobs.lever.co/aircall/13df67eb-2f59-4819-9266-ee35be751769 dead checked 2026-09-14 HTTP 404
- Director, Forward Deployed Engineering & AI GTM Lead Aircall http 404 https://jobs.lever.co/aircall/1ee12092-9b19-46db-a4a4-c2bc4902396c dead checked 2026-09-14 HTTP 404
- Director, Forward Deployed Engineering & AI GTM Lead Aircall http 404 https://jobs.lever.co/aircall/af40e77c-554a-436b-b6cb-bf1eca20c9d7 dead checked 2026-09-14 HTTP 404
- GTM Enablement Intern Aircall http 404 https://jobs.lever.co/aircall/daecac18-ae6c-45ea-9e0c-d307d18f1a14 dead checked 2026-09-14 HTTP 404
- Go-To-Market Engineer I, SMB Apollo.io redirected to https://job-boards.greenhouse.io/apolloio?error=true with no trace of this req https://job-boards.greenhouse.io/apolloio/jobs/5778017004 dead checked 2026-09-14 HTTP 200
- GTM Data Solutions Architect Chorus http 403 https://www.zoominfo.com/careers?gh_jid=8641894002 dead checked 2026-09-14 HTTP 403
- GTM Integration Engineer III Chorus http 403 https://www.zoominfo.com/careers?gh_jid=8716257002 dead checked 2026-09-14 HTTP 403
- Senior Program Manager, GTM Chorus http 403 https://www.zoominfo.com/careers?gh_jid=8654483002 dead checked 2026-09-14 HTTP 403
- GTM Engineer - CX Clay req id is gone from the employer board feed https://jobs.ashbyhq.com/claylabs/e43101dd-4e98-4c60-bc1b-adbbb38c7b15 dead checked 2026-09-14 HTTP 200
- GTM Engineer - Partnerships Clay req id is gone from the employer board feed https://jobs.ashbyhq.com/claylabs/242be863-2f62-44a7-909d-6c351dee81d1 dead checked 2026-09-14 HTTP 200
- GTM Engineer - Seller Efficiency Clay req id is gone from the employer board feed https://jobs.ashbyhq.com/claylabs/d5c7f612-10e7-4080-8b8a-d51e70fff9c5 dead checked 2026-09-14 HTTP 200
- GTM Ops Manager - EMEA Clay req id is gone from the employer board feed https://jobs.ashbyhq.com/claylabs/2620226a-13b5-48be-a9a9-ff7769552a21 dead checked 2026-09-14 HTTP 200
- GTM Applications Engineer Cursor 200 but the page carries no trace of this req (js-only shell or wrong page) https://jobs.ashbyhq.com/cursor/9d7c8f36-eeb7-4e9f-acbe-d959f6280e46 unverified checked 2026-09-14 HTTP 200
- GTM Strategy & Ops Lead - APJ Cursor 200 but the page carries no trace of this req (js-only shell or wrong page) https://jobs.ashbyhq.com/cursor/7e1d8e07-c87b-4388-892a-6b138bebf665 unverified checked 2026-09-14 HTTP 200
- Senior Staff Systems Engineer, GTM Fivetran 200 but the page carries no trace of this req (js-only shell or wrong page) https://www.fivetran.com/careers/job?gh_jid=7810381003 unverified checked 2026-09-14 HTTP 200
- Senior Staff Systems Engineer, GTM Fivetran 200 but the page carries no trace of this req (js-only shell or wrong page) https://www.fivetran.com/careers/job?gh_jid=7826669003 unverified checked 2026-09-14 HTTP 200
- GTM AI Engineer Gong redirected to https://job-boards.greenhouse.io/gongio?error=true with no trace of this req https://job-boards.greenhouse.io/gongio/jobs/4697977006 dead checked 2026-09-14 HTTP 200
- GTM Engineer (GTM Automations) Gong redirected to https://job-boards.greenhouse.io/gongio?error=true with no trace of this req https://job-boards.greenhouse.io/gongio/jobs/4693864006 dead checked 2026-09-14 HTTP 200
- GTM Engineer Hebbia AI req id is gone from the employer board feed https://jobs.ashbyhq.com/hebbia-ai/4b1d51bc-2985-471b-b3b5-1ddf62e0a50a dead checked 2026-09-14 HTTP 200
- Go-to-Market Engineer Hightouch redirected to https://job-boards.greenhouse.io/hightouch?error=true with no trace of this req https://job-boards.greenhouse.io/hightouch/jobs/5823552004 dead checked 2026-09-14 HTTP 200
- Senior GTM Enablement Manager, Operations Intercom redirected to https://job-boards.greenhouse.io/intercom?error=true with no trace of this req https://job-boards.greenhouse.io/intercom/jobs/7441053 dead checked 2026-09-14 HTTP 200
- GTM Engineer - Revenue Programs Make http 403 https://www.make.com/en/careers-detail?gh_jid=7778897003 dead checked 2026-09-14 HTTP 403
- Sales Recruiter Notion req id is gone from the employer board feed (page still renders it) https://jobs.ashbyhq.com/notion/f663839e-46ac-44ad-9720-da2b6aa28093 dead checked 2026-09-14 HTTP 200
- Senior GTM AI Advisor Outreach req id is gone from the employer board feed (page still renders it) https://jobs.lever.co/outreach/91b45521-0ad3-499f-8c05-514beb39c2e5 dead checked 2026-09-14 HTTP 200
- GTM Systems Engineer, Salesforce Ramp req id is gone from the employer board feed https://jobs.ashbyhq.com/ramp/ffc09fc0-7785-48db-a203-a148f62534be dead checked 2026-09-14 HTTP 200
- Software Engineer, Frontend, Ramp Revenue Ramp req id is gone from the employer board feed https://jobs.ashbyhq.com/ramp/1540a41f-d88f-4c89-9b08-5b9fade1ee81 dead checked 2026-09-14 HTTP 200
- Senior GTM Engineer, Systems Engineering Sanity req id is gone from the employer board feed (page still renders it) https://www.sanity.io/careers/senior-gtm-engineer-systems-engineering dead checked 2026-09-14 HTTP 200
- Growth Engineer Stripe req id is gone from the employer board feed https://stripe.com/jobs/search?gh_jid=8008880 dead checked 2026-09-14 HTTP 200
- Staff Domain Expert, AI in GTM Workato redirected to https://www.workato.com/careers#open-roles with no trace of this req https://job-boards.greenhouse.io/workato/jobs/8474237002 dead checked 2026-09-14 HTTP 200
