# Legal Response Protocol — Overview
**Quick Summary of Flow Node Legal Requests**

---

## Purpose and Scope
- Handle subpoenas, court orders, warrants, emergencies, admin requests, MLATs
- Audience: Node Operators, Legal Officers, Evidence Custodians
- Core Goal: Balance legal compliance with maximum protection of individual safety and anonymity

---

## Guiding Principles
1. **Minimization First** ✂️ – disclose only what's legally required
2. **Transparency Where Lawful** 🪞 – notify affected parties and LOTUS governance if permitted
3. **Complete Auditability** 📊 – log, hash, and retain every request and response
4. **Safety & Confidentiality Priority** 🛡️ – protect victims, reporters, vulnerable individuals
5. **Professional Legal Review** ⚖️ – all compelled disclosures reviewed by Legal Officer unless exigent

# Legal Response Team — Roles & Responsibilities

---

## Node Lead
**Responsibility:** Final decision maker  
- Ensure playbook steps executed correctly
- Approve final disclosure packages
- Publish audit logs to LOTUS
- Escalate to LOTUS Convenor if needed

## Legal Officer
**Responsibility:** Legal analysis & strategy  
- Verify jurisdiction & authority
- Draft formal responses
- Negotiate scope narrowing
- Advise on notification
- Determine privilege claims
- Prepare protective motions

## Compliance Officer
**Responsibility:** Data handling & package preparation  
- Extract requested data
- Redact per legal guidance
- Record custody metadata
- Coordinate secure transfer
- Maintain preservation holds

## LOTUS Convenor
**Responsibility:** Cross-node governance  
- On-chain attestation
- Coordinate notifications across nodes
- Governance oversight
- Inter-node legal support

## Evidence Custodian
**Responsibility:** Evidence integrity  
- Maintain chain-of-custody
- Sign custody transitions
- Manage secure storage
- Provide evidence for legal proceedings

## Auditor Liaison
**Responsibility:** External audit coordination  
- Manage auditor access under NDA
- Provide encrypted packages
- Log auditor activity
- Coordinate quarterly/annual audits

# Legal Request Intake — First 24 Hours

---

## Step 1: Receipt & Logging
- Create Node Legal Log entry
- Assign unique `legalRequestId` (UUID)
- Scan & store original request securely
- Log timestamp, authority, type, contact, deadline

**Example JSON:**
```json
{
  "legalRequestId": "uuid-here",
  "receivedAt": "2026-02-26T14:30:00Z",
  "requestingAuthority": "City District Court",
  "jurisdiction": "Sweden/Stockholm",
  "requestType": "subpoena",
  "contactInfo": "prosecutor@district-court.se",
  "deadline": "2026-03-12T23:59:59Z",
  "receivedBy": "compliance-officer-alice"
}
```

Step 2: Acknowledgment
Send neutral acknowledgment within 24h
Do not confirm possession of specific data
Template:

Subject: Acknowledgement of Legal Request [legalRequestId]

Dear [Requesting Authority],

We acknowledge receipt of your [request type] dated [date], 
reference number [their reference].

The request has been logged in our system as: [legalRequestId]

We are conducting the necessary legal review and will respond 
in accordance with applicable law and the timelines specified 
in your request.

Point of contact: [Legal Officer name and email]

[Node Name] Legal Team

---

# Legal Analysis Phase (24–72 Hours)

---

## Jurisdiction Verification
- Confirm authority & geographic jurisdiction
- Verify foreign requests via MLATs/treaties
- Flag questionable jurisdiction for review

## Scope Analysis
- Map requested items to internal data
- Identify PII, victim-sensitive fields, verification artifacts
- Determine what metadata vs content is needed

## Minimization Strategy
- Limit time range
- Limit fields (only IDs, timestamps, hashes)
- Propose anonymization
- Separate metadata from content

**Example JSON:**
```json
{
  "narrowingProposalId": "uuid",
  "legalRequestId": "uuid-reference",
  "originalScope": "All data from 2020-2026 for all users in Node",
  "proposedScope": "Incident #12345, March 2025, verification events only, identifiers hashed",
  "proposedFields": ["reportId", "verificationHash", "timestamp", "outcome"],
  "rationale": "Minimization principle; satisfies investigative need",
  "proposedBy": "legal-officer-bob",
  "proposedAt": "2026-02-26T17:00:00Z"
}
```

