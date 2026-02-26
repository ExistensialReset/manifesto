# FLOW Universal Reporting Protocol — Implementation Draft

**Status:** Draft  
**Scope:** All Flow Nodes, Spirals, and participants  
**Purpose:** Provide a single, accessible, privacy-preserving, and democratic reporting pathway for every issue in Flow, with clear triage, verification, escalation, audit, and inclusion rules. This version adds concrete implementation details: priority scoring, anonymous verification workflow, anti‑abuse controls, SLA/escalation matrix, telemetry schema, and legal contingency procedures.

---

## 1 Principles and Scope

- **One Pathway, All Issues** — every report (infrastructure, safety, accessibility, social, other) enters the same system and follows the same metadata, triage, and audit pipeline.  
- **Accessibility First** — support for app, web, SMS, assisted kiosk intake, and sensor inputs; materials and flows accessible to people with disabilities and limited connectivity.  
- **Privacy and Optional Anonymity** — reporters may choose anonymity; all data encrypted in transit and at rest; PII separated from public logs.  
- **Democratic Resolution** — Nodes use LOTUS selection and rotation for dispute resolution and resource allocation when needed.  
- **No Financial Barriers** — reporting is free and device-agnostic.  
- **Auditability** — every step logged (anonymized) for independent audit and SLA verification.

---

## 2 Channels, Data Model, and Metadata Schema

### Channels
- **Digital Portal / App** — primary UI for rich reports (images, video, GPS).  
- **SMS / USSD** — lightweight reporting for basic devices and low bandwidth.  
- **Node Kiosks / Hubs** — assisted intake in public spaces; staff can help file reports without collecting PII on-chain.  
- **Automated Sensors / IoT** — environmental triggers (e.g., blocked ramp) create sensor reports with corroboration flags.  
- **Direct Node Contact** — phone or in-person intake routed into the same system.

### Minimal Report Schema (JSON)
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

## 3 Priority Matrix and Automated Triage

### Priority scoring (automated)
- **Severity base:** Minor=1, Major=5, Urgent=10.  
- **Corroboration bonus:** +3 per corroborating sensor/report (capped at +9).  
- **Vulnerability multiplier:** if location flagged as high‑risk (schools, hospitals) ×1.5.  
- **Repeat report penalty:** if same location has >3 unresolved reports in 7 days, add +5.  

**Priority score = (Severity base + Corroboration bonus + Repeat penalty) × Vulnerability multiplier.**

### Routing rules
- **Score ≥ 15:** Immediate escalation to Critical queue (SLA: ack within 4 hours, mitigation within 24 hours).  
- **Score 8–14:** High priority (SLA: ack within 24 hours, plan within 7 days).  
- **Score 2–7:** Normal priority (SLA: ack within 72 hours, action within 30 days).  
- **Score 0–1:** Low priority (monitor; action as resources permit).

### Automated triage heuristics
- Sensor match + photo + GPS cluster → auto‑escalate to High.  
- Multiple anonymous reports from distinct reporters within 48h → increase corroborationCount.  
- Spam patterns (repeated identical text, high frequency from same reporterHash) → route to manual review and rate‑limit.

---

## 4 Anonymous Verification Workflow and Corroboration

### Stepwise verification for anonymous reports
1. **Sensor corroboration:** check IoT triggers, CCTV, or environmental sensors. If matched, increment corroborationCount.  
2. **Media validation:** request optional photo; run automated integrity checks (metadata, EXIF, hash) and image‑forensics flags.  
3. **Witness attestation:** allow two independent witnesses (different Node IDs) to attest via short signed statement; each adds +3 corroboration.  
4. **On‑site verifier:** Node may dispatch a verifier for physical confirmation; verifier signs a verification event recorded in encrypted local logs.  
5. **Decision:** if corroborationCount ≥ 2 or sensor match + photo, treat as actionable; otherwise mark as investigatory and schedule follow‑up.

### Handling anonymous but high‑risk reports
- If anonymous report scores ≥ 15, Node must perform rapid sensor and witness checks and either deploy mitigation or escalate to LOTUS temporary task force within SLA.

