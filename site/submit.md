# Submit a GTM tool: listing is free, placement is not for sale

> Anyone can submit a tool or a correction. Every submission is verified against public sources before it is listed, and the verification is the product. BENCH-TESTED cannot be bought at any price.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](llms.txt). The whole dataset: [directory.json](data/directory.json).*

---
[Directory](index.md) / Submit

**Submit a tool**

## Listing is free. Verification is mandatory. Placement is not for sale.

Anyone can submit a tool. Every submission is verified against public sources before it is listed, and the verification is the product. No vendor can pay to be listed, to be listed sooner, to rank higher, to be featured, to remove a none-found, or to soften a note. There is no sponsored tier and there will not be one.

BENCH-TESTED cannot be bought at any price. It means Andrew personally ran the tool on a stated date. A vendor can offer access so a bench test becomes possible, that offer is recorded in the entry's notes, and the offer buys a test, never a verdict. The verdict ships whatever it says.

- [Open the submission form](https://github.com/andrewcmcguire/gtm-mcp-directory/issues/new?template=tool-submission.yml)

- [Read the methodology first](methodology.md)

**How the queue works**
The submission queue is a GitHub issue form on the public gtm-mcp-directory repo, and it is open. A
submission is free and it is not a listing: nothing lands in the data until the claims below are
checked by hand against the vendor's own documentation.

**What the form asks for**

Vendor and product name, vendor URL, a suggested category from the 15 on file, one plain sentence on what it does, whether an MCP server exists and who built it, the MCP URL if one is claimed, the auth model, the API documentation URL, a public GitHub org if there is one, whether a solo operator can get API access, and one optional box for anything the tool does badly. That last one is the most interesting box on the form.

Contact name, role and email are collected and never published. They are used to ask follow up questions and nothing else.

**What happens after you submit**

1. The vendor URL is fetched live and has to resolve, return 200, and describe the product.

2. The product is checked against all 293 existing entries by normalised name, because 16 deliberate cross listings already exist.

3. If an MCP is claimed, the URL is fetched. A 200 passes. A 401 passes, because an auth gated live endpoint is still a live endpoint. A 403 is inconclusive and gets re-checked by hand. A 404 means the claim fails and the entry is recorded none-found, not official.

4. Official means first party. A third party wrapper is recorded as community.

5. The access gate is determined independently from published pricing or docs, with a source URL, not from what the submitter said. If the two disagree, ours ships and the disagreement goes in the notes.

6. What it does is rewritten in plain language. Vendor copy never ships as the description.

7. AI features are separated from automation with an AI label on it. Every existing entry does this and a new one does not get a pass.

8. At least two independent sources, and the vendor's own site cannot be both of them.

9. Tier is RESEARCHED and last_checked is the date the checklist was completed. Never BENCH-TESTED. A submitted entry cannot be bench tested by definition.

10. The counter is re-run and the index table is regenerated from its output, never hand edited.

Target turnaround is 14 days.

**The acknowledgement you sign**

"I understand listing is free, that Andrew verifies every claim independently, that nothing here can be paid for, and that a BENCH-TESTED tier can only be earned by Andrew running the tool himself."

**If your tool is already listed and something is wrong**

Open an issue on the same repo naming the entry and the field. A correction is the most valuable thing anyone can send. The whole reason this is free and public is that other operators correct it faster than one person can re-check 293 entries.

If you would rather not be crawled, say so and you are removed from the crawl. The entry keeps its documentation URL and a note. It does not get delisted, because delisting for asking would be a punishment and this directory does not punish.
