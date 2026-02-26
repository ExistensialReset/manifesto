# Evidence and Decision Matrix — Unforgivable Harm Protocol

**Status:** Draft  
**Scope:** All Flow Nodes, Spirals, and participants  
**Purpose:** Provide a clear, operational matrix that maps *evidence types and strength* to *decision thresholds and permitted actions* for incidents classified as unforgivable harm. The matrix supports victim‑centric response, preserves anonymity, and produces auditable proofs for LOTUS oversight.

---

## 1. Overview and Intent

This matrix translates qualitative judgments into repeatable, auditable rules so Nodes can act quickly and consistently. It defines **three evidence tiers**, the **decision authority** required at each tier, the **immediate actions permitted**, and the **documentation and audit artifacts** required to proceed. Examples illustrate typical cases.

---

## 2. Evidence Tiers (Definitions)

### Tier A — Direct Corroborated Evidence
- **What it is:** Clear, contemporaneous, and independently corroborated material evidence (e.g., timestamped CCTV footage showing assault; medical report documenting injuries with timestamp; weapon recovered and logged).  
- **Properties:** High integrity, low ambiguity, chain‑of‑custody traceable.  
- **Proof artifacts:** hashed media file; VerificationEvent with signer; chain‑of‑custody hash.

### Tier B — Corroborated Testimonial / Sensor Evidence
- **What it is:** Multiple independent attestations or sensor matches (e.g., two independent witness attestations from different NodeIDs; IoT sensor logs matching time/location; photo with validated EXIF and corroborating sensor).  
- **Properties:** Medium integrity; requires verification steps to rule out collusion.  
- **Proof artifacts:** witness attestations (signed), sensor proof hashes, media integrity report.

### Tier C — Single or Uncorroborated Report
- **What it is:** Single anonymous report, single witness without independent corroboration, or unverified media.  
- **Properties:** Low integrity; actionable only after further corroboration or immediate mitigations to protect safety.  
- **Proof artifacts:** original report hash, any submitted media hash, automated triage logs.

---

## 3. Decision Thresholds and Permitted Immediate Actions

| **Threshold** | **Evidence Requirement** | **Decision Authority** | **Immediate Permitted Actions** | **Audit Artifacts Required** |
|---|---|---|---|---|
| **Immediate Isolation / Emergency Intervention** | **Tier A** OR **Tier B + imminent risk indicators** (threat to life, ongoing violence) | Node Lead or On‑site Verifier; must notify LOTUS within 1 hour | Isolate alleged perpetrator from victim environment; call emergency services; secure scene; temporary suspension of Node privileges; temporary protective measures for victim | VerificationEvent hash; media hash; chain‑of‑custody; emergency action log |
| **Rapid Mitigation & Investigation** | **Tier B** (≥2 independent corroborations) | Node Lead with remote LOTUS notification; may request LOTUS panel if cross‑node action needed | Deploy on‑site verifier; temporary access restrictions; preserve evidence; begin formal investigation | Witness attestations; sensor hashes; VerificationEvent(s); selectionProofHash if LOTUS used |
| **Precautionary Mitigation** | **Tier C** with high priority score (e.g., location vulnerability, repeat reports) | Node Duty Officer; escalate to Node Lead within SLA | Temporary mitigations (signage, temporary barriers, increased patrols); schedule on‑site verification; offer victim support | Report hash; mitigation task record; scheduled verification event |
| **Investigatory / Monitoring** | **Tier C** without high-risk indicators | Automated triage / Node intake staff | Monitor, request additional evidence, schedule follow-up; no coercive action | Report hash; triage logs; follow-up schedule |

---

## 4. Decision Flow (Stepwise)

1. **Intake & Triage:** compute priority score and assign provisional evidence tier.  
2. **Immediate Safety Check:** if imminent danger flagged, execute *Immediate Isolation / Emergency Intervention* and notify LOTUS.  
3. **Evidence Verification:** run media integrity checks, sensor correlation, and witness validation. Update evidence tier accordingly.  
4. **Authority Check:** map updated tier to decision authority per matrix. If LOTUS panel required, publish selectionProofHash and escalate.  
5. **Action & Documentation:** perform permitted actions; record VerificationEvent(s) and publish required hashes on‑chain.  
6. **Follow-up & Audit:** schedule remediation, victim support, and independent audit as required.

