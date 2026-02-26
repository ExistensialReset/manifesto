### FLOW_LOTTERY_PARAMETERS_AND_RNG_SPEC.md (Visual Edition)

**Status:** Draft  
**Scope:** LOTUS Protocol, Global Node Governance  
**Purpose:** Complete, auditable, operational specification for LOTUS lottery parameters, RNG and selection proofs, auditor procedures, telemetry and anomaly detection, cryptographic requirements, failure SLAs, inclusion and legal rules. Authoritative reference for pilot and audits.

---

### 1 Parameters Appendix

**Default pilot parameters — adjust after pilot via LOTUS governance.**

| **Parameter** | **Default Value** | **Rationale / Visual Cue** |
|---|---:|---|
| **Mandate duration** | **9 months** | ⏳ Continuity + rotation balance |
| **Max mandates per person per year** | **2** | ⚠️ Avoid burnout & capture |
| **Max concurrent mandates per Node** | **3** | ⚠️ Limits local power concentration |
| **Verifier monthly limit per Node** | **20 verifications** | 📊 Triggers cross‑node attest, reduce capture risk |
| **Cross‑node attest threshold** | **≥2 external Node attestations** | 🔒 External validation before full activation |
| **Default recovery timelock** | **72 hours** | ⏳ Community veto & visibility |
| **Max timelock extension** | **14 days adaptive** | ⚠️ High‑risk anomalies; justification required |
| **Selection exclusion radius** | **Immediate Node + household + 1st‑degree relations** | ⚠️ Avoid conflicts of interest |
| **Training window** | **48 hours after selection** | 🏫 Ensure panel readiness |
| **Training duration** | **30–60 minutes** | 🏫 Trauma‑informed, confidentiality, conflict rules |
| **Audit cadence** | **Quarterly anomaly scan; annual independent audit** | 🔍 Operational monitoring & deep review |
| **RNG commit‑reveal window** | **Commit 24h; Reveal 24h** | ⏳ Prevent last‑minute manipulation |
| **Minimum committers per epoch** | **3 geographically distributed Nodes** | 🌍 Resilience, anti‑manipulation |
| **Anomaly trigger thresholds** | **e.g., >3× expected verifications in 7 days; repeated selection overlap >2σ** | ⚠️ Manual review flag |

> **Tip:** Color‑coded cells or icons help operators scan critical vs informational parameters quickly.

---

### 2 RNG and Selection Proof Specification

#### 2.1 Goals
- **Verifiable, unbiased randomness** for all LOTUS selections.  
- **Minimal on‑chain footprint** while enabling full off‑chain proofs for auditors.  
- **Clear failure modes and fallback rules.**

#### 2.2 High Level Flow

1. **Epoch start:** publish immutable on‑chain seed (block hash or dedicated seed tx).  
2. **Commit phase:** Nodes publish commits: `commit = H(nodeID || epoch || nonce || nodeEntropy)`.  
3. **Reveal phase:** Nodes reveal `nodeEntropy`; verify `H(nodeID || epoch || nonce || reveal) == commit`.  
4. **Combine randomness:** `finalRandomness = H(onChainSeed || commit1 || commit2 || ... || commitN || epochNonce)`. Use HKDF for multiple outputs.  
5. **Deterministic selection:** HMAC‑DRBG (SHA‑256) seeded with `finalRandomness` to sample without replacement.  
6. **Publish proofs:** minimal hashes on‑chain: `epoch | onChainSeedHash | commitListHash | selectionProofHash | timestamp`.

> **Visual:** Flowchart style steps help operators and auditors track RNG and selection lifecycle.

#### 2.3 Selection Proof Object

**Compact JSON proof per epoch.** Store only hashes on‑chain; full proof available to authorized auditors.

**Key fields checklist**
- `epoch`  
- `onChainSeedHash` ✅  
- `commitListHash` ✅  
- `revealListHash` ✅  
- `selectionProofHash` ✅  
- `selectionAlgorithm` (HMAC‑DRBG‑SHA256) ✅  
- `selectionParameters` (pool size, sample size, exclusion filters) ✅  
- `commitList` / `revealList` ✅  
- `selectionOrder` ✅  
- `aggregateSignature` ✅

