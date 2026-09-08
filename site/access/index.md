# Request a key for the hosted GTM MCP Directory endpoint

> The hosted MCP endpoint needs a free key. A work email address is approved automatically, usually within about ten minutes. The hosted copy records, per key, the number of calls and the date last used, and nothing else.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

*Maintained by Andrew McGuire (https://andrewcmcguire.com), who also publishes https://gtmsignals.co and https://justsaid.ai.*

---
[Directory](../index.md) / Request a key

**The hosted MCP endpoint**

## Request a key. It is free.

The hosted copy of the directory's MCP server at `https://andrewcmcguire.com/gtm-directory/api/mcp` requires a key since 2026-09-08. Without one it answers 401 with a JSON body that points back here. A key looks like `gtmd_` followed by 32 characters, and it is presented one of two ways, shown below the form.

If you were sent back here, a required field was missing or the email did not look real. Fill it in and send it again.

*The HTML page carries a form here. It posts to `/gtm-directory/api/access` as application/x-www-form-urlencoded. Its fields:*

- **Name**: `name` (text required)
- **Email**: `email` (email required)
- **Company optional**: `company` (text)
- **Use case**: `use_case` (textarea required)
- **Client**: `client` (select)
- **You may email me the key and occasional directory changes. No marketing.**: `consent` (checkbox required)

Name, email and company are used to send the key and to ask a follow up question if the use case is unclear. They are never published. The form posts to this site's own origin and nowhere else.

**The policy**

Keys are free. A request from a work email address is approved automatically, usually within about ten minutes, by the directory's access desk, and the key arrives by email. Requests from free-mail addresses or without a clear use case are reviewed by Drew, the directory's operator, and answered within a day.

The hosted copy records, per key, the number of calls and the date last used, and nothing else: no query text, no tool arguments, no IP log kept. A key can be revoked on request by replying to the email it came in.

The local install needs no key because the code and the data are public. The [data endpoint](../data.md) needs no key either.

**Presenting the key, first way: a header**

Any client that supports headers sends `Authorization: Bearer gtmd_...`. Cursor, Claude Code and Claude Desktop all do. Replace the placeholder with your key:

```
{
 "mcpServers": {
 "gtm-directory": {
 "url": "https://andrewcmcguire.com/gtm-directory/api/mcp",
 "headers": {
 "Authorization": "Bearer gtmd_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
 }
 }
 }
}
```

The same thing as one line for Claude Code:

```
claude mcp add --transport http gtm-directory https://andrewcmcguire.com/gtm-directory/api/mcp --header "Authorization: Bearer gtmd_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

**Presenting the key, second way: the per-key URL**

A client that only accepts a URL, such as a claude.ai custom connector, cannot send a header. It uses the per-key URL instead, which carries the key as the last path segment:

```
{
 "mcpServers": {
 "gtm-directory": {
 "url": "https://andrewcmcguire.com/gtm-directory/api/mcp/k/gtmd_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
 }
 }
}
```

Treat that URL like the key it contains. Do not paste it into anything public.

**The fallback host**

Both forms also work on `https://d1hkopq5aq852m.cloudfront.net/gtm-directory/api/mcp`. Some clients hit a Cloudflare 403 on the apex host today. If yours does, swap the host and keep the rest of the URL and the key exactly as they are.

**Or run it yourself, no key**

The server is a public Python package in the [gtm-mcp-directory](https://github.com/andrewcmcguire/gtm-mcp-directory) repo and the data is [one JSON file](../data/directory.json). A local install loads that file once and answers from memory, makes zero outbound requests, and asks nobody for anything. The [install block is on the front page](../index.md#install).
