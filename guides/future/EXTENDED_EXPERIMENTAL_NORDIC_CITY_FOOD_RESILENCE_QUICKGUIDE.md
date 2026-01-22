# EXTENDED_EXPERIMENTAL_NORDIC_CITY_FOOD_RESILIENCE.py – Documentation

**Status:** EXPERIMENTAL / NON-NORMATIVE  
**Version:** Simulator v5.2  
**Authors:** Grok (xAI), in collaboration with Elinor Frejd, Gemini, ChatGPT  
**Date:** January 22, 2026  
**Purpose:** Epistemic exploration and systems learning for urban food self-sufficiency and resilience in Nordic cities.

---

## 1. Overview
This is an **experimental simulator** modeling potential future scenarios for urban food sovereignty in Nordic cities, focusing on:

- Hydroponics and vertical farming  
- Self-sufficiency and resilience  
- Nordic city-specific parameters  
- Multi-metric measurement: Sovereignty, DIVINE (M-OS-R principles), Economic NPV/IRR, Ecological Resilience, Cultural Integrity, GIP compliance  

**Important:** This is **not a production tool or policy recommendation**; it is intended for research and exploration purposes only.

---

## 2. Key Features

### a) City Data
Simulates 5 Nordic cities with parameters such as:

- Population & area  
- Sun hours & annual precipitation  
- Geothermal potential  
- Flood risk  
- Policy support and import cost per capita  

### b) Diet and Crop Profiles
- Diets: omnivore, vegetarian, vegan, flexitarian  
- Crops: local, semi-local, exotic (rice, coffee/cacao, exotic fruits)  
- Each crop has multipliers for energy, water, CO₂, biodiversity, and Nordic feasibility  

### c) Technology & Climate
- Tech levels: basic → high (affects yields)  
- Climate scenarios: baseline, optimistic, pessimistic (+2°C, floods)  
- Policy levels: low → high subsidy (affects costs)  
- Time horizons: 1–20 years  

### d) Monte Carlo Simulation
- 1000 iterations per scenario  
- Random variations: yield ±10%, costs ±5%, Σ unforeseen ±15%  
- Robustness: mean ± standard deviation

Choose mode:

1 – Interactive
2 – Full batch with all scenarios
Follow prompts or let full batch run 1000 Monte Carlo iterations
Results:
Console: Executive summary
PDF: Full report with tables and key insights
Plots: 6-panel visualization of key metrics
This simulator is designed for researchers, system thinkers, and urban planners who want to explore Nordic urban food resilience under multiple realistic and experimental scenarios.