**Concise SelectionProof JSON example**
```json
{
  "epoch": "string",
  "onChainSeedHash": "hex",
  "commitListHash": "hex",
  "revealListHash": "hex",
  "selectionProofHash": "hex",
  "selectionAlgorithm": "HMAC-DRBG-SHA256",
  "selectionParameters": {
    "poolSize": 1000,
    "sampleSize": 50,
    "exclusionFilters": "Immediate Node + household"
  },
  "commitList": [
    {"nodeID": "node:abc", "nonce": "n1", "commit": "hex"}
  ],
  "revealList": [
    {"nodeID": "node:abc", "nonce": "n1", "reveal": "hex"}
  ],
  "selectionOrder": ["memberHash1","memberHash2"],
  "aggregateSignature": "hex"
}
```

**On‑chain minimal fields:** `epoch | onChainSeedHash | commitListHash | selectionProofHash | timestamp`.

#### 2.4 Anti‑Manipulation Measures
- Enforce commit‑reveal windows with timeouts.  
- Require minimum committers; abort and reschedule if threshold not met.  
- Enforce geographic distribution for committers.  
- Publish proof hashes on‑chain immediately to prevent retroactive tampering.  
- Mandate red‑team testing pre‑pilot and annually.

---

### 3 Cryptographic Appendix

#### 3.1 Algorithms and Encodings
- **Hash:** SHA‑256 (hex lowercase).  
- **DRBG:** HMAC‑DRBG with SHA‑256.  
- **Signature key types:** Ed25519 recommended.  
- **Aggregate signatures:** BLS12‑381 optional for compact aggregation; fallback to MuSig2 or deterministic multisig if BLS not available.  
- **Multisig recovery tx:** explicit `k‑of‑n`, timelock, and proof fields.  
- **Encoding:** JSON UTF‑8; hex for binary fields.

#### 3.2 Example Verification Commands
- **Verify commit:** `sha256(nodeID || epoch || nonce || reveal) == commit`.  
- **Recompute randomness:** `sha256(onChainSeed || commit1 || ... || commitN || epochNonce)`.  
- **Reproduce selection:** use HMAC‑DRBG seeded with `finalRandomness`.

---

### 4 Auditor Checklist and Access Model

#### 4.1 Roles
- **Independent Auditor:** full proofs under NDA.  
- **Public Auditor:** verify on‑chain hashes only.

#### 4.2 Access Model
- **Minimal on‑chain exposure:** only hashes published publicly.  
- **Full proofs:** encrypted delivery to authorized auditors via ephemeral keys; access logged and attested on‑chain.  
- **Audit request flow:** auditor → LOTUS approval → Node provides encrypted proof → auditor verifies → publishes attestation hash.

#### 4.3 Step by Step Checklist
1. Retrieve on‑chain `onChainSeedHash`, `commitListHash`, `selectionProofHash`.  
2. Request full commit/reveal logs from Nodes (encrypted).  
3. Verify each commit matches its reveal.  
4. Recompute `finalRandomness`.  
5. Reproduce selection and compare with `selectionProofHash`.  
6. Verify aggregate signature.  
7. Check anomaly telemetry and thresholds.  
8. Confirm cross‑node attest thresholds and timelock adherence.  
9. Publish anonymized attestation hash on‑chain.

> **Checklist format:** auditors can tick steps to confirm compliance and produce a concise attestation.

---

### 5 Telemetry and Anomaly Detection

#### 5.1 Telemetry Fields (anonymized)
- `nodeIDHash` — SHA‑256 of NodeID salted per epoch.  
- `epoch` — selection epoch.  
- `verificationsCount` — number of verifications by Node in window.  
- `selectionOverlapCount` — repeated selections per member across epochs.  
- `commitLatencyMs` — median commit latency.  
- `revealLatencyMs` — median reveal latency.  
- `failedReveals` — count.  
- `anomalyFlag` — boolean.

