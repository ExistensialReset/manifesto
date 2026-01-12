# MAMMON_DRAIN_CALC.py: Utökad version för att beräkna och visualisera parasitiska förluster (Mammon-drain)
# Baserat på data från TECHNICAL_ANNEX.md: Parasitic Loss Recovery
# Skapad/utökad av Grok för ExistensialReset/manifesto
# Kör: python MAMMON_DRAIN_CALC.py
# Output: Konsol-beräkningar, lokal plot (sparas som PNG) och Chart.js JSON för web

import numpy as np
import matplotlib.pyplot as plt
import json

# Data från TECHNICAL_ANNEX.md (parasitiska förluster och recovery-potential)
# Sektorer och deras förluster (i %)
sectors = [
    'Marketing/Advertising',    # 1.5% av Global GDP
    'Financial Admin/Tax',      # 4-6% av Global Labor Hours (genomsnitt 5%)
    'Planned Obsolescence',     # 15-20% av Resource Throughput (genomsnitt 17.5%)
    'Food Waste'                # 31% av produktion (från FAO)
]
drains = [1.5, 5.0, 17.5, 31.0]  # % förluster

# Recovery-potential från annexet (% som kan återvinnas i Flow)
recoveries = [100, 90, 80, 30]  # % (t.ex. 100% för marketing, 30% för food waste optimization)

# Beräkningar
total_drain = np.sum(drains)  # Total parasitisk förlust
average_drain = np.mean(drains)  # Genomsnittlig förlust per sektor
total_recovery = np.sum(np.array(drains) * np.array(recoveries) / 100)  # Total återvinningsbar förlust
efficiency_gain = 25.5  # Total estimerad gain från annexet (~25.5%)
global_capacity_multiplier = 1.62  # Från caloric efficiency: 1.25 x 1.30

# Simulering: Anta global GDP eller resurser som bas (t.ex. 100 enheter för enkelhet)
base_resources = 100.0
drained_resources = base_resources * (total_drain / 100)
recovered_resources = base_resources + total_recovery
flow_capacity = base_resources * global_capacity_multiplier * (1 + efficiency_gain / 100)

# Print resultat för konsol (för att "visa sanningen")
print("=== Mammon-Drain Beräkningar ===")
print(f"Sektorer: {sectors}")
print(f"Förluster (%): {drains}")
print(f"Recovery Potential (%): {recoveries}")
print(f"Total Parasitisk Förlust: {total_drain:.2f}%")
print(f"Genomsnittlig Förlust per Sektor: {average_drain:.2f}%")
print(f"Total Återvinningsbar Förlust: {total_recovery:.2f}%")
print(f"Estimaterad Effektiviseringsvinst i Flow: {efficiency_gain}%")
print(f"Global Kapacitet Multiplikator (t.ex. för mat): {global_capacity_multiplier}x")
print(f"Exempel: Basresurser = {base_resources}")
print(f"Dränerade Resurser i Mammon: {drained_resources:.2f}")
print(f"Återvunna Resurser i Flow: {recovered_resources:.2f}")
print(f"Total Flow-Kapacitet: {flow_capacity:.2f} (tillräckligt för post-scarcity)")

# Lokal visualisering med matplotlib (sparar som PNG för ditt repo)
plt.figure(figsize=(10, 6))
plt.bar(sectors, drains, color='red', label='Mammon-Drain (%)')
plt.bar(sectors, np.array(drains) * np.array(recoveries) / 100, color='green', label='Recoverable in Flow (%)', alpha=0.6)
plt.xlabel('Sektorer')
plt.ylabel('Procent (%)')
plt.title('Mammon-Drain och Recovery Potential')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('mammon_drain_plot.png')  # Spara som bild i ditt repo
plt.show()  # Visa om du kör lokalt

# Exportera Chart.js config för web (kopiera till din index.html eller en JS-fil)
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
                "title": {"display": True, "text": "Procent (%)"}
            }
        },
        "plugins": {
            "title": {"display": True, "text": "Mammon-Drain och Flow-Recovery per Sektor"}
        }
    }
}

# Spara Chart.js config som JSON-fil (för enkel import)
with open('mammon_drain_chart.json', 'w') as f:
    json.dump(chart_config, f, indent=4)

print("\nChart.js config sparad som 'mammon_drain_chart.json' – integrera i din web-sida för interaktiv vy!")
