# FLOW_LOTTERY_PARAMETERS_AND_RNG_SPEC.md

**Status:** Draft  
**Scope:** LOTUS Protocol, Global Node Governance  
**Purpose:** Provide a complete, auditable, and operational specification for LOTUS lottery parameters, RNG and selection proofs, auditor procedures, telemetry and anomaly detection, cryptographic requirements, failure SLAs, and inclusion and legal contingency rules. This file is the authoritative reference for pilot implementation and independent audits.

---

## 1 Parameters Appendix

**Default parameters** intended for pilot adoption. Values may be adjusted after pilot evaluation via LOTUS governance.

| **Parameter** | **Default Value** | **Rationale** |
|---|---:|---|
| **Mandate duration** | **9 months** | Balance continuity and rotation. |
| **Max mandates per person per year** | **2** | Prevents capture and burnout. |
| **Max concurrent mandates per Node** | **3** | Limits local concentration of power. |
| **Verifier monthly limit per Node** | **20 verifications** | Triggers cross‑node attest to reduce capture risk. |
| **Cross‑node attest threshold** | **≥2 external Node attestations** for Nodes >20 verifications/month | External validation before full activation. |
| **Default recovery timelock** | **72 hours** | Community visibility and veto window. |
| **Max timelock extension** | **14 days (adaptive)** | For high‑risk anomalies; requires documented justification. |
| **Selection exclusion radius** | **Immediate Node + household + first‑degree relations** | Prevents local conflicts of interest. |
| **Training window** | **48 hours after selection** | Ensures panel readiness. |
| **Training duration** | **30–60 minutes** | Trauma‑informed, confidentiality, conflict rules. |
| **Audit cadence** | **Quarterly anomaly scan; annual independent audit** | Operational monitoring and deep review. |
| **RNG commit‑reveal window** | **Commit 24h; reveal 24h** | Prevents last‑minute manipulation. |
| **Minimum committers per epoch** | **3 geographically distributed Nodes** | Resilience and anti‑manipulation. |
| **Anomaly trigger thresholds** | e.g., **>3× expected verifications in 7 days; repeated selection overlap >2σ** | Flags for manual review. |

---

## 2 RNG and Selection Proof Specification

### 2.1 Goals
- Produce **verifiable, unbiased randomness** for all LOTUS selections.  
- Keep **on‑chain footprint minimal** while enabling full off‑chain proofs for authorized auditors.  
- Provide **clear failure modes** and fallback rules.

### 2.2 High Level Flow
1. **Epoch seed publication**  
   - Publish an immutable on‑chain seed at epoch start (e.g., block hash or dedicated seed transaction). Field: `onChainSeedHash`.
2. **Commit phase**  
   - Participating Nodes publish commits:  
     `commit = H(nodeID || epoch || nonce || nodeEntropy)` using SHA‑256. Commits posted on‑chain or to a signed Node log.
3. **Reveal phase**  
   - After commit window closes, Nodes publish `reveal = nodeEntropy`. Verify `H(nodeID || epoch || nonce || reveal) == commit`.
4. **Combined randomness derivation**  
   - Compute `finalRandomness = H(onChainSeed || commit1 || commit2 || ... || commitN || epochNonce)`. Use HKDF for multiple outputs.
5. **Deterministic selection**  
   - Use HMAC‑DRBG (SHA‑256) seeded with `finalRandomness` to sample without replacement from the eligible pool. Produce ordered selection list and `selectionProofHash`.
6. **Publication**  
   - Publish minimal on‑chain proof hashes: `epoch | onChainSeedHash | commitListHash | selectionProofHash | timestamp`.

### 2.3 Selection Proof Object
A compact JSON proof object is produced per selection epoch. Store only hashes on‑chain; full proof available to authorized auditors.

**SelectionProof JSON Schema (concise)**  
```json
{
  "epoch": "string",
  "onChainSeedHash": "hex",
  "commitListHash": "hex",
  "revealListHash": "hex",
  "selectionProofHash": "hex",
  "selectionAlgorithm": "HMAC-DRBG-SHA256",
  "selectionParameters": {
    "poolSize": "integer",
    "sampleSize": "integer",
    "exclusionFilters": "string"
  },
  "commitList": [
    {"nodeID": "string", "nonce": "string", "commit": "hex"}
  ],
  "revealList": [
    {"nodeID": "string", "nonce": "string", "reveal": "hex"}
  ],
  "selectionOrder": ["memberHash1","memberHash2"],
  "aggregateSignature": "hex"
}
```

