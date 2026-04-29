"""
Quickstart: connect to the RTK Motion MCP server and call a free tool.

This script makes raw JSON-RPC calls over the streamable-HTTP MCP transport.
For real client integration use the official MCP SDK
(https://github.com/modelcontextprotocol/python-sdk) — this is a minimal
dependency-free demo to prove the server is reachable from your environment.
"""

import json
import urllib.request

ENDPOINT = "https://api.rtkmotion.io/mcp"
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json, text/event-stream",
}


def rpc(method: str, params: dict | None = None, request_id: int = 1) -> dict:
    payload: dict = {"jsonrpc": "2.0", "id": request_id, "method": method}
    if params is not None:
        payload["params"] = params
    req = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(payload).encode(),
        headers=HEADERS,
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read())


def main() -> None:
    # Initialize the MCP session
    init = rpc("initialize", {
        "protocolVersion": "2024-11-05",
        "capabilities": {},
        "clientInfo": {"name": "rtkmotion-quickstart", "version": "0.1.0"},
    })
    info = init["result"]["serverInfo"]
    print(f"Connected to {info['name']} v{info['version']}")

    # List the available tools
    tools = rpc("tools/list", request_id=2)["result"]["tools"]
    print(f"\nServer exposes {len(tools)} tools:")
    for t in tools:
        desc = (t.get("description", "") or "").split("\n", 1)[0][:80]
        print(f"  {t['name']:<22} {desc}")

    # Call a free tool — browse_catalog
    print("\nCalling browse_catalog (free) ...")
    result = rpc("tools/call", {"name": "browse_catalog", "arguments": {}}, request_id=3)
    print(json.dumps(result["result"], indent=2)[:600] + " ...")


if __name__ == "__main__":
    main()
