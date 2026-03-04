flowchart TD
    A[Baseline Violation Detected] --> B[Node Self-Correction 72h]
    B --> C[Voluntary Redistribution Window]
    C --> D[Report to Regional LOTUS]
    D --> E[Regional Recovery Triggered 7d]
    E --> F[Redistribute Regional Surplus]
    F --> G[Report to Global LOTUS]
    G --> H[Global Recovery / Audit]
    A --> I[Emergency Override Triggered]
    E --> I
    I --> B
    I --> F
    J[Baseline Amendment Proposal] --> D
    D --> J