---

## 5. Chain of Custody and Proof Requirements

- **Hashing:** All media, sensor logs, and attestations must be hashed (SHA‑256) at capture and stored encrypted off‑chain. Hashes are published on‑chain as verification anchors.  
- **VerificationEvent:** Every verifier signs a JSON VerificationEvent (see ANONYMOUS_VERIFICATION_WORKFLOW) and the event hash is published on‑chain.  
- **Chain-of-Custody Record:** For Tier A evidence, maintain a signed chain-of-custody record with timestamps and custody transitions; publish custody hash.  
- **Access Controls:** Full proofs released only to authorized auditors under NDA; auditor access logged and attested on‑chain.

---

## 6. Victim Support and Non-Displacement Rule

- **Victim never moves:** prioritize measures that protect the victim in place (safe room, escort, temporary barrier) rather than relocating the victim.  
- **Immediate offers:** safety planning, medical triage, trauma-informed contact, and legal guidance referrals. Record offer and acceptance as part of the audit trail.  
- **Confidentiality:** victim PII stored encrypted off‑chain; only minimal on‑chain hashes recorded.

---

## 7. Appeals, Review, and False Reporting

- **Appeal Path:** any party affected by a decision may request review; appeals are handled by a different LOTUS panel or independent auditor depending on severity.  
- **False Reporting:** verified malicious reports (demonstrably fabricated) trigger trust-score penalties and temporary suspension for non-anonymous reporters; appeals allowed.  
- **Review Cadence:** all unforgivable harm cases undergo mandatory independent audit within 30 days of closure.

---

## 8. Examples (Illustrative)

- **Example A (Tier A):** CCTV shows assault; medical report confirms injury. Action: immediate isolation, emergency services, LOTUS notified; evidence hashed and chain-of-custody recorded.  
- **Example B (Tier B):** Two independent witnesses (different NodeIDs) attest to repeated harassment; IoT door sensor logs match timestamps. Action: on-site verification, temporary access restriction, investigation opened.  
- **Example C (Tier C):** Single anonymous report alleging past abuse with no corroboration. Action: precautionary mitigation (offer support, schedule verification), monitor for corroboration.

---

## 9. Operational Responsibilities and SLAs

- **Node Lead:** authorizes rapid mitigation and ensures VerificationEvent publication. SLA: initial risk assessment within **1 hour**.  
- **On-site Verifier:** conducts physical verification and signs VerificationEvent. SLA: deploy within **4 hours** for Critical.  
- **LOTUS Convenor:** coordinates cross-node panel when escalated. SLA: convene panel within **24–48 hours** for cross-node mandates.

---

## 10. Implementation Checklist (Minimum)

- Publish this matrix in NodePolicy and commit hash on-chain.  
- Implement VerificationEvent JSON schema and hashing pipeline.  
- Implement chain-of-custody workflow and encrypted off-chain storage.  
- Train verifiers in trauma-informed procedures and evidence handling.  
- Run tabletop exercises and red-team tests for legal compulsion scenarios.

---

## 11. JSON Metadata Example

``` 
// Document metadata
{
  "document": {
    "title": "Evidence and Decision Matrix — Unforgivable Harm Protocol",
    "status": "Draft",
    "scope": "All Flow Nodes, Spirals, and participants",
    "purpose": "Map evidence types and strength to decision thresholds, permitted actions, authority, and required audit artifacts for incidents classified as unforgivable harm."
  }
}
```


