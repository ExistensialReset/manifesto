# FLOW NODE ENERGY PRODUCTION, CONSUMPTION & STORAGE

**Purpose:**  
Document realistic energy consumption by crop, node energy production, storage strategies, and integration with CAPEX/OPEX for all Flow node types.

**Population:** 500 people  
**Node Types:** Urban, Peri‑Urban, Regional  
**Units:** Energy in kWh, Costs in USD

---

## 1. Energy Consumption per Crop (Real‑World Data)

This section uses real hydroponic/CEA benchmarks:

| Crop Type | Realistic Energy Use (kWh/kg) | Source / Notes |
|-----------|------------------------------:|----------------|
| Leafy greens (lettuce, spinach) | 30–150 | Vertical farm LED + HVAC load¹ |
| Microgreens | 30–120 | Less light hours, small footprint¹ |
| Mushrooms (indoor low‑light) | 50–150 | Only HVAC + humidity control² |
| Lentils (hydroponic/CEA) | 80–200 | Higher nutrient control¹ |
| Mung beans (hydroponic) | 80–200 | Similar to lentils¹ |
| Spirulina (photobioreactor) | 100–250 | Long light periods, mixing³ |
| Tomatoes & other veggies | 120–280 | Trellis + pollination + lights¹ |

**Notes:**  
¹ Based on vertical farming commercial data (energy consumption per kg produced).  
² Mushroom houses require climate (humidification) but no lighting.  
³ Photobioreactors require constant circulation and lighting.

---

## 2. Crop Yield Assumptions (per Node Type)

| Node Type | Crops Included | Annual Yield (Total kg) |
|-----------|----------------|-------------------------|
| Urban | Leafy greens, microgreens, mushrooms | 6,000 |
| Peri‑Urban | Nuts, legumes, berries, mushroom logs | 8,000 |
| Regional | Spirulina, lentils, mung beans | 10,000 |

> Yields are realistic for high‑intensity hydroponic and agroforestry systems.

---

## 3. Energy Consumption by Node (kWh/year)

For each node, total energy is calculated by yield × crop energy use.

### 3.1 Urban Node

| Crop | Yield (kg) | kWh/kg | Total (kWh/yr) |
|------|------------:|--------:|---------------:|
| Leafy greens | 3,500 | 90 | 315,000 |
| Microgreens | 1,500 | 80 | 120,000 |
| Mushrooms | 1,000 | 80 | 80,000 |
| **Total** | **6,000** | — | **515,000** |

### 3.2 Peri‑Urban Node

| Crop | Yield (kg) | kWh/kg | Total (kWh/yr) |
|------|------------:|--------:|---------------:|
| Nuts & Legumes | 4,000 | 90 | 360,000 |
| Berries | 2,000 | 120 | 240,000 |
| Mushroom logs | 2,000 | 65 | 130,000 |
| **Total** | **8,000** | — | **730,000** |

### 3.3 Regional Node

| Crop | Yield (kg) | kWh/kg | Total (kWh/yr) |
|------|------------:|--------:|---------------:|
| Spirulina | 5,000 | 150 | 750,000 |
| Lentils | 3,000 | 140 | 420,000 |
| Mung beans | 2,000 | 140 | 280,000 |
| **Total** | **10,000** | — | **1,450,000** |

---

## 4. Node Renewable Energy Production (Realistic)

Solar and wind generation capacity based on real DSM- and solar/PV industry data:

| Node | PV Capacity | PV Yield (kWh/yr) | Wind Capacity | Wind Yield (kWh/yr) | Total Production |
|------|------------|------------------|---------------|--------------------|------------------|
| Urban | 50 kW | ~40,000¹ | 5 kW | ~8,000¹ | ~48,000 |
| Peri‑Urban | 150 kW | ~120,000¹ | 20 kW | ~32,000¹ | ~152,000 |
| Regional | 300 kW | ~240,000¹ | 50 kW | ~80,000¹ | ~320,000 |

