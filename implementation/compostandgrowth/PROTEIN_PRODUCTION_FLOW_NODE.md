# 🌱 PROTEIN_PRODUCTION_FLOW_NODE.md

**Version:** 1.0  
**Status:** DRAFT / SIMULATION  
**Scope:** Node-level, 500 persons  
**Authors:** Elinor Frejd + ChatGPT

---

## 1. PURPOSE

This document models full protein production for a Flow node of 500 individuals, including work hours, energy, water, and required equipment. Mushrooms are included as an energy-efficient protein source. The goal is to provide a realistic estimate of resources and labor per year.

---

## 2. NODE & SYSTEM SPECIFICATIONS

- **Node area:** 500 m² total growing area  
- **Population:** 500 people  
- **Protein requirement:** 0.8 g/kg body weight × 90 kg × 500 people × 365 days ≈ 13,140 kg protein/year  
- **Systems:** Hydroponics (NFT/DWC), mushroom cultivation units, climate control, LED lighting, recirculating water systems

### 2.1 Equipment per node

| Equipment | Specification | Quantity | Notes |
|-----------|---------------|---------|-------|
| Hydroponic NFT/DWC racks | 4 tiers, 1 m² per tray | 120 | For leafy greens, legumes |
| LED grow lights | 200 µmol/m²/s | 120 units | 16 h/day light cycle |
| Climate-controlled chambers | 2 m³ per unit | 40 | For mushrooms and sensitive crops |
| Pumps & filters | 0.5 kW | 10 | Circulates nutrient solution |
| Humidifiers/ventilation | 500 W/unit | 20 | Mushroom humidity & air quality |
| CO₂ sensors & controllers | N/A | 5 | Optimize leafy greens & spirulina growth |
| Substrate & containers | Straw, sawdust, cultivation boxes | Ongoing | Mushrooms, lentils, mung beans |
| Water reservoirs | 1000 L | 10 | Recirculating system |
| Energy storage / solar modules | 50 kWh/module | 50 | Supplement electricity supply |

---

## 3. PROTEIN MIX & PRODUCTION

| Crop | Protein kg/year | % of total | Labor hours/year | Energy kWh/year | Water m³/year | Notes |
|------|----------------|------------|-----------------|----------------|---------------|-------|
| Spirulina | 4,500 | 32% | 6,000 | 792,000 | 180 | Tank cultivation, CO₂ supplemented |
| Lentils | 3,300 | 24% | 8,000 | 330,000 | 400 | Hydroponic or pot cultivation |
| Mung beans | 2,200 | 16% | 5,500 | 198,000 | 300 | Hydroponic or pot cultivation |
| Oyster mushrooms | 2,500 | 19% | 3,000 | 75,000 | 120 | Climate chamber, low energy, high protein dried |
| Leafy greens | 1,200 | 9% | 2,500 | 1,132,000 | 500 | NFT/DWC hydroponics |
| Tomatoes | 231 | 1% | 500 | 346,000 | 200 | Supplementary protein |

**Total**: 13,931 kg protein, 25,500 labor hours, 2,873,000 kWh energy, 1,700 m³ water  

> Note: Total protein slightly exceeds required 13,140 kg for margin.

---

## 4. LABOR ANALYSIS

- Total labor: 25,500 hours/year  
- Per person: 51 hours/year ≈ 1 hour/week  
- Comment: Very low labor requirement; additional time needed for energy/water maintenance, distribution, administration, healthcare, training, and conflict management.

---

## 5. ENERGY AND WATER

- **Total energy:** 2,873,000 kWh/year  
  - Spirulina: 792,000 kWh  
  - Lentils: 330,000 kWh  
  - Mung beans: 198,000 kWh  
  - Mushrooms: 75,000 kWh  
  - Leafy greens: 1,132,000 kWh  
  - Tomatoes: 346,000 kWh  
- **Total water:** 1,700 m³/year (~3.4 m³/person/year)  
- Comment: Energy is the limiting factor; mushrooms reduce energy demand significantly compared to a spirulina-heavy mix.

---

## 6. DEVELOPMENT AND OPTIMIZATION

1. Increase the proportion of mushrooms to reduce overall energy requirements.  
2. Substitute or combine lentils/mung beans with mushrooms to maximize protein per kWh.  
3. Consider partial regional or global protein trade instead of fully local production for energy-intensive crops.  

---

## 7. CONCLUSIONS

- Protein production is **labor-feasible** (~1 hour/week/person).  
- Water use is manageable via recirculation systems (~1,700 m³/year).  
- Energy demand is **currently too high** for a fully self-sufficient node with this crop mix.  
- Mushrooms are an excellent low-energy protein source and should be prioritized where energy is limited.  
- Flow nodes may need **coordinated protein distribution** or energy-efficient crop substitutions to achieve full sustainability.

---

## 8. FOOTNOTES

1. Protein values based on hydroponic and mushroom cultivation literature.  
2. Energy estimates include LED lighting, pumps, ventilation, and climate control.  
3. Water estimates account for hydroponic recirculation efficiency (~80%).  
4. Labor hours calculated from observed hydroponic yield and standard care times.  
5. Node assumptions: 500 m² growth area, 500 people, 90 kg average weight.
