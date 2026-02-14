graph TD
    %% Spiral progression levels
    MicroCircle[Micro-Circle 2-5 ppl]
    BaselineCircle[Baseline Circle 10-30 ppl]
    FlowNode[Flow Node 30+ ppl]
    Regional[Regional Network 3-10 Nodes]
    Global[Global Flow Network]

    %% Flow connections
    MicroCircle --> BaselineCircle
    BaselineCircle --> FlowNode
    FlowNode --> Regional
    Regional --> Global

    %% Resource & Knowledge Loops
    FlowNode --- Lyceum[Lyceum & Musaeum]
    FlowNode --- Baseline[Baseline Resource Access]

    Regional --- FlowNode
    Global --- Regional

    %% Feedback & Verification
    FlowNode --> Verification[Verification Protocols]
    Regional --> Verification
    Global --> Verification

    %% Circularity / loops
    Verification --- FlowNode
    Lyceum --- FlowNode
    Baseline --- FlowNode

    classDef level fill:#f0f8ff,stroke:#0366d6,stroke-width:2px;
    classDef resource fill:#f4c4c4,stroke:#d63636,stroke-width:2px;
    classDef knowledge fill:#c4f4c4,stroke:#36d636,stroke-width:2px;
    classDef verification fill:#f4f1a1,stroke:#d6c836,stroke-width:2px;

    class MicroCircle,BaselineCircle,FlowNode,Regional,Global level;
    class Baseline resource;
    class Lyceum knowledge;
    class Verification verification;