# HELIX_NODE_V2.5 – Excel/Sheets-kompatibel Budget & Testplan

**Version:** 2.5  
**Datum:** 2026-01-25

---

## 1. Fullskalig Nod – Budget

| Kategori                 | Kostnad_MSEK | Kommentar | Formel för % av total | Total_Budget |
|---------------------------|--------------|-----------|--------------------|--------------|
| Mark & Förberedelser      | 26.0         | Bygglov inkl. rökregler | =B2/SUM(B2:B6) | =SUM(B2:B6) |
| Konstruktion & Arkitektur | 71.0         | +1.0 MSEK för rökventilation & isolering | =B3/SUM(B2:B6) | =SUM(B2:B6) |
| Biologiska system         | 18.0         | Aquaponics & fuktkontroll | =B4/SUM(B2:B6) | =SUM(B2:B6) |
| Säkerhet & Resiliens      | 17.5         | +1.0 MSEK rökdetektorer & sensorer | =B5/SUM(B2:B6) | =SUM(B2:B6) |
| Digitala & Operationella  | 5.3          | +0.3 MSEK opt-in app | =B6/SUM(B2:B6) | =SUM(B2:B6) |
| **Total**                 | =SUM(B2:B6)  |  |  |  |

---

## 2. Kostnadsökning V2.4 → V2.5

| Post                     | Ökning_MSEK | Kommentar |
|---------------------------|------------|-----------|
| Isolering                 | 0.5        | Luftspalt mot rök/vibrationer |
| Ventilation               | 0.5        | Individuella ventiler / HEPA |
| Brandskydd                | 0.5        | Rökdetektorer / dimsprinklers |
| Sensorer                  | 0.5        | Anonyma rök-sensorer |
| Digitalt                  | 0.3        | M-OS-R app notiser |
| **Total ökning**          | =SUM(B2:B6)|  |

---

## 3. Prototyp 1:10 – Test & Budget

| Element                  | Kostnad_MSEK | Kommentar |
|---------------------------|--------------|-----------|
| Mini-dwelling (6 m²)      | 1.9–3.2      | Test av ventilation, rök & ljud |
| Ventilation & Filter      | 0.2–0.5      | 1:10-skalad HEPA, opt-in styrning |
| Röksimulering             | 0.1–0.2      | E-cigg / rökmaskin |
| Test & Monitorering       | 0.2–0.5      | Läckage, filtereffektivitet, ljudnivå |
| **Totalt**                | 0.5–1.0      | Inkluderat i prototypbudget |

### Prototyp-testplan

| Testpunkt                     | Beskrivning | Målvärde / Notering |
|--------------------------------|------------|--------------------|
| Kontinuerlig rökning           | 8h/dag i 6 mån |  |
| Läckage-test                   | Adjacent dwelling | Ingen detekterbar rök |
| Filtereffektivitet             | Veckovis mätning | >95% partiklar borttagna |
| Luftfuktighet                  | RH | <75% |
| Ljudnivå från ventilation      | dB | <40 dB |
| Social dynamik / konflikt      | Medling + teknisk verifiering | Standard uppfyllt |

---

## 4. Subventioner & Sweat Equity

| Källa                  | Belopp_MSEK | Kommentar |
|------------------------|-------------|-----------|
| EU Green Deal          | 16–26       | Hållbar tech + rökfiltrering |
| Göteborgs Stad         | 5–10        | Tillgängliga & privata ytor |
| Sweat Equity           | 8–10        | Boende installerar filter, opt-in testning |
| **Total bidrag**       | =SUM(B2:B4) | Reducerar egen investering & ROI-tid |

---

## 5. ROI-beräkning

| Scenario                  | Total_Investering_MSEK | Årlig_Drift_MSEK | ROI_År | Formel |
|----------------------------|-----------------------|-----------------|--------|--------|
| Fullskalig nod (medel)    | 137.8                 | 0.4             | =B2/C2 | =B2/C2 |
| Fullskalig nod (subvention)| 118                   | 0.4             | =B3/C3 | =B3/C3 |
| Fullskalig nod (buffert)  | 165                   | 0.4             | =B4/C4 | =B4/C4 |
| Prototyp (subvention)     | 0.5–1.0               | 0.05            | =B5/C5 | =B5/C5 |

---

## 6. Konfliktprotokoll (Social + Teknisk)

| Steg | Handling | Ansvar |
|------|---------|--------|
| 1    | Teknisk verifiering (mät läckage) | Boende / system |
| 2    | Om ja → förstärk ventilation | System / tekniker |
| 3    | Om nej → medling mellan boende | Boendekoordination |
| 4    | Ultimat veto → byte av dwelling | Boende |

---

## 7. Långtidstest – Filter & Ventilation

| Testparameter                 | Frekvens | Målvärde | Notering |
|--------------------------------|----------|-----------|----------|
| Filtereffektivitet              | Veckovis | >95%     | Testar HEPA |
| Läckage                        | Månadsvis | Ingen rök | Adjacent dwellings |
| Luftfuktighet                  | Daglig    | <75% RH | Kopplat till aquaponics |
| Ljudnivå                        | Veckovis | <40 dB | Ventilation |
| Social dynamik / konflikter     | Vid behov | L × S × I | Medlingsprotokoll |

---

## 8. Checklista inför fullskalig implementation

- [ ] Uppdatera CAD/ventilation med HEPA i varje dwelling  
- [ ] Testa prototyp 1:10 med röksimulering  
- [ ] Mät filtereffektivitet och luftflöde  
- [ ] Dokumentera resultat i stadgar + protokoll  
- [ ] Kommunikationsplan med boende för opt-in rökning  
- [ ] Budget & ROI verifiering  

---

✨ **L × S × I** ✨

- **Lugn:** Dwelling isolerad, inga störningar  
- **Spontanitet:** Rök när du vill, inget schema  
- **Inkännande:** Systemet skyddar alla utan att kontrollera någon  

💙❄️🌿🌀🚬