# Key requested: what happens next

> Your request for a hosted endpoint key was received. A work email address is approved automatically, usually within about ten minutes; other requests are reviewed within a day.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) /
[Request a key](index.md) / Sent

**Received**

## Thank you. Here is what happens next.

Your request is in the queue. Nothing else is needed from you.

**If you used a work email address**

The directory's access desk approves it automatically, usually within about ten minutes, and the key arrives by email from the directory. Check the spam folder if it is not there in twenty.

**If you used a free-mail address, or the use case was thin**

Drew, the directory's operator, reads it and answers within a day. A short reply asking what your agent will do with the directory is not a refusal; it is the question the form asked.

**When the key arrives**

It looks like `gtmd_` followed by 32 characters. Put it in an `Authorization: Bearer` header, or use the per-key URL if your client only takes a URL. [Both forms are shown on the request page](index.md), with the fallback host for clients that hit a Cloudflare 403 on the apex.

The hosted copy records, per key, the number of calls and the date last used, and nothing else. To revoke the key, reply to the email it came in.

- [Back to the directory](../index.md)

- [Every tool, A to Z](../tools/index.md)
