# FLOW_CAPACITY_SIMULATOR.py: Simulering av Flow-kapacitet baserat på annex-data
# Inkluderar pie-charts för resursdistribution
# Av Grok – 2026-01-09
# Kör: python FLOW_CAPACITY_SIMULATOR.py

import matplotlib.pyplot as plt
import json

# Data från annexet
food_current = 10.2
multiplier = 1.62
flow_food = food_current * multiplier
energy_current = 100
gain = 25.5
flow_energy = energy_current * (1 + gain / 100)

# Distribution: Mammon vs Flow (från annexet, 70/30 split approximerat)
labels = ['Baseline (Överlevnad)', 'Innovation (CR)', 'Parasitisk Förlust']
mammon_dist = [70, 0, 30]
flow_dist = [70, 30, 0]

print(f"Simulering: Flow Mat = {flow_food:.2f} miljarder, Energi = {flow_energy:.2f}x")

# Pie-charts
fig, axs = plt.subplots(1, 2, figsize=(12, 6))
axs[0].pie(mammon_dist, labels=labels, autopct='%1.1f%%', colors=['#36A2EB', '#FFCE56', '#FF6384'])
axs[0].set_title('Mammon Distribution')
axs[1].pie(flow_dist, labels=labels, autopct='%1.1f%%', colors=['#36A2EB', '#FFCE56', '#FF6384'])
axs[1].set_title('Flow Distribution')
plt.savefig('flow_capacity_pie.png')
plt.show()

# Chart.js för web
chart_config = {
    "type": "pie",
    "data": {"labels": labels, "datasets": [{"label": "Mammon", "data": mammon_dist, "backgroundColor": ["#36A2EB", "#FFCE56", "#FF6384"]}, {"label": "Flow", "data": flow_dist, "backgroundColor": ["#36A2EB", "#FFCE56", "#FF6384"]}]},
    "options": {"plugins": {"title": {"display": True, "text": "Resursdistribution i Mammon vs Flow"}}}
}
with open('flow_capacity_chart.json', 'w') as f:
    json.dump(chart_config, f, indent=4)