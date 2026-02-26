# FLOW_ID_v3.md

**Status:** DRAFT  
**Scope:** Global Node Protocol  
**Primary Placement:** `/core/FLOW_ID.md`  
**Purpose:** Define FLOW_ID_v3, a decentralized, privacy-preserving identity protocol that guarantees **one human = one ID**, fully compatible with Flow principles, governance via LOTUS Protocol, and post-monetary operation.

---

## 1. Overview and Goals

**Purpose:** Provide a robust, decentralized identity system for Flow, with **privacy, security, and auditability** without reliance on banks or state authorities.  

**Core guarantees:**  
- Uniqueness: one human ↔ one ID  
- Physical binding: initial verification is face-to-face  
- Cryptographic control: private keys held locally, never shared  
- Recoverability: social recovery (k-of-n) without exposing PII  
- Auditability: anonymized logs for system health checks  
- Resistance: Sybil attacks, collusion, and coordinated fraud  

**Design principles:**  
- Physical verification at Nodes  
- Local private key ownership  
- Randomized social verification  
- Minimal ledger metadata  
- Non-coercion  
- Post-monetary compatibility  
- Optional rotation of keys for security and emergency recovery  

---

## 2. Terminology and Core Components

- **Node:** physical location or verifier group authorized to perform initial verification.  
- **Verifier:** previously verified member authorized to sign verification events.  
- **FLOW_ID record:** ledger entry with public key hash, verification hash, NodeID, timestamp, and status flag; contains no PII.  
- **Verification event:** cryptographically signed attestations by verifiers after physical check.  
- **Recovery Set:** randomly selected verified members (standard 5); k-of-n signatures required (3/5) for recovery or rotation.  
- **Node Policy:** local, published rules defining ID types, verification steps, verifier training, and incident response.

---

## 3. Protocol Flow and Operational Procedures

### 3.1 Initial Registration
1. **Session initiation:** Applicant requests registration at a Node; Node issues ephemeral session token.  
2. **Physical check:** Three randomly selected verifiers at Node perform face-to-face validation against Node Policy. Verification is signed cryptographically.  
3. **Key generation:** Private key generated locally (hardware wallet / secure enclave recommended). Node never receives private key. Air-gapped methods (QR, USB) used if needed.  
4. **Ledger publication:** Individual publishes public key + anonymized verification hash to Flow ledger. Verifier signatures + NodeID stored as hashes.  
5. **Recovery set selection:** Randomly selects 5 verified members across Nodes. Applicant consents.  

> **Note:** Training can occur **after initial lottery selection** to reduce bias and manipulation risk; completion timestamped within 48h.  

---

### 3.2 Normal Operation
- All Flow actions signed by private key.  
- Ledger validates public key is active and unflagged.  
- Nodes perform audits to detect anomalies in usage patterns without exposing PII.

---

### 3.3 Recovery and Key Rotation
- **Trigger:** User reports loss or requests rotation.  
- **Process:** k-of-n (3/5) recovery signatures produce on-ledger recovery transaction with **timelock 72h**.  
- **Safeguards:** Veto window for original keyholder; multi-channel confirmations for verifiers; full audit trail of attempts.  

---

## 4. Threat Model and Mitigations

**Primary threats:** Node infiltration, coordinated Sybil attacks, social engineering, coercion, key extraction.  

**Mitigations:**  
- **Cross-node randomization:** Verifiers for initial checks and recovery drawn from global pool.  
- **Rate limits & quorum constraints:** Nodes cannot perform unlimited verifications without cross-node attestations.  
- **Behavioral anomaly detection:** Monitor anonymized metadata for suspicious patterns.  
- **Multi-channel verifier confirmation:** Require physical + app or token confirmation.  
- **Timelocks and alerts:** Recovery transactions include delays + public anonymous alerts.  
- **Device security guidance:** Hardware wallets or secure enclaves, open-source tooling, clear user education.  
- **Auditability without PII:** Ledger exports enable verification of system health and distribution without exposing identities.  

---

## 5. Node Governance, Compliance, and Privacy

### 5.1 Node Requirements
- Publish Node Policy: accepted ID types, verification steps, training, incident response, retention rules.  
- Maintain minimal local notes; support annual deletion requests except cryptographic proofs needed for ongoing validity.  

### 5.2 Audits and Dispute Resolution
- Annual independent audits of anonymized ledger exports.  
- Local dispute panels randomly drawn from verified members handle suspected infiltration or contested verification.  

### 5.3 Privacy Guarantees
- Ledger stores **only hashes, NodeIDs, timestamps, status flags**.  
- Verification hashes are one-way; correlation requires Node + local data.  
- Export formats support counts and timelines without exposing personal data.  

---

## 6. Implementation Roadmap and Next Steps

### 6.1 Pilot (6 months)
- Deploy 3 pilot Nodes in diverse regions; 500–2,000 participants.  
- Run red-team simulations, recovery drills, usability testing.  
- Metrics: verification latency, false positives, recovery success rate, flagged anomalies.  

### 6.2 Technical Deliverables
- Client SDK: key generation, signing, recovery, UI patterns.  
- Reference hardware workflow & open documentation for key custody.  
- Ledger schema (JSON-LD), multisig recovery transactions (k-of-n, timelock).  

### 6.3 Governance Deliverables
- Node Policy template, verifier training curriculum, audit checklist.  
- Non-monetary incentives; strict prohibition on paid verification.  

### 6.4 Migration
- Re-attestation path for existing FLOW_ID holders: short physical re-check + signature with legacy key, or limited grandfathering until re-attested.  

### 6.5 Validation
- Independent security review and privacy impact assessment before full rollout.  

---

## 7. Additional Enhancements (from v2 → v3)
- UX simplification: clear instructions, recovery illustrations, post-selection training timestamped.  
- RNG & verifier selection compliant with `/core/RNG_AND_LOG_SPEC.md` for unmanipulable random selection.  
- Node Policy standardization: minimal cross-node standards to ensure fairness.  
- Offline / P2P ledger replication: consensus model specified to avoid split-brain scenarios.  
- Hardware loss fallback: temporary social recovery lock before permanent reset.  

---

## 8. References
- LOTUS Protocol: `/core/LOTUS_Protocol.md`  
- Harm Boundaries Protocol: `/ethos/THE_HARM_BOUNDARY_PROTOCOL.md`  
- RNG & Log Spec: `/core/RNG_AND_LOG_SPEC.md`  

---
