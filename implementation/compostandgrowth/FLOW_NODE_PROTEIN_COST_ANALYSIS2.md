# FLOW_NODE_PROTEIN_COST_ANALYSIS.md
## Version 2.0
## Status: Pilot & Global Planning
## Scope: 500-Person Flow Node, 500 m²
## Governance: LOTUS Majority Required for Modifications

---

# PURPOSE

This document provides a comprehensive, quantitative plan for **protein self-sufficiency** in a Flow Node. It integrates:

- Crop yields & protein content
- Energy & water requirements
- Labor in Flow-hours
- Equipment (CAPEX) and operational costs (OPEX)
- Regional energy feasibility
- Recommendations for automation and inter-node protocols

---

# I. NODE & POPULATION ASSUMPTIONS

- Population: 500 individuals  
- Average body weight: 90 kg  
- Annual protein requirement: 13,140 kg (500 × 0.8 g/kg/day × 365 days)  
- Cultivation area: 500 m²  
- Automation Level: 3–4 (climate control, LED, robotic handling, recirculation)

---

# II. PROTEIN CROP MIX & YIELD

| Crop            | Protein kg/yr | Labor h/kg | Energy kWh/kg | Water L/kg | Notes |
|-----------------|---------------|------------|---------------|------------|-------|
| Spirulina       | 3,500         | 0.15       | 145           | 20         | High-protein algae; energy-intensive |
| Lentils         | 3,500         | 0.10       | 100           | 10         | Energy-efficient, robust |
| Mung Beans      | 2,500         | 0.12       | 87            | 15         | Fast-growing legume |
| Mushrooms       | 2,500         | 0.08       | 35            | 12         | Low-energy, high-yield |
| Leafy Greens    | 1,200         | 0.05       | 17            | 5          | Complementary protein |
| Tomatoes        | 231           | 0.06       | 35            | 12         | Minor protein contribution |
| **Total**       | **13,431**    | –          | –             | –          | Slight surplus over requirement |

---

# III. LABOR REQUIREMENTS & FLOW-HOURS

- Total labor: 1,456 hours/year  
- Per person: 2.9 hours/year (~0.06 h/week)  
- Assumes Automation Level 3–4 with robotic harvest, automated climate and nutrient control

> Notes: Automation assumptions must be verified in pilot.

---

# IV. ENERGY REQUIREMENTS

- Total energy for protein crops: 1,190,985 kWh/year  

| Crop            | Energy kWh/kg | Annual kWh |
|-----------------|---------------|------------|
| Spirulina       | 145           | 507,500    |
| Lentils         | 100           | 350,000    |
| Mung Beans      | 87            | 217,500    |
| Mushrooms       | 35            | 87,500     |
| Leafy Greens    | 17            | 20,400     |
| Tomatoes        | 35            | 8,085      |

**Total:** 1,190,985 kWh/year  

> Recommendations: Prioritize mushrooms and legumes in energy-limited nodes. Use spirulina in high-energy nodes.

---

# V. WATER REQUIREMENTS

- Total water: 181,272 L/year (~362 L/person/year)  
- Fully feasible with recirculating hydroponics / rainwater integration

| Crop            | Water L/kg | Annual L |
|-----------------|------------|----------|
| Spirulina       | 20         | 70,000   |
| Lentils         | 10         | 35,000   |
| Mung Beans      | 15         | 37,500   |
| Mushrooms       | 12         | 30,000   |
| Leafy Greens    | 5          | 6,000    |
| Tomatoes        | 12         | 2,772    |

---

# VI. CAPEX & OPEX

| Item                  | Quantity | Cost (USD) | Notes |
|-----------------------|----------|------------|-------|
| NFT Racks             | 120      | 240,000    | 4 tiers per rack |
| Climate Chambers       | 40       | 200,000    | Fully automated |
| LED Grow Lights        | 120      | 60,000     | Smart LED |
| Pumps & Reservoirs     | 10       | 10,000     | Recirculating system |
| Sensors & Monitoring   | –        | 25,000     | Climate, nutrient, water sensors |
| Solar + Wind Modules   | 50       | 125,000    | Must clarify production/day vs year |
| Installation & Labor   | –        | 100,000    | One-time CAPEX |
| **Total CAPEX**        | –        | 760,000    | – |

**OPEX:** ~150,000 USD/year for energy, nutrients, water, replacement parts

> Clarification needed: actual solar/wind production and coverage.

---

# VII. REGIONAL ENERGY FEASIBILITY

| Region              | Available kWh/year | Deficit (kWh/year) | Strategy |
|--------------------|-----------------|------------------|----------|
| Europe             | 720,000         | 470,985          | Import spirulina; focus mushrooms/legumes |
| North America      | 950,000         | 240,985          | Hybrid production; possible spirulina |
| South America      | 850,000         | 340,985          | Hybrid; mushrooms & legumes priority |
| Asia               | 900,000         | 290,985          | Hybrid; mushrooms & legumes priority |
| Oceania            | 800,000         | 390,985          | Import spirulina; mushrooms/legumes focus |
| North Africa       | 1,000,000       | 190,985          | Spirulina possible; export surplus |
| Sub-Saharan Africa | 750,000         | 440,985          | Mushrooms/legumes focus; import high-energy crops |

---

# VIII. INTER-NODE PROTEIN PROTOCOL (DRAFT)

1. Nodes identify **surplus / deficit** per crop monthly.  
2. Surplus high-energy protein (spirulina) exported to energy-limited nodes.  
3. Energy-efficient protein (mushrooms, legumes) produced locally in energy-limited nodes.  
4. Trade agreements encoded in **INTER-NODE_PROTEIN_FLOW_PROTOCOL.md**.  
5. Recirculating nutrient streams and waste products can be shared regionally.

---

# IX. RECOMMENDATIONS

- Pilot with **mushroom-heavy, legume-rich protein mix** in energy-limited node.  
- Automate labor-intensive processes (Automation Level 3–4).  
- Maximize LED efficiency, add reflectors, optimize cycles.  
- Implement energy storage and hybrid generation (solar + wind).  
- Model inter-node protein flows for full self-sufficiency.  
- Monitor real energy and labor usage for validation.

---

# X. CONCLUSION

- Protein self-sufficiency is feasible **with automation, optimized crop mix, and node network collaboration**.  
- Full energy self-sufficiency for high-energy crops (spirulina) requires either **energy surplus nodes** or **inter-node trade**.  
- Water and labor requirements are manageable within Flow-node framework.  
- Next step: pilot implementation + simulation of inter-node flows + refinement of energy models.

---

# XI. FOOTNOTES / CLARIFICATIONS

- All energy and water numbers per kg assume recirculating hydroponics/controlled climate.  
- Labor assumes high automation: robotic harvest, automated nutrient and climate control.  
- Solar + Wind module production must be clearly defined: kWh/day vs kWh/year.  
- CAPEX/OPEX numbers are indicative; regional variation must be applied.

---
