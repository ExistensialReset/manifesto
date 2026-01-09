# CAPACITY_VISUALIZER.py: Visualiserar global resurskapacitet före/efter Flow-övergång
# Baserat på TECHNICAL_ANNEX.md: Caloric Efficiency, Energy Entropy, etc.
# Skapad av Grok för ExistensialReset/manifesto
# Kör: python CAPACITY_VISUALIZER.py
# Output: Tabell, pie-chart för distribution, och JSON för web

import numpy as np
import matplotlib.pyplot as plt
import json

# Data från TECHNICAL_ANNEX.md
current_food_capacity = 10.2  # Billioner människor (FAO)
food_waste = 31  # %
food_recovery = 30  # % gain
energy_potential = 100  # x human demand (IEA)
fossil_subsidies = 7  # Trillion USD (IMF)
total_efficiency_gain = 25.5  # %

# Beräkningar: Före/efter
current_surplus = 1.25  # Nuvarande surplus
flow_food_multiplier = current_surplus * (1 + food_recovery / 100)  # 1.62x
flow_food_capacity = current_food_capacity * flow_food_multiplier  # Total i Flow
flow_energy_capacity = energy_potential * (1 + total_efficiency_gain / 100)  # Utökad

# Exempel-distribution för pie-chart (baserat på 70/30 split från annexet)
labels = ['Baseline (Survival)', 'Innovation (CR Allocation)', 'Parasitic Loss (Mammon)']
mammon_dist = [70, 0, 30]  # % i Mammon
flow_dist = [70, 30, 0]    # % i Flow

# Print tabell för konsol
print("=== Global Kapacitet Visualisering ===")
print(f"Nuvarande Matkapacitet: {current_food_capacity} miljarder människor")
print(f"Matförlust i Mammon: {food_waste}%")
print(f"Recovery i Flow: {food_recovery}%")
print(f"Flow Matkapacitet: {flow_food_capacity:.2f} miljarder (multiplikator: {flow_food_multiplier}x)")
print(f"Nuvarande Energi Potential: {energy_potential}x demand")
print(f"Flow Energi Kapacitet: {flow_energy_capacity:.2f}x (med {total_efficiency_gain}% gain)")
print(f"Fossil Subsidier (som kan omdirigeras): ${fossil_subsidies} trillion")

# Pie-chart för Mammon vs Flow
fig, axs = plt.subplots(1, 2, figsize=(12, 6))
axs[0].pie(mammon_dist, labels=labels, autopct='%1.1f%%', colors=['blue', 'green', 'red'])
axs[0].set_title('Resursdistribution i Mammon')
axs[1].pie(flow_dist, labels=labels, autopct='%1.1f%%', colors=['blue', 'green', 'red'])
axs[1].set_title('Resursdistribution i Flow')
plt.savefig('capacity_pie.png')
plt.show()

# Chart.js config för web (pie-chart)
chart_config = {
    "type": "pie",
    "data": {
        "labels": labels,
        "datasets": [
            {"label": "Mammon", "data": mammon_dist, "backgroundColor": ["#36A2EB", "#FFCE56", "#FF6384"]},
            {"label": "Flow", "data": flow_dist, "backgroundColor": ["#36A2EB", "#FFCE56", "#FF6384"]}
        ]
    },
    "options": {
        "plugins": {"title": {"display": True, "text": "Resursdistribution Före/Efter Flow"}}
    }
}

with open('capacity_chart.json', 'w') as f:
    json.dump(chart_config, f, indent=4)

print("\nCapacity chart sparad som 'capacity_chart.json' – perfekt för att visa latent potential!")