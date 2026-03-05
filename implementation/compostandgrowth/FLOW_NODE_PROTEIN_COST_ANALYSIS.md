# FLOW_NODE_PROTEIN_COST_ANALYSIS.md

## Version 1.3 – Full Node Protein Self-Sufficiency Planning
**Status:** Draft – Internal Planning  
**Scope:** 500-person Flow Node  
**Governance:** LOTUS Majority Required for Implementation

---

# Purpose

This document provides a **comprehensive, quantified plan** for protein self-sufficiency in a Flow node, including:

- Crop selection & protein yield  
- Labor and Flow-hour conversion  
- Energy & water requirements  
- Equipment specification  
- CAPEX/OPEX  
- Regional feasibility

Goal: Evaluate full self-sufficiency while respecting Flow baseline standards.

---

# I. Node & Population Assumptions

- Population: 500 individuals  
- Average Body Weight: 90 kg  
- Daily Protein Requirement: 0.8 g/kg → 72 g/day/person  
- Annual Protein Need: 13,140 kg/year total  
- Node Area: 500 m² production  
- Configuration: 120 NFT racks, 40 climate chambers, 120 LED lights, pumps, sensors, reservoirs, 50 solar modules (50 kWh each)

---

# II. Crop Mix & Protein Yield

| Crop         | Protein Yield (kg/year) | % of Total | Labor (h/kg) | Energy (kWh/kg) | Water (L/kg) |
|--------------|------------------------|------------|--------------|----------------|--------------|
| Spirulina    | 3,500                  | 27%        | 0.15         | 145            | 20           |
| Lentils      | 3,500                  | 27%        | 0.10         | 100            | 10           |
| Mung Beans   | 2,500                  | 19%        | 0.12         | 87             | 15           |
| Mushrooms    | 2,500                  | 19%        | 0.08         | 35             | 12           |
| Leafy Greens | 1,200                  | 9%         | 0.06         | 17             | 5            |
| Tomatoes     | 231                    | 1%         | 0.04         | 35             | 12           |
| **Total**    | 13,431                 | 100%       | –            | –              | –            |

> Adjusted to reduce energy-intensive spirulina proportion, increase mushrooms and legumes.

---

# III. Labor Requirements & Flow-Hour Conversion

| Crop         | Total Labor (h/year) | Hours/Person/Year | Hours/Person/Week | Cost Equivalent (USD @ $10/h) |
|--------------|-------------------|-----------------|-----------------|-------------------------------|
| Spirulina    | 525               | 1.05            | 0.02            | $5,250                        |
| Lentils      | 350               | 0.7             | 0.01            | $3,500                        |
| Mung Beans   | 300               | 0.6             | 0.01            | $3,000                        |
| Mushrooms    | 200               | 0.4             | 0.008           | $2,000                        |
| Leafy Greens | 72                | 0.144           | 0.003           | $720                          |
| Tomatoes     | 9                 | 0.018           | 0.0003          | $90                           |
| **Total**    | 1,456             | 2.912           | ~0.055          | $14,560                       |

> Labor extremely low per person. Flow-hour accounting aligns with node baseline.

---

# IV. Energy Requirements

| Crop         | Energy (kWh/kg) | Total Energy (kWh/year) |
|--------------|----------------|------------------------|
| Spirulina    | 145            | 507,500                |
| Lentils      | 100            | 350,000                |
| Mung Beans   | 87             | 217,500                |
| Mushrooms    | 35             | 87,500                 |
| Leafy Greens | 17             | 20,400                 |
| Tomatoes     | 35             | 8,085                  |
| **Total**    | –              | 1,190,985              |

> Solar modules (50 x 50 kWh) produce 125,000 kWh → node requires networked energy or higher efficiency

---

# V. Water Requirements

| Crop         | Water (L/kg) | Total Water (L/year) |
|--------------|-------------|-------------------|
| Spirulina    | 20          | 70,000            |
| Lentils      | 10          | 35,000            |
| Mung Beans   | 15          | 37,500            |
| Mushrooms    | 12          | 30,000            |
| Leafy Greens | 5           | 6,000             |
| Tomatoes     | 12          | 2,772             |
| **Total**    | –           | 181,272           |

> Fully feasible with closed-loop water systems

---

# VI. CAPEX & OPEX

| Item                     | Quantity | Unit Cost (USD) | Total (USD) |
|--------------------------|---------|----------------|------------|
| NFT Racks                | 120     | 2,000          | 240,000    |
| Climate Chambers         | 40      | 5,000          | 200,000    |
| LED Grow Lights          | 120     | 500            | 60,000     |
| Pumps & Reservoirs       | 10      | 1,000          | 10,000     |
| Sensors & Monitoring     | –       | 25,000         | 25,000     |
| Solar Modules            | 50      | 2,500          | 125,000    |
| Installation & Labor     | –       | –              | 100,000    |
| **Total CAPEX**          | –       | –              | 760,000    |

> OPEX (annual): energy, nutrients, water, replacement LEDs ~ $150,000/year

---

# VII. Regional Feasibility

| Region        | Renewable Energy (kWh/year) | Protein Energy Demand (kWh/year) | Gap (kWh) |
|---------------|----------------------------|---------------------------------|-----------|
| Europe        | 720,000                    | 1,190,985                        | 470,985   |
| North America | 950,000                    | 1,190,985                        | 240,985   |
| South America | 850,000                    | 1,190,985                        | 340,985   |
| Asia          | 900,000                    | 1,190,985                        | 290,985   |
| Oceania       | 800,000                    | 1,190,985                        | 390,985   |
| North Africa  | 1,000,000                  | 1,190,985                        | 190,985   |
| Sub-Saharan Africa | 750,000               | 1,190,985                        | 440,985   |

> Node energy networks or inter-node trade required for full self-sufficiency

---

# VIII. Recommendations

1. **Crop Adjustment**  
   - Focus on mushrooms, legumes, leafy greens in energy-limited nodes  
   - Use spirulina in high-energy nodes  
   - Explore alternative protein crops: tempeh, soy sprouts, algae  

2. **Energy Efficiency**  
   - Smart LED lighting, reflectors, growth cycle optimization  
   - Automation to reduce labor and energy per kg  

3. **Node Network Strategy**  
   - Specialized high-energy nodes produce spirulina  
   - Low-energy nodes produce mushrooms & legumes  
   - Inter-node trade for energy-intensive protein  

4. **Automation & Labor Management**  
   - Reduce total labor to ~30 h/person/year  
   - Flow-hour accounting aligns with baseline  

5. **Water Recirculation**  
   - Closed-loop systems  
   - Rainwater & greywater integration  

---

# IX. Next Steps

- Pilot test of mushroom-heavy protein mix  
- Measure real energy consumption for LED and climate chambers  
- Calculate regional CAPEX/OPEX variations  
- Develop INTER-NODE_PROTEIN_FLOW_PROTOCOL for trade & energy sharing  

---

# X. Conclusion

- Protein self-sufficiency is **feasible** with proper crop mix, automation, and networked energy  
- Mushrooms and legumes reduce energy bottleneck  
- Spirulina remains energy-intensive → best for high-energy nodes  
- Full self-sufficiency requires Flow node cooperation and inter-node trade  

---

# End of Document
