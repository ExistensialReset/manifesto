# FLOW_LOTTERY_PARAMETERS_AND_RNG_SPEC.md

## Overview
**Purpose:** Define the default parameters for LOTUS lottery governance, Node operations, and provide a fully auditable RNG and selection proof specification for Flow. Includes auditor checklist to verify integrity, reproducibility, and compliance with privacy-preserving principles.

**Scope:** Applies to initial mandate lotteries, verifier selections, recovery set selections, and Node audits.

---

## Parameters Appendix

| Parameter | Default Value | Rationale |
|---|---:|---|
| Mandate duration | 9 months | Matches Mandate of Nine Moons; balances continuity with rotation. |
| Max mandates per person per year | 2 | Prevents over-burdening or capture of Nodes by individuals. |
| Max concurrent mandates per Node | 3 | Limits local concentration of decision power. |
| Verifier monthly limit per Node | 20 verifications | Reduces risk of single-actor capture; triggers cross-node attest. |
| Cross-node attest threshold | ≥2 external Node attestations for Nodes >20 verifications/month | Ensures external validation before full activation. |
| Default recovery timelock | 72 hours | Provides community visibility and veto window for recovery. |
| Max timelock extension | 14 days (adaptive) | For high-risk anomalies; requires documented justification. |
| Selection exclusion radius | Immediate Node + household + first-degree relations | Prevents local conflicts of interest. |
| Training window | 48 hours after selection | Ensures panel readiness before deliberation. |
| Training duration | 30–60 minutes | Trauma-informed, confidentiality, conflict rules. |
| Audit cadence | Quarterly anomaly scan; annual independent audit | Balances operational monitoring with deeper review. |
| RNG commit-reveal window | Commit 24h; reveal 24h | Prevents last-minute manipulation while keeping selection timely. |
| Anomaly trigger thresholds | e.g., >3× expected verifications in 7 days; repeated selection overlap >2σ | Triggers manual review and adaptive timelocks. |

---

## RNG and Selection Proof Specification

### High-Level Flow
1. **On-chain Seed Publication**  
   - Publish a public, immutable on-chain seed at start of each epoch (block hash or dedicated transaction).

2. **Node Entropy Commits**  
   - Each Node publishes:  
     `commit = H(nodeID || epoch || nonce || nodeEntropy)`  
   - Commits posted on-chain or signed log.

3. **Reveal Phase**  
   - Nodes reveal `nodeEntropy`. Verifiers check:  
     `H(nodeID || epoch || nonce || reveal) == commit`.

4. **Combined Randomness Derivation**  
   - `finalRandomness = H(onChainSeed || commit1 || commit2 || ... || commitN || epochNonce)`  
   - Use HKDF if multiple outputs needed.

5. **Selection Algorithm**  
   - Deterministic RNG stream (e.g., HMAC-DRBG) to sample without replacement from eligible pool.  
   - Record selection order + `selectionProofHash`.

---

### Selection Proof Format
Each selection event publishes a compact proof object (JSON) with hashes on-chain. Full proofs available for authorized auditors.

**Fields:**
- `epoch`: string  
- `onChainSeedHash`: hex string  
- `commitListHash`: hex string (hash of concatenated commits)  
- `revealListHash`: hex string (hash of concatenated reveals)  
- `selectionProofHash`: hex string (hash of selection details)  
- `selectionAlgorithm`: string (e.g., HMAC-DRBG-SHA256)  
- `selectionParameters`: string (pool size, sample size, exclusion filters)  
- `aggregateSignature`: Node aggregate signature over proof object  

**On-chain fields (minimal):**  
`epoch | onChainSeedHash | commitListHash | selectionProofHash | timestamp`

---

### Auditor Checklist
1. Retrieve on-chain seed and commit/reveal logs for the epoch.  
2. Verify each commit matches its reveal: `H(nodeID || epoch || nonce || reveal) == commit`.  
3. Recompute combined randomness and reproduce selection deterministically.  
4. Compare reproduced selection order against `selectionProofHash`.  
5. Verify aggregate Node signature over proof object.  
6. Check anomaly triggers:  
   - Node verification counts  
   - Selection overlaps  
   - Commit/reveal latency patterns  
7. Confirm cross-node attest thresholds were met before activation.  
8. Review timelock adherence and adaptive extensions for flagged anomalies.  
9. Document audit findings; publish anonymized attestation hash on-chain.

---

### Anti-Manipulation Measures
- Commit-reveal enforced with timeouts.  
- Minimum 3 independent Nodes geographically distributed to finalize randomness.  
- Fallback seed handling: failed reveals excluded; if below minimum committers, abort epoch and reschedule.  
- Public proof hashes immediately on-chain; full proof only for authorized auditors.  
- Adaptive timelocks for anomalies; escalation to LOTUS governance if suspicious.

---

### Operational Recommendations
- Implement standard reference libraries for commit-reveal, HKDF, deterministic sampling.  
- Log anonymized telemetry for anomaly detection (Node verification counts, selection overlaps, commit/reveal latencies).  
- Independent red-team verification of RNG before pilot and annually.  
- Document failure modes and fallback rules.

---

### Ledger Entry Example (JSON-LD)

```
{ "publicKeyHash": "sha256:...", "verificationHash": "sha256:...", "NodeID": "node:abc123", "timestamp": "2026-02-26T04:45:00Z", "statusFlag": "active", "selectionProofHash": "sha256:..." } 
```