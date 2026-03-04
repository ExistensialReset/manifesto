flowchart TD
    %% Node Layer
    NBASE[Baseline Violation Detected]
    NLOTUS[Node LOTUS Panel]
    NSC[Node Self-Correction (72h)]
    NVOL[Voluntary Redistribution Window]
    NREP[Node Report to Regional LOTUS]
    NAMEND[Node Baseline Amendment Proposal]

    %% Regional Layer
    RLOTUS[Regional LOTUS Panel]
    RREC[Regional Recovery Triggered (7d)]
    RRED[Redistribute Regional Surplus]
    RREP[Report to Global LOTUS]
    RREV[Review Node Amendments]

    %% Global Layer
    GLOTUS[Global LOTUS Panel]
    GREC[Global Recovery / Audit]
    GAMEND[Approve/Reject Baseline Amendments]
    GRED[Global Surplus Audit & Redistribution]
    GEMERG[Emergency Override]

    %% Flöden
    NBASE --> NSC --> NREP --> RREC --> RRED --> RREP --> GREC
    NSC --> NVOL --> RRED
    NAMEND --> RREV --> GAMEND
    NBASE --> GEMERG
    RREC --> GEMERG
    GEMERG --> NSC
    GEMERG --> RRED