**On‑chain minimal fields**: `epoch | onChainSeedHash | commitListHash | selectionProofHash | timestamp`.

### 2.4 Anti‑Manipulation Measures
- **Commit‑reveal windows** enforced with timeouts.  
- **Minimum committers** required; if fewer reveal, abort epoch and reschedule.  
- **Geographic distribution** requirement for committers.  
- **Immediate on‑chain publication of proof hashes** to prevent retroactive tampering.  
- **Red team testing** mandatory before pilot and annually.

---

## 3 Cryptographic Appendix

### 3.1 Algorithms and Encodings
- **Hash function:** **SHA‑256** (hex lowercase).  
- **DRBG:** **HMAC‑DRBG with SHA‑256** for deterministic RNG stream.  
- **Key types:** **Ed25519** recommended for signatures; **BLS12‑381** optional for aggregate signatures if supported.  
- **Signature aggregation:** Prefer **BLS** for compact aggregate signatures; if not available, use MuSig2 or deterministic multisig with explicit aggregation steps.  
- **Multisig recovery transactions:** Use on‑chain multisig format with explicit `k-of-n`, timelock, and proof fields.  
- **Encoding:** JSON UTF‑8; hex for binary fields.

### 3.2 Example Verification Commands
- Verify commit: `sha256(nodeID || epoch || nonce || reveal) == commit`.  
- Recompute final randomness: `sha256(onChainSeed || commit1 || ... || commitN || epochNonce)`.  
- Reproduce selection using HMAC‑DRBG seeded with final randomness.

---

## 4 Auditor Checklist and Access Model

### 4.1 Auditor Roles
- **Independent Auditor:** external party with access to full proofs under NDA.  
- **Public Auditor:** may verify on‑chain hashes and reproduce selection using public data only.

### 4.2 Access Model
- **Minimal on‑chain exposure:** only hashes published publicly.  
- **Full proofs access:** encrypted delivery to authorized auditors via ephemeral keys; access logged and attested on‑chain (attestationHash).  
- **Audit request flow:** auditor requests proof → LOTUS governance approves → Node provides encrypted proof → auditor verifies and publishes attestation hash.

### 4.3 Step by Step Audit Checklist
1. Retrieve on‑chain `onChainSeedHash`, `commitListHash`, `selectionProofHash`.  
2. Obtain full commit/reveal logs from Nodes (encrypted).  
3. Verify each commit matches reveal: `sha256(nodeID || epoch || nonce || reveal) == commit`.  
4. Recompute `finalRandomness` and reproduce selection using documented algorithm and parameters.  
5. Confirm reproduced selection order matches `selectionProofHash`.  
6. Verify aggregate signature over proof object.  
7. Check anomaly telemetry and thresholds.  
8. Confirm cross‑node attest thresholds and timelock adherence.  
9. Publish anonymized attestation hash on‑chain with summary of findings.

---

## 5 Telemetry Schema and Anomaly Detection

### 5.1 Telemetry Fields (anonymized)
- `nodeIDHash` — SHA‑256 of NodeID.  
- `epoch` — selection epoch.  
- `verificationsCount` — number of verifications by Node in window.  
- `selectionOverlapCount` — count of repeated selections per member across epochs.  
- `commitLatencyMs` — median commit latency.  
- `revealLatencyMs` — median reveal latency.  
- `failedReveals` — count.  
- `anomalyFlag` — boolean.

### 5.2 Anonymization Rules
- All Node identifiers in telemetry are hashed with a per‑epoch salt before storage. Salt is ephemeral and not stored long‑term.  
- Telemetry aggregates only; raw identifiers never published.  
- Retention: telemetry retained for **12 months** for operational review; anonymized aggregates retained indefinitely.

