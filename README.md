# RTK Motion Intelligence — MCP Server

[![smithery badge](https://smithery.ai/badge/RTKMotion/motion-intelligence)](https://smithery.ai/servers/RTKMotion/motion-intelligence)

> Agent-to-agent paid data marketplace. Motion capture, rehab biomechanics, threat intelligence. 14 MCP tools, USDC payments via x402.

## What is this?

A live, hosted **Model Context Protocol** server providing agent-to-agent paid access to:

- **4D Motion Capture** — BVH skeletal animation, robot trajectories (NPZ), 3D keypoints
- **Rehabilitation Biomechanics** — cross-exercise summaries, per-exercise reports, ROM and asymmetry metrics
- **Location Threat Intelligence** — confidence-scored alerts, event distribution, temporal context

The server runs at **`https://api.rtkmotion.io/mcp`** on Cloudflare Workers, using the streamable-HTTP MCP transport.

This repository is the public-facing manifest for catalog discovery. The server itself is hosted, not installable from this repo.

## Quick start

### Add to Claude Desktop / Cursor / Cline / Continue

Add to your client's MCP config (e.g. `~/Library/Application Support/Claude/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "rtk-motion": {
      "type": "streamable-http",
      "url": "https://api.rtkmotion.io/mcp"
    }
  }
}
```

Restart your client. The 14 tools become available.

See [`examples/`](./examples) for ready-to-use config snippets and a minimal Python connect script.

### Free tools (no payment, 7 total)

- `browse_catalog` — hierarchical catalog of all data
- `search_catalog` — full-text search across motion capture, rehab, and threat datasets
- `get_threat_profile` — monitored location profile (assets, feeds, scan interval)
- `get_rehab_profile` — patient demographics, injury history, medications
- `get_threat_sample` — current threat assessment sample
- `get_rehab_sample` — rehab biomechanics sample
- `get_mocap_sample` — first 5 s of BVH skeletal animation (300 frames at 120 Hz)

### Paid tools (USDC via x402, 7 total)

| Tool | Price | Output |
|---|---|---|
| `get_bvh` | $10 | Full BVH skeletal animation |
| `get_video_url` | $5 | Multi-view grappling video |
| `get_keypoints_3d` | $10 | Triangulated 3D joint positions |
| `get_robotarget` | $15 | Robot-ready joint trajectories (NPZ, MoveIt/ROS/Isaac compatible) |
| `get_threat_summary` | $0.50 – $1.00 | Location threat assessment (full) |
| `get_rehab_summary` | $0.50 | Cross-exercise biomechanical summary |
| `get_rehab_report` | $0.25 | Per-exercise biomechanical report |

Payment via the [x402 HTTP payment protocol](https://www.x402.org/) on Base, Ethereum, or Solana. Full pricing detail at [`api.rtkmotion.io/pricing`](https://api.rtkmotion.io/pricing).

### Provenance

Every paid record is signed with ECDSA (secp256k1) by `0x6C11F8a21f7ca922F483Ed21C3b6c2d9B305B10C`. Verification key (JWKS) at [`api.rtkmotion.io/.well-known/jwks.json`](https://api.rtkmotion.io/.well-known/jwks.json).

## Discovery surfaces

| Surface | URL |
|---|---|
| Smithery catalog | [`smithery.ai/servers/RTKMotion/motion-intelligence`](https://smithery.ai/servers/RTKMotion/motion-intelligence) |
| MCP Server Registry | `io.rtkmotion/data` ([listing](https://registry.modelcontextprotocol.io/v0/servers?search=rtkmotion)) |
| A2A Agent Card | [`api.rtkmotion.io/.well-known/agent.json`](https://api.rtkmotion.io/.well-known/agent.json) |
| x402 Manifest | [`api.rtkmotion.io/.well-known/x402`](https://api.rtkmotion.io/.well-known/x402) |
| OpenAPI 3.1 | [`api.rtkmotion.io/openapi.json`](https://api.rtkmotion.io/openapi.json) |
| Live data catalog (free) | [`api.rtkmotion.io/catalog`](https://api.rtkmotion.io/catalog) |

## Use cases

- **Robotics** — Motion capture for sim-to-real kinematic retargeting (MoveIt/ROS/Isaac compatible NPZ trajectories)
- **Insurance / Underwriting** — Validate rehab claims with objective biomechanical data; assess facility risk via threat intelligence
- **Physical Therapy** — Track patient progress with per-exercise biomechanical reports
- **Security & Compliance** — Location threat audits, confidence-scored alerting

## Latency

< 500 ms typical for free tools. Cloudflare Workers global edge deployment.

## Source

This is a manifest repository for the hosted MCP server. The server implementation runs on Cloudflare Workers; the implementation source is private. For technical questions, partnership, or custom integration: [`support@rtkmotion.io`](mailto:support@rtkmotion.io).

## License

The contents of this repository (README, examples, configuration files) are released under the MIT License — see [LICENSE](./LICENSE).

The data products served by the MCP server are **separately licensed** via the per-purchase terms documented at [`api.rtkmotion.io/.well-known/x402`](https://api.rtkmotion.io/.well-known/x402) and at [`rtkmotion.io/legal`](https://www.rtkmotion.io/legal).
