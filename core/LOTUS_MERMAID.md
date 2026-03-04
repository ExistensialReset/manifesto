flowchart TD
    %% ==============================
    %% NODE LAYER
    %% ==============================
    subgraph NODE["Node Layer (Local)"]
        direction TB
        NL[Node LOTUS Panel]:::lotus
        N1[Baseline Violation Detected]:::baseline
        N2[Node Self-Correction (72h)]:::action
        N3[Surplus > 2× Baseline?]:::action
        N4[Voluntary Redistribution Window / Local Surplus Allocation]:::action
        N5[Node Report to Regional LOTUS (24/48/72h)]:::report
        N6[Baseline Amendment Proposal (Local)]:::proposal
    end

    %% ==============================
    %% REGIONAL LAYER
    %% ==============================
    subgraph REGIONAL["Regional Layer"]
        direction TB
        RL[Regional LOTUS Panel]:::lotus
        R1[Regional Recovery Triggered (7d)]:::action
        R2[Redistribute Regional Surplus / Emergency Pools]:::action
        R3[Report to Global LOTUS]:::report
        R4[Review Node Amendments / Proposals]:::proposal
    end

    %% ==============================
    %% GLOBAL LAYER
    %% ==============================
    subgraph GLOBAL["Global Layer"]
        direction TB
        GL[Global LOTUS Panel]:::lotus
        G1[Global Recovery Trigger / Audit]:::action
        G2[Approve/Reject Baseline Amendments]:::proposal
        G3[Global Surplus Audit & Redistribution]:::action
        G4[Structural / Emergency Override]:::critical
    end

    %% ==============================
    %% FLOWS
    %% ==============================

    %% Baseline Recovery Flow
    N1 --> N2 --> N5 --> R1 --> R2 --> R3 --> G1

    %% Surplus Flow
    N3 --> N4 --> R2
    R3 --> G3

    %% Baseline Amendment Flow
    N6 --> R4 --> G2

    %% Emergency / Override
    N1 --> GL
    R1 --> GL
    G4 --> N2
    G4 --> R2

    %% KPI / Reporting
    N5 --> R1
    R3 --> G1

    %% ==============================
    %% STYLING
    %% ==============================
    classDef lotus fill:#ffd966,stroke:#b58900,stroke-width:2px,color:#000,font-weight:bold;
    classDef action fill:#66ccff,stroke:#006699,stroke-width:2px,color:#000;
    classDef baseline fill:#ff6666,stroke:#900,stroke-width:2px,color:#fff;
    classDef proposal fill:#cce0ff,stroke:#004080,stroke-width:2px,color:#000;
    classDef report fill:#d4f8d4,stroke:#006600,stroke-width:2px,color:#000;
    classDef critical fill:#ff0000,stroke:#660000,stroke-width:3px,color:#fff;