---

## 5 SLA, Escalation Matrix, and LOTUS Integration

### SLA table

| Priority | Ack time | Required action | Escalation if missed |
|---|---:|---:|---|
| Critical (score ≥15) | 4 hours | Mitigation or temporary fix within 24 hours | Escalate to regional Node + LOTUS lottery task force |
| High (8–14) | 24 hours | Plan and schedule within 7 days | Escalate to cross‑node Spiral after 7 days |
| Normal (2–7) | 72 hours | Action within 30 days | Escalate to Node consortium after 30 days |
| Low (0–1) | 7 days | Monitor; action as resources permit | No automatic escalation |

### Escalation rules
- **Node capacity check:** if Node cannot meet SLA, it must request LOTUS lottery assignment within SLA window.  
- **LOTUS temporary task force:** randomly selected panel (per LOTUS RNG) forms a short mandate (max 3 months) to resolve backlog; mandate follows Mandate of Nine Moons rules for rotation and audit.  
- **Conflict cases:** social or interpersonal disputes follow `CONFLICT_ESCALATION_PATHS.md` and may trigger a LOTUS panel with trauma‑informed training.

---

## 6 Anti‑Abuse, Rate Limits, and Moderation

- **Per‑reporter rate limit:** anonymous reporterHash or phone number limited to X reports/day (configurable per pilot).  
- **Per‑IP / per‑Node throttling:** automatic throttles for high submission rates; suspected coordinated campaigns flagged for manual review.  
- **Spam detection:** ML heuristics and rule‑based filters (duplicate text, impossible GPS jumps) route to moderation queue.  
- **False report penalties:** verified malicious actors (non‑anonymous) face trust score penalties and temporary reporting suspension; appeals handled via LOTUS dispute panel.

---

## 7 Telemetry, Auditability, and Transparency

### Telemetry schema (anonymized)
- `nodeIDHash`, `epoch`, `verificationsCount`, `selectionOverlapCount`, `commitLatencyMs`, `revealLatencyMs`, `failedReveals`, `anomalyFlag`, `reportsReceived`, `avgResponseTime`.

### Anonymization and retention
- Node identifiers salted per epoch and hashed; salts ephemeral.  
- Raw telemetry retained **12 months** for operational review; aggregated anonymized metrics retained indefinitely.  
- Public dashboard shows anonymized KPIs: reports by category, SLA compliance rates, backlog counts, and escalation counts.

### Audit process
- Quarterly automated anomaly scans; annual independent audit of anonymized logs and SLA compliance. Auditors receive encrypted proofs under NDA and publish attestation hashes on‑chain.

---

## 8 Inclusion, Accessibility, and Legal Contingencies

### Accessibility
- Provide multi‑format training and intake: audio prompts, large text, simplified language, and assisted kiosk workflows.  
- Offer language localization and live interpreter options via Node hubs.  
- Nodes must document accommodation workflows in NodePolicy.

### Small pools and diaspora
- For small or dispersed communities, use cross‑node pooling and stratified sampling to ensure fairness and avoid over‑exposure.

### Legal contingency policy
- Nodes publish a **Legal Response Policy**: steps for lawful requests (minimization, LOTUS notification where safe, legal counsel). Any compelled PII disclosure must be logged and reported to LOTUS governance unless legally prohibited.

---

## 9 Pilot Plan and Operational Next Steps

### Pilot scope (3–6 months)
- **Nodes:** 3 diverse Nodes.  
- **Participants:** 500–2,000.  
- **Deliverables:** intake channels (app, SMS, kiosk), triage engine, anonymous verification workflow, telemetry pipeline, public dashboard, red‑team spam and abuse tests, one independent auditor.

### Pilot metrics
- Time to first ack, time to mitigation, % SLA met per priority, % anonymous reports resolved, false positive rate, user satisfaction.

### Minimum technical deliverables before pilot
- Report JSON schema and API spec.  
- Priority scoring engine and triage rules.  
- Anonymous verification workflow implementation.  
- Rate‑limit and anti‑abuse rules.  
- Telemetry schema and dashboard.  
- Legal Response Policy template.

