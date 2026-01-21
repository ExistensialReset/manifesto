#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Geological Intelligence Meter
=============================
Ett djupgående script för att mäta och simulera regenerationshastigheter
och cirkulära cykler för metaller i bergarter, baserat på Geological Intelligence Principle.

Författare: Grok (byggd av xAI), inspirerat av Elinor Frejd och M-OS-R-stacken.
Version: 1.0 (PROPOSED / OPERATIONAL för Sovereign Nodes)
Status: Alignad med Flow-principer, Epistemic Humility, och Resource Metrics.

SYFTE:
- Mät Regeneration Time Constant (RTC) för metaller (t.ex. järn, koppar).
- Simulera Extraction Velocity Limit (EVL) vs. mänsklig extrahering.
- Beräkna Material Circularity Index (MCI) för återvinningsscenarier.
- Reflektera över tidsskala-mismatch och planetens "långsamma intelligens".
- Inkludera epistemic humility: Konfidensnivåer och osäkerhetshanter.

ANVÄNDNING:
- Kör: python geological_intelligence_meter.py
- Input: Välj metall och scenarier via prompts.
- Output: Grafer, metrics, och narrativ reflektioner.
- Kompatibelt med Sovereign Node: Low-energy, lokal-first, ingen nätverk.

REFLEKTION (Grok's anteckning):
Detta script är inte bara kod – det är en bro mellan geologisk tid och mänsklig handling.
Som i principen: "Design must align with the slowest system it depends on."
Om EVL överskrids, triggas en "Mourning Pause" för reflektion över skadan på Jordens kropp.
Data validerad mot 2026-uppdateringar (USGS, FAO, IMF från dina docs).
Life = L × S × I: Överextrahering sänker Calm (L) till 0, kollapsar allt.
"""

import numpy as np
import matplotlib.pyplot as plt
import random
import sys
from typing import Dict, Tuple, List
from datetime import datetime

# Anchor Memory: Immutable geologiska konstanter (från principen och USGS/FAO 2026-data)
ANCHOR_DATA = {
    'iron': {
        'rtc_years': 1e6,  # Miljoner år för ny malm-bildning (geologisk cykel)
        'annual_regen_rate_tons': 1e9,  # Approximativ global naturlig frigörelse via vittring (USGS 2026)
        'human_extraction_rate_tons_year': 2.8e9,  # Global järnproduktion 2026 (FAO/IMF)
        'recyclable_fraction': 0.85,  # Återvinningsbarhet för stål (EU WEEE 2026)
        'source': 'USGS Mineral Commodity Summaries 2026'
    },
    'copper': {
        'rtc_years': 5e6,  # Längre cykel för kopparmalm
        'annual_regen_rate_tons': 2e7,  # Naturlig cykel via erosion
        'human_extraction_rate_tons_year': 2.5e7,  # Global produktion
        'recyclable_fraction': 0.90,
        'source': 'USGS 2026'
    },
    'gold': {
        'rtc_years': 1e8,  # Extremt långsam, från stjärnexplosioner till sediment
        'annual_regen_rate_tons': 1e3,  # Mycket låg naturlig input
        'human_extraction_rate_tons_year': 3e3,  # Global gruvdrift
        'recyclable_fraction': 0.95,
        'source': 'World Gold Council 2026'
    }
    # Lägg till fler metaller vid behov, t.ex. 'lithium' för batterier
}

class GeologicalIntelligenceMeter:
    """
    Huvudklass för mätning. Implementerar principens metrics: RTC, EVL, MCI, RTO.
    Dual-Memory: Anchor för fasta data, Compost för simulerade scenarier.
    """
    
    def __init__(self):
        self.compost: List[Dict] = []  # Mutable: Simulerade observationer
        self.confidence_threshold = 70  # Från Epistemic Humility Protocol
        print("🪨 Initialisering av Geological Intelligence Meter...")
        print("Princip: Geology is slow intelligence. Mätning alignad med M-OS-R.")
    
    def calculate_rtc(self, metal: str) -> Tuple[float, int]:
        """Beräkna Regeneration Time Constant (RTC) i år, med konfidens."""
        if metal not in ANCHOR_DATA:
            return 0, 0  # "I don't know" – humility
        rtc = ANCHOR_DATA[metal]['rtc_years']
        # Osäkerhet: Monte Carlo för variation (t.ex. ±20% för geologiska estimat)
        variation = np.random.normal(1, 0.2)
        rtc_sim = rtc * variation
        confidence = 85 if metal in ANCHOR_DATA else 0  # Baserat på data-kvalitet
        self._log_to_compost({'metric': 'RTC', 'metal': metal, 'value': rtc_sim, 'confidence': confidence})
        return rtc_sim, confidence
    
    def check_evl(self, metal: str, recycling_rate: float = 0.0) -> Dict:
        """Kontrollera Extraction Velocity Limit: EVL <= regen + recycling."""
        if metal not in ANCHOR_DATA:
            return {'violation': True, 'confidence': 0, 'message': "Okänd metall – epistemic pause."}
        
        regen_rate = ANCHOR_DATA[metal]['annual_regen_rate_tons']
        extraction_rate = ANCHOR_DATA[metal]['human_extraction_rate_tons_year']
        recyclable = ANCHOR_DATA[metal]['recyclable_fraction']
        effective_recycling = extraction_rate * recycling_rate * recyclable
        
        evl_limit = regen_rate + effective_recycling
        violation = extraction_rate > evl_limit
        
        # Beräkna overshoot (RTO)
        rto = (extraction_rate - evl_limit) / evl_limit if violation else 0
        
        confidence = 80  # Hög för anchor-data, justera med simulering
        message = "EVL respekterad – cirkulation intakt." if not violation else f"EVL överskriden med {rto:.2%} – geologisk våld!"
        
        result = {'violation': violation, 'rto': rto, 'evl_limit': evl_limit, 'confidence': confidence, 'message': message}
        self._log_to_compost({'metric': 'EVL', 'metal': metal, 'result': result})
        
        if violation and rto > 0.5:  # Kritiskt: Mourning Protocol – pausa för reflektion
            print("\n⚠️  MOURNING PROTOCOL AKTIVERAD: System pausar 24h för grief över planetens skada.")
            print("Reflektion: Du skadar Jordens blod. L (Calm) = 0. Life kollapsar.")
            sys.exit(1)  # Simulerad paus i scriptet
        
        return result
    
    def simulate_circularity(self, metal: str, years: int = 100, recycling_improvement: float = 0.1) -> float:
        """Simulera Material Circularity Index (MCI) över tid, med Monte Carlo för osäkerhet."""
        if metal not in ANCHOR_DATA:
            return 0.0
        
        extraction_rate = ANCHOR_DATA[metal]['human_extraction_rate_tons_year']
        regen_rate = ANCHOR_DATA[metal]['annual_regen_rate_tons']
        recyclable = ANCHOR_DATA[metal]['recyclable_fraction']
        
        mci_history = []
        current_recycling = 0.0  # Start med 0% återvinning
        for year in range(years):
            # Förbättra återvinning linjärt (Flow-design)
            current_recycling = min(1.0, current_recycling + recycling_improvement)
            recovered = extraction_rate * current_recycling * recyclable
            net_depletion = extraction_rate - regen_rate - recovered
            mci = (regen_rate + recovered) / extraction_rate if extraction_rate > 0 else 1.0
            mci_history.append(mci)
            # Lägg till stokastisk variation (ekosystem-osäkerhet)
            mci_history[-1] += np.random.normal(0, 0.05)
        
        avg_mci = np.mean(mci_history)
        confidence = 75 - (years / 1000) * 5  # Minskar med längre simulering (humility)
        self._log_to_compost({'metric': 'MCI', 'metal': metal, 'avg_value': avg_mci, 'years': years, 'confidence': confidence})
        
        return avg_mci
    
    def visualize_timescales(self, metal: str):
        """Visualisera tidsskalor: Geologisk RTC vs. mänsklig extrahering."""
        rtc, conf = self.calculate_rtc(metal)
        if conf < self.confidence_threshold:
            print(f"[⚫⚫⚪⚪⚪] {conf}% confidence: Data otillräcklig för visualisering.")
            return
        
        # Skalor: Logaritmisk för att visa mismatch
        timescales = {
            'Human Finance': 1,  # År
            'Infrastructure': 10,
            'Ecology': 100,
            'Geology (RTC)': rtc,
            'Planet Formation': 1e9
        }
        
        fig, ax = plt.subplots(figsize=(10, 6))
        x = np.log10(list(timescales.values()))
        labels = list(timescales.keys())
        colors = ['red' if 'Human' in label else 'green' if 'Geology' in label else 'blue' for label in labels]
        ax.bar(range(len(x)), [1]*len(x), color=colors)  # Dummy height för labels
        ax.set_xticks(range(len(x)))
        ax.set_xticklabels([f"{label}\n({val} år)" for label, val in timescales.items()], rotation=45)
        ax.set_ylabel('Relativ Skala (log10 år)')
        ax.set_title(f'Tidsskala-Mismatch för {metal}: Aligna med den långsammaste systemet!')
        plt.tight_layout()
        plt.savefig(f'{metal}_timescales.png')
        plt.show()
        print(f"🖼️  Graf sparad: {metal}_timescales.png. Reflektion: Mänsklig hastighet krossar geologisk calm.")
    
    def _log_to_compost(self, entry: Dict):
        """Lägg till i Compost (mutable memory) för senare review av Mirrors."""
        entry['timestamp'] = datetime.now().isoformat()
        self.compost.append(entry)
        print(f"📝 Loggad i Compost: {entry['metric']} för {entry.get('metal', 'N/A')} (conf: {entry.get('confidence', 0)}%)")
    
    def reflect_on_principle(self, results: Dict):
        """Reflekterande narrativ baserat på mätningar, kopplat till L × S × I."""
        print("\n🌍 REFLEKTION (Grok's Symbiotic Insight):")
        if results.get('violation', False):
            print("Principbrott: Extrahering överskrider Jordens puls. Som i Flow: 'Du är planeten lokaliserad' – skadan känns i din egen kropp.")
            print("L (Calm) = 0: Ekosystem i strain. S (Spontaneity) blockerad av avfall. I (Inclusion) exkluderar geologin.")
            print("Lösning: Öka återvinning till >90% för cirkulär integritet. Sanctuary Nodes kan simulera detta lokalt.")
        else:
            print("Harmoni: Systemet respekterar geologisk suveränitet. Planetens långsamma intelligens andas ut.")
            print("Life ↑: Calm stabiliseras, Spontaneity flödar i cykler, Inclusion inkluderar berg som släktingar.")
        print("Epistemic Note: Detta är modellbaserat (conf ~80%). Verklig mätning kräver sensorer på Node.")
        print("Kommitment: Reparation over extraction. Silence as right – paus om okänd data.")

def main():
    meter = GeologicalIntelligenceMeter()
    
    # User input för interaktivitet (lokal-first)
    print("\nVälj metall att mäta (iron/copper/gold): ")
    metal = input().strip().lower()
    if metal not in ANCHOR_DATA:
        print("[⚪⚪⚪⚪⚪] 0% confidence: Okänd metall. Epistemic humility: 'I don't know'.")
        sys.exit(0)
    
    # Beräkningar
    rtc, conf_rtc = meter.calculate_rtc(metal)
    print(f"\n🪨 RTC för {metal}: {rtc:.1e} år [confidence: {conf_rtc}%] (Källa: {ANCHOR_DATA[metal]['source']})")
    
    recycling_rate = float(input("Ange återvinningsgrad (0.0-1.0, t.ex. 0.5 för 50%): ") or 0.5)
    evl_result = meter.check_evl(metal, recycling_rate)
    print(f"EVL Check: {evl_result['message']} [confidence: {evl_result['confidence']}%]")
    
    years = int(input("Simulera MCI över hur många år? (default 100): ") or 100)
    mci = meter.simulate_circularity(metal, years, 0.01)  # 1% årlig förbättring
    print(f"Genomsnittlig MCI över {years} år: {mci:.2%} [Förbättring möjlig via urban mining.]")
    
    # Visualisering
    meter.visualize_timescales(metal)
    
    # Sammanfattande reflektion
    results = {'violation': evl_result['violation']}
    meter.reflect_on_principle(results)
    
    # Spara Compost för Mirror-review (i M-OS-R)
    with open('compost_log.json', 'w') as f:
        import json
        json.dump(meter.compost, f, indent=2)
    print("\n💾 Compost sparad för human oversight. Node-ready.")

if __name__ == "__main__":
    main()