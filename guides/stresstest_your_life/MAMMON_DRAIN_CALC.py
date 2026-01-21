# MAMMON_DRAIN_CALC.py
# Extended version to calculate and visualize parasitic losses (Mammon-drain)
# Based on TECHNICAL_ANNEX.md: Parasitic Loss Recovery
# Outputs: console calculations, local plot (PNG), Chart.js JSON for web

import numpy as np
import matplotlib.pyplot as plt
import json

# Sectors and their losses (%)
sectors = [
    'Marketing/Advertising',    
    'Financial Admin/Tax',      
    'Planned Obsolescence',     
    'Food Waste'                
]
drains = [1.5, 5.0, 17.5, 31.0]  

# Recovery potential (%)
recoveries = [100, 90, 80, 30]  

# Calculations
total_drain = np.sum(drains)
average_drain = np.mean(drains)
total_recovery = np.sum(np.array(drains) * np.array(recoveries) / 100)
efficiency_gain = 25.5  
global_capacity_multiplier = 1.62  

base_resources = 100.0
drained_resources = base_resources * (total_drain / 100)
recovered_resources = base_resources + total_recovery
flow_capacity = base_resources * global_capacity_multiplier * (1 + efficiency_gain / 100)

# Console output
print("=== Mammon-Drain Calculations ===")
print(f"Sectors: {sectors}")
print(f"Losses (%): {drains}")
print(f"Recovery Potential (%): {recoveries}")
print(f"Total Parasitic Loss: {total_drain:.2f}%")
print(f"Average Loss per Sector: {average_drain:.2f}%")
print(f"Total Recoverable Loss: {total_recovery:.2f}%")
print(f"Estimated Efficiency Gain in Flow: {efficiency_gain}%")
print(f"Global Capacity Multiplier (e.g., food): {global_capacity_multiplier}x")
print(f"Base Resources = {base_resources}")
print(f"Drained Resources in Mammon: {drained_resources:.2f}")
print(f"Recovered Resources in Flow: {recovered_resources:.2f}")
print(f"Total Flow Capacity: {flow_capacity:.2f} (sufficient for post-scarcity)")

# Plot and save as PNG
plt.figure(figsize=(10, 6))
plt.bar(sectors, drains, color='red', label='Mammon-Drain (%)')
plt.bar(sectors, np.array(drains) * np.array(recoveries) / 100, color='green', label='Recoverable in Flow (%)', alpha=0.6)
plt.xlabel('Sectors')
plt.ylabel('Percent (%)')
plt.title('Mammon-Drain and Recovery Potential')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('mammon_drain_plot.png')
plt.show()

# Export Chart.js config
chart_config = {
    "type": "bar",
    "data": {
        "labels": sectors,
        "datasets": [
            {
                "label": "Mammon-Drain (%)",
                "data": drains,
                "backgroundColor": "rgba(255, 99, 132, 0.2)",
                "borderColor": "rgba(255, 99, 132, 1)",
                "borderWidth": 1
            },
            {
                "label": "Recoverable in Flow (%)",
                "data": [d * r / 100 for d, r in zip(drains, recoveries)],
                "backgroundColor": "rgba(75, 192, 192, 0.2)",
                "borderColor": "rgba(75, 192, 192, 1)",
                "borderWidth": 1
            }
        ]
    },
    "options": {
        "scales": {
            "y": {
                "beginAtZero": True,
                "title": {"display": True, "text": "Percent (%)"}
            }
        },
        "plugins": {
            "title": {"display": True, "text": "Mammon-Drain and Flow Recovery per Sector"}
        }
    }
}

with open('mammon_drain_chart.json', 'w') as f:
    json.dump(chart_config, f, indent=4)

print("\nChart.js config saved as 'mammon_drain_chart.json' – integrate in your web page for interactive view!")