### 5.3 Anomaly Detection Rules
- **Trigger A:** `verificationsCount` > 3× expected in 7 days → flag.  
- **Trigger B:** `selectionOverlapCount` > 2σ above mean → flag.  
- **Trigger C:** `failedReveals` > 1 in epoch for minimum committers → abort epoch.  
- Flagged events generate automatic adaptive timelock and escalation to LOTUS governance.

---

## 6 Failure Modes, SLAs, and Fallback Rules

### 6.1 Failure Modes
- **Missing reveals** from committers.  
- **Insufficient committers** below minimum.  
- **Detected anomaly** in telemetry or selection overlap.  
- **Network partition** preventing timely commit/reveal.

### 6.2 SLAs and Actions
- **Commit phase timeout**: 24 hours. If commiters fail to commit, abort epoch and reschedule within 24 hours.  
- **Reveal phase timeout**: 24 hours. If reveals missing but minimum committers met, proceed excluding missing commits and log anomaly.  
- **Abort threshold**: if fewer than minimum committers reveal, abort epoch and reschedule within 48 hours.  
- **Emergency escalation**: if anomalyFlag true and adaptive timelock invoked, LOTUS governance must convene within **72 hours** to review.  
- **Audit SLA**: independent auditor must deliver attestation within **30 days** of request.

### 6.3 Fallback Randomness
- If commit/reveal fails and abort is not possible, use fallback deterministic seed derived from multiple recent on‑chain block hashes plus a pre‑registered fallback Node entropy set. Fallback use must be logged and audited.

---

## 7 Inclusion, Accessibility, and Legal Contingencies

### 7.1 Inclusion Rules
- Provide **alternative participation paths** for members with limited connectivity (longer commit/reveal windows, assisted submission via Node).  
- Provide **language support** and accessible training materials (audio, large text, simplified text).  
- Define **accommodation workflows** for neurodiversity and disabilities; Nodes must document accommodations in NodePolicy.

### 7.2 Small Pool and Diaspora Handling
- For small eligible pools, use stratified sampling with expanded exclusion radius or temporary cross‑node pooling to preserve randomness and fairness.

### 7.3 Legal Contingency Clause
- Nodes must publish a **Legal Response Policy** describing how they handle lawful requests (subpoenas, court orders). Policy must include: minimization steps, LOTUS notification where safe, and a requirement to seek legal counsel. Any compelled PII disclosure must be logged and reported to LOTUS governance unless legally prohibited.

---

## 8 Governance, Parameter Updates, and Pilot Plan

### 8.1 Parameter Governance
- Default parameters are pilot defaults. Changes require a documented proposal, pilot testing, and LOTUS ratification. Parameter changes are published on‑chain as a new parameter set hash.

### 8.2 Pilot Plan Summary
- **Phase 0 Spec Freeze:** publish JSON Schema and Crypto Appendix.  
- **Phase 1 Dry Run:** synthetic epochs, auditor reproduction, red‑team RNG tests.  
- **Phase 2 Pilot:** 3 Nodes, 500–2,000 participants, live commit/reveal epochs, one independent auditor. Collect metrics and adjust parameters.  
- **Phase 3 Review:** publish audit attestation hash on‑chain, update parameters via LOTUS process, prepare scale‑up.

---

## 9 Appendices

### 9.1 Example Ledger Entry
```json
{
  "publicKeyHash": "sha256:...",
  "verificationHash": "sha256:...",
  "NodeID": "node:abc123",
  "timestamp": "2026-02-26T04:45:00Z",
  "statusFlag": "active",
  "selectionProofHash": "sha256:..."
}
```

### 9.2 JSON Schema References
- **SelectionProof schema** as in Section 2.3. Implementers must publish exact JSON Schema files in the code repository prior to pilot.

### 9.3 Recommended Deliverables Before Pilot
- Exact JSON Schema for selection proofs and commit/reveal logs.  
- Cryptographic Appendix with sample code and test vectors.  
- Auditor access procedures and NDA templates.  
- Telemetry schema and anonymization implementation.  
- Red‑team test plan and schedule.

---

**Usage Note:** This file is the authoritative LOTUS RNG and parameter specification for pilot implementation. Publish the human‑readable spec and commit the spec hash to the Flow ledger. Nodes and auditors must reference this document for compliance, implementation, and audits.
