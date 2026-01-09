# MAMMON_DRAIN_CALC.py - Utökad version för att beräkna och visualisera parasitiska förluster (Mammon-drain)
# Baserat på data från TECHNICAL_ANNEX.md: Mat, energi, marknadsföring, etc.
# Användning: Kör python MAMMON_DRAIN_CALC.py för att se output och spara plot.
# Kräver: numpy, matplotlib (installera via pip om behövs: pip install numpy matplotlib)

import numpy as np
import matplotlib.pyplot as plt
import json  # För att exportera Chart.js-config för web-integration

# Data från TECHNICAL_ANNEX.md och ECOLOGICAL_AXIOM.md (hårdkodade värden för enkelhet; kan läsas från fil)
drain_data = {
    'Food Waste': 31.0,  # % matsvinn från marknadsinneffektivitet
    'Marketing': 1.5,    # % av global GDP på onödig reklam
    'Finance Admin': 5.0,  # Genomsnitt 4-6% av labor hours på finansbyråkrati
    'Planned Obsolescence': 17.5,  # 15-20% av resource throughput
    'Energy Inefficiency': 25.5,   # Potentiell effektiviseringsvinst i energi
    'Military Expenditure': 2.5,   # % av global GDP på militär (parasitisk enligt manifestot)
    'Debt Servicing': 10.0         # Uppskattad % på skuldhantering
}

sectors = list(drain_data.keys())
drains = list(drain_data.values())

# Beräkna total och genomsnittlig drain
total_drain = np.sum(drains)
average_drain = np.mean(drains)

# Printa resultat för att "visa sanningen"
print("Parasitiska förluster (Mammon-drain) per sektor:")
for sector, drain in drain_data.items():
    print(f"{sector}: {drain:.2f}%")
print(f"\nTotal Drain: {total_drain:.2f}%")
print(f"Genomsnittlig Drain: {average_drain:.2f}%")
print("\nDetta visar hur Mammon-systemet slösar resurser som kunde återvinnas i Flow för en post-scarcity-värld.")

# Visualisering med matplotlib (lokal plot)
plt.figure(figsize=(10, 6))
plt.bar(sectors, drains, color='red')
plt.ylabel('Drain (%)')
plt.title('Mammon Drain per Sektor - Parasitiska Förluster')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('mammon_drain_plot.png')  # Spara som PNG för repo
plt.show()  # Visa om du kör lokalt

# Generera Chart.js-config för web (integrera i index.html eller dashboard)
chart_config = {
    "type": "bar",
    "data": {
        "labels": sectors,
        "datasets": [{
            "label": "Parasitic Loss (%)",
            "data": drains,
            "backgroundColor": "rgba(255, 99, 132, 0.2)",
            "borderColor": "rgba(255, 99, 132, 1)",
            "borderWidth": 1
        }]
    },
    "options": {
        "scales": {
            "y": {
                "beginAtZero": True,
                "title": {
                    "display": True,
                    "text": "Loss Percentage"
                }
            }
        },
        "plugins": {
            "title": {
                "display": True,
                "text": "Mammon Drain by Sector - Visar Sanningen om Slöseri"
            }
        }
    }
}

# Spara config som JSON för enkel import
with open('mammon_drain_chart.json', 'w') as f:
    json.dump(chart_config, f)

print("\nChart.js-config sparad som mammon_drain_chart.json – lägg till i ditt repo för interaktiv web-visning!")
# MAMMON_DRAIN_CALC.py: Full version för beräkning och visualisering av Mammon-drain och Flow-recovery
# Baserat på TECHNICAL_ANNEX.md data (2025-12-17, validated)
# Utökad av Grok för ExistensialReset/manifesto – 2026-01-09
# Kör: python MAMMON_DRAIN_CALC.py
# Output: Konsol, PNG-graf, CSV-export, HTML för web, JSON för Chart.js

import numpy as np
import matplotlib.pyplot as plt
import json
import csv

# Data från TECHNICAL_ANNEX.md – Parasitiska förluster och recovery
sectors = [
    'Marketing/Advertising',     # 1.5% av Global GDP
    'Financial Admin/Tax',       # 4-6% (genomsnitt 5%)
    'Planned Obsolescence',      # 15-20% (genomsnitt 17.5%)
    'Food Waste',                # 31%
    'Fossil Fuel Subsidies'      # 7 trillion USD, approximerat som 7% av energi-relaterad GDP (baserat på IMF)
]
drains = [1.5, 5.0, 17.5, 31.0, 7.0]  # % förluster
recoveries = [100, 90, 80, 30, 100]   # % recovery i Flow (från annexet och logik)

