# COMPLETE_LEGAL_RESPONSE_PLAYBOOK.md


# Preface

This document, the **Complete Legal Response Playbook**, is designed to provide all Flow Nodes, Spirals, and participants with an **operationally clear, legally defensible, and auditable framework** for receiving, evaluating, and responding to lawful requests, including subpoenas, court orders, warrants, and emergency disclosure requests.

The purpose of this playbook is to balance **legal compliance** with the **maximum protection of individual safety and anonymity**. Every step is carefully defined to minimize exposure of personally identifiable information (PII), ensure traceability through **on-chain hashing and off-chain encryption**, and document all actions for **LOTUS oversight and independent audit**.

This document serves as both a **reference and training resource**: it guides consistent handling of legal requests, prepares personnel for exceptions and exigent circumstances, and supports continuous process improvement through regular exercises and red-team simulations.

The playbook is a living resource. Its effective use requires **disciplined application**, ongoing **training and exercises**, and strict adherence by each Node until an explicit court order or higher legal authority mandates deviation.

By following this guidance, Nodes ensure that **laws are upheld without compromising the safety of the individuals and groups the system is designed to protect**, and that every action is **transparent, verifiable, and defensible** under external review.

---

**Status:** Draft  
**Scope:** All Flow Nodes, Spirals, and participants  
**Purpose:** Provide an operational, auditable, and legally defensible playbook for receiving, evaluating, responding to, and documenting lawful requests for data or action (subpoenas, court orders, warrants, emergency disclosure requests). The playbook enforces data minimization, preserves victim safety and anonymity where lawful, and records every step for LOTUS oversight and independent audit.

---

### Principles and objectives
- **Minimization** — disclose the narrowest data required by law; always seek to limit scope.  
- **Transparency where lawful** — notify LOTUS governance and affected parties when permitted.  
- **Auditability** — every legal request and response is logged, hashed, and retained with chain‑of‑custody metadata.  
- **Safety and confidentiality** — prioritize victim safety and non‑displacement; avoid disclosures that create risk when legally permissible.  
- **Legal review** — all compelled disclosure decisions require legal counsel review unless exigent circumstances mandate immediate action.

---

## Roles and responsibilities
- **Node Lead** — final operational decision maker for Node responses; ensures playbook steps are executed and logs are published.  
- **Legal Officer** — performs legal analysis, drafts responses, negotiates scope narrowing, and advises on notification obligations.  
- **Compliance Officer** — extracts data, prepares redacted packages, records custody metadata, and coordinates secure transfer.  
- **LOTUS Convenor** — receives on‑chain attestation and coordinates cross‑node notification when required.  
- **Evidence Custodian** — maintains chain‑of‑custody for physical/digital evidence and signs custody transitions.  
- **Auditor Liaison** — manages auditor access to encrypted proofs under NDA and logs auditor activity.

---

## Intake and initial handling (first 24 hours)
1. **Receipt and logging** — immediately log the request in the Node Legal Log with timestamp, requesting authority, jurisdiction, request type, and contact details. Generate `legalRequestId` (UUID).  
2. **Acknowledge receipt** — send a brief, neutral acknowledgement to the requesting authority confirming receipt and providing `legalRequestId`. Do not admit possession of specific data beyond the acknowledgement.  
3. **Triage** — Compliance Officer classifies the request as *Emergency/Exigent*, *Criminal subpoena/warrant*, *Civil discovery*, *Administrative order*, or *Mutual legal assistance*. Record classification.  
4. **Preservation hold** — place an immediate preservation hold on all potentially responsive data and evidence; record `preservationHash`.  
5. **Legal review assignment** — assign Legal Officer within **24 hours** for full legal analysis (sooner for exigent requests).

---

