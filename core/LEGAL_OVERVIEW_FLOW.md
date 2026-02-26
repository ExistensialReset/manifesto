# ⚖️ Legal Overview Flow — Core Playbook

**Status:** Draft  
**Scope:** All Flow Nodes, Spirals, and participants  
**Purpose:** High-level overview of lawful requests, compelled disclosures, and audit/compliance flows. Emphasizes victim safety, privacy, auditable proof, and LOTUS oversight.  

---

## Foreword

This playbook provides a **structured, auditable, and legally defensible framework** for handling all lawful requests affecting Flow Node operations. It prioritizes victim safety, data minimization, and transparency where legally permissible. The document serves both as a **guideline for day-to-day operations** and as a **reference for audits, LOTUS oversight, and red-team testing**. All steps are designed to ensure consistency, reproducibility, and accountability across the network.

---

## 1. Principles & Objectives

| Principle | Description | Visual Cue |
|-----------|-------------|------------|
| **Minimization** | Disclose only the narrowest data required; limit scope aggressively | 🟢 Green |
| **Transparency** | Notify LOTUS and affected parties when lawful | 🔵 Blue |
| **Auditability** | Log every request and response; chain-of-custody and hashes required | 🟣 Purple |
| **Safety & Confidentiality** | Protect victims; avoid displacement; PII minimized | 🔴 Red |
| **Legal Review** | All decisions reviewed by counsel unless exigent | 🟠 Orange |

---

## 2. Roles & Responsibilities

- **Node Lead** — Operational decision maker, ensures playbook compliance.  
- **Legal Officer** — Reviews law, drafts responses, negotiates narrowing, advises on notifications.  
- **Compliance Officer** — Executes data retrieval, redaction, and custody logging.  
- **LOTUS Convenor** — Oversees cross-node notification and attestation.  
- **Verifier / Evidence Custodian** — Maintains custody chain for all actions.  
- **Auditor Liaison** — Manages auditor access to proofs, logs activity on-chain.

---

## 3. Intake & Initial Handling (0–24h)

- **Receipt & Log:** Assign `legalRequestId`, timestamp, authority, request type.  
- **Acknowledgement:** Neutral receipt notice; do **not** reveal specific data.  
- **Triage:** Classify as *Emergency/Exigent*, *Criminal*, *Civil*, *Administrative*, *MLAT*.  
- **Preservation Hold:** Immediate hold; record `preservationHash`.  
- **Legal Assignment:** Assign Legal Officer for review (sooner if exigent).

---

## 4. Legal Analysis & Narrowing (24–72h)

- **Jurisdiction Check:** Validate authority and scope; foreign requests → MLAT.  
- **Scope Analysis:** Map request to data schema; flag PII & sensitive fields.  
- **Minimization Strategy:** Suggest narrowed date ranges, specific reportIds, metadata-only exports.  
- **Privilege & Protection Assessment:** Identify confidentiality or safety risks; prepare protective motions if needed.  
- **Decision Record:** Legal Officer recommends; Node Lead approves or escalates.

---

## 5. Response Preparation & Redaction

- **Data Extraction:** Only approved fields; follow `exportPackage` schema.  
- **Redaction Rules:** Deterministic; hash PII; store mapping in encrypted custody record.  
- **Chain-of-Custody:** Record actor, action, timestamp, storage hash, signature.  
- **Encryption & Transfer:** Use recipient public key; log `packageHash` and `encryptionMetadata`.  
- **LOTUS Notification:** Publish on-chain attestation when lawful.

---

## 6. Emergency / Exigent Flow

- **Immediate Compliance:** Narrowest data; document rationale post-action.  
- **Post-Action Legal Review:** Document exigency, legal basis, retroactive narrowing.  
- **On-Chain Attestation:** Publish `exigentActionHash` when permitted.

---

## 7. Notification & Victim Safety

- **Timing:** Notify only when safe & lawful.  
- **Safety Measures:** Temporary protection, safe channels, confidentiality orders.  
- **Non-Displacement Principle:** Avoid forcing relocation due to disclosure.

---

## 8. High-Level Flow Diagram (Visual)

[Legal Request Received] → [Intake & Logging] → [Triage Classification] → [Legal Analysis & Narrowing] → [Compliance Extraction & Redaction] → [LOTUS Attestation / Notification] → [Audit & Follow-up]

- **Color Legend:**  
  - 🟢 Minimized / Low-Risk Actions  
  - 🟡 Medium-Risk / Escalation  
  - 🔴 High-Risk / Exigent / Safety Critical  
  - 🔵 Oversight / Audit / Governance  

---

## 9. Training & Testing

- Mandatory training for all roles.  
- Tabletop exercises and red-team scenarios quarterly.  
- LOTUS reviews playbook annually or post-incident.

---

## 10. Implementation Checklist (Pilot Ready)

- Commit playbook hash on-chain.  
- Deploy `legalRequestId` logging & preservation automation.  
- Implement `exportPackage` & `custodyRecord` schemas.  
- Establish ephemeral key issuance & auditor ACL.  
- Train Node Leads, Legal Officers, Compliance Officers, Evidence Custodians.  
- Schedule tabletop & red-team exercises.

---

> ⚠️ **Note:** All compelled disclosures must follow this playbook unless explicitly overridden by court order; document any deviations with legal basis and publish attestation hash when permitted.

---

## 11. Mermaid Flow Diagram (Color-Coded)

```mermaid
flowchart TD
    %% Top-down Legal Overview Flow
    A[🟢 Legal Request Received] --> B[🟡 Intake & Logging]
    B --> C[🟡 Triage Classification]
    C --> D[🟢 Legal Analysis & Narrowing]
    D --> E[🟢 Compliance Extraction & Redaction]
    E --> F[🔵 LOTUS Attestation / Notification]
    F --> G[🔴 Audit & Follow-up]

    %% Styling for readability
    classDef green fill:#d4f8d4,stroke:#333,stroke-width:2px,color:#000,font-size:16px,padding:15px;
    classDef yellow fill:#fff3b0,stroke:#333,stroke-width:2px,color:#000,font-size:16px,padding:15px;
    classDef red fill:#ffcccc,stroke:#333,stroke-width:2px,color:#000,font-size:16px,padding:15px;
    classDef blue fill:#cce0ff,stroke:#333,stroke-width:2px,color:#000,font-size:16px,padding:15px;

    class A,D,E green
    class B,C yellow
    class F blue
    class G red
