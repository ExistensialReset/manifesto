# LEGAL_OVERVIEW_FLOW.md

**Scope:** High-Level Legal & Governance Architecture  
**Purpose:** Visual overview of how Nodes, Spirals, Playbooks, Legal, Verification, and LOTUS interact.

---

```mermaid
%%{init: {
  "theme": "base",
  "themeVariables": {
    "fontSize": "18px",
    "fontFamily": "Arial",
    "primaryTextColor": "#000000"
  }
}}%%

flowchart TB

%% ===== COLOR DEFINITIONS =====
classDef node fill:#FFE9A8,stroke:#222,color:#000,stroke-width:2px
classDef spiral fill:#A8E6FF,stroke:#222,color:#000,stroke-width:2px
classDef playbook fill:#E6FFA8,stroke:#222,color:#000,stroke-width:2px
classDef legal fill:#FFC9DC,stroke:#222,color:#000,stroke-width:2px
classDef verify fill:#D6E4FF,stroke:#222,color:#000,stroke-width:2px
classDef audit fill:#C8FFD8,stroke:#222,color:#000,stroke-width:2px
classDef lotus fill:#D5C8FF,stroke:#222,color:#000,stroke-width:3px

%% ===== LAYER 1 — GOVERNANCE =====
LOTUS[LOTUS Governance]:::lotus

%% ===== LAYER 2 — LEGAL & OVERSIGHT =====
LEGAL[Legal / Compliance]:::legal
VERIFY[Evidence Verifiers]:::verify
AUDIT[Audit Layer]:::audit

%% ===== LAYER 3 — OPERATIONAL STRUCTURE =====
SPIRALS[Spirals]:::spiral
PLAYBOOKS[Playbooks]:::playbook

%% ===== LAYER 4 — EXECUTION =====
NODES[Flow Nodes]:::node

%% ===== FLOW RELATIONSHIPS =====
LOTUS --> LEGAL
LOTUS --> AUDIT
LEGAL --> PLAYBOOKS
PLAYBOOKS --> SPIRALS
SPIRALS --> NODES
NODES --> VERIFY
VERIFY --> AUDIT
AUDIT --> LOTUS
