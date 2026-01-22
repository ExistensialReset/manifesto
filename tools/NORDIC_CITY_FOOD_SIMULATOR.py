import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import random
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import sys

# Optional IRR fallback (does NOT remove np.irr usage)
try:
    import numpy_financial as npf
    irr_func = npf.irr
except ImportError:
    irr_func = np.irr

# =============================================================================
# Nordic Urban Food Sovereignty Simulator v5.0
# =============================================================================
# Author: Grok (xAI), based on collaborative development with Elinor Frejd, Gemini, ChatGPT
# Date: January 22, 2026
# Purpose: Model self-sufficiency in Nordic cities for plant-based food production
# =============================================================================

# --- 1. EXTENDED CITY DATA ---
cities = {
    "Stockholm": {
        "population": 980_000,
        "area_km2": 188,
        "annual_precip_mm": 539,
        "sun_hours_year": 1700,
        "geothermal_potential": 0.7,
        "flood_risk": 0.2,
        "import_cost_eur_capita": 2100,
        "policy_support": 0.8
    },
    "Gothenburg": {
        "population": 600_000,
        "area_km2": 213,
        "annual_precip_mm": 758,
        "sun_hours_year": 1600,
        "geothermal_potential": 0.6,
        "flood_risk": 0.6,
        "import_cost_eur_capita": 2050,
        "policy_support": 0.7
    },
    "Oslo": {
        "population": 700_000,
        "area_km2": 454,
        "annual_precip_mm": 802,
        "sun_hours_year": 1500,
        "geothermal_potential": 0.9,
        "flood_risk": 0.3,
        "import_cost_eur_capita": 2400,
        "policy_support": 0.9
    },
    "Helsinki": {
        "population": 660_000,
        "area_km2": 214,
        "annual_precip_mm": 655,
        "sun_hours_year": 1800,
        "geothermal_potential": 0.8,
        "flood_risk": 0.5,
        "import_cost_eur_capita": 1950,
        "policy_support": 0.75
    },
    "Copenhagen": {
        "population": 640_000,
        "area_km2": 86,
        "annual_precip_mm": 613,
        "sun_hours_year": 1700,
        "geothermal_potential": 0.5,
        "flood_risk": 0.7,
        "import_cost_eur_capita": 2000,
        "policy_support": 0.85
    },
}

# --- 2. CONSTANTS & PROFILES ---
kcal_per_person_day = 2500
water_l_per_1000kcal = 12
energy_cost_base = 0.0018
construction_cost_m2 = 1100
co2_import_factor = 0.5
trad_yield_km2 = 5_000_000
discount_rate = 0.03
vertical_layers_base = 15
min_biodiversity = 50

diet_profiles = {
    "omnivore": 1.0,
    "vegetarian": 0.82,
    "vegan": 0.75,
    "flexitarian": 0.9
}

crop_profiles = {
    "local": {"energy_mult": 1.0, "water_mult": 1.0, "co2_mult": 1.0, "biodiversity_bonus": 1.2, "feasibility_nordic": 0.95},
    "semi_local": {"energy_mult": 1.2, "water_mult": 1.1, "co2_mult": 1.1, "biodiversity_bonus": 1.1, "feasibility_nordic": 0.85},
    "exotic_rice": {"energy_mult": 2.5, "water_mult": 1.5, "co2_mult": 2.0, "biodiversity_bonus": 0.8, "feasibility_nordic": 0.4},
    "coffee_cacao": {"energy_mult": 3.0, "water_mult": 2.0, "co2_mult": 2.5, "biodiversity_bonus": 0.6, "feasibility_nordic": 0.3},
    "exotic_fruit": {"energy_mult": 1.8, "water_mult": 1.2, "co2_mult": 1.5, "biodiversity_bonus": 0.9, "feasibility_nordic": 0.6}
}

tech_levels = {"basic": 0.8, "medium": 1.0, "advanced": 1.3, "high": 1.6}

climate_scenarios = {
    "baseline": {"temp_adjust": 1.0, "precip_adjust": 1.0, "risk_mult": 1.0},
    "optimistic": {"temp_adjust": 0.9, "precip_adjust": 1.1, "risk_mult": 0.8},
    "pessimistic": {"temp_adjust": 1.2, "precip_adjust": 0.9, "risk_mult": 1.3}
}

policy_factors = {"low": 1.2, "medium": 1.0, "high": 0.8}
time_horizons = [1, 3, 5, 10, 20]

