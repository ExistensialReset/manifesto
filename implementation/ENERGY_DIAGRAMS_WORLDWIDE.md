# ENERGY_DIAGRAMS_WORLDWIDE.md

**Version:** 1.0  
**Status:** ACTIVE / CANONICAL  
**Repository Location:** `/implementation/ENERGY_DIAGRAMS_WORLDWIDE.md`  
**Authors:** Elinor Frejd and ChatGPT  

---

## 1. PURPOSE

Provides a **text-based visual overview** of renewable energy production, Node-level surplus, and cost per kWh for all regions.  
Everything is fully **markdown-compatible (INUTI)**.

---

## 2. ENERGY PRODUCTION BY SOURCE (kWh/year per Node)

| Region          | Solar    | Wind     | Biogas  | Geothermal | Total Energy |
|-----------------|---------|---------|---------|------------|--------------|
| Europe          | 200 000 | 90 000  | 180 000 | 250 000    | 720 000      |
| North America   | 230 000 | 110 000 | 190 000 | 280 000    | 810 000      |
| South America   | 180 000 | 70 000  | 160 000 | 200 000    | 610 000      |
| Oceania         | 240 000 | 100 000 | 200 000 | 300 000    | 840 000      |
| Asia            | 210 000 | 80 000  | 170 000 | 240 000    | 700 000      |
| North Africa    | 220 000 | 60 000  | 150 000 | 220 000    | 650 000      |
| Sub-Saharan Africa | 190 000 | 50 000 | 140 000 | 200 000    | 580 000      |

> Text-based stacked representation: `█ Solar █ Wind █ Biogas █ Geothermal`

---

## 3. NODE SURPLUS / DEFICIT

| Region           | Energy Produced | Baseline Load | Surplus/Deficit |
|-----------------|----------------|---------------|----------------|
| Europe          | 720 000        | 500 000       | +220 000       |
| North America   | 810 000        | 500 000       | +310 000       |
| South America   | 610 000        | 500 000       | +110 000       |
| Oceania         | 840 000        | 500 000       | +340 000       |
| Asia            | 700 000        | 500 000       | +200 000       |
| North Africa    | 650 000        | 500 000       | +150 000       |
| Sub-Saharan Africa | 580 000     | 500 000       | +80 000        |

> Surplus energy can be shared across regional Nodes via Flow coordination.

---

## 4. COST PER KWH VISUAL

| Region             | Cost per kWh (USD) | Bar |
|-------------------|------------------|-----|
| Europe             | 0.40             | ████████ |
| North America      | 0.42             | █████████ |
| South America      | 0.38             | ███████ |
| Oceania            | 0.44             | ██████████ |
| Asia               | 0.40             | ████████ |
| North Africa       | 0.35             | ██████ |
| Sub-Saharan Africa | 0.36             | ██████ |

> Longer bars = higher cost; shorter bars = cheaper kWh.

---

## 5. NODE ENERGY MIX EXAMPLE (Europe Node)
Solar      ██████████ 200k kWh Wind       ████ 90k kWh Biogas     ████████ 180k kWh Geothermal ███████████ 250k kWh

> Quick reference for the proportion of each energy source per Node.

---

## 6. NODE SURPLUS HEATMAP (Text Approximation)

Oceania         ██████████ +340k North America   █████████ +310k Europe          ████████ +220k Asia            ███████  +200k North Africa    ██████   +150k South America   █████    +110k Sub-Saharan     ████     +80k

> Longer bars indicate larger surplus available for regional sharing.

---

## 7. NOTES

- All diagrams are **text-based** for markdown compatibility (INUTI).  
- Bars and percentages are proportional estimates.  
- Helps identify which regions can export energy and which may need efficiency improvements.  
- Fully compatible with Flow Node planning and environmental principles.

---

*End of ENERGY_DIAGRAMS_WORLDWIDE.md*