#### 5.2 Anonymization Rules
- Hash Node identifiers with a per‑epoch salt before storage; salt ephemeral.  
- Store aggregates only; raw identifiers never published.  
- Retain raw telemetry **12 months**; anonymized aggregates retained indefinitely.

#### 5.3 Anomaly Detection Rules
- **Trigger A:** `verificationsCount` > 3× expected in 7 days → flag.  
- **Trigger B:** `selectionOverlapCount` > 2σ above mean → flag.  
- **Trigger C:** `failedReveals` > 1 for minimum committers → abort epoch.  
- Flagged events trigger adaptive timelock and escalation to LOTUS governance.

---

### 6 Failure Modes, SLAs and Fallback Rules

#### 6.1 Failure Modes
- Missing reveals from committers.  
- Insufficient committers below minimum.  
- Telemetry anomalies or selection overlap.  
- Network partitions preventing timely commit/reveal.

#### 6.2 SLAs and Actions
- **Commit phase timeout:** 24 hours → abort epoch and reschedule within 24 hours.  
- **Reveal phase timeout:** 24 hours → if minimum committers met, proceed excluding missing commits and log anomaly.  
- **Abort threshold:** fewer than minimum committers reveal → abort and reschedule within 48 hours.  
- **Emergency escalation:** anomalyFlag true → LOTUS governance convenes within **72 hours**.  
- **Audit SLA:** independent auditor delivers attestation within **30 days** of request.

#### 6.3 Fallback Randomness
- If commit/reveal fails and abort is not possible, derive fallback seed from multiple recent on‑chain block hashes plus pre‑registered fallback Node entropy. Fallback use must be logged and audited.

---

### 7 Inclusion, Accessibility and Legal Contingencies

#### 7.1 Inclusion Rules
- Provide alternative participation paths for limited connectivity (longer windows, assisted submission via Node).  
- Provide language support and accessible training materials (audio, large text, simplified text).  
- Define accommodation workflows for neurodiversity and disabilities; Nodes document accommodations in NodePolicy.

#### 7.2 Small Pool and Diaspora Handling
- For small eligible pools, use stratified sampling with expanded exclusion radius or temporary cross‑node pooling to preserve randomness and fairness.

#### 7.3 Legal Contingency Clause
- Nodes must publish a **Legal Response Policy** describing handling of lawful requests (subpoenas, court orders). Policy must include minimization steps, LOTUS notification where safe, and requirement to seek legal counsel. Any compelled PII disclosure must be logged and reported to LOTUS governance unless legally prohibited.

---

### 8 Governance, Parameter Updates and Pilot Plan

#### 8.1 Parameter Governance
- Default parameters are pilot defaults. Changes require documented proposal, pilot testing, and LOTUS ratification. Parameter changes published on‑chain as a new parameter set hash.

#### 8.2 Pilot Plan Summary
- **Phase 0 Spec Freeze:** publish JSON Schema and Crypto Appendix.  
- **Phase 1 Dry Run:** synthetic epochs, auditor reproduction, red‑team RNG tests.  
- **Phase 2 Pilot:** 3 Nodes, 500–2,000 participants, live commit/reveal epochs, one independent auditor. Collect metrics and adjust parameters.  
- **Phase 3 Review:** publish audit attestation hash on‑chain, update parameters via LOTUS process, prepare scale‑up.

---

### 9 Appendices

#### 9.1 Example Ledger Entry
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

#### 9.2 JSON Schema References
- SelectionProof schema as in Section 2.3. Exact JSON Schema files must be published prior to pilot.

#### 9.3 Recommended Deliverables Before Pilot
- Exact JSON Schema for selection proofs and commit/reveal logs.  
- Cryptographic Appendix with sample code and test vectors.  
- Auditor access procedures and NDA templates.  
- Telemetry schema and anonymization implementation.  
- Red‑team test plan and schedule.

---

**Usage Note:** This document is the authoritative LOTUS RNG and parameter specification for pilot implementation. Publish the human‑readable spec and commit the spec hash to the Flow ledger. Nodes and auditors must reference this file for compliance and audits.