# Legal Response Protocol — Operational Handbook

## Purpose and Scope
This guide provides the operational framework for Flow Nodes receiving, evaluating, and responding to lawful requests for data or action.

* **Core Goal:** Balance legal compliance with maximum protection of individual safety and anonymity.
* **Guiding Formula:** $LUGN \times SPONTANITET \times INKÄNNANDE = LIV$ (Ensure the legal process does not extinguish the 'Flow').

## Guiding Principles
1. **Minimization First** ✂️: Disclose only the narrowest data required by law.
2. **Transparency Where Lawful** 🪞: Notify LOTUS governance and affected parties.
3. **Complete Auditability** 📊: Every request is logged, hashed, and retained.
4. **Safety Priority** 🛡️: Protect victim safety and prevent forced displacement.

## Documentation Map
- [Team Structure & Roles](ROLES.md)
- [Intake & Triage Process](INTAKE.md)
- [Legal Analysis & Minimization](ANALYSIS.md)
- [Emergency Handling](EMERGENCY.md)
- [JSON Schema Reference](SCHEMAS.md)


# Team Structure and Roles

| Role | Primary Responsibility | Key Actions |
| :--- | :--- | :--- |
| **Node Lead** | Final Decision Maker | Approve disclosure, publish audit logs to LOTUS. |
| **Legal Officer** | Analysis & Strategy | Jurisdiction check, negotiate scope, draft responses. |
| **Compliance Officer** | Data Handling | Extract data, prepare redacted packages, record metadata. |
| **LOTUS Convenor** | Coordination | Cross-node governance, on-chain attestations. |
| **Evidence Custodian** | Integrity | Chain-of-custody, secure storage management. |
| **Auditor Liaison** | Verification | Coordinate quarterly/annual external audits under NDA. |


# Initial Intake Process (First 24 Hours)

### Step 1: Receipt and Logging
Immediately create an entry in the Node Legal Log. Generate a unique `legalRequestId` (UUID).

### Step 2: Acknowledgment
Send a neutral acknowledgment within 24 hours. **Do not admit possession of specific data.**

> **Template:**
> "We acknowledge receipt of your request [legalRequestId]. We are conducting a legal review per applicable law. Point of contact: [Legal Officer]."

### Step 3: Triage and Classification
Categorize as: `Emergency`, `Criminal`, `Civil Discovery`, `Administrative`, or `MLAT`.

### Step 4: Preservation Hold
Place a hold on all potentially responsive data to prevent deletion. Generate a `preservationHash`.

```json
{
  "preservationId": "uuid-123",
  "legalRequestId": "uuid-reference",
  "preservationScope": "Data related to reportId: XYZ",
  "preservationHash": "sha256:...",
  "initiatedAt": "2026-02-26T15:00:00Z"
}
```

Rights of Affected Individuals
​Individuals have the right to:
​Ask what was disclosed.
​Request Node legal support.
​Access safety planning if disclosure creates risk.
​<!-- end list -->

# Emergency Handling (Exigent Circumstances)

**Scenario:** Imminent threat to life, child endangerment, or ongoing violent criminal activity.

1. **Verify Emergency:** Ensure the request comes from a verified official channel and describes a specific, immediate threat.
2. **Minimal Disclosure:** Provide only what is necessary to prevent the immediate harm (e.g., general location, not full history).
3. **Post-Facto Review:** A full legal review and audit must be performed within 24 hours after the emergency disclosure.

**Philosophy:**
*Follow the Law* ✅ | *Protect People* 🛡️ | *Document Everything* 📝

# JSON Schema Reference

All legal actions within the node must be logged using these structures to ensure compatibility with the LOTUS audit layer.

### Legal Request Intake
```json
{
  "legalRequestId": "uuid",
  "receivedAt": "ISO8601",
  "requestingAuthority": "string",
  "jurisdiction": "string",
  "requestType": "subpoena|warrant|emergency|civil",
  "deadline": "ISO8601"
}
```

Disclosure Log entry
​Every data packet sent to an authority must be logged:

```
{
  "disclosureId": "uuid",
  "legalRequestId": "uuid",
  "dataHash": "sha256:...",
  "recipient": "string",
  "authorizedBy": "node-lead-id",
  "timestamp": "2026-02-26T21:00:00Z"
}
```