```
// Evidence tiers
{
  "evidenceTiers": [
    {
      "id": "A",
      "name": "Direct Corroborated Evidence",
      "description": "Clear, contemporaneous, and independently corroborated material evidence (e.g., timestamped CCTV footage showing assault; medical report documenting injuries with timestamp; weapon recovered and logged).",
      "properties": "High integrity, low ambiguity, chain-of-custody traceable.",
      "requiredArtifacts": [
        "hashed media file",
        "VerificationEvent with signer",
        "chain-of-custody hash"
      ],
      "examples": [
        "CCTV footage with timestamp showing assault",
        "Medical report with timestamp and clinician signature confirming injuries",
        "Recovered weapon logged and photographed with custody record"
      ]
    },
    {
      "id": "B",
      "name": "Corroborated Testimonial or Sensor Evidence",
      "description": "Multiple independent attestations or sensor matches (e.g., two independent witness attestations from different NodeIDs; IoT sensor logs matching time/location; photo with validated EXIF and corroborating sensor).",
      "properties": "Medium integrity; requires verification steps to rule out collusion.",
      "requiredArtifacts": [
        "signed witness attestations",
        "sensor proof hashes",
        "media integrity report"
      ],
      "examples": [
        "Two independent witness attestations from different NodeIDs",
        "IoT door sensor logs matching reported timestamps",
        "Photo with validated EXIF plus sensor corroboration"
      ]
    },
    {
      "id": "C",
      "name": "Single or Uncorroborated Report",
      "description": "Single anonymous report, single witness without independent corroboration, or unverified media.",
      "properties": "Low integrity; actionable only after further corroboration or immediate precautionary mitigations to protect safety.",
      "requiredArtifacts": [
        "original report hash",
        "submitted media hash (if any)",
        "automated triage logs"
      ],
      "examples": [
        "Single anonymous report alleging past abuse with no corroboration",
        "Single witness statement without independent verification",
        "Unverified video or photo with no sensor match"
      ]
    }
  ]
}
```


```
// Decision matrix
{
  "decisionMatrix": [
    {
      "threshold": "Immediate Isolation / Emergency Intervention",
      "evidenceRequirement": "Tier A OR Tier B + imminent risk indicators (threat to life, ongoing violence)",
      "decisionAuthority": "Node Lead or On-site Verifier (must notify LOTUS within 1 hour)",
      "permittedImmediateActions": [
        "Isolate alleged perpetrator from victim environment",
        "Call emergency services",
        "Secure scene and preserve evidence",
        "Temporary suspension of Node privileges",
        "Temporary protective measures for victim"
      ],
      "requiredAuditArtifacts": [
        "VerificationEvent hash",
        "media hash",
        "chain-of-custody hash",
        "emergency action log"
      ]
    },
    {
      "threshold": "Rapid Mitigation & Investigation",
      "evidenceRequirement": "Tier B (≥2 independent corroborations)",
      "decisionAuthority": "Node Lead with remote LOTUS notification; may request LOTUS panel if cross-node action needed",
      "permittedImmediateActions": [
        "Deploy on-site verifier",
        "Temporary access restrictions",
        "Preserve evidence",
        "Begin formal investigation"
      ],
      "requiredAuditArtifacts": [
        "Witness attestations",
        "sensor hashes",
        "VerificationEvent(s)",
        "selectionProofHash if LOTUS used"
      ]
    },
    {
      "threshold": "Precautionary Mitigation",
      "evidenceRequirement": "Tier C with high priority score (e.g., location vulnerability, repeat reports)",
      "decisionAuthority": "Node Duty Officer; escalate to Node Lead within SLA",
      "permittedImmediateActions": [
        "Temporary mitigations (signage, temporary barriers, increased patrols)",
        "Schedule on-site verification",
        "Offer victim support"
      ],
      "requiredAuditArtifacts": [
        "Report hash",
        "mitigation task record",
        "scheduled verification event"
      ]
    },
    {
      "threshold": "Investigatory / Monitoring",
      "evidenceRequirement": "Tier C without high-risk indicators",
      "decisionAuthority": "Automated triage / Node intake staff",
      "permittedImmediateActions": [
        "Monitor and request additional evidence",
        "Schedule follow-up",
        "No coercive action"
      ],
      "requiredAuditArtifacts": [
        "Report hash",
        "triage logs",
        "follow-up schedule"
      ]
    }
  ]
}
```

