# How do I let an AI agent book meetings? Read the calendar before writing to it

> 26 tools here are tagged with booking a meeting and 12 with reading availability. The split matters, and here is how to wire it.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[Learn](index.md) / How to actually do it

**How to actually do it**

# How do I let an AI agent book meetings for me?

**The short answer**

Split it into two permissions. Reading availability is safe and immediately useful: 12 entries here are tagged with it. Writing an event holds somebody else's time, and that is the one to keep behind an approval until you trust the chain feeding it.

## The two jobs, deliberately separate

| Step | The job | Tools tagged | Official MCP | Free tier |
|---|---|---|---|---|
| Read calendar availability | [read calendar availability](../jobs/read-calendar-availability.md) | 12 | 6 | 2 |
| Book the meeting | [book a meeting](../jobs/book-a-meeting.md) | 26 | 10 | 3 |
| Route the inbound lead to the right owner | [route an inbound lead](../jobs/route-inbound-lead.md) | 9 | 4 | 1 |
| Answer the inbound chat | [answer an inbound chat or call](../jobs/answer-inbound-chat.md) | 21 | 12 | 6 |

## The tools an agent can call

- [Cal.com](../tools/cal-com.md) Official MCP · Free to start
Open-source scheduling infrastructure - booking pages, event types, and a scheduling API/platform - offered both as a free, self-hostable open-source...
- [Calendly](../tools/calendly.md) Official MCP · Free to start
Prospect-facing scheduling links and booking pages that let invitees book meetings directly onto a rep's calendar based on defined availability rules.
- [Tavus](../tools/tavus.md) Official MCP · Free to start
Developer platform for building real-time, two-way conversational AI video agents ("Conversational Video Interface") - positioned for GTM use cases...
- [Avoma](../tools/avoma.md) Official MCP · Paid, self-serve
AI meeting platform combining scheduling, note-taking, and conversation intelligence (deal insights, coaching) for sales teams.
- [Chili Piper](../tools/chili-piper.md) Official MCP · Paid, self-serve
Inbound lead-routing and instant meeting-booking platform ("Concierge") that qualifies web-form leads and books them directly onto the right rep's...
- [HighLevel (GoHighLevel)](../tools/highlevel.md) Official MCP · Paid, self-serve
An all-in-one agency CRM covering contacts, pipelines, conversations, calendars, payments and campaign automation across many client sub-accounts...
- [Mixmax](../tools/mixmax.md) Official MCP · Paid, self-serve
Gmail-native sales engagement layer that runs email sequences, tracking, calendaring and meeting notes from inside the inbox.
- [Artisan AI (Ava)](../tools/artisan-ai.md) Official MCP · Enterprise only
An AI agent ("Ava") that finds and enriches B2B leads, writes and sends personalized outreach, handles replies, and books meetings - marketed as...
- [RevenueHero](../tools/revenuehero.md) Official MCP · Gate unknown
Instant meeting-scheduling and inbound-lead-routing tool that qualifies web-form leads against CRM data and books them directly onto the right rep's...
- [SavvyCal](../tools/savvycal.md) Community MCP · Paid, self-serve
Prospect-facing scheduling/booking-page tool (Calendly competitor) built around letting invitees overlay their own calendar on the organizer's...

1 more are on the linked page. The cut is the display limit, not a ranking.

## The three rules that keep this boring

- **Never let the agent invent availability.** It must read the calendar, not reason about it. A confidently wrong time is worse than no answer.

- **Routing is a business rule, not a judgement call.** 9 entries are tagged [route an inbound lead](../jobs/route-inbound-lead.md). Owner, territory and round robin logic belong in the routing tool where they can be audited, not in a prompt where they cannot.

- **Confirm in writing, to a human.** The agent's last step is a message a person can read and cancel, not a silent calendar write.

## Where scheduling coverage actually sits

Scheduling & Routing has 5 official servers and 2 community across 14 entries, with 6 entries whose access gate could not be established from public sources. It is a middling category by coverage, which is worth knowing before you design a flow that assumes the booking step is the easy one.

## Sources

- [The GTM MCP Directory, Scheduling and Routing](../categories/scheduling-routing.md) this site
- [The GTM MCP Directory, book a meeting](../jobs/book-a-meeting.md) this site

Every number on this page is generated from directory.json at build time and carries the date it was baked: 2026-09-03. Nothing is typed by hand, nothing is rounded, and nothing is estimated. The underlying data is [published in full](../data.md). Where the honest answer is a zero, the zero is printed.

## Related questions

- [Which scheduling tools can an AI agent use to book a meeting?](which-tools-can-book-a-meeting.md)
- [How do I give an AI agent access to my sales calls?](how-do-i-give-an-ai-agent-access-to-my-sales-calls.md)
- [What is an AI agent in sales?](what-is-an-ai-agent-in-sales.md)
- [How do I stop an AI agent writing bad data to my CRM?](how-do-i-stop-an-agent-writing-bad-data-to-my-crm.md)

## In the directory

- [Book a meeting](../jobs/book-a-meeting.md)
- [Scheduling and Routing](../categories/scheduling-routing.md)
