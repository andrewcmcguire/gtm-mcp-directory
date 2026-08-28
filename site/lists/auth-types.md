# GTM tools by MCP auth type: OAuth, API key or neither

> How the 165 GTM tools with an MCP server authenticate. OAuth, API key, both, or not recorded, with the verbatim auth field on every row. Counted 2026-08-28.

*Markdown twin of the HTML page at the same path. Same content, no navigation, no styling, no scripts. Links below point at other twins. Site map for machines: [llms.txt](../llms.txt). The whole dataset: [directory.json](../data/directory.json).*

---
[Directory](../index.md) /
[The lists](index.md) / By auth type

**List · auth**

## How a GTM MCP server asks you to log in.

Auth is the difference between an agent your security team will allow and an agent it will not. OAuth hands the server a scoped token the vendor can revoke. An API key pasted into a config file is as powerful as whatever the vendor scoped it to, lives in plain text on the machine running the agent, and is revoked by rotating it. Both are normal. Knowing which one you are about to wire in is not optional.

165 of 293 entries have a server of any kind (144 official, 21 community). The buckets below are a keyword match over the mcp_auth field, disclosed as such, with the verbatim field printed on every row of every page.

- [OAuth](auth-oauth.md)**46** of 165 servers
- [API key](auth-api-key.md)**44** of 165 servers
- [OAuth or an API key](auth-either.md)**46** of 165 servers
- [Third party platform auth](auth-third-party.md)**4** of 165 servers
- [Auth not recorded](auth-unrecorded.md)**25** of 165 servers

- [OAuth](auth-oauth.md) - 46 of 165 servers. The server takes the user through a browser sign in and holds a scoped token. Nothing is pasted into a config file, and access can be...
- [API key](auth-api-key.md) - 44 of 165 servers. The server authenticates with a key or token the operator generates and pastes in. Simple to wire, and the key is as powerful as whatever...
- [OAuth or an API key](auth-either.md) - 46 of 165 servers. Both paths are documented. Usually OAuth for a hosted server and a key for the self hosted or legacy endpoint.
- [Third party platform auth](auth-third-party.md) - 4 of 165 servers. Auth is handled by a connector platform sitting between the agent and the vendor, so the credential lives with the platform rather than...
- [Auth not recorded](auth-unrecorded.md) - 25 of 165 servers. The mcp_auth field on the entry is blank, or says unknown. Published as blank rather than guessed.
