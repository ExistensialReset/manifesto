# FLOW_GOVERNANCE_LOTTERIES.md

**Status:** Draft  
**Scope:** Global Node Protocol  
**Purpose:** Define a transparent, auditable, and democratic lotteried-based governance process for Flow decision-making, including Nodes, Mirrors, and other decision organs.

---

## Overview

The **LOTUS Protocol** in /core ensures that all key decision-making bodies in Flow are populated via a verifiable lottery system, preserving fairness, randomness, and rotation principles. It includes explicit safeguards, mandatory training, recovery, and auditability.

**Key Principles:**
- All decisions are made by randomly selected members, except for emergency or exceptional cases.  
- **One person = one vote/lottery entry**; no monetary or external incentives.  
- The victim never moves; the alleged violator moves if relocation or rotation is required.  
- Mandates have **maximum duration: 9 months** (Mandate of Nine Moons).  
- All members must have Flow baseline knowledge (non-coercion, LxSxI, post-monetary understanding).

---

## Lottery Panel Selection

**Process:**
1. **Eligible Pool:** All Node members except those in the immediate Node of the incident.  
2. **Conflict Screening:** Members with direct relationships to parties are excluded.  
3. **Random Selection:** Lottery conducted using cryptographically verifiable RNG (see `/core/RNG_AND_LOG_SPEC.md`).  
4. **Training:** After lottery, selected members complete 30–60 min e-learning on trauma-informed judgment, confidentiality, and conflict-of-interest.  
5. **Recusal:** Members may recuse themselves; recusal is logged.  
6. **Rotation Limit:** Each member may serve **max twice per calendar year**.

**Audit and Documentation:**
- All selection, recusal, and vote logs are exportable in CSV/JSON for independent audit.  
- Public reports can anonymize individual votes to protect against coercion.  
- Interim actions must have strict expiration and full documentation to prevent indefinite measures.

---

## Mandate Rules

- **Duration:** Maximum 9 months per Mandate.  
- **Rotation:** After 9 months, or earlier if necessary, all members are rotated out.  
- **Interim Extensions:** Only allowed with explicit justification and logged with timestamps.  
- **Evidence Handling:** Concrete examples of incontrovertible evidence required to reduce subjective interpretation.  

---

## Decision Documentation

- Decisions are logged in a standardized format including:
  - Decision ID  
  - Panel member hashes  
  - NodeID  
  - Timestamp  
  - Selection proof hash  
  - Status flags (active, recused, completed)  

- Logs are **cryptographically verifiable**, auditable without exposing PII.

---

## RNG & Verification

- **Seed & Nonce:** Node generates ephemeral seeds per event.  
- **Deterministic Verification:** RNG output can be audited independently.  
- **Commit-Reveal Scheme:** Ensures unbiased selection.  
- **Audit Trail:** Full logs for both RNG and member selection.

---

## Audit & Logs

- **CSV/JSON Export:** Standardized export for all selection, recusal, and voting events.  
- **Quarterly Audit:** Conducted by independent auditors using anonymized data.  
- **Anomaly Detection:** Track patterns in selections and decisions to prevent collusion or manipulation.

---

## Flow Baseline Knowledge Requirement

All selected members must have **mandatory Flow baseline knowledge**:
- Non-coercion  
- Calm × Spontaneity × Empathy (LxSxI)  
- Post-monetary principles  
- Knowledge of Flow resource, node, and verification systems  

Baseline knowledge ensures that all decisions respect Flow ethics and governance culture.

---

## Safeguards

- **Randomization:** Cross-node verification prevents local capture.  
- **Recusal Logging:** All recusals logged with proof of notice.  
- **Adaptive Timelocks:** For recovery or emergency decision adjustments.  
- **Public Ledger Hashes:** All selection proofs and RNG outputs stored for transparency.

---

## References

- `/core/RNG_AND_LOG_SPEC.md` — Cryptographically verifiable lottery RNG and log standards.  
- `/core/FLOW_ID_v3.md` — Identity verification protocol for members.  
- `/structure_in_flow/FLOW_SPIRAL_MAX.md` — High-level spiral timeline context.  

---