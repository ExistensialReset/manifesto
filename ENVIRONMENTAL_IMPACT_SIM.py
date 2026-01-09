# ENVIRONMENTAL_IMPACT_SIM.py: Simulering av ekologisk impact baserat på 2025-data
# Från ECOLOGICAL_AXIOMS.md och externa källor (e-waste 65M tons)
# Av Grok – 2026-01-09

import matplotlib.pyplot as plt
import json

# Data (2025-uppdaterad)
e_waste_current = 65.3  # M tons (UN 2025)
e_waste_reduction_flow = 80  # % recovery från annexet
co2_from_foodwaste = 3.3  # B tons eq (FAO)
energy_potential = 100  # x demand
gain = 25.5

# Simulering
flow_e_waste = e_waste_current * (1 - e_waste_reduction_flow / 100)
flow_co2_savings = co2_from_foodwaste * (gain / 100)

print(f"Flow E-waste: {flow_e_waste:.2f} M tons (från 65.3)")
print(f"CO2-spar: {flow_co2_savings:.2f} B tons")

# Pie-chart: Impact fördelning
labels = ['E-waste Reduction', 'CO2 Savings', 'Energy Gain']
impacts = [e_waste_reduction_flow, gain, 30]  # % exempel
plt.pie(impacts, labels=labels, autopct='%1.1f%%')
plt.title('Ekologisk Gain i Flow (2025-data)')
plt.savefig('environmental_impact_pie.png')

# Chart.js
chart_config = {
    "type": "pie",
    "data": {"labels": labels, "datasets": [{"data": impacts, "backgroundColor": ["#FF6384", "#36A2EB", "#FFCE56"]}]},
    "options": {"plugins": {"title": {"display": True, "text": "Ekologisk Impact"}}}
}
with open('environmental_impact_chart.json', 'w') as f:
    json.dump(chart_config, f, indent=4)