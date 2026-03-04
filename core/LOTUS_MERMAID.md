flowchart TD
    %% ==============================
    %% NODE LAYER
    %% ==============================
    NLOTUS[Node LOTUS Panel]
    NBASE[Baseline Violation Detected]
    NSC[Node Self-Correction (72h)]
    NSUR[Surplus > 2x Baseline?]
    NVOL[Voluntary Redistribution Window / Local Surplus Allocation]
    NREP[Node Report to Regional LOTUS]
    NAMEND[Node Baseline Amendment Proposal]

    %% ==============================
    %% REGIONAL LAYER
    %% ==============================
    RLOTUS[Regional LOTUS Panel]
    RREC[Regional Recovery Triggered (7d)]
    RRED[Redistribute Regional Surplus / Emergency Pools]
    RREP[Report to Global LOTUS]
    RREV[Review Node Amendments / Proposals]

    %% ==============================
    %% GLOBAL LAYER
    %% ==============================
    GLOTUS[Global LOTUS Panel]
    GREC[Global Recovery Trigger / Audit]
    GAMEND[Approve/Reject Baseline Amendments]
    GRED[Global Surplus Audit & Redistribution]
    GEMERG[Structural / Emergency Override]

    %% ==============================
    %% FLOWS
    %% ==============================
    NBASE --> NSC --> NREP --> RREC --> RRED --> RREP --> GREC
    NSUR --> NVOL --> RRED
    NREP --> RREC
    NAMEND --> RREV --> GAMEND
    NBASE --> GEMERG
    RREC --> GEMERG
    GEMERG --> NSC
    GEMERG --> RRED

    %% ==============================
    %% STYLING
    %% ==============================
    class NLOTUS,RLOTUS,GLOTUS lotus
    class NSC,RREC,GREC,NSUR,RRED,GRED action
    class NBASE baseline
    class NAMEND,RREV,GAMEND proposal
    class NREP,RREP report
    class GEMERG critical

    classDef lotus fill:#ffd966,stroke:#b58900,stroke-width:2px,color:#000,font-weight:bold;
    classDef action fill:#66ccff,stroke:#006699,stroke-width:2px,color:#000;
    classDef baseline fill:#ff6666,stroke:#900,stroke-width:2px,color:#fff;
    classDef proposal fill:#cce0ff,stroke:#004080,stroke-width:2px,color:#000;
    classDef report fill:#d4f8d4,stroke:#006600,stroke-width:2px,color:#000;
    classDef critical fill:#ff0000,stroke:#660000,stroke-width:3px,color:#fff;