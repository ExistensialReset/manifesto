%% FLOW – Radial-ish Node Map (Black Text)
graph TD

    %% CENTRAL NODE
    FN[Flow Node: 30+ people]

    %% SATELLITES
    PT[Professional Team]
    VT[Volunteer/Research Team]
    LY[Lyceum Musaeum]
    BL[Baseline Resource Access]

    %% CONNECT SATELLITES TO CENTER
    FN --> PT
    FN --> VT
    FN --> LY
    FN --> BL

    %% LOOP SATELLITES (simulate circle)
    PT -.-> VT
    VT -.-> LY
    LY -.-> BL
    BL -.-> PT

    %% COLOR CLASSES
    classDef node fill:#c8e6c9,stroke:#388e3c,stroke-width:2px,color:#000;
    classDef team fill:#bbdefb,stroke:#1976d2,stroke-width:2px,color:#000;
    classDef lyceum fill:#d1c4e9,stroke:#512da8,stroke-width:2px,color:#000;
    classDef baseline fill:#ffcdd2,stroke:#c62828,stroke-width:2px,color:#000;

    %% ASSIGN CLASSES
    class FN node;
    class PT,VT team;
    class LY,BL lyceum;