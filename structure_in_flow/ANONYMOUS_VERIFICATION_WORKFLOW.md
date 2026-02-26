### ANONYMOUS_VERIFICATION_WORKFLOW.md

**Status:** Draft  
**Scope:** Flow Universal Reporting Protocol; Node verification and corroboration for anonymous reports  
**Purpose:** Define a stepwise, auditable, privacy‑preserving workflow that lets Nodes verify anonymous reports reliably, escalate high‑risk cases quickly, and produce cryptographic proofs for auditors without exposing reporter PII.

---

### 1. Goals and design constraints
- **Goal:** Turn anonymous signals into actionable, verifiable items while preserving reporter anonymity and minimizing false positives.  
- **Constraints:** No PII on‑chain; all verification steps logged as hashes; minimal on‑device exposure; timeliness consistent with SLA tiers.

---

### 2. Definitions and primitives
- **Report** — the submitted item (schema per Report JSON).  
- **CorroborationCount** — integer tally of independent evidence items (sensor, witness, media, verifier).  
- **Verification Event** — signed, local Node record that attests to a physical or digital check; stored encrypted off‑chain and referenced on‑chain by hash.  
- **Actionable Threshold** — default **CorroborationCount ≥ 2** or priority score ≥ 15 triggers operational action.  
- **Audit Proof** — JSON object containing commit/reveal proof hashes, verification event hashes, and selectionProofHash when LOTUS panels are used.

---

### 3. Stepwise anonymous verification workflow

1. **Automated intake and initial scoring**  
   - System computes priority score from severity, location, and initial corroboration.  
   - If score < 8, mark as *investigatory* and schedule passive follow‑up; otherwise proceed to active verification.

2. **Sensor and data corroboration (automated)**  
   - Query IoT sensors, public CCTV metadata, environmental sensors, and prior reports at same location.  
   - If a sensor match exists, increment **CorroborationCount** and attach sensor proof hash to report.

3. **Media request and automated integrity checks**  
   - Prompt anonymous reporter (optional) to upload photo/video; accept but do not require.  
   - Run automated checks: EXIF timestamp consistency, hash stability, basic image‑forensics flags.  
   - If media passes integrity checks, increment **CorroborationCount** and store media hash.

4. **Witness attestation step**  
   - Offer a lightweight witness attestation flow: two independent witnesses (different NodeIDs) submit short signed attestations (template below).  
   - Each valid witness adds +3 to **CorroborationCount**.

5. **Remote verifier triage**  
   - If CorroborationCount ≥ 2, assign remote verifier to confirm via phone/app prompts or coordinate with local Node staff for on‑site check.  
   - Verifier records a **Verification Event**: signed statement, timestamp, and hashed summary stored on‑chain as verificationHash.

6. **On‑site verification (if required)**  
   - For high‑risk or urgent items (score ≥ 15), dispatch on‑site verifier immediately.  
   - On‑site verifier follows safety protocols, documents findings, signs Verification Event, and uploads encrypted evidence to Node storage.

7. **Decision and action**  
   - If Verification Event confirms issue, mark report actionable and create remediation task with SLA.  
   - If insufficient corroboration, mark as investigatory and schedule follow‑up; do not discard without at least one passive recheck window.

8. **Escalation to LOTUS**  
   - If Node cannot meet SLA or issue requires cross‑node resources, trigger LOTUS lottery assignment. Include selectionProofHash and verification event hashes in the escalation packet.

---

### 4. Verifier templates and messages

- **Witness attestation template (short)**  
  - *I, [VerifierNodeID], attest that on [ISO8601 timestamp] I observed [short description]. I confirm this statement is true to the best of my knowledge.* — signed, hashed.

- **Verification Event structure (JSON)**  
```json
{
  "eventId":"uuid",
  "reportId":"uuid",
  "verifierNode":"node:abc",
  "timestamp":"ISO8601",
  "method":"sensor|media|witness|on-site|remote",
  "outcome":"confirmed|not_confirmed|inconclusive",
  "evidenceHashes":["sha256:..."],
  "signature":"hex"
}
```

---

### 5. Privacy, logging and audit proofs
- **On‑chain**: only store `reportId`, `verificationHash` (sha256 of Verification Event), `timestamp`, and `statusFlag`.  
- **Off‑chain encrypted logs**: full Verification Event and evidence stored encrypted; auditors access via ephemeral keys after LOTUS approval.  
- **Audit proof object**: includes selectionProofHash (if LOTUS used), list of verificationHash values, and a signed Node attestation. Auditors verify hashes reproduce the off‑chain content.

---

### 6. Timelines and SLAs within workflow
- **Automated intake & sensor check:** immediate (minutes).  
- **Media integrity check:** within 1 hour.  
- **Witness attestation window:** 48 hours recommended.  
- **Remote verifier triage:** ack within SLA tier (Critical 4h, High 24h).  
- **On‑site verification:** deploy within 24h for Critical; within 7 days for High.

---

### 7. Anti‑abuse and quality controls
- **Rate limits:** per reporterHash and per phone number; anonymous flows limited to X submissions/day (pilot configurable).  
- **Spam detection:** ML + rule filters route suspicious reports to moderation queue.  
- **Verifier rotation:** no single verifier may perform >20 verifications/month without cross‑node attest.  
- **Dispute path:** if reporter (attributed) disputes outcome, Node opens review and may escalate to LOTUS panel.

---

### 8. Edge cases and fallback rules
- **No corroboration but high risk claim:** treat as urgent investigatory; deploy temporary mitigations (signage, temporary barrier) while verification proceeds.  
- **Sensor mismatch but multiple independent anonymous reports:** increase priority and request witness attestations.  
- **Connectivity constraints:** allow Node staff to assist filing and to perform offline evidence capture; staff must not attach PII on‑chain.

---

### 9. Implementation checklist for Nodes
- Implement witness attestation UI and signer flow.  
- Implement media integrity checks and evidence hashing pipeline.  
- Implement encrypted off‑chain storage with auditor access controls.  
- Add Verification Event signer and on‑chain verificationHash publication.  
- Configure SLAs and automated triage thresholds per pilot parameters.

---
