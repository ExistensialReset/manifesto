# FLOW Report Workflows — Operational Specification

**Status:** Draft  
**Scope:** All Flow Nodes, Spirals, and participants  
**Purpose:** Provide a single, accessible, privacy‑preserving, and democratic operational workflow for intake, triage, verification, escalation, remediation, audit, and inclusion. This specification includes concrete priority scoring, anonymous verification steps, anti‑abuse controls, SLA and escalation matrices, telemetry schema, legal contingency procedures, and pilot requirements.

---

## 1. Principles and Scope

- **One Pathway, All Issues** — every report (infrastructure, safety, accessibility, social, other) enters the same system and follows a unified metadata, triage, and audit pipeline.  
- **Accessibility First** — support for app, web, SMS/USSD, assisted kiosk intake, and sensor inputs; accessible formats for disabilities and low connectivity.  
- **Privacy & Optional Anonymity** — reporters may remain anonymous; PII is separated, encrypted, and never stored on‑chain.  
- **Democratic Resolution** — LOTUS selection and rotation used for escalations and temporary task forces to avoid capture.  
- **No Financial Barriers** — reporting is free and device‑agnostic.  
- **Auditability** — every step logged (anonymized) for independent audit and SLA verification.

---

## 2. Channels and Minimal Report Schema

### Channels
- **Digital Portal / App** — primary UI for rich reports (images, video, GPS).  
- **SMS / USSD** — low‑bandwidth reporting for basic phones.  
- **Assisted Node Kiosks / Hubs** — staff‑assisted intake without publishing PII.  
- **Automated Sensors / IoT** — environmental triggers (blocked ramp, flooding).  
- **Direct Node Contact** — phone or in‑person intake routed into the same system.

### Minimal Report JSON Schema (example)
```json
{
  "reportId": "uuid",
  "category": "Infrastructure|Safety|Accessibility|Social|Other",
  "location": {"type":"gps|text","value":"..."},
  "severity": "Minor|Major|Urgent",
  "severityScore": 0,
  "description": "string",
  "attachments": ["hash1","hash2"],
  "reporterType": "anonymous|nodeId|name",
  "reporterHash": "sha256(...)",
  "timestamp": "ISO8601",
  "corroborationCount": 0,
  "nodeAssigned": "node:abc123",
  "statusHistory": [{"status":"received","timestamp":"...","actor":"node:..."}],
  "slaDeadline": "ISO8601"
}
```

---

## 3. Priority Scoring, Automated Triage, and Routing

### Priority scoring formula
- **Severity base:** Minor = 1; Major = 5; Urgent = 10.  
- **Corroboration bonus:** +3 per independent corroboration (sensor, verified report, witness), capped at +9.  
- **Repeat penalty:** +5 if >3 unresolved reports at same location in 7 days.  
- **Vulnerability multiplier:** ×1.5 if location is high‑risk (school, hospital, transit hub).  

\[
\text{Priority score} = (\text{Severity base} + \text{Corroboration bonus} + \text{Repeat penalty}) \times \text{Vulnerability multiplier}
\]

### Priority buckets and SLAs
- **Critical (score ≥ 15):** Ack within **4 hours**; mitigation or temporary fix within **24 hours**.  
- **High (8–14):** Ack within **24 hours**; plan and schedule within **7 days**.  
- **Normal (2–7):** Ack within **72 hours**; action within **30 days**.  
- **Low (0–1):** Monitor; action as resources permit; ack within **7 days**.

### Automated heuristics
- **Auto‑escalate** when sensor + media + GPS cluster match.  
- **Increment corroborationCount** for multiple independent reports within 48 hours.  
- **Spam detection** routes suspicious submissions to moderation and applies rate limits.

---

## 4. Anonymous Verification Workflow (Stepwise)

**Goal:** Convert anonymous signals into actionable items while preserving anonymity and producing auditable proofs.

### Key primitives
- **CorroborationCount:** integer tally of independent evidence items.  
- **Verification Event:** signed local Node record (encrypted off‑chain) referenced on‑chain by hash.  
- **Actionable threshold:** default **CorroborationCount ≥ 2** or priority score ≥ 15.

### Stepwise process
1. **Automated intake & initial scoring** — compute priority score; if score < 8 mark investigatory; otherwise proceed.  
2. **Sensor corroboration** — query IoT, public CCTV metadata, environmental sensors; add sensor proof hash if matched.  
3. **Media integrity check** — optional reporter upload; run EXIF/time checks and basic forensics; add proof hash if valid.  
4. **Witness attestation** — allow two independent witnesses (different NodeIDs) to submit signed attestations; each adds +3 corroboration.  
5. **Remote verifier triage** — if CorroborationCount ≥ 2, assign remote verifier for phone/app confirmation or coordinate local staff. Verifier creates a Verification Event.  
6. **On‑site verification** — for Critical or unresolved High cases, dispatch on‑site verifier; sign Verification Event and upload encrypted evidence.  
7. **Decision & action** — confirmed → create remediation task with SLA; inconclusive → investigatory follow‑up and scheduled recheck.  
8. **Escalation** — if Node cannot meet SLA or issue requires cross‑node resources, trigger LOTUS lottery assignment with selectionProofHash and verification event hashes.

### Verification Event JSON (example)
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

## 5. Escalation Matrix and LOTUS Integration

### Node escalation rules
- If Node cannot meet SLA, it must request LOTUS assignment within the SLA window.  
- LOTUS assigns a temporary task force via verifiable lottery when local capacity is insufficient.

### LOTUS temporary task force
- **Mandate duration:** ≤ 3 months (short mandate).  
- **Selection:** cryptographically verifiable RNG; members complete trauma‑informed and confidentiality training.  
- **Scope:** resolve backlog, high‑risk issues, or conflicts that cannot be resolved locally.  
- **Audit:** all actions logged and subject to independent audit.

