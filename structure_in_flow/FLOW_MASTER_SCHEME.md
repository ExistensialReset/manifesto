%% FLOW – Radial-ish Node Map with Satellites (Black Text)
graph TD
    %% Central Node
    FN[Flow Node: 30+ people]

    %% Satellites around Flow Node
    PT[Professional Team]
    VT[Volunteer/Research Team]
    LY[Lyceum Musaeum]
    BL[Baseline Resource Access]

    %% Place satellites visually around FN
    FN --> PT
    FN --> VT
    FN --> LY
    FN --> BL

    %% Loop satellites to simulate circle
    PT -.-> VT
    VT -.-> LY
    LY -.-> BL
    BL -.-> PT

    %% Inter-Node Connections
    FN2[Flow Node B]
    FN3[Flow Node C]
    FN --- FN2
    FN --- FN3

    %% Baseline links
    BL2[Baseline B]
    BL3[Baseline C]
    BL --- BL2
    BL2 --- BL3
    BL3 --- BL

    %% Professionals across nodes
    PT2[Professional B]
    PT3[Professional C]
    PT --- PT2
    PT2 --- PT3
    PT3 --- PT

    %% Lyceum across nodes
    LY2[Lyceum B]
    LY3[Lyceum C]
    LY --- LY2
    LY2 --- LY3
    LY3 --- LY

    %% Regional & Global
    REG[Regional Network: 3-10 Nodes]
    GLOB[Global Flow Network: Multiple Regions]
    FN --> REG
    REG --> GLOB

    %% COLOR CLASSES (BLACK TEXT)
    classDef node fill:#c8e6c9,stroke:#388e3c,stroke-width:2px,color:#000;
    classDef team fill:#bbdefb,stroke:#1976d2,stroke-width:2px,color:#000;
    classDef lyceum fill:#d1c4e9,stroke:#512da8,stroke-width:2px,color:#000;
    classDef baseline fill:#ffcdd2,stroke:#c62828,stroke-width:2px,color:#000;
    classDef network fill:#ffe0b2,stroke:#ef6c00,stroke-width:2px,color:#000;

    %% ASSIGN CLASSES
    class FN,FN2,FN3 node;
    class PT,PT2,PT3,VT team;
    class LY,LY2,LY3 lyceum;
    class BL,BL2,BL3 baseline;
    class REG,GLOB network;

    %% Manual node styling to “spread” satellites
    style PT fill:#bbdefb,stroke:#1976d2,stroke-width:2px,color:#000
    style VT fill:#bbdefb,stroke:#1976d2,stroke-width:2px,color:#000
    style LY fill:#d1c4e9,stroke:#512da8,stroke-width:2px,color:#000
    style BL fill:#ffcdd2,stroke:#c62828,stroke-width:2px,color:#000
    style FN fill:#c8e6c9,stroke:#388e3c,stroke-width:2px,color:#000