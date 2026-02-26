# LOTUS_PROTOCOL.md

**Status:** DRAFT  
**Scope:** Global Node Governance  
**Purpose:** Establish lottery-based panel formation, mandate rules, and decision-making in Flow, fully auditable and aligned with Flow principles.

---

## 1. Core Principles

- **Democratic lottery:** All decision-making organs are selected randomly from qualified Node members.  
- **Victim-first principle:** If relevant, the victim never moves; the alleged violator is removed.  
- **Mandates:** Maximum of 9 months for Mandate of Nine Moons; other panels serve until decisions are made, with rotation applied if mandates overrun.  
- **Transparency:** All RNG, logs, and decisions are fully auditable without cloud dependency.  
- **Baseline knowledge:** All panelists must incorporate Flow baseline knowledge into decisions.  
- **Non-coercion & post-monetary:** No monetization, tokens, or coercive practices are used.

---

## 2. Lottery & Panel Formation

- **Selection pool:** Includes all qualified Node members except those in the nearest Node to the incident.  
- **Conflict-of-interest screening:** Automatic exclusion for direct relations; self-recusal logged.  
- **RNG & Draw:** Conducted offline using verified deterministic methods (e.g., HMAC-DRBG).  
- **Public publication:** Nonce, context string, and SHA256(H) hash published immediately.  
- **Post-selection training:** Panelists complete short orientation within 48 hours covering trauma-informed decision-making, confidentiality, and Flow baseline knowledge.  
- **Rotation & Limits:** Members cannot be selected more than twice per calendar year; rotation triggers applied if mandate exceeds limits.

---

## 3. Mandate & Duration

- **Mandate of Nine Moons:** Maximum 9 months.  
- **Other panels:** Serve until the decision is concluded; if extended beyond 9 months, rotation applies.  
- **Interim extensions:** Must be documented; per-interval and cumulative limits enforced.  
- **Mirrors:** Reflected in all related decision-making organs for consistency.

---

## 4. Decision Protocol & Documentation

- **Quorum & Supermajority:** Defined per decision type; supermajority required for veto override or extraordinary decisions.  
- **Decision logs:** Must include event_type, timestamp, responsible_member(s), evidence summary, rationale, next_deadline.  
- **Baseline knowledge application:** Decisions must reflect Flow principles (non-coercion, post-monetary, LxSxI, etc.).  
- **Anonymity:** Individual votes can be anonymized in public reports to prevent pressure.

---

## 5. RNG & Verification

- **Seed & Nonce:** Private seed rotated quarterly; public nonce + context + SHA256(H) hash published.  
- **Deterministic & verifiable:** Auditor can verify RNG outputs offline.  
- **Multi-party option:** Multiple seeds can be XORed for higher trust if needed.  
- **Offline operation:** RNG and logs fully functional without any cloud service dependency.

---

## 6. Audit & Log Management

- **Formats:** CSV and JSON with fields: event_id, timestamp_iso, node_id, context_string, public_nonce, hash_of_H, algorithm, output_summary, auditor_hash, notes.  
- **Retention:** Encrypted locally for 90 days.  
- **Compost:** After 90 days, sensitive fields anonymized/deleted; published hashes retained.  
- **Exportable & Reviewable:** Logs fully exportable for independent audit.  
- **Quarterly audits:** Conducted and discrepancies addressed.

---

## 7. Special Flow Clauses

- No monetization, tokens, or conditional baseline.  
- Victim-first principles applied where relevant.  
- Non-coercion and baseline human rights strictly maintained.  
- All procedural steps documented and auditable.

---

## 8. Reviewer Checklist

### 8.1 Lottery & Panel Formation
- [ ] Correct selection pool? (nearest Node excluded)  
- [ ] Conflict-of-interest screening complete?  
- [ ] Lottery conducted with verified RNG offline?  
- [ ] Public nonce, context, SHA256(H) hash published?  
- [ ] Timestamp of lottery logged?  
- [ ] Members within max mandates/year?  
- [ ] Self-recusals documented?  
- [ ] Votes anonymized where required?  
- [ ] Orientation/training completed within 48h post-lottery?

### 8.2 Mandate & Duration
- [ ] Mandate of Nine Moons ≤ 9 months?  
- [ ] Other panels monitored for overlong mandates?  
- [ ] Rotation triggers correctly applied?  
- [ ] Interim extensions documented, within limits?

### 8.3 Decision Protocol & Documentation
- [ ] Quorum met?  
- [ ] Supermajority enforced for veto/critical decisions?  
- [ ] Decision logs include all required fields?  
- [ ] Flow baseline knowledge applied in rationale?  
- [ ] Mirrors reflect lottery-based consistency?

### 8.4 RNG & Verification
- [ ] Private seed rotated quarterly?  
- [ ] Public nonce + context + hash published?  
- [ ] RNG verified offline?  
- [ ] Multi-party seed combination applied if required?  
- [ ] No cloud service used?

### 8.5 Audit & Log Management
- [ ] CSV/JSON formats verified?  
- [ ] Exportable for independent review?  
- [ ] Retention and compost rules followed?  
- [ ] Quarterly audit performed and discrepancies addressed?

### 8.6 Special Flow Clauses
- [ ] No monetization, tokens, or conditional baseline?  
- [ ] Victim-first principles applied if relevant?  
- [ ] Non-coercion and baseline human rights maintained?  
- [ ] All procedural steps fully documented and auditable?

---

## 9. LOTUS Protocol Mermaid Diagram

```mermaid 
flowchart LR
    %% 🌸 LOTUS Protocol – Maxad Flow‑version
    LOTUS["🌸 LOTUS Protocol"] --> LOTTERY["🎲 Lottery Selection"]
    LOTUS --> MANDATE["📜 Mandate Rules"]
    LOTUS --> DECISION["📝 Decision Documentation"]
    LOTUS --> RNG["🔑 RNG & Verification"]
    LOTUS --> AUDIT["📊 Audit & Logs"]
    LOTUS --> BASELINE["🌱 Flow Baseline Knowledge"]

    %% Lottery
    LOTTERY --> POOL["🧑‍💻 Qualified Pool"]
    LOTTERY --> CONFLICT["🤝 Conflict Screening"]
    LOTTERY --> TRAINING["🏫 Post-Selection Training"]

    %% Mandate
    MANDATE --> DURATION["⏳ Mandate Duration & Rotation"]
    MANDATE --> EXTENSIONS["🔄 Interim Extensions"]

    %% Decision
    DECISION --> LOGS["🗂️ Decision Logs"]
    DECISION --> ANON["🕵️‍♀️ Anonymized Votes"]

    %% RNG
    RNG --> SEED["🗝️ Seed & Nonce"]
    RNG --> VERIFY["✔️ Deterministic Verification"]

    %% Audit
    AUDIT --> EXPORT["💾 CSV/JSON Export"]
    AUDIT --> QUARTERLY["🔍 Quarterly Audit"]

    %% Baseline Knowledge
    BASELINE --> NONCOERCION["💛 Non-Coercion"]
    BASELINE --> LxSxI["🧘 LxSxI: Calm×Spontaneity×Empathy"]
    BASELINE --> POSTMONEY["🌍 Post-Monetary"]


