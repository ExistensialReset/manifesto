RNG_AND_LOG_SPEC.md
Status: DRAFT
Scope: Global Node Protocol
Primary Placement: /core/RNG_AND_LOG_SPEC.md  
Purpose: Provide a minimal, auditable, and implementable specification for verifiable random draws and standardized logging compatible with Flow principles.

OVERVIEW
This specification ensures RNG operations used for lotteries, random selection, and time‑based events are deterministic for audit, transparent, and privacy preserving. All timestamps use ISO 8601 UTC. No participant PII is stored in logs.

REQUIREMENTS
Open documentation: Algorithm and log schema published in repo.

Determinism: Same inputs produce same outputs.

Public nonce publication: Publish a public nonce and metadata at time of draw.

Seed confidentiality: Private seeds remain local and rotated per policy.

Minimal PII: Use pseudonymous participant_id only when necessary.

Exportability: Logs exportable to CSV and JSON.

RNG METHOD (HMAC‑DRBG HYBRID)
Inputs:
  - public_nonce: ISO 8601 UTC timestamp + node_id (e.g., 2026-02-26T01:25:00Z_node-01)
  - private_seed: node-local secret seed (kept offline)
  - context_string: short description (e.g., "flow_lottery_2026-02-26")

Procedure:
  1. Compute H = HMAC_SHA256(private_seed, public_nonce || context_string)
  2. Use H as seed for a deterministic CSPRNG (e.g., HMAC-DRBG per NIST SP 800-90A)
  3. Derive random_value(s) as required (e.g., uniform integer in [0,N-1])

Publication:
  - Immediately publish: public_nonce, context_string, SHA256(H) as hash_of_H, algorithm identifier.
  - Do NOT publish private_seed.

Verification:
  - Auditor with access to private_seed (or after controlled seed disclosure) recomputes H and verifies SHA256(H) == published hash_of_H.
Notes

Seed rotation: Rotate private_seed quarterly; log rotation events with timestamp and responsible_id.

Multi‑party option: Combine multiple independent private seeds via XOR before HMAC for higher trust.

Threat model: Assume node compromise; require periodic third‑party audits and public hash publication to detect tampering.

LOG FORMAT
CSV fields (one row per RNG event):  
event_id,timestamp_iso,node_id,context_string,public_nonce,hash_of_H,algorithm,output_summary,auditor_hash,notes

CSV example row:
evt-0001,2026-02-26T01:25:00Z,node-01,flow_lottery_2026-02-26,2026-02-26T01:25:00Z_node-01,3f2a...9b,HMAC-DRBG,winner_index=7,,initial_run
JSON schema
{
  "event_id": "string",
  "timestamp_iso": "string",
  "node_id": "string",
  "context_string": "string",
  "public_nonce": "string",
  "hash_of_H": "string",
  "algorithm": "string",
  "output_summary": "string",
  "auditor_hash": "string (optional)",
  "notes": "string (optional)"
}
RETENTION AND COMPOST POLICY
Retention: Encrypted RNG logs retained locally for 90 days by default.

Compost: After 90 days, sensitive fields are anonymized or deleted; published hash records remain in the public archive for audit.

VERIFICATION WORKFLOW
Publish: After draw, publish public_nonce, context_string, hash_of_H, algorithm, output_summary.

Audit: Auditor recomputes H from private_seed (if available under audit) and verifies SHA256(H) equals published hash_of_H.

Dispute: On mismatch, freeze related actions and initiate FLOW_VERIFICATION_PROTOCOL.md audit.

COMMIT MESSAGE (PR‑ready)
Add RNG and logging minimal spec: HMAC-DRBG hybrid method, public_nonce policy, ISO 8601 timestamps, CSV/JSON log schema, seed rotation and retention policy.
