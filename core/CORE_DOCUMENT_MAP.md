# CORE_DOCUMENT_MAP.md

**Version:** 1.0  
**Status:** Master Overview  
**Scope:** /core  
**Purpose:** Complete overview of all /core documents, their function, relationships, versioning, and invariant connections.

---

## 1. CORE DOCUMENTS OVERVIEW

| Document | Version | Purpose | Key Role in Flow | Versioning / Compost Notes |
|----------|--------|--------|-----------------|---------------------------|
| `RESOURCE_METRIC_STANDARDS.md` | 3.0 | Defines Baseline per participant | Sets minimum biological, cognitive, and temporal standards; foundation for system ethics and operations | MAJOR changes when Baseline or core protocol changes; previous MAJOR → /compostandgrowth |
| `RISK_MANAGEMENT.md` | 1.2 | Systemic risk identification and mitigation | Maintains operational integrity; maps threats, mitigations, interdependencies, escalation | MAJOR version updates when structural thresholds or critical triggers change |
| `RNG_AND_LOG_SPEC.md` | Draft | Verifiable, auditable RNG and logging | Ensures transparency, deterministic auditability, and minimal PII in RNG draws and time-based events | Draft currently; formal MAJOR release triggers compost of previous draft |
| `SANCTION_PROTOCOL.md` | Active | Governance intervention escalation | Defines proportional, founder-independent sanction levels; links to post-hoc review | MAJOR version on structural model or threshold change |
| `STRATEGIC_PREPARATION_FRAMEWORK.md` | 1.1 | Spiral-based deployment roadmap | Guides Node formation, replication, and generational system robustness; founder reduction | MAJOR version if spiral phases or success criteria change |
| `STRUCTURAL_INVARIANTS.md` | Core Reference | Immutable system structures | Guarantees decentralization, baseline security, conflict metabolism, and founder irrelevance | Updates only if core systemic invariants are adjusted |
| `VERSIONING_AND_COMPOST_POLICY.md` | 1.0 | Versioning, archival, and compost rules | Preserves historical integrity; manages active vs composted documents | Only MAJOR version changes trigger composting |

---

## 2. DOCUMENT RELATIONSHIPS

- **Foundational Layer:** `RESOURCE_METRIC_STANDARDS.md` → defines baseline metrics that underpin all operational decisions.  
- **Integrity Layer:** `RISK_MANAGEMENT.md` & `SANCTION_PROTOCOL.md` → operational and governance safeguards, connected to baseline metrics.  
- **Verification Layer:** `RNG_AND_LOG_SPEC.md` → ensures auditability, deterministic draws, and secure logging for system events.  
- **Strategic Layer:** `STRATEGIC_PREPARATION_FRAMEWORK.md` → roadmap for spiral growth, replication, and founder reduction.  
- **Invariant Layer:** `STRUCTURAL_INVARIANTS.md` → ensures all Nodes, all Phases, and all cultural/political contexts comply with non-negotiable principles.  
- **Historical / Structural Layer:** `VERSIONING_AND_COMPOST_POLICY.md` → governs versioning, archival, and composting of previous MAJOR versions.  

---

## 3. HIERARCHY AND PHASE ALIGNMENT

- **Phase 0 (Micro-Circle):** Focused on internal coherence → guided by baseline, invariants, risk understanding, and documentation.  
- **Phase 1 (Node Stabilization):** Multi-role, legal-compliant Node → risk and sanction protocols active; RNG may support transparent selections.  
- **Phase 2 (Node Replication):** Independent Nodes → structural invariants and cross-node knowledge transfer ensure replicability.  
- **Phase 3 (Networked Federation):** Regional coordination → strategic preparation framework ensures governance and resource flows.  
- **Phase 4 (Cultural Adoption):** Pattern diffusion → system-level metrics tracked; historical documentation preserves lineage.

---

## 4. OPERATIONAL PRINCIPLES

1. **Founder Irrelevance:** All phases and protocols enforce structural survival without individual dependency.  
2. **Decentralization:** No central authority; Nodes coordinate voluntarily.  
3. **Baseline Security:** All Nodes guarantee minimum energy, resource, and temporal requirements.  
4. **Pause & Stabilize:** Stress, burnout, or conflict triggers contraction and stabilization before further expansion.  
5. **Documentation First:** Knowledge capture precedes any scaling.  
6. **Audit & Verification:** RNG and logs ensure deterministic, privacy-respecting accountability.  
7. **Compost & Growth:** Previous MAJOR versions preserved for memory; nothing is deleted.  

---

## 5. CORE METRICS (SYSTEM-LEVEL)

- Resource regeneration and energy sustainability  
- Recovery and nervous system health  
- Conflict resolution timelines  
- Role redundancy and knowledge transfer  
- Baseline fulfillment and auditable verification  
- Founder dependency levels  
- Contraction/pause readiness  
- External interface quality (legal, cultural, media)

---

## 6. INTEGRATION RULES

- Strategic preparation guides operational execution.  
- Structural invariants enforce non-negotiable system rules.  
- Risk management and sanction protocols maintain integrity.  
- RNG & logging specification enables verification of randomness-dependent processes.  
- All active documents follow versioning and compost policy.  

---

## 7. VERSIONING PRINCIPLES

- **Major (X.0):** Structural, threshold, baseline, or core protocol changes → previous MAJOR composted.  
- **Minor (X.Y):** Clarifications, precision, formatting, non-structural improvements → previous minor remains active.  
- **Compost:** Preserves historical record, immutable, enables system memory and learning.

---

## 8. FINAL OBSERVATIONS

- Flow is generational: patience, documentation, and founder-reduction are mandatory.  
- Scale emerges from stability, not ambition.  
- Nodes must survive political, cultural, and environmental shifts while preserving invariants.  
- Historical memory preserved via composting ensures growth without erasure.  

---

```mermaid
flowchart TD
    %% Core / Phase Structure
    RM[RESOURCE_METRIC_STANDARDS.md] -->|Baseline Metrics| RM_Risk[RISK_MANAGEMENT.md]
    RM --> RNG[RNG_AND_LOG_SPEC.md]
    RM_Risk --> SAN[SANCTION_PROTOCOL.md]
    SAN --> SPF[STRATEGIC_PREPARATION_FRAMEWORK.md]
    SPF --> INV[STRUCTURAL_INVARIANTS.md]
    INV --> VCP[VERSIONING_AND_COMPOST_POLICY.md]

    %% Phase Alignment
    RM --> Phase0["Phase 0: Micro-Circle"]
    RM_Risk --> Phase1["Phase 1: Node Stabilization"]
    SAN --> Phase2["Phase 2: Node Replication"]
    SPF --> Phase3["Phase 3: Networked Federation"]
    INV --> Phase4["Phase 4: Cultural Adoption"]