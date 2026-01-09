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