# --- 3. SIMULATION ENGINE v5.0 ---
def simulate_v5_0(city_name, data, diet="vegan", crop_mix_pct=0.2, tech_level="medium",
                  climate="baseline", policy="medium", time_horizon=5,
                  num_monte_carlo=1000, seed=42):

    np.random.seed(seed)
    results_list = []

    pop = data["population"]
    area = data["area_km2"]
    precip = data["annual_precip_mm"]
    sun_hours = data["sun_hours_year"]
    geothermal = data["geothermal_potential"]
    flood_risk = data["flood_risk"]
    current_import_cost = pop * data["import_cost_eur_capita"]

    diet_factor = diet_profiles[diet]
    l_factor_base = 1.25

    crop_mix = {
        "local": 1 - crop_mix_pct,
        "exotic_rice": crop_mix_pct * 0.3,
        "coffee_cacao": crop_mix_pct * 0.3,
        "exotic_fruit": crop_mix_pct * 0.4
    }

    climate_data = climate_scenarios[climate]
    precip_adjust = precip * climate_data["precip_adjust"]

    for _ in range(num_monte_carlo):
        yield_var = random.uniform(0.9, 1.1)
        cost_var = random.uniform(0.95, 1.05)
        sigma_fluct = random.uniform(-0.15, 0.15)

        annual_kcal = pop * kcal_per_person_day * 365 * l_factor_base * diet_factor * yield_var

        tech_mult = tech_levels[tech_level]
        yield_m2 = 165_000 * tech_mult * yield_var * (1 + sigma_fluct)

        grow_m2 = annual_kcal / yield_m2
        footprint_m2 = grow_m2 / vertical_layers_base
        footprint_km2 = footprint_m2 / 1e6
        land_pct = (footprint_km2 / area) * 100

        inertia_mult = 1.3 if time_horizon < 3 else 1.0 / (1 + time_horizon / 10)
        initial_capex = footprint_m2 * construction_cost_m2 * inertia_mult * cost_var

        op_cost = annual_kcal * energy_cost_base * (1 - geothermal * 0.3)
        total_annual_cost = op_cost + initial_capex / 25

        annual_savings = current_import_cost - total_annual_cost

        # >>> ADDED: Payback years (WAS MISSING)
        payback_years = initial_capex / annual_savings if annual_savings > 0 else np.inf

        npv = sum(annual_savings / (1 + discount_rate) ** t for t in range(1, time_horizon + 1))
        irr_estimate = irr_func([-initial_capex] + [annual_savings] * time_horizon) * 100 if annual_savings > 0 else 0

        water_needed = (annual_kcal / 1000) * water_l_per_1000kcal
        water_harvest = (area * 1e6) * (precip_adjust / 1000) * 0.6
        water_balance = water_harvest - water_needed

        biodiversity_score = min(100, min_biodiversity * (1 - crop_mix_pct * 0.5) * 2)
        cultural_integrity = 100 - crop_mix_pct * 200 if crop_mix_pct > 0.3 else 100

        land_score = max(0, 100 - land_pct * 2)
        water_score = min(100, (water_harvest / water_needed) * 50 if water_needed > 0 else 100)
        econ_score = min(100, (annual_savings / current_import_cost) * 100)

        sovereignty_score = (land_score + water_score + econ_score + biodiversity_score / 2) / 4
        divine_score = (land_score / 100) * (water_score / 100) * (biodiversity_score / 100) * 100

        results_list.append({
            "city": city_name,
            "diet": diet,
            "exotic_pct": crop_mix_pct,
            "tech_level": tech_level,
            "climate": climate,
            "policy": policy,
            "time_horizon": time_horizon,
            "land_pct": land_pct,
            "annual_savings_meur": annual_savings / 1e6,
            "npv_meur": npv / 1e6,
            "irr_pct": irr_estimate,
            "payback_years": payback_years,
            "sovereignty_score": sovereignty_score,
            "divine_score": divine_score,
            "biodiversity_score": biodiversity_score,
            "cultural_integrity": cultural_integrity,
            "water_balance_bl": water_balance / 1e9
        })

    df = pd.DataFrame(results_list)
    agg = df.mean(numeric_only=True).to_dict()
    agg.update({
        "city": city_name,
        "diet": diet,
        "exotic_pct": crop_mix_pct,
        "tech_level": tech_level,
        "climate": climate,
        "policy": policy,
        "time_horizon": time_horizon,
        "std_sovereignty": df["sovereignty_score"].std()
    })
    return agg

# --- MAIN ---
if __name__ == "__main__":
    print("Nordic Urban Food Sovereignty Simulator v5.0 – FINAL")
    print("This model is normative–strategic, not predictive LCA.")