# RTK Motion Intelligence — MCP Server

[![MCP Toplist](https://mcptoplist.com/badge/io.rtkmotion%2Fdata.svg)](https://mcptoplist.com/server/io.rtkmotion%2Fdata)

[![smithery badge](https://smithery.ai/badge/RTKMotion/motion-intelligence)](https://smithery.ai/servers/RTKMotion/motion-intelligence)

> Agent-to-agent paid data marketplace. **Two-person (dyadic) motion capture in a shared coordinate frame**, rehab biomechanics, threat intelligence, and commercial-carrier truck-sighting intelligence (RTK Spotter). 21 MCP tools, gasless USDC payments via x402 (EIP-3009).

**[rtkmotion.io](https://www.rtkmotion.io)** · [Developer docs](https://www.rtkmotion.io/developers) · [Live catalog](https://api.rtkmotion.io/catalog) · [Pricing](https://api.rtkmotion.io/pricing) · [Shared-frame mocap spec](./docs/SHARED_FRAME_MOCAP_SPEC.md)

## What is this?

A live, hosted **Model Context Protocol** server providing agent-to-agent paid access to:

- **4D Motion Capture** — BVH skeletal animation, multi-view video, robot-ready joint trajectories (NPZ). **Two-person (dyadic) capture in a shared coordinate frame**: both actors' global root translation and orientation are preserved in one capture-volume frame, so contact, separation and relative pose are recoverable directly from the files. Most released datasets canonicalize each actor to its own origin, which destroys inter-actor geometry irreversibly — see the [specification](./docs/SHARED_FRAME_MOCAP_SPEC.md) and its pre-purchase verification procedure
- **Rehabilitation Biomechanics** — cross-exercise summaries, per-exercise reports, ROM and asymmetry metrics
- **Location Threat Intelligence** — confidence-scored alerts, event distribution, temporal context
- **RTK Spotter — Commercial Vehicle Intelligence** — de-identified commercial-carrier truck sightings (per-USDOT bundles) plus a geo-stripped truck-recognition CV/OCR training corpus. Commercial carriers only; faces + bystander plates blurred; FMCSA-public labels (USDOT, carrier, equipment)

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

Restart your client. The 21 tools become available.

See [`examples/`](./examples) for ready-to-use config snippets and a minimal Python connect script.

### Free tools (no payment, 10 total)

- `browse_catalog` — hierarchical catalog of all data
- `search_catalog` — full-text search across motion capture, rehab, threat, and Spotter datasets
- `get_mocap_sample` — first 5 s of BVH skeletal animation (300 frames at 60 fps)
- `get_calibration` — multi-camera capture-rig calibration
- `get_threat_profile` — monitored location profile (assets, feeds, scan interval)
- `get_threat_sample` — current threat assessment sample
- `get_rehab_profile` — patient demographics, injury history, medications
- `get_rehab_sample` — rehab biomechanics sample
- `get_spotter_carrier_profile` — commercial-carrier coverage + de-identification posture
- `get_spotter_cv_profile` — truck CV/OCR corpus profile (image count, label schema)

### Paid tools (USDC via x402, 11 total)

| Tool | Price | Output |
|---|---|---|
| `get_bvh` | $10 | Full BVH skeletal animation |
| `get_video_url` | $5 | Multi-view grappling video |
| `get_robotarget` | $15 | Robot-ready joint trajectories (NPZ, MoveIt/ROS/Isaac compatible) |
| `get_trial_bvh` | $0.25 | Trial BVH slice (5 s) — evaluate quality |
| `get_trial_robotarget` | $0.25 | Trial NPZ trajectory (5 s) — evaluate quality |
| `get_threat_summary` | $0.50 – $1.00 | Location threat assessment (lite / full) |
| `get_rehab_summary` | $0.50 | Cross-exercise biomechanical summary |
| `get_rehab_report` | $0.25 | Per-exercise biomechanical report |
| `get_spotter_carrier` | $5 | Per-USDOT commercial-carrier sighting bundle (de-identified crops + trail) |
| `get_spotter_cv_sample` | $0.25 | Trial slice of the truck CV/OCR corpus |
| `get_spotter_cv` | $50 | Full geo-stripped truck-recognition CV/OCR training corpus |

Payment via the [x402 payment protocol](https://www.x402.org/) on Base, Ethereum, or Solana. The preferred path is gasless x402 `exact` / EIP-3009 — the agent signs a single-use transfer authorization and passes it as `x_payment` (no gas for the buyer); a legacy on-chain `payment_tx` is also accepted (and is the path for Solana). Full pricing detail at [`api.rtkmotion.io/pricing`](https://api.rtkmotion.io/pricing).

### Provenance

Every paid record is signed with ECDSA (secp256k1) by `0x6C11F8a21f7ca922F483Ed21C3b6c2d9B305B10C`. Verification key (JWKS) at [`api.rtkmotion.io/.well-known/jwks.json`](https://api.rtkmotion.io/.well-known/jwks.json).

## Discovery surfaces

| Surface | URL |
|---|---|
| Website | [`rtkmotion.io`](https://www.rtkmotion.io) · [developer docs](https://www.rtkmotion.io/developers) |
| Glama connector | [`glama.ai/mcp/servers/RTKMotion/motion-intelligence`](https://glama.ai/mcp/servers/RTKMotion/motion-intelligence) |
| Smithery catalog | [`smithery.ai/servers/RTKMotion/motion-intelligence`](https://smithery.ai/servers/RTKMotion/motion-intelligence) |
| MCP Server Registry | `io.rtkmotion/data` ([listing](https://registry.modelcontextprotocol.io/v0/servers?search=rtkmotion)) |
| A2A Agent Card | [`api.rtkmotion.io/.well-known/agent.json`](https://api.rtkmotion.io/.well-known/agent.json) |
| x402 Manifest | [`api.rtkmotion.io/.well-known/x402`](https://api.rtkmotion.io/.well-known/x402) |
| OpenAPI 3.1 | [`api.rtkmotion.io/openapi.json`](https://api.rtkmotion.io/openapi.json) |
| Live data catalog (free) | [`api.rtkmotion.io/catalog`](https://api.rtkmotion.io/catalog) |

## Use cases

- **Robotics** — Motion capture for sim-to-real kinematic retargeting (MoveIt/ROS/Isaac compatible NPZ trajectories). Dyadic captures support two-person interaction and contact-rich manipulation work that single-actor corpora cannot express
- **Human interaction / HOI modelling** — Two-person motion in one shared coordinate frame, so contact, separation and relative pose are recoverable per frame rather than approximated
- **Insurance / Underwriting** — Validate rehab claims with objective biomechanical data; assess facility risk via threat intelligence; vet commercial carriers via Spotter sighting bundles
- **Physical Therapy** — Track patient progress with per-exercise biomechanical reports
- **Security & Compliance** — Location threat audits, confidence-scored alerting
- **Fleet & Logistics / Computer Vision** — Commercial-carrier movement corroboration and cargo-fraud investigation from de-identified truck sightings; train truck-recognition detection/OCR models on the geo-stripped CV corpus

## Latency

< 500 ms typical for free tools. Cloudflare Workers global edge deployment.

## Specifications

- [**Shared-Frame Multi-Actor Motion Capture — a delivery specification**](./docs/SHARED_FRAME_MOCAP_SPEC.md)
  — a vendor-neutral spec for delivering multi-actor mocap without destroying
  inter-actor geometry, with a pre-purchase verification procedure a buyer can
  run against any supplier. Draft, published for comment.
  Canonical URL: `https://github.com/RTKMotion/motion-intelligence/blob/main/docs/SHARED_FRAME_MOCAP_SPEC.md`

## Source

This is a manifest repository for the hosted MCP server. The server implementation runs on Cloudflare Workers; the implementation source is private. For technical questions, partnership, or custom integration: [`support@rtkmotion.io`](mailto:support@rtkmotion.io).

## License

The contents of this repository (README, examples, configuration files) are released under the MIT License — see [LICENSE](./LICENSE).

The data products served by the MCP server are **separately licensed** via the per-purchase terms documented at [`api.rtkmotion.io/.well-known/x402`](https://api.rtkmotion.io/.well-known/x402) and at [`rtkmotion.io/legal`](https://www.rtkmotion.io/legal).