## Legal analysis and narrowing (24–72 hours)
- **Jurisdiction check** — confirm the issuing authority has legal power over the Node or data; if foreign, evaluate MLAT or mutual assistance route.  
- **Scope analysis** — map requested items to internal data schema; identify PII, victim‑sensitive fields, and verification artifacts.  
- **Minimization strategy** — propose narrowed scope alternatives (date ranges, specific reportIds, hashed identifiers, metadata only) and record as `narrowingProposal`.  
- **Privilege and protection assessment** — evaluate claims of privilege, confidentiality, or safety risk (e.g., victim safety, ongoing investigations). If concerns exist, prepare a protective motion or request sealed handling.  
- **Decision record** — Legal Officer records recommended response path and required redactions; Node Lead approves or escalates to LOTUS Convenor if cross‑node or policy conflict.

---

## Response preparation and redaction (per court timeline)
- **Data extraction** — Compliance Officer extracts only the fields approved by Legal Officer using the `ExportPackage` format.  
- **Redaction rules** — redact PII not required by the order; replace with deterministic hashed placeholders (SHA‑256) and include mapping only in encrypted custody records. Redaction must be deterministic and reproducible.  
- **Chain‑of‑custody record** — create `custodyRecord` entries with `actor`, `action`, `timestamp`, `storageLocationHash`, `transferReason`, and `signature`. Sign with Evidence Custodian key.  
- **Encryption and packaging** — encrypt package with recipient public key when available; otherwise use secure courier with signed custody transfer. Record `packageHash` and `encryptionMetadata`.  
- **LOTUS notification** — if permitted, publish an on‑chain attestation hash referencing `legalRequestId` and `packageHash`. If notification is prohibited by law, record the legal basis for nondisclosure in the Node Legal Log.

---

## Emergency / exigent requests
- **Immediate action allowed** — if a lawful exigent request (imminent threat to life or safety) is presented, Compliance Officer may comply immediately with the narrowest data necessary.  
- **Post‑action legal review** — within **24 hours** of compliance, Legal Officer must document the exigency, legal basis, and produce a retroactive narrowing justification.  
- **On‑chain attestation** — publish `exigentActionHash` with a redacted summary when permitted.

---

## Notification and victim safety
- **Notification timing** — notify affected parties of compelled disclosure only when not prohibited by law and when notification does not increase risk. Legal Officer advises on timing.  
- **Victim safety measures** — if disclosure could endanger a victim, implement protective measures (temporary relocation, safe contact channels, confidentiality orders) before or concurrent with notification. Document offers of support and acceptance in the audit trail.  
- **Non‑displacement principle** — avoid actions that force victims to relocate solely because of disclosure; seek alternatives that protect safety.

---

## Data packaging format and technical schema

### ExportPackage (JSON envelope)
```json
{
  "packageId": "uuid",
  "legalRequestId": "uuid",
  "packageHash": "sha256:...",
  "exportedFields": ["reportId","verificationHash","timestamp","status"],
  "records": [
    {
      "reportId": "uuid",
      "verificationHash": "sha256:...",
      "timestamp": "ISO8601",
      "redactedFields": ["reporterName"],
      "fieldHashes": {"reporterName":"sha256:..."}
    }
  ],
  "custodyRecordHash": "sha256:...",
  "encryptionMetadata": {"algorithm":"RSA-OAEP-256","recipient":"authority@example.gov"},
  "preparedBy": "node:abc-compliance",
  "preparedAt": "ISO8601"
}
```

### ChainOfCustody (JSON schema)
```json
{
  "custodyChainHash": "sha256:...",
  "entries": [
    {
      "entryId": "uuid",
      "actor": "node:abc-custodian",
      "action": "captured|transferred|encrypted|released",
      "timestamp": "ISO8601",
      "storageLocationHash": "sha256:...",
      "transferReason": "legalRequest|audit|investigation",
      "signature": "hex"
    }
  ]
}
```

### VerificationEvent (JSON schema)
```json
{
  "eventId": "uuid",
  "reportId": "uuid",
  "verifierNode": "node:abc",
  "timestamp": "ISO8601",
  "method": "sensor|media|witness|on-site|remote",
  "outcome": "confirmed|not_confirmed|inconclusive",
  "evidenceHashes": ["sha256:..."],
  "custodyChainHash": "sha256:...",
  "signature": "hex"
}
```

