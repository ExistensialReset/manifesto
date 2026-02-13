# SOCIETY STRUCTURE AND PRODUCTION IN FLOW

*A comprehensive overview of how communities organize in Flow — integrating Nodes, Teams, Lyceum Musaeum, Baseline, and Production Systems.*

---

## 1. Central Concepts

- **Flow Node:** The core hub of a community. Coordinates professionals, volunteers, Lyceum Musaeum, and resource access.  
- **Professional Teams:** Certified staff ensuring healthcare, social support, and other critical functions.  
- **Volunteer / Research Teams:** Mentors, artisans, researchers, and event organizers who contribute knowledge, creativity, and innovation.  
- **Lyceum Musaeum:** The living knowledge and creativity center; a space for free exploration, learning, and making.  
- **Baseline Resource Access:** Guaranteed access to essential resources: food, energy, tools, and infrastructure.

---

## 2. Visual Overview

```mermaid
graph TD
    %% Nodes
    NodeA[Flow Node A]
    NodeB[Flow Node B]
    NodeC[Flow Node C]

    %% Professional Teams
    PT_A[Professional Team]
    PT_B[Professional Team]
    PT_C[Professional Team]

    %% Volunteers / Research
    VT_A[Volunteers / Researchers]
    VT_B[Volunteers / Researchers]
    VT_C[Volunteers / Researchers]

    %% Lyceum
    LyceumA[Lyceum Musaeum]
    LyceumB[Lyceum Musaeum]
    LyceumC[Lyceum Musaeum]

    %% Baseline
    BaselineA[Baseline Resource Access]
    BaselineB[Baseline Resource Access]
    BaselineC[Baseline Resource Access]

    %% Node Connections
    NodeA --> PT_A
    NodeA --> VT_A
    NodeA --> LyceumA
    NodeA --> BaselineA

    NodeB --> PT_B
    NodeB --> VT_B
    NodeB --> LyceumB
    NodeB --> BaselineB

    NodeC --> PT_C
    NodeC --> VT_C
    NodeC --> LyceumC
    NodeC --> BaselineC

    %% Inter-node Resource Sharing
    BaselineA --- BaselineB
    BaselineB --- BaselineC
    BaselineC --- BaselineA

    %% Professional Coordination
    PT_A --- PT_B
    PT_B --- PT_C
    PT_C --- PT_A

    %% Lyceum Exchange
    LyceumA --- LyceumB
    LyceumB --- LyceumC
    LyceumC --- LyceumA

    classDef professional fill:#8fd3f4,stroke:#0366d6,stroke-width:2px;
    classDef volunteer fill:#f4f1a1,stroke:#d6c836,stroke-width:2px;
    classDef lyceum fill:#c4f4c4,stroke:#36d636,stroke-width:2px;
    classDef baseline fill:#f4c4c4,stroke:#d63636,stroke-width:2px;
    class Node fill:#f0f0f0,stroke:#999,stroke-width:2px;

    class PT_A,PT_B,PT_C professional;
    class VT_A,VT_B,VT_C volunteer;
    class LyceumA,LyceumB,LyceumC lyceum;
    class BaselineA,BaselineB,BaselineC baseline;