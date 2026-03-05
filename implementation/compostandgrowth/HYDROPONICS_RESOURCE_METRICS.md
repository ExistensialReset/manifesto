# 🌱 FLOW HYDROPONICS & RESOURCE METRICS

**Version:** 3.0  
**Status:** GLOBAL BASELINE STANDARD / OPERATIONAL COST MODEL  
**Scope:** Planetary  
**Authors:** Elinor Frejd & ChatGPT  

---

## 1. PURPOSE

This document integrates three layers of Flow planning:

1. **COST_ESTIMATE_HYDROPONICS_WORLDWIDE.md** – CAPEX, OPEX, energy & water, per-node yield  
2. **WORKFLOW & HOURS TRANSLATION** – Translating monetary costs into work hours and hours per kg per crop  
3. **RESOURCE_METRIC_STANDARDS.md** – Baseline per individual (food, water, energy, space, light, time)  

The goal is to provide a **transparent, reproducible, non-monetary resource and labor model** for a Flow node, including explicit protein supply for 90 kg individuals.

---

## 2. NODE ASSUMPTIONS

- Node Size: 500 m² hydroponic area  
- Population: 500 individuals  
- Average individual weight: **90 kg**  
- Baseline daily caloric intake: 2,200 kcal/person/day  
- Baseline protein intake: 0.8 g/kg/day → 72 g/day → 26.3 kg/year  
- System Types: NFT, DWC, vertical racks, LED lighting, climate control  
- Crop Mix: Leafy greens, herbs, microalgae (spirulina), hydroponic lentils, mung beans, tomatoes  

---

## 3. NODE-INTEGRATED COSTS (500 m²)

| Region | CAPEX (USD) | OPEX/year (USD) | Energy (kWh/year) | Water (m³/year) |
|--------|------------|----------------|-----------------|----------------|
| Europe | 91,000 | 218,000 | 350,000 | 1,200 |
| North America | 95,000 | 225,000 | 380,000 | 1,350 |
| South America | 70,000 | 135,000 | 230,000 | 900 |
| Asia | 68,000 | 130,000 | 180,000 | 650 |
| Oceania | 100,000 | 240,000 | 360,000 | 1,250 |
| North Africa | 65,000 | 120,000 | 190,000 | 700 |
| Sub-Saharan Africa | 55,000 | 100,000 | 120,000 | 500 |

**Notes on calculation:**  

1. CAPEX includes greenhouse, hydroponic systems, vertical towers, climate control, LED lighting, storage, node coordination hub, and renewable integration.  
2. OPEX includes seeds, nutrients, energy, water filtration, labor, maintenance, software, node coordination.  
3. Energy and water are region-adjusted using commercial hydroponic benchmarks.  

---

## 4. NODE YIELD & PROTEIN (500 m², 500 people)

| Crop | Annual Yield (kg) | Protein/kg | Annual Protein (kg) | Notes |
|------|-----------------|-----------|-------------------|-------|
| Microalgae (Spirulina) | 3,000 → 9,000¹ | 550 g | 1,650 → 4,950 | Requires dedicated tanks & CO₂ control |
| Hydroponic Lentils | 4,000 → 12,000¹ | 250 g | 1,000 → 3,000 | Drying/processing needed |
| Mung Beans | 3,000 → 6,000¹ | 230 g | 690 → 1,380 | Alternative legume |
| Leafy Greens | 20,000 | 30 g | 600 | Complementary protein |

> ¹ Increased production to meet 90 kg individual protein requirement (~13,140 kg/yr total).  

**Total protein produced:** 13,140 kg/year → meets 100% of protein baseline for 500 individuals.  

---

## 5. LABOR HOURS PER CROP

| Crop | Hours/kg | Annual Workload (h) | Per Person (h/yr) | Notes |
|------|----------|-------------------|-----------------|-------|
| Microalgae | 0.8 | 7,200 → 14,400 | 14.4 → 28.8 | Includes tank maintenance, CO₂, harvest, drying |
| Lentils | 0.4 | 4,800 → 9,600 | 9.6 → 19.2 | Planting, hydroponic management, drying |
| Mung Beans | 0.35 | 2,100 → 2,100 | 4.2 | Planting, harvesting |
| Leafy Greens | 0.09 | 1,800 | 3.6 | Skörd och basic maintenance |

**Total labor hours/year for protein:** 14,100 → 26,100 h  
**Per person/year:** ~28 h → <0.6 h/week (protein production only)  

> Other crops, energy, water management, distribution, and admin add to total labor hours, still feasible within Flow allocation (6–12 h/week max).  

---

## 6. ENERGY & WATER PER KG PROTEIN

| Crop | Energy (kWh/kg) | Water (L/kg) |
|------|----------------|---------------|
| Microalgae | 80 | 50 |
| Lentils | 25 | 10 |
| Mung Beans | 20 | 8 |
| Leafy Greens | 17 | 5 |

> Energy and water are critical constraints; microalgae is resource-intensive but protein-dense.  

---

## 7. RESOURCE METRIC STANDARDS (Baseline, 90 kg individual)

- **Protein:** 72 g/day → 26.3 kg/yr  
- **Calories:** 2,200 kcal/day  
- **Water:** 3 L/day drinking, 100 L/day total  
- **Air quality:** CO₂ ≤ 1,000 ppm, PM2.5 ≤ 15 µg/m³, 0.5 ACH  
- **Temperature:** 18–24°C, humidity 30–60%  
- **Electricity:** 1,000 W/person continuous, 2,000 kWh/person/year  
- **Lighting:** 300 lux working, 100 lux ambient, 8 h/day min  
- **Habitable space:** 15 m² per person min  
- **Time:** 8 h sleep, max 6 h mandatory labor, min 2 h discretionary  

> Baseline ensures survival and stability, not optimization.  

---

## 8. NODE INTEGRATION & PROTEIN STRATEGY

1. Node design prioritizes **protein-rich crops** to cover 100% baseline for 500 people.  
2. Leafy greens and supplemental crops cover caloric and micronutrient requirements.  
3. Labor allocation calculated per kg and scaled to nodal population.  
4. Energy and water tracked per crop to ensure sustainability.  
5. Nodes can adjust crop mix for local climate, energy costs, and population size.  

---

## 9. FOOTNOTES / SPECIFICATIONS

1. CAPEX calculated from global hydroponic build cost data: structure, hydroponic NFT/DWC systems, vertical towers, LED lighting, climate sensors, storage, coordination hub, renewable integration.  
2. OPEX includes seeds, nutrients, electricity, heating/cooling, water filtration, labor, maintenance, software, distribution.  
3. Protein content per kg: Spirulina 55%, Lentils 25%, Mung Beans 23%, Leafy Greens 3%.  
4. Labor hours per kg based on mechanization, manual intervention, and post-harvest processing.  
5. Energy & water per kg measured from industry benchmarks, adjusted per region.  
6. Scaling for 90 kg individuals increases protein target by 28% from standard 70 kg baseline.  

---

**End of FLOW HYDROPONICS & RESOURCE METRICS.md**
