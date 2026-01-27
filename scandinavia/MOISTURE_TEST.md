# HELIX_NODE V2.8 – MOISTURE TESTING: Technical Guide & Protocols
**Version:** 2.8 (Moisture-Resilience Edition)  
**Date:** January 27, 2026  
**Context:** Gothenburg, Sweden (RH 70-90% Winter)  
**Status:** Implementation-ready for Prototype (1:10 scale)

---

## 1. RATIONALE & SCIENTIFIC FOUNDATION
Moisture is the "silent killer" in the HELIX design, especially given Gothenburg’s coastal climate. The integration of "The Ocean" (20 m³ of water) creates significant evaporation, while smoking in Soul Dwellings adds condensation risks. Mycelium, being hygroscopic, risks mold growth if Relative Humidity (RH) exceeds 80%.

**Observable Facts:**
* **RH Thresholds:** Mold (e.g., *Aspergillus niger*) initiates growth at 75% RH over 48 hours (Source: IVL Swedish Environmental Research Institute).
* **Material Absorption:** Mycelium has a 70-80% pore volume; over-absorption leads to structural weakening (Source: RISE/Chalmers).
* **Dew Point Physics:** At 20°C/80% RH, the dew point is 16°C, causing surface condensation on cooler walls.

---

## 2. TECHNICAL ADJUSTMENTS (ITERATIVE DESIGN)
* **If RH >70%:** Activate secondary Desiccant Dehumidifiers (Munters system).
* **If Absorption >5%:** Apply hydrophobic bio-coating (silicon-based) to mycelium surfaces.
* **If Mold Detected:** Increase UV-C filtration in the HVAC/FTX loop and raise zone temp to >22°C.

---

## 3. CORE TESTING PROTOCOLS

### Protocol A: RH Cycling (7-Day Simulation)
* **Purpose:** Validate <70% average RH under variable Gothenburg weather cycles.
* **Tools:** DHT22 sensors, Raspberry Pi logger, Climate chamber.
* **Step:** Cycle between 40% (Dry) and 90% (Peak Wet) RH over 24-hour intervals.
* **Criteria:** Pass if average remains <70% with <5 condensation drops/m².

### Protocol B: Capillary Suction (Mycelium Integrity)
* **Purpose:** Measure water uptake weight to prevent structural swelling.
* **Tools:** Digital scale (±0.1g), Mycelium samples, distilled salt-water bath (0.5 ppt).
* **Step:** Submerge samples for 24 hours; weigh before and after.
* **Criteria:** Pass if weight increase is <5%.

### Protocol C: Mold Resistance (28-Day Exposure)
* **Purpose:** Confirm zero biological growth under high moisture stress.
* **Tools:** Agar plates, incubator (25°C), microscope (400x).
* **Step:** Inoculate samples with mold spores (*Penicillium*); monitor weekly for 28 days.
* **Criteria:** Pass if 0 visible colonies and ATP levels <10 RLU.

### Protocol D: HVAC & Smoke Filtration (FTX Validation)
* **Purpose:** Ensure condensation and smoke particles are removed effectively.
* **Tools:** Anemometer, OPC-N3 Particle Counter, smoke generator.
* **Step:** Simulate 10 cigarettes/hr + 10L moisture injection into a Soul Dwelling model.
* **Criteria:** Pass if >99% filtration efficiency and <2L residual condensation.

---

## 4. FOLLOW-UP & DOCUMENTATION
All logs are stored in the M-OS-R digital twin for annual validation. Failure in any protocol triggers an immediate design iteration (e.g., doubling ventilation flow or mycelium recipe adjustment).
