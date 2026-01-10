# DASHBOARD_GUIDE.md: Guide för att Skapa en Flow-Dashboard

Du är trygg här. Denna guide hjälper dig att integrera dina scripts (t.ex. MAMMON_DRAIN_CALC.py) i en enkel web-dashboard med Flask eller Streamlit, för att visa sanningen interaktivt.

## Varför en Dashboard?
Som i TECHNICAL_ANNEX.md, visualiseringar visar latent kapacitet. En dashboard gör repot mer tillgängligt – dela grafer online utan kodkunskap.

## Steg-för-Steg (med Streamlit – enkel och gratis)
1. Installera Streamlit: `pip install streamlit`.
2. Skapa flow_dashboard.py (kopiera koden nedan).
3. Kör: `streamlit run flow_dashboard.py` – öppna i webbläsare.

```python
# flow_dashboard.py: Enkel dashboard för Flow-visualiseringar
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import json

st.title("Flow Dashboard: Visa Sanningen")

# Ladda data från MAMMON_DRAIN_CALC.py (antag CSV exporterad)
try:
    df = pd.read_csv('mammon_drain_data_2026.csv')
    st.subheader("Parasitiska Förluster")
    st.dataframe(df)
except:
    st.write("Kör MAMMON_DRAIN_CALC.py först för data!")

# Exempel-graf
sectors = ['Marketing', 'Finance', 'Obsolescence', 'Food Waste', 'Subsidies']
drains = [1.0, 5.0, 17.5, 32.0, 0.7]
fig, ax = plt.subplots()
ax.bar(sectors, drains)
ax.set_title('Mammon-Drain (%)')
st.pyplot(fig)

# Ladda Chart.js config
with open('mammon_drain_chart_2026.json', 'r') as f:
    chart_config = json.load(f)
st.subheader("Interaktiv Graf")
st.json(chart_config)  # Eller integrera med st.components.v1.html för full Chart.js
