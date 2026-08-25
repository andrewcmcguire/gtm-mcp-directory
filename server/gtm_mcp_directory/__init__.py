"""The GTM MCP Directory, as an MCP server.

Part of Agent Operator. Local, stdio, zero outbound requests at query time.

The package loads a baked `directory.json` once at startup, verifies it against
the build report and its own content checksum, and serves every answer from
memory. Nothing here touches the network, and nothing here writes to `data/`.
"""

SERVER_NAME = "gtm-directory"
SERVER_VERSION = "0.1.0"
PRODUCT_NAME = "The GTM MCP Directory"
UMBRELLA = "Agent Operator"
REPO = "https://github.com/andrewcmcguire/gtm-mcp-directory"

__all__ = [
    "SERVER_NAME",
    "SERVER_VERSION",
    "PRODUCT_NAME",
    "UMBRELLA",
    "REPO",
]
