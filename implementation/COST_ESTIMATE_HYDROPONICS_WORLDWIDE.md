# COST_ESTIMATE_HYDROPONICS_WORLDWIDE.md

**Version:** 1.0  
**Status:** ACTIVE / CANONICAL  
**Location:** `/implementation/COST_ESTIMATE_HYDROPONICS_WORLDWIDE.md`  
**Authors:** Elinor Frejd & ChatGPT

---

## 1. PURPOSE

This document estimates the 10-year costs for building, operating, and sustaining hydroponics-based Flow Nodes globally. Costs are calculated for Europe/North America, South America, Oceania, Asia, North Africa, and Sub-Saharan Africa, providing baseline planning for FLOW_SRS.

---

## 2. NODE PARAMETERS

| Parameter | Description |
|-----------|-------------|
| Population per Node | 50–500 people |
| Hydroponic area | 2–5 m² per person for leafy greens, scaled by Node population |
| Energy autonomy | 100% renewable energy target (solar + wind + battery storage) |
| Water recycling | 90–95% recovery and reuse |
| Production target | 200–300 kg/year/person of leafy greens, herbs, and vegetables |

---

## 3. CAPITAL COST ESTIMATES (USD per Node)

| Region | Construction & Infrastructure | Hydroponic Systems | Renewable Energy | Water Treatment & Pumps | Total per Node |
|--------|------------------------------|------------------|-----------------|------------------------|----------------|
| Europe/North America | 1,500,000 | 750,000 | 500,000 | 250,000 | 3,000,000 |
| South America | 800,000 | 400,000 | 250,000 | 150,000 | 1,600,000 |
| Oceania | 1,200,000 | 600,000 | 400,000 | 200,000 | 2,400,000 |
| Asia | 900,000 | 450,000 | 300,000 | 150,000 | 1,800,000 |
| North Africa | 700,000 | 350,000 | 200,000 | 120,000 | 1,370,000 |
| Sub-Saharan Africa | 500,000 | 250,000 | 150,000 | 100,000 | 1,000,000 |

---

## 4. ANNUAL OPERATING COSTS (USD per Node)

| Region | Staff & Expertise | Energy Maintenance | Nutrient & Inputs | Water Management | Miscellaneous | Total Annual |
|--------|-----------------|-----------------|-----------------|----------------|---------------|--------------|
| Europe/North America | 300,000 | 50,000 | 60,000 | 20,000 | 10,000 | 440,000 |
| South America | 150,000 | 25,000 | 30,000 | 12,000 | 5,000 | 222,000 |
| Oceania | 240,000 | 40,000 | 50,000 | 16,000 | 8,000 | 354,000 |
| Asia | 180,000 | 30,000 | 40,000 | 15,000 | 7,000 | 272,000 |
| North Africa | 140,000 | 25,000 | 30,000 | 12,000 | 5,000 | 212,000 |
| Sub-Saharan Africa | 100,000 | 20,000 | 25,000 | 10,000 | 5,000 | 160,000 |

---

## 5. 10-YEAR TOTAL COST (CAPEX + OPEX)

| Region | 10-Year Total Estimate |
|--------|-----------------------|
| Europe/North America | 7,400,000 |
| South America | 3,820,000 |
| Oceania | 6,940,000 |
| Asia | 4,520,000 |
| North Africa | 3,490,000 |
| Sub-Saharan Africa | 2,600,000 |

**Assumptions:**
- CAPEX upfront in year 0  
- OPEX annual, inflated at 2% per year  
- Energy systems maintained for 10 years with minor replacements included  
- Labor includes skilled hydroponics operators and Node coordinators  

---

## 6. NOTES AND CONSIDERATIONS

1. **Scaling:** Costs scale linearly with Node population; economies of scale reduce per-person costs for Nodes above 200 people.  
2. **Energy Dependence:** High renewable penetration increases CAPEX but reduces OPEX over time.  
3. **Local Material Sourcing:** Cost variations depend on proximity to hydroponic hardware manufacturers.  
4. **Risk Factors:** Political stability, water availability, import tariffs, and local expertise can significantly impact actual costs.  
5. **Currency Fluctuation:** All costs expressed in USD; regional currencies may fluctuate affecting capital needs.  

