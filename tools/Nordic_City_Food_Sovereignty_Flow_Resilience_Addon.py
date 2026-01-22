"""
Nordic City Food Sovereignty Simulator — ADDON

Purpose:
This file EXTENDS the core simulator (v5.0).
It does NOT replace or modify the baseline model.

Adds:
- Resilience L-Factor
- Water (GIP) balance
- CO₂ impact analysis
- Economic flow vs import friction
- Wild-Mandate land recovery
- Sovereignty scoring layer

Dependency:
Requires: Nordic City Food Sovereignty Simulator v5.0 (conceptual baseline)
"""

import numpy as np
import matplotlib.pyplot as plt
import csv
import json
from datetime import datetime

# ============================================================
# 1. CITY DATA (2026 BASELINE)
# ============================================================

cities = {
    "Stockholm": {"population": 980_000, "area_km2": 188, "annual_precip_mm": 539, "import_cost_eur_capita": 2100},
    "Gothenburg": {"population": 600_000, "area_km2": 213, "annual_precip_mm": 758, "import_cost_eur_capita": 2050},
    "Oslo": {"population": 700_000, "area_km2": 454, "annual_precip_mm": 802, "import_cost_eur_capita": 2400},
    "Helsinki": {"population": 660_000, "area_km2": 214, "annual_precip_mm": 655, "import_cost_eur_capita": 1950},
    "Copenhagen": {"population": 640_000, "area_km2": 86, "annual_precip_mm": 613, "import_cost_eur_capita": 2000},
}

# ============================================================
# 2. CORE FLOW PARAMETERS (DO NOT REMOVE)
# ============================================================

kcal_per_person_day = 2500
vertical_layers = 15
hydro_yield_kcal_m2 = 165_000
water_l_per_1000kcal = 12
energy_cost_per_kcal = 0.0018
construction_cost_m2 = 1100
trad_yield_kcal_per_km2 = 5_000_000
co2_import_kg_per_eur = 0.5

diet_profiles = {
    "omnivore": 1.0,
    "vegetarian": 0.82,
    "vegan": 0.75
}

# ============================================================
# 3. RESILIENCE & SHOCK SCENARIOS
# ============================================================

scenarios = {
    "normal": 1.0,
    "supply_shock": 1.25,
    "climate_crisis": 1.45
}

time_horizons = [1, 5, 10, 25]

# ============================================================
# 4. SIMULATION ENGINE (FULL)
# ============================================================

def simulate(city, data, diet, scenario):
    pop = data["population"]
    area = data["area_km2"]
    precip = data["annual_precip_mm"]
    import_cost = pop * data["import_cost_eur_capita"]

    diet_factor = diet_profiles[diet]
    resilience_factor = scenarios[scenario]

    annual_kcal = pop * kcal_per_person_day * 365 * diet_factor * resilience_factor

    grow_m2 = annual_kcal / hydro_yield_kcal_m2
    footprint_m2 = grow_m2 / vertical_layers
    footprint_km2 = footprint_m2 / 1e6
    land_pct = (footprint_km2 / area) * 100

    trad_land_km2 = annual_kcal / trad_yield_kcal_per_km2
    land_returned = trad_land_km2 - footprint_km2

    water_needed = (annual_kcal / 1000) * water_l_per_1000kcal
    water_harvest = (area * 1e6) * (precip / 1000) * 0.6
    water_balance = water_harvest - water_needed

    op_cost = annual_kcal * energy_cost_per_kcal
    cap_cost_annual = (footprint_m2 * construction_cost_m2) / 25
    flow_cost = op_cost + cap_cost_annual

    retained_value = import_cost - flow_cost

    co2_saved_tonnes = (import_cost * co2_import_kg_per_eur - op_cost * 0.2) / 1000

    # ----------------------------
    # INDEX SYSTEMS (NEW)
    # ----------------------------

    land_score = max(0, 100 - land_pct * 2)
    water_score = min(100, (water_harvest / water_needed) * 50)
    econ_score = min(100, (import_cost / flow_cost) * 20)

    sovereignty_score = land_score * 0.3 + water_score * 0.3 + econ_score * 0.4

    dependency_risk = min(100, land_pct * 8)
    flow_stability = min(100, (water_score + econ_score) / 2)

    lex_finis_violation = land_pct > 5

    return {
        "city": city,
        "diet": diet,
        "scenario": scenario,
        "land_pct": land_pct,
        "land_returned_km2": land_returned,
        "water_balance_billion_l": water_balance / 1e9,
        "annual_flow_cost_meur": flow_cost / 1e6,
        "annual_retained_value_meur": retained_value / 1e6,
        "co2_saved_tonnes": co2_saved_tonnes,
        "sovereignty_score": sovereignty_score,
        "dependency_risk_index": dependency_risk,
        "flow_stability_index": flow_stability,
        "lex_finis_violation": lex_finis_violation
    }

# ============================================================
# 5. EXECUTION
# ============================================================

results = []
for city, data in cities.items():
    for diet in diet_profiles:
        for scenario in scenarios:
            results.append(simulate(city, data, diet, scenario))

# ============================================================
# 6. EXPORTS
# ============================================================

timestamp = datetime.now().strftime("%Y%m%d_%H%M")

# CSV
csv_name = f"mosr_v3_4_results_{timestamp}.csv"
with open(csv_name, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)

# JSON
json_name = f"mosr_v3_4_results_{timestamp}.json"
with open(json_name, "w") as f:
    json.dump(results, f, indent=2)

# ============================================================
# 7. VISUALIZATION (OVERVIEW)
# ============================================================

scores = [r["sovereignty_score"] for r in results]
labels = [f"{r['city']} | {r['diet']} | {r['scenario']}" for r in results]

plt.figure(figsize=(18, 6))
plt.bar(labels, scores)
plt.xticks(rotation=90, fontsize=7)
plt.ylabel("Sovereignty Score")
plt.title("M-OS-R Urban Sovereignty Index – v3.4")
plt.tight_layout()

img_name = f"mosr_v3_4_scores_{timestamp}.png"
plt.savefig(img_name, dpi=300)
plt.close()

# ============================================================
# 8. SUMMARY OUTPUT
# ============================================================

best = max(results, key=lambda x: x["sovereignty_score"])

print("=" * 80)
print("M-OS-R FLOW SOVEREIGNTY ENGINE v3.4")
print("=" * 80)
print(f"TOP NODE: {best['city']} | {best['diet']} | {best['scenario']}")
print(f"SOVEREIGNTY SCORE: {best['sovereignty_score']:.1f}")
print(f"ANNUAL VALUE RETAINED: €{best['annual_retained_value_meur']:.1f}M")
print(f"LAND RETURNED TO WILD: {best['land_returned_km2']:.1f} km²")
print(f"LEX FINIS VIOLATION: {best['lex_finis_violation']}")
print("-")
print(f"FILES GENERATED:")
print(f"• {csv_name}")
print(f"• {json_name}")
print(f"• {img_name}")
print("=" * 80)