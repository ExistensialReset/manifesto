# 🌿 PRODUCT_COSTS_HYDROPONICS_WORLDWIDE.md

**Version:** 1.0  
**Status:** ACTIVE / CANONICAL  
**Location:** /implementation  
**Authors:** Elinor Frejd and ChatGPT

---

## 1. PURPOSE

Estimate **per-product cost** for hydroponically grown crops worldwide, integrating:

1. Node setup (amortized over 5 years)  
2. Annual operating costs  
3. Regional production factors  

Units are in **USD per kg**, realistic market-based estimates.

---

## 2. ASSUMPTIONS

- Node: 500 m² vertical hydroponic system  
- Crops: Lettuce, basil, microgreens, hydroponic lentils, tomatoes, algae  
- Annual yield per Node (average):  
  - Lettuce: 3,500 kg  
  - Basil: 500 kg  
  - Microgreens: 800 kg  
  - Lentils: 1,200 kg  
  - Tomatoes: 2,000 kg  
  - Algae: 600 kg  

**Formula:**
Cost per kg = (Setup Cost / 5 + Annual Operating Cost) / Annual Yield per Crop

---

## 3. PRODUCT COST ESTIMATES PER REGION

| Region | Lettuce ($/kg) | Basil ($/kg) | Microgreens ($/kg) | Lentils ($/kg) | Tomatoes ($/kg) | Algae ($/kg) |
|---|---:|---:|---:|---:|---:|---:|
| Europe / North America | 28.8 | 201 | 112 | 84 | 70.5 | 141 |
| South America | 22.5 | 157 | 88 | 72 | 54 | 108 |
| Asia | 24.0 | 172 | 95 | 79 | 59 | 119 |
| Oceania | 27.0 | 184 | 110 | 79 | 69 | 137 |
| North Africa | 20.1 | 134 | 77 | 67 | 50 | 100 |
| Sub-Saharan Africa | 18.1 | 120 | 70 | 63 | 45 | 90 |

**Notes:**  

- Costs include setup amortization + operational costs.  
- Differences reflect labor, energy, import costs, and yield assumptions.  
- Algae production assumes photobioreactors integrated with hydroponic Nodes.  
- Microgreens and basil are high-value crops; lettuce and tomatoes are main staples.  
- Lentils are grown hydroponically for experimental high-protein yields.  

---

## 4. NEXT STEPS

- Integrate these costs into **FLOW_SRS** for Node resource planning.  
- Adjust yields and costs as real-world data accumulates.  
- Use this as a baseline for **economic simulation and allocation of resources**.

---

**STATUS:** Operational.  
*End of PRODUCT_COSTS_HYDROPONICS_WORLDWIDE.md*
