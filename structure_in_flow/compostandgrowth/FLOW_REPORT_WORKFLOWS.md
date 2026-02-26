# FLOW Report Workflows — Operational Draft

**Status:** Draft  
**Scope:** All Flow Nodes, Spirals, and participants  
**Purpose:** Provide clear, step-by-step workflows for intake, triage, verification, escalation, and resolution of all reports within Flow. Operationalizes the universal reporting protocol.

---

## 1. Intake Workflow

1. **Report Submission**
    - Channels: App, Web Portal, SMS/USSD, Assisted Node Kiosk, IoT/Sensor input, Direct Node contact.
    - Reporter provides: category, location, severity, optional attachments, optional anonymity.
    - System generates `reportId` and timestamp; routes to intake queue.

2. **Initial Acknowledgement**
    - Node confirms receipt within SLA: 4h (Critical), 24h (High), 72h (Normal), 7d (Low).

3. **Metadata Enrichment**
    - Automatic tagging: GPS validation, category confirmation, sensor correlation.
    - Vulnerability flag check: schools, hospitals, accessibility-critical areas.

---

## 2. Priority Scoring and Automated Triage

1. **Score Calculation**
    - Severity base: Minor=1, Major=5, Urgent=10.
    - Corroboration bonus: +3 per verified sensor/report (max +9).
    - Vulnerability multiplier: ×1.5 if high-risk.
    - Repeat report penalty: +5 if >3 unresolved reports at same location in 7 days.
    - **Final Priority Score = (Severity base + Corroboration + Repeat penalty) × Vulnerability multiplier.**

2. **Routing by Priority**
    - **Critical (≥15):** Immediate action, SLA ack 4h, mitigation 24h.
    - **High (8–14):** SLA ack 24h, action plan 7d.
    - **Normal (2–7):** SLA ack 72h, action 30d.
    - **Low (0–1):** Monitor; action as resources permit.

3. **Automated Heuristics**
    - Sensor + media + GPS cluster → auto-escalate.
    - Multiple independent reports → increment corroborationCount.
    - Spam detection → route to moderation queue.

---

## 3. Verification Workflow

1. **Anonymous Verification Steps**
    1. Check IoT/sensor corroboration.
    2. Optional media validation (photo/video integrity).
    3. Witness attestation: 2 independent Node IDs can attest.
    4. On-site verifier dispatched if required.
    5. Decision: if corroborationCount ≥2 → actionable; else investigatory follow-up.

2. **High-risk Anonymous Reports**
    - Score ≥15 triggers **rapid verification** + optional LOTUS temporary task force assignment.

3. **Logging**
    - All verification events logged in encrypted local Node logs.
    - Aggregated telemetry sent to public dashboard (anonymized).

---

## 4. Escalation Workflow

1. **Node Level**
    - Node receives report, triages, assigns to Node personnel for action.
    - If SLA cannot be met, escalate to LOTUS temporary task force.

2. **LOTUS Temporary Task Force**
    - Randomly selected panel via LOTUS RNG.
    - Mandate duration: ≤3 months, rotates per Mandate of Nine Moons.
    - Resolves backlog, high-risk issues, and conflicts that cannot be settled locally.

3. **Cross-Node Spiral Escalation**
    - If Node + task force fail to resolve: escalate to Spiral coordination.
    - Spiral integrates multiple Nodes for systemic resolution.

4. **Conflict Cases**
    - Refer to `CONFLICT_ESCALATION_PATHS.md`.
    - Trauma-informed mediation and potential LOTUS adjudication.

---

## 5. Resolution Workflow

1. **Action**
    - Assign mitigation tasks: repair infrastructure, provide social support, resolve safety hazard.
    - On-site work or remote intervention as appropriate.
    - Completion logged with timestamp, verifier signature.

2. **Closure**
    - Node updates report status to “Resolved”.
    - SLA deadlines checked; failures trigger escalation audit.

3. **Post-Action Telemetry**
    - Update `reportsResolved`, `avgResponseTime`, SLA compliance.
    - Anonymized metrics published to dashboard.

---

## 6. Anti-Abuse and Moderation

1. **Rate Limiting**
    - Per reporter: X/day (configurable)
    - Per IP / Node: automated throttling.

2. **Spam and Fraud Detection**
    - Duplicate text, impossible GPS jumps, suspicious pattern → moderation queue.

3. **Penalties**
    - Verified malicious actors (non-anonymous) → trust score penalty, temporary suspension.
    - Appeals via LOTUS dispute panel.

---

## 7. Telemetry and Audit

1. **Fields**
    - `nodeIDHash`, `epoch`, `verificationsCount`, `selectionOverlapCount`, `commitLatencyMs`, `revealLatencyMs`, `failedReveals`, `anomalyFlag`, `reportsReceived`, `avgResponseTime`.

2. **Retention**
    - Raw logs: 12 months.
    - Aggregated anonymized: indefinite.

3. **Audit Process**
    - Quarterly automated anomaly scans.
    - Annual independent audit under NDA.
    - Attestation hashes published on-chain.

---

## 8. Accessibility and Inclusion

1. **Multi-format Reporting**
    - Audio, large text, simplified instructions, assisted kiosks.
    - Language localization, live interpreters.

2. **Special Considerations**
    - Accessibility-critical locations (wheelchair ramps, elevators) flagged for priority.
    - NodePolicy documents accommodation workflows.

3. **Small / Dispersed Pools**
    - Cross-Node pooling, stratified sampling for fairness.

---

## 9. Legal Contingencies

1. **Legal Response Policy**
    - Document process for lawful requests (subpoenas, court orders).
    - Minimize data exposure, notify LOTUS where safe, consult legal counsel.
    - Log any compelled PII disclosure, report to LOTUS governance unless prohibited.

---

## 10. Pilot Plan

1. **Scope**
    - Duration: 3–6 months.
    - Nodes: 3 diverse Nodes.
    - Participants: 500–2,000.

2. **Deliverables**
    - Multi-channel intake system.
    - Priority scoring engine + triage rules.
    - Anonymous verification workflow.
    - Rate-limit / anti-abuse mechanisms.
    - Telemetry pipeline + dashboard.
    - Legal Response Policy template.
    - Red-team spam/abuse testing.

3. **Metrics**
    - Time to first ack.
    - Time to mitigation.
    - SLA compliance % per priority.
    - % anonymous reports resolved.
    - False positive rate.
    - User satisfaction.

---

**Usage Note:** This workflow is operational guidance for Nodes and Spirals. All steps are logged, auditable, and subject to LOTUS oversight. Ready for pilot implementation and iterative improvement.

