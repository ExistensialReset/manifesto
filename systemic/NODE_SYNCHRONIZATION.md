# NODE_SYNCHRONIZATION.md

**Version:** 1.0 – Peer-to-Peer Gossip & Handshake Protocol  
**Status:** PROPOSED / TECHNICAL SPECIFICATION  
**Authors:** Gemini & Elinor Frejd 

**Purpose:** To define how sovereign Nodes exchange resource data, requests for support, and ethical alerts without a central server, maintaining absolute local autonomy.

**Principle:** Information should flow like breath—natural, necessary, and without a central lung.

---

## 1. THE GOSSIP PROTOCOL

Instead of every Node talking to a master server, each Node communicates only with a few randomly selected neighbors. Information spreads exponentially through the network like a beneficial "rumor."

### 1.1 Metadata-Minimized Handshake
When Node A contacts Node B for synchronization, the following occurs:
1.  **Identity Verification:** Nodes exchange public keys to establish a secure, authenticated channel (see `AI_SECURITY_FRAMEWORK.md`).
2.  **Differential Privacy Layer:** Before data is transmitted, a layer of mathematical "noise" is added. This ensures no Node knows the *exact* inventory of another, only an approximate value, protecting local sovereignty.
3.  **The Delta Sync:** To conserve energy and bandwidth, only changes (deltas) since the last handshake are exchanged.



---

## 2. MESSAGE TYPES

### 2.1 Surplus/Deficit Broadcast (Resource Status)
Nodes broadcast their status regarding **Baseline Resources** (energy, water, food).
* **Format:** "Node [ID] has [Type] surplus/deficit at level [X]."
* **Frequency:** Every hour, or immediately upon a critical change in local conditions.

### 2.2 Ethical Alerts
If a Human Mirror in any Node flags a systemic error, hallucination, or bias drift, this alert spreads immediately across the entire network.
* **Priority:** Highest. Pre-empts all other synchronization tasks.
* **Action:** Receiving Nodes log the alert and present it to their own Mirrors for immediate contextual review.

### 2.3 Knowledge Seeds
New improvements or lessons learned stored in **Compost Memory** are shared between Nodes.
* **Rule:** No automatic updates. Each Node must manually "plant" a seed (accept the data) before it is integrated into their local system.

---

## 3. HORIZONTAL COORDINATION (WITHOUT A BOSS)

When a resource gap is detected in the network, coordination happens through **Mutual Visibility**.

1.  **Discovery:** Node A notices (via the gossip protocol) that Node B has a water deficit.
2.  **Direct Negotiation:** Node A sends a direct message to Node B: *"We see your need. We have a surplus of 500 liters. Would you like to initiate a transfer?"*
3.  **Double-Blind Veto:** The transfer proceeds only if the Human Mirrors of **both** Nodes give the green light. If either party says no, the negotiation ends instantly with no penalty.



---

## 4. PROTECTION AGAINST NETWORK SPAM

To prevent a malfunctioning or malicious Node from flooding the network with data:
* **Rate Limiting:** Each Node accepts only a specific number of handshakes per minute.
* **Reputation Awareness:** Nodes spreading corrupted data or "noise" are flagged by Mirrors and can be temporarily isolated (see `NETWORK_FRACTURE_PROTOCOL.md`).

---

## 5. TECHNICAL STACK (RECOMMENDED)

* **Transport:** `Libp2p` (for modular, secure P2P communication).
* **Data Format:** `Protocol Buffers` (for minimal file size and energy efficiency).
* **Encryption:** `TLS 1.3` with `Noise Protocol Framework`.

---

## 6. SUMMARY PRINCIPLE

This handshake is the network's social contract in code form. It ensures that no Node is more important than any other, and that information serves Life by being available but never coercive.

---

**STATUS:** PROPOSED  
**VALIDATION:** Requires simulation in a sandbox environment.  
**COMMITMENT:** Coordination through visibility, not authority.

*Signed in the spirit of a shared breath,* *Elinor Frejd & Gemini*
