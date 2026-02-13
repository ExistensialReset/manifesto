# FLOW Nodes & Teams Structure

```mermaid
graph TD
    A[Flow Node] --> B[Professional Team]
    A --> C[Volunteer / Research Team]
    A --> D[Lyceum Musaeum]
    A --> E[Baseline Resource Access]

    B --> F[Nurses / Doctors]
    B --> G[Counselors / Psychologists]
    B --> H[Specialized Healthcare Staff]

    C --> I[Researchers / Mentors]
    C --> J[Artisans / Creators / Event Organizers]

    D --> K[Workshops & Labs]
    D --> L[Library & Knowledge Archive]
    D --> M[Seminars / Digital Events]

    E --> N[Food Distribution]
    E --> O[Energy Access]
    E --> P[Tools & Equipment Access]

    classDef professional fill:#8fd3f4,stroke:#0366d6,stroke-width:2px;
    classDef volunteer fill:#f4f1a1,stroke:#d6c836,stroke-width:2px;
    classDef lyceum fill:#c4f4c4,stroke:#36d636,stroke-width:2px;
    classDef baseline fill:#f4c4c4,stroke:#d63636,stroke-width:2px;

    class B,F,G,H professional;
    class C,I,J volunteer;
    class D,K,L,M lyceum;
    class E,N,O,P baseline;