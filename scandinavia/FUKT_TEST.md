# HELIX_NODE V2.8 – FUKTTESTNING: Teknisk guide & Protokoll
**Version:** 2.8 (Fukt-resiliens utgåva)  
**Datum:** 27 januari 2026  
**Kontext:** Göteborg, Sverige (RH 70-90% vintertid)  
**Status:** Redo för implementering i prototyp (skala 1:10)

---

## 1. RASONEMANG OCH VETENSKAPLIG GRUND
Fukt är den "tysta mördaren" i HELIX-designen, särskilt i Göteborgs havsnära klimat. Integrationen av "The Ocean" (20 m³ vatten) skapar betydande avdunstning, medan rökning i Soul Dwellings adderar risk för kondens. Mycelium är hygroskopiskt och riskerar mögelväxt om den relativa luftfuktigheten (RH) överstiger 80%.

**Observerbara fakta:**
* **RH-trösklar:** Mögel (t.ex. *Aspergillus niger*) börjar växa vid 75% RH under 48 timmar (Källa: IVL Svenska Miljöinstitutet).
* **Materialabsorption:** Mycelium har en porvolym på 70-80%; överabsorption leder till strukturell försvagning (Källa: RISE/Chalmers).
* **Daggpunktens fysik:** Vid 20°C/80% RH är daggpunkten 16°C, vilket orsakar ytkondens på svalare väggar.

---

## 2. TEKNISKA JUSTERINGAR (ITERATIV DESIGN)
* **Om RH >70%:** Aktivera sekundära sorptionsavfuktare (Munters-system).
* **Om absorption >5%:** Applicera hydrofob bio-beläggning (silikonbaserad) på myceliumytor.
* **Om mögel upptäcks:** Öka UV-C-filtrering i FTX-slingan och höj zontemperaturen till >22°C.

---

## 3. KÄRNPROTOKOLL FÖR TESTNING

### Protokoll A: RH-cykling (7-dagars simulering)
* **Syfte:** Validera <70% genomsnittlig RH under varierande göteborgska vädercykler.
* **Verktyg:** DHT22-sensorer, Raspberry Pi-logger, klimatkammare.
* **Steg:** Cykla mellan 40% (torr) och 90% (toppfukt) RH i 24-timmarsintervaller.
* **Kriterier:** Godkänt om genomsnittet förblir <70% med <5 kondensdroppar/m².

### Protokoll B: Kapillärsugning (Mycelium-integritet)
* **Syfte:** Mäta viktökning genom vattenupptag för att förhindra strukturell svällning.
* **Verktyg:** Digital våg (±0,1g), mycelium-prover, destillerat saltvattenbad (0,5 ppt).
* **Steg:** Sänk ner prover i 24 timmar; väg före och efter.
* **Kriterier:** Godkänt om viktökningen är <5%.

### Protokoll C: Mögelresistens (28-dagars exponering)
* **Syfte:** Bekräfta noll biologisk tillväxt under hög fuktstress.
* **Verktyg:** Agarplattor, inkubator (25°C), mikroskop (400x).
* **Steg:** Inokulera prover med mögelsporer (*Penicillium*); övervaka veckovis i 28 dagar.
* **Kriterier:** Godkänt om 0 synliga kolonier och ATP-nivåer <10 RLU.

### Protokoll D: FTX- & rökfiltrering (Validering)
* **Syfte:** Säkerställa att kondens och rökpartiklar avlägsnas effektivt.
* **Verktyg:** Anemometer, OPC-N3 partikelräknare, rökgenerator.
* **Steg:** Simulera 10 cigaretter/timme + 10L fuktinjektion i en Soul Dwelling-modell.
* **Kriterier:** Godkänt om >99% filtreringseffektivitet och <2L kvarvarande kondens.

---

## 4. UPPFÖLJNING & DOKUMENTATION
Alla loggar lagras i M-OS-R (den digitala tvillingen) för årlig validering. Misslyckande i något protokoll utlöser en omedelbar designjustering (t.ex. dubblering av ventilationsflöde eller justering av mycelium-receptet).