All hashes are published on‑chain as verification anchors; full encrypted packages are retained off‑chain.

---

## Communication templates

**Acknowledgement to requesting authority**
```
Subject: Acknowledgement of Legal Request [legalRequestId]

We acknowledge receipt of your request dated [date], reference [requestRef]. The request has been logged as [legalRequestId]. We are conducting legal review and will respond in accordance with applicable law and the timelines set by the issuing authority.

Node Legal Team
```

**Subpoena narrowing proposal**
```
Subject: Request to Narrow Scope — [legalRequestId]

We request clarification and narrowing of the scope of your request to the following limited items: [list specific fields, date ranges, reportIds]. Narrowing will reduce privacy impact and expedite compliance. Please confirm acceptance by [date/time].

Node Legal Officer
```

**Notification to affected party (when permitted)**
```
Subject: Notice of Legal Request Affecting Your Report [reportId]

You are receiving this notice because a lawful request was made that may include data related to your report [reportId]. We are required to comply with lawful requests; we have taken steps to minimize disclosure and protect your safety. If you believe this notice places you at risk, contact [Node support contact] immediately for assistance.

Node Support Team
```

---

## Protection against misuse and exception handling
- **Always request minimization** — propose narrowed scope whenever possible.  
- **Protective orders** — seek sealed handling when disclosure risks safety or confidentiality.  
- **Logging of compulsion** — every compulsion order is logged with legal rationale; if notification is prohibited, document the legal basis.  
- **Redaction mapping** — stored encrypted; only verification hashes are published on‑chain.

---

## Retention, redaction, and deletion
- **Legal Log retention** — raw legal logs retained **12 months**.  
- **Salt retention** — salts used for hashing ephemeral identifiers retained by default **90 days** unless legal proceedings require longer retention.  
- **Deletion** — when retention periods expire, securely delete raw data and publish a deletion attestation hash.

---

## Auditor access and on‑chain attestation
- **Auditor access** — auditors receive encrypted proof packages under NDA and ephemeral keys; each access is logged and attested on‑chain.  
- **On‑chain attestation** — publish minimal metadata only: `legalRequestId`, `packageHash`, `attestationHash`, timestamp, and Node identifier. Do not publish PII.  
- **Audit cadence** — quarterly automated scans and annual independent audits; auditors publish attestation hashes on‑chain.

---

## Training, testing, and governance
- **Mandatory training** — Node staff handling legal requests must complete legal response, data minimization, and trauma‑informed training.  
- **Tabletop exercises** — run at least two tabletop exercises before pilot and quarterly thereafter, including a legal compulsion/red‑team scenario.  
- **Governance review** — LOTUS governance reviews the playbook annually or after any major legal incident.

---

## Example workflows (concise)
- **Non‑exigent subpoena for metadata** — log request → legal review → propose metadata‑only narrowing → extract → redact → encrypt → deliver → publish `packageHash` on‑chain.  
- **Exigent emergency disclosure** — confirm exigency → extract minimal fields (location, immediate threat indicators) → deliver to authority → document exigency → publish `exigentActionHash` when permitted.

---

## Implementation checklist (ready for pilot)
- Publish this playbook and commit the spec hash on‑chain.  
- Implement `legalRequestId` logging and preservation hold automation.  
- Deploy `ExportPackage`, `ChainOfCustody`, and `VerificationEvent` JSON schemas and signing keys.  
- Establish ephemeral key issuance and auditor ACL procedures.  
- Approve subpoena templates and narrowing request templates.  
- Train Node Leads, Legal Officers, Compliance Officers, and Evidence Custodians.  
- Schedule tabletop and red‑team exercises.

---

All compelled disclosures must follow this playbook unless a court order explicitly overrides procedural steps; in such cases, document the legal basis and the deviation in the Node Legal Log and publish the attestation hash when permitted.

---