---

## 7. NEXT STEPS

- Integrate into `/systemic/FLOW_SRS.md` for global planning.  
- Update annually with real-world data from deployed Nodes.  
- Explore modular Node designs to reduce CAPEX in lower-income regions.  
- Evaluate potential subsidies or material sharing between Nodes globally.  

---

*End of COST_ESTIMATE_HYDROPONICS_WORLDWIDE.md*

**Version:** 1.0  
**Status:** Active  
**Scope:** Global Hydroponic Nodes  
**Location:** /implementations

**Authors:** Elinor Frejd, Gemini, DeepSeek  
**Date:** 2026-03-04  

---

# PURPOSE

Provide a comprehensive cost estimate for establishing hydroponic Nodes worldwide, per region, to fulfill baseline nutrition requirements.  
Integrates with FLOW_SRS.md for resource allocation, RTC-Guardian, and Sigma-Flow.

---

# I. ASSUMPTIONS

- **Node Size:** ~100 people per Node  
- **Modules per Node:** 6 hydroponic modules (~100 m² each)  
- **Regional Network:** 5–20 Nodes per region  
- **Energy Source:** Solar + grid backup  
- **Water Efficiency:** 10 L/kg produce  
- **Baseline Coverage:** 100% of recommended daily intake per Node  
- **Costs Include:** Construction, equipment, installation, training, annual operation

---

# II. COST ELEMENTS PER NODE

| Component | Capital Cost (USD) | Annual Operating Cost (USD) | Notes |
|-----------|------------------|----------------------------|-------|
| Hydroponic Modules | 300,000 | 30,000 | LED, pumps, tanks, sensors |
| Node Building / Infrastructure | 100,000 | 10,000 | Housing for modules, distribution hub |
| Backup Soil Modules | 50,000 | 5,000 | Contingency in case of failure |
| Energy & Water Systems | 80,000 | 20,000 | Solar panels, batteries, water filtration |
| Lyceum Workshop Setup | 40,000 | 5,000 | Training, tools, knowledge center |
| Personnel (Operators + Support) | 0 | 50,000 | Covered by baseline, estimate equivalent value |
| Contingency | 50,000 | 0 | 10–15% of capital |

**Total per Node:** Capital ≈ $620,000 | Annual Operating ≈ $120,000

---

# III. COST ESTIMATES PER REGION

| Region | Nodes | Capital Cost (Million USD) | Annual Operating Cost (Million USD) | Notes |
|--------|-------|---------------------------|------------------------------------|-------|
| Europe | 20 | 12.4 | 2.4 | Higher labor & energy costs |
| North America | 20 | 12.4 | 2.4 | Similar to Europe |
| South America | 20 | 9.0 | 1.6 | Lower construction cost, higher logistics |
| Oceania | 5 | 3.1 | 0.6 | Smaller network, high shipping costs |
| Asia | 20 | 10.8 | 2.0 | Costs vary widely by country |
| North Africa | 10 | 6.2 | 1.2 | Desert conditions, higher water setup |
| Sub-Saharan Africa | 10 | 6.2 | 1.2 | Logistics & power infrastructure impact |

**Global Total:** Capital ≈ $60.1 million | Annual Operating ≈ $11.4 million

> Note: Estimates may vary ±20–30% due to local construction, energy, and labor differences.

---

# IV. ADDITIONAL NOTES

1. **Scaling Up:** Economies of scale for modules, energy, and coordination nodes (RCN).  
2. **Energy Optimization:** Solar power reduces operating cost over time.  
3. **Hydroponic Efficiency:** LED & nutrient recycling improve water/energy efficiency by 10–30%.  
4. **Regional Coordination Nodes (RCN):** Estimated $250k per RCN, annual ops $50k.  
5. **Contingency:** Disaster recovery, redundancy, and spare parts included in line items; extreme events may require additional budgeting.

---

# V. INTEGRATION WITH FLOW_SRS.md

- Capital and operating costs feed into:  
  - **RTC-Guardian** (resource timing & flow capacity)  
  - **Sigma-Flow allocation** (creative surplus vs. necessity)  
  - **Baseline Shield** (ensuring nutrition & access stability)  