### Cross‑Node Spiral escalation
- If Node + task force fail, escalate to Spiral coordination for systemic resolution and resource allocation.

### Conflict cases
- Social or interpersonal disputes follow `CONFLICT_ESCALATION_PATHS.md` and may trigger LOTUS adjudication with trauma‑informed panels.

---

## 6. Anti‑Abuse, Rate Limits, and Moderation

- **Per‑reporter rate limit:** configurable X reports/day for anonymous flows (pilot sets value).  
- **Per‑IP / per‑Node throttling:** automatic throttles for high submission rates.  
- **Spam detection:** ML heuristics and rule filters (duplicate text, impossible GPS jumps) route to moderation.  
- **Verified malicious actors:** non‑anonymous offenders receive trust score penalties and temporary suspension; appeals via LOTUS dispute panel.  
- **Coordinated attack detection:** pattern analysis (geo clustering, timing) triggers emergency escalation and temporary hardening of intake.

---

## 7. Telemetry, Auditability, and Transparency

### Telemetry schema (anonymized)
- `nodeIDHash` — SHA‑256(NodeID + epoch salt)  
- `epoch`  
- `reportsReceived`  
- `verificationsCount`  
- `selectionOverlapCount`  
- `commitLatencyMs`  
- `revealLatencyMs`  
- `failedReveals`  
- `avgResponseTime`  
- `anomalyFlag`

### Anonymization & retention
- Node identifiers salted per epoch and hashed; salts ephemeral.  
- Raw logs retained **12 months**; aggregated anonymized metrics retained indefinitely.  
- Public dashboard displays anonymized KPIs: reports by category, SLA compliance, backlog, escalations.

### Audit process
- Quarterly automated anomaly scans; annual independent audit under NDA.  
- Auditors receive encrypted proofs; publish attestation hashes on‑chain.

---

## 8. Failure Modes, SLAs, and Fallback Rules

### Failure modes
- Missing reveals from committers (RNG context).  
- Insufficient committers.  
- Telemetry anomalies or selection overlap.  
- Network partitions preventing timely commit/reveal.

### SLAs and actions
- **Commit phase timeout:** 24 hours → abort epoch and reschedule within 24 hours.  
- **Reveal phase timeout:** 24 hours → if minimum committers met, proceed excluding missing commits and log anomaly.  
- **Abort threshold:** fewer than minimum committers reveal → abort and reschedule within 48 hours.  
- **Emergency escalation:** anomalyFlag true → LOTUS convenes within **72 hours**.  
- **Audit SLA:** independent auditor delivers attestation within **30 days** of request.

### Fallback randomness (LOTUS RNG context)
- If commit/reveal fails and abort is not possible, derive fallback seed from multiple recent on‑chain block hashes plus pre‑registered fallback Node entropy; log and audit fallback use.

---

## 9. Inclusion, Accessibility, and Small‑Pool Handling

### Accessibility
- Multi‑format intake: audio prompts, large text, simplified language, assisted kiosk workflows.  
- Language localization and live interpreter options via Node hubs.  
- Nodes must document accommodation workflows in NodePolicy.

### Small pools and diaspora
- For small or dispersed eligible pools, use cross‑node pooling, stratified sampling, or expanded exclusion radius to preserve fairness and avoid over‑exposure.

---

## 10. Legal Contingency and Data Minimization

- Nodes publish a **Legal Response Policy** describing handling of lawful requests (subpoenas, court orders).  
- Policy must include minimization steps, LOTUS notification where safe, and requirement to seek legal counsel.  
- Any compelled PII disclosure must be logged and reported to LOTUS governance unless legally prohibited.

---

## 11. Pilot Plan and Operational Deliverables

### Pilot scope (3–6 months)
- **Nodes:** 3 diverse Nodes.  
- **Participants:** 500–2,000.  
- **Deliverables:** intake channels (app, SMS, kiosk), priority scoring engine, anonymous verification workflow, rate‑limit/anti‑abuse mechanisms, telemetry pipeline and dashboard, legal response template, red‑team tests, one independent auditor.

### Pilot metrics
- Time to first ack; time to mitigation; SLA compliance % per priority; % anonymous reports resolved; false positive rate; user satisfaction.

### Minimum technical deliverables before pilot
- Report JSON Schema and API spec.  
- Priority scoring engine and triage rules (pseudocode).  
- Anonymous verification workflow implementation.  
- Rate‑limit and anti‑abuse rules.  
- Telemetry schema and dashboard.  
- Legal Response Policy template.

---

## 12. Appendices

### A. Example report (JSON)
```json
{
  "reportId":"123e4567-e89b-12d3-a456-426614174000",
  "category":"Accessibility",
  "location":{"type":"gps","value":"57.7089,11.9746"},
  "severity":"Major",
  "severityScore":5,
  "description":"Ramp blocked by construction materials",
  "attachments":["sha256:..."],
  "reporterType":"anonymous",
  "reporterHash":"sha256:...",
  "timestamp":"2026-02-26T07:00:00Z",
  "corroborationCount":1,
  "nodeAssigned":"node:goteborg-01",
  "statusHistory":[{"status":"received","timestamp":"2026-02-26T07:00:00Z","actor":"system"}],
  "slaDeadline":"2026-03-05T07:00:00Z"
}
```

### B. Verification Event example
(See Section 4 for JSON structure.)

### C. Priority scoring examples
- **Urgent incident at hospital with sensor match:** Severity 10 + Corroboration 3 = 13 × 1.5 = 19.5 → **Critical**.  
- **Minor infrastructure, single anonymous report:** 1 + 0 = 1 → **Low**.