**Notes:**  
¹ Solar (800–1,000 kWh per kW installed/yr) and wind (~1,600–2,000 per kW installed/yr) based on global average production.

---

## 5. Energy Surplus/Deficit by Node

| Node | Consumption (kWh/yr) | Production (kWh/yr) | Surplus/Deficit |
|------|---------------------:|--------------------:|----------------:|
| Urban | 515,000 | 48,000 | −467,000 |
| Peri‑Urban | 730,000 | 152,000 | −578,000 |
| Regional | 1,450,000 | 320,000 | −1,130,000 |
| **Total** | **2,695,000** | **520,000** | **−2,175,000** |

> Even with sizeable solar/wind installations, none of the nodes can fully cover direct crop energy demand with on-site renewables alone — *but this is expected* in high‑intensity CEA.

---

## 6. Energy Storage Strategy

To buffer intermittency and cover short peaks, energy storage is required:

### 6.1 Battery Storage (Short‑Term)

| Node | Recommended Storage | Cost (USD/kWh) | Total Cost (USD) |
|------|--------------------:|----------------|-----------------:|
| Urban | 500 kWh | 350 | 175,000 |
| Peri‑Urban | 1,000 kWh | 350 | 350,000 |
| Regional | 2,000 kWh | 350 | 700,000 |

**Rationale:** Enough for 1–2 days of peak load.

### 6.2 Long‑Term Storage (Hydrogen)

Used to store seasonal or prolonged surplus when higher renewable generation is available.

| Node | Capacity (kg H₂) | Approx. Stored kWh | Notes |
|------|------------------:|------------------:|-------|
| Urban | 50 | ~1,400 | Small buffer |
| Peri‑Urban | 150 | ~4,200 | Seasonal buffer |
| Regional | 300 | ~8,400 | Large seasonal buffer |

Hydrogen electrolysers + tanks cost estimated **$800–1,200 per kg installed**.

---

## 7. Integration with CAPEX / OPEX

### 7.1 CAPEX – Energy Systems

| Node | PV + Wind Capex | Battery Capex | H₂ System Capex | Total Energy Capex |
|------|----------------:|--------------:|---------------:|------------------:|
| Urban | 48,000 | 175,000 | 50,000 | 273,000 |
| Peri‑Urban | 152,000 | 350,000 | 150,000 | 652,000 |
| Regional | 320,000 | 700,000 | 300,000 | 1,320,000 |

> PV/Wind Capex approximated at ~$1,000–1,500 per kW installed; Hydrogen ~ $800–1,200/kg capacity; batteries ~ $350/kWh.

### 7.2 OPEX – Energy Costs

| Node | Energy Opex/yr | Notes |
|------|----------------:|-------|
| Urban | 20,000 | Battery replacement + grid backup |
| Peri‑Urban | 30,000 | Maintenance & partial grid |
| Regional | 80,000 | Higher intensity systems |

---

## 8. Inter‑Node Energy Flow Protocol

### Principles

1. Nodes with surplus on good days (e.g., solar peaks) feed into shared buffer.
2. Regional nodes prioritized for high‑intensity crops and hydrogen export.
3. Batteries used for daily dispatch; hydrogen used for seasonal storage.

---

## 9. Summary

| Node | Consumption | Production | Storage | Net Balance |
|------|-------------|------------|---------|-------------|
| Urban | 515,000 | 48,000 | 500/50 | −466,950 |
| Peri‑Urban | 730,000 | 152,000 | 1,000/150 | −577,850 |
| Regional | 1,450,000 | 320,000 | 2,000/300 | −1,129,700 |

Energy demands dominated by LED & HVAC loads — typical for controlled environment agriculture (CEA).

---

## 10. Notes & Next Steps

- Crop energy coefficients reflect current hydroponic and photobioreactor benchmarks.  
- Renewable yields based on real global solar/wind average production.  
- Storage modelling provided for grid decoupling and buffering.  

---

*End of FLOW_NODE_ENERGY_PRODUCTION_AND_STORAGE.md*
