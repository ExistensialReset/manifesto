# hydroponic_selfsufficiency.py
# Simulates plant-based self-sufficiency in megacities using hydroponics / vertical farming
# Inspired by Existential Reset Manifesto principles: Baseline, Flow, Ecological Stewardship

import pandas as pd

# --- City data (population, available area in km² for cultivation) ---
cities = {
    'New York': {'population': 8_800_000, 'available_area_km2': 120},   # rooftops + vertical farms
    'Lagos': {'population': 15_000_000, 'available_area_km2': 150},
    'Jakarta': {'population': 10_600_000, 'available_area_km2': 80},
    'Tokyo': {'population': 14_000_000, 'available_area_km2': 200}
}

# --- Crop data (calories per m²/year, water usage L/m²/year, energy use kWh/m²/year) ---
# Simplified mix: leafy greens + potatoes + beans + hydroponic algae
crops = {
    'leafy_greens': {'calories_per_m2': 5000, 'water_per_m2': 100, 'energy_per_m2': 1},  
    'potato': {'calories_per_m2': 8000, 'water_per_m2': 200, 'energy_per_m2': 1.5},
    'beans': {'calories_per_m2': 7000, 'water_per_m2': 150, 'energy_per_m2': 1.2},
    'algae': {'calories_per_m2': 9000, 'water_per_m2': 50, 'energy_per_m2': 0.8}
}

# --- Constants ---
daily_calories_per_person = 2500  # kcal/person/day
days_per_year = 365

results = []

for city_name, data in cities.items():
    population = data['population']
    available_area_m2 = data['available_area_km2'] * 1_000_000  # km² -> m²
    
    # Total annual calorie requirement
    annual_calorie_need = daily_calories_per_person * population * days_per_year
    
    # Assume even distribution of cultivation among crops
    average_calories_per_m2 = sum([crops[crop]['calories_per_m2'] for crop in crops]) / len(crops)
    
    # Total potential calories produced
    total_calories_produced = available_area_m2 * average_calories_per_m2
    
    # Self-sufficiency percentage (max 100%)
    self_sufficiency_percent = min(total_calories_produced / annual_calorie_need * 100, 100)
    
    # Total water and energy requirements
    average_water_per_m2 = sum([crops[crop]['water_per_m2'] for crop in crops]) / len(crops)
    average_energy_per_m2 = sum([crops[crop]['energy_per_m2'] for crop in crops]) / len(crops)
    total_water_liters = available_area_m2 * average_water_per_m2
    total_energy_kwh = available_area_m2 * average_energy_per_m2
    
    results.append({
        'City': city_name,
        'Population': population,
        'Available_Area_m2': available_area_m2,
        'Annual_Calorie_Need': annual_calorie_need,
        'Annual_Calories_Produced': total_calories_produced,
        'Self_Sufficiency_%': self_sufficiency_percent,
        'Water_Liters': total_water_liters,
        'Energy_kWh': total_energy_kwh
    })

df = pd.DataFrame(results)
print(df)