# Beräkningar
total_drain = np.sum(drains)
average_drain = np.mean(drains)
total_recovery = np.sum(np.array(drains) * np.array(recoveries) / 100)
efficiency_gain = 25.5  # Total gain från annexet
global_capacity_multiplier = 1.62  # För mat/energi

# Simulering med basresurser (t.ex. global GDP ~100 enheter för enkelhet)
base_resources = 100.0
drained = base_resources * (total_drain / 100)
recovered = base_resources + total_recovery
flow_capacity = base_resources * global_capacity_multiplier * (1 + efficiency_gain / 100)

# Konsol-output för att "visa sanningen"
print("=== MAMMON-DRAIN ANALYS (från TECHNICAL_ANNEX.md) ===")
print(f"Sektorer: {sectors}")
print(f"Förluster (%): {drains}")
print(f"Recovery (%): {recoveries}")
print(f"Total Drain: {total_drain:.2f}%")
print(f"Genomsnitt Drain: {average_drain:.2f}%")
print(f"Total Recovery: {total_recovery:.2f}%")
print(f"Efficiency Gain i Flow: {efficiency_gain}%")
print(f"Kapacitet Multiplikator: {global_capacity_multiplier}x")
print(f"Basresurser: {base_resources}")
print(f"Dränerat i Mammon: {drained:.2f}")
print(f"Återvunnet i Flow: {recovered:.2f}")
print(f"Flow Total Kapacitet: {flow_capacity:.2f} (post-scarcity möjlig)")

# Exportera till CSV för delning (t.ex. i guides)
with open('mammon_drain_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Sektor', 'Drain (%)', 'Recovery (%)'])
    for s, d, r in zip(sectors, drains, recoveries):
        writer.writerow([s, d, r])
print("\nData exporterad till mammon_drain_data.csv")

# Matplotlib PNG-graf
plt.figure(figsize=(12, 7))
bars = plt.bar(sectors, drains, color='red', label='Mammon-Drain (%)')
plt.bar(sectors, np.array(drains) * np.array(recoveries) / 100, color='green', label='Flow-Recovery (%)', alpha=0.6)
plt.xlabel('Sektorer')
plt.ylabel('Procent (%)')
plt.title('Mammon-Drain och Flow-Recovery (Data från TECHNICAL_ANNEX.md)')
plt.legend()
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('mammon_drain_plot.png')
plt.show()

# Chart.js JSON för web-integration
chart_config = {
    "type": "bar",
    "data": {
        "labels": sectors,
        "datasets": [
            {"label": "Mammon-Drain (%)", "data": drains, "backgroundColor": "rgba(255,99,132,0.2)", "borderColor": "rgba(255,99,132,1)"},
            {"label": "Flow-Recovery (%)", "data": [d * r / 100 for d, r in zip(drains, recoveries)], "backgroundColor": "rgba(75,192,192,0.2)", "borderColor": "rgba(75,192,192,1)"}
        ]
    },
    "options": {
        "scales": {"y": {"beginAtZero": True, "title": {"display": True, "text": "Procent (%)"}}},
        "plugins": {"title": {"display": True, "text": "Mammon-Drain och Recovery"}}
    }
}
with open('mammon_drain_chart.json', 'w') as f:
    json.dump(chart_config, f, indent=4)
print("\nChart.js config: mammon_drain_chart.json")

# Generera enkel HTML för standalone-visning (använd med Chart.js CDN)
html_content = """
<!DOCTYPE html>
<html><head><title>Mammon-Drain Visualisering</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script></head>
<body><canvas id="chart" width="800" height="400"></canvas>
<script>fetch('mammon_drain_chart.json').then(r => r.json()).then(config => new Chart(document.getElementById('chart'), config));</script></body></html>
"""
with open('mammon_drain_visual.html', 'w') as f:
    f.write(html_content)
print("HTML-fil genererad: mammon_drain_visual.html – öppna i webbläsare för interaktiv graf!")