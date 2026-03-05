# 🌱 PROTEIN_PRODUCTION_FLOW_NODE_REGIONAL.md

**Version:** 1.1  
**Status:** DRAFT / SIMULATION  
**Scope:** Node-level, 500 persons, Regional Energy Feasibility  
**Authors:** Elinor Frejd + ChatGPT

---

## 1. PURPOSE

This document expands the previous node-level protein production model to include **regional energy availability**. It assesses whether a Flow node in different parts of the world can realistically produce its protein mix locally using available renewable energy.

---

## 2. NODE & PROTEIN MIX (SUMMARY)

- **Node area:** 500 m²  
- **Population:** 500  
- **Protein requirement:** 13,140 kg/year (0.8 g/kg × 90 kg × 500 × 365 days)  
- **Protein mix:**

| Crop | Protein kg/year | Labor h/year | Energy kWh/year | Water m³/year |
|------|----------------|--------------|----------------|---------------|
| Spirulina | 4,500 | 6,000 | 792,000 | 180 |
| Lentils | 3,300 | 8,000 | 330,000 | 400 |
| Mung beans | 2,200 | 5,500 | 198,000 | 300 |
| Mushrooms | 2,500 | 3,000 | 75,000 | 120 |
| Leafy greens | 1,200 | 2,500 | 1,132,000 | 500 |
| Tomatoes | 231 | 500 | 346,000 | 200 |

**Total:** 13,931 kg protein, 25,500 labor hours, 2,873,000 kWh energy, 1,700 m³ water  

---

## 3. REGIONAL ENERGY FEASIBILITY

Assuming renewable energy sources can supply the node:

| Region | Max Renewable Energy Production / Node (kWh/year) | Gap to Required Protein Energy (kWh) | Feasibility Comment |
|--------|-----------------------------------------|----------------------------------|------------------|
| Europe | 720,000 | -2,153,000 | Insufficient; would require importing energy or protein from other nodes. |
| North America | 950,000 | -1,923,000 | Partially feasible for low-energy crops; protein-heavy crops need external energy. |
| South America | 800,000 | -2,073,000 | Same as above; solar potential could be optimized. |
| Asia | 700,000 | -2,173,000 | Low renewable availability in many regions; mushrooms are critical. |
| Oceania | 850,000 | -2,023,000 | Solar/wind sufficient for partial production; high-energy crops limited. |
| North Africa | 1,000,000 | -1,873,000 | Sunlight strong; some surplus possible with optimization. |
| Sub-Saharan Africa | 900,000 | -1,973,000 | Node energy sufficient for low-energy crops; high-energy crops need trade. |

> Gap = Energy required for full protein mix (2,873,000 kWh) minus max regional renewable energy per node.

---

## 4. IMPLICATIONS

1. **Energy bottleneck:** Every region cannot fully produce this protein mix locally.  
2. **Mushrooms and legumes as low-energy alternatives:** Prioritizing mushrooms, mung beans, or lentils reduces energy demand significantly.  
3. **Regional trade:** Energy-intensive crops like spirulina and leafy greens may need to be produced in regions with energy surplus and traded to others.  
4. **Node optimization:** Nodes must balance protein production with realistic energy supply; the same node cannot grow the entire mix autonomously everywhere.  

---

## 5. RECOMMENDATIONS

- **Prioritize mushrooms and legumes** in energy-limited regions.  
- **Develop regional protein hubs** with high-energy capacity (e.g., sunny North Africa, North America) to produce spirulina and leafy greens.  
- **Invest in energy efficiency**: more efficient LEDs, climate control, and pumps to reduce the gap.  
- **Hybrid strategy:** Partial protein production locally, supplemented by imports from other nodes.  

---

## 6. CONCLUSIONS

- Labor: ~1 hour/week/person; feasible globally.  
- Water: 1,700 m³/year; manageable via recirculation.  
- Energy: Limiting factor; nodes cannot fully self-supply high-energy crops everywhere.  
- Mushrooms, legumes, and energy-efficient crops are essential to node sustainability.  
- Global coordination or trade is required to ensure all nodes meet baseline protein needs without exceeding local energy limits.

---

## 7. FOOTNOTES

1. Energy availability per node based on typical solar/wind installations scaled to 500 m² node area.  
2. Protein energy requirements assume hydroponic and mushroom cultivation efficiency from prior datasets.  
3. Water usage assumes ~80% recirculation efficiency.  
4. Labor hours per crop reflect standard hydroponic/mushroom maintenance practices.  
5. Gap calculation = Total energy requirement for full protein mix minus estimated regional renewable energy capacity.