- Regional data adjusts global flow (~5% for specialty trade).

---

# VI. VERSIONING AND COMPOST POLICY

- **Version 1.0** → MAJOR update  
- First global hydroponic cost estimation → root active file  
- Previous versions (if any) moved to `/compostandgrowth`  
- Ensures genealogical traceability per VERSIONING_AND_COMPOST_POLICY.md

---

**Implementation Reference:** FOOD_SYSTEM_P2.md  
**Version:** 1.0 — Preliminary Global Cost Estimation  
**Purpose:** Provide estimated capital and annual operating costs for regional hydroponic networks to meet baseline nutrition in multiple Nodes worldwide.

---

## 1. ASSUMPTIONS

- **Node Size:** ~100 people per Node  
- **Modules per Node:** 6 hydroponic modules (~100 m² each)  
- **Regional Network:** 5–20 Nodes per region  
- **Energy Source:** Solar + grid backup (where available)  
- **Water Efficiency:** 10 L/kg produce  
- **Baseline Coverage:** 100% of recommended daily intake per Node  
- **Costs:** Include construction, equipment, installation, training, and annual operation

---

## 2. COST ELEMENTS PER NODE

| Component | Capital Cost (USD) | Annual Operating Cost (USD) | Notes |
|-----------|------------------|----------------------------|-------|
| Hydroponic Modules | 300,000 | 30,000 | LED, pumps, tanks, sensors |
| Node Building / Infrastructure | 100,000 | 10,000 | Housing for modules, distribution hub |
| Backup Soil Modules | 50,000 | 5,000 | Contingency in case of failure |
| Energy & Water Systems | 80,000 | 20,000 | Solar panels, batteries, water filtration |
| Lyceum Workshop Setup | 40,000 | 5,000 | Training, tools, knowledge center |
| Personnel (Operators + Support) | 0 | 50,000 | Covered by baseline, estimate equivalent value |
| Contingency | 50,000 | 0 | 10–15% of capital |

**Total per Node:** Capital ≈ $620,000 | Annual Operating ≈ $120,000

---

## 3. COST ESTIMATES PER REGION

| Region | Nodes | Capital Cost (Million USD) | Annual Operating Cost (Million USD) | Notes |
|--------|-------|---------------------------|------------------------------------|-------|
| Europe | 20 | 12.4 | 2.4 | Higher labor & energy costs |
| North America | 20 | 12.4 | 2.4 | Similar to Europe |
| South America | 20 | 9.0 | 1.6 | Lower construction cost, higher logistics |
| Oceania | 5 | 3.1 | 0.6 | Smaller network, high shipping costs |
| Asia | 20 | 10.8 | 2.0 | Costs vary widely by country |
| North Africa | 10 | 6.2 | 1.2 | Desert conditions, higher water setup |
| Sub-Saharan Africa | 10 | 6.2 | 1.2 | Logistics & power infrastructure impact |

**Global Total:** Capital ≈ $60.1 million | Annual Operating ≈ $11.4 million  

> Note: These are conservative preliminary estimates. Local variations in construction, energy costs, and labor can increase or decrease totals ±20–30%.

---

## 4. ADDITIONAL NOTES

1. **Scaling Up:** Increasing Nodes per region increases economies of scale for modules, energy, and RCN.  
2. **Energy Optimization:** Fully solar-powered Nodes reduce operating costs over time.  
3. **Hydroponic Efficiency:** Advances in LED and nutrient recycling can reduce water/energy costs by 10–30%.  
4. **Regional Coordination Nodes (RCN):** Not included in per-Node costs. Estimated $250k per RCN, annual ops $50k.  
5. **Contingency:** Disaster recovery, redundancy, and spare parts are included in contingency line, but extreme events could require additional budgeting.

---

## 5. INTEGRATION WITH FLOW_SRS.md

- The above cost model provides baseline data for **regional implementation metrics** in FLOW_SRS.md.  
- Capital and operational expenses feed into:  
  - RTC-Guardian (resource timing and flow capacity)  
  - Sigma-Flow allocation (creative surplus vs. necessity)  
  - Baseline Shield (ensuring nutrition and access stability)  
- Adjust per-region data for global coordination and specialty trade (~5% global flow).

---