# CHECKLISTA: Fuktvalidering av Mycelium-isolering
**Syfte:** Att verifiera materialets integritet i fuktiga miljöer (Aquaponics) och skandinaviskt klimat.  
**Mål:** Uppnå tekniskt godkännande för försäkring och bygglov.  
**Version:** 1.1 (Uppdaterad med tillägg för mätbarhet och M-OS-R-integration, 2026-01-25)  
**Koppling till HELIX_NODE:** Tester integreras i 1:10-prototypen (kostnad: ca 0.5–1 MSEK, inkl. sensorik från kalkylens kategori E). Använd open-source verktyg för att minimera friktion (S – Spontanitet).

---

## 1. Materialets Hydrofoba Egenskaper
Innan montering i prototypen ska materialets naturliga motståndskraft mot väta fastställas.  
**Δ TILLÄGG:** Använd standardiserade metoder från EN 13501-1 och EN 13423 för att säkerställa kompatibilitet med EU-normer. Dokumentera med foton och data för repo:et.

- [ ] **Kapillärsugningstest:** Mät hur snabbt och djupt vatten tränger in i blocket vid direkt kontakt.  
  **Δ TILLÄGG:** Mät kvantitativt (t.ex. <5% viktökning efter 24 timmars exponering vid 100% RH) med våg och timer; använd ASTM D6486 som referens för noggrannhet.

- [ ] **Ytbehandlingskontroll:** Testa effektiviteten av naturliga vaxer eller oljor för att skapa en vattenavvisande yta utan att försämra diffusionsöppenheten.  
  **Δ TILLÄGG:** Verifiera med kontaktvinkel-mätning (kontaktvinkel >90° för hydrofobi); testa långsiktigt (7 dagar) för att säkerställa ingen nedbrytning av behandling.

- [ ] **Ånggenomgångsmotstånd:** Verifiera att materialet "andas" (lågt ångmotstånd) för att förhindra innesluten fukt.  
  **Δ NY PUNKT:** **Ångdiffusionsresistans (μ-värde):** Mät μ <10 för att säkerställa god ånggenomsläpplighet (enligt EN ISO 12572); detta skyddar mot kondens i Göteborgs fuktiga vintrar.

---

## 2. In-situ Tester (I Prototypen)
Tester som utförs under drift i 1:10-modellen för att simulera verkliga förhållanden.  
**Δ TILLÄGG:** Integrera med M-OS-R-sensorer (t.ex. trådlösa RH-sensorer från kategori E) för realtidsdata utan invasiv övervakning (I – Inkännande). Kör tester i klimatrum för att simulera -10°C till +25°C.

- [ ] **Daggpunktsanalys:** Placera sensorer inuti mycelium-väggen för att se var daggpunkten hamnar vid -10°C ute och +25°C inne (med hög luftfuktighet från aquaponics).  
  **Δ TILLÄGG:** Använd hygrometrar för exakt beräkning (daggpunkt >5°C från innervägg); logga data automatiskt för att undvika manuell stress (L – Lugn).

- [ ] **Relativ fuktighet (RH) i konstruktionen:** Kontrollera att RH inuti isoleringen aldrig överstiger 75% under längre perioder (gränsen för mögelpåväxt).  
  **Δ NY PUNKT:** **RH-cyklingstest:** Simulera dagliga fluktuationer (60–80% RH) i 14 dagar för att verifiera stabilisering; gräns: <80% genomsnittligt för att möta Boverket:s OVK-krav.

- [ ] **Viktförändring över tid:** Väg specifika testblock i konstruktionen periodvis för att se om de ackumulerar fukt (hygroskopisk viktökning).  
  **Δ TILLÄGG:** Mät veckovis (t.ex. <2% viktökning per vecka); inkludera torkcykel för att testa återhämtning (t.ex. med FTX-systemet).

---

## 3. Biologisk Stabilitet & Nedbrytning
Säkerställa att isoleringen inte "vaknar till liv" eller bryts ner av mikroorganismer.  
**Δ TILLÄGG:** Använd labbtester från ackrediterade institut (t.ex. SP Technical Research Institute i Borås) för objektiv verifiering; detta stärker försäkringsgodkännande.

- [ ] **Inaktiveringsverifiering:** Ta prover för att bekräfta att värmebehandlingen (avdödningen) av myceliet var 100% framgångsrik.  
  **Δ TILLÄGG:** Använd mikrobiell analys (t.ex. PCR-test för sporer); gräns: 0% aktiv tillväxt efter 150°C-behandling i 2 timmar.

- [ ] **Mögelresistensprov:** Exponera materialet för extrem fukt (90% RH) under 28 dagar och okulärbesiktiga samt analysera efter sporbildning.  
  **Δ NY PUNKT:** **Mögelklassning (EN 13423):** Klassa materialet som M0 (ingen påväxt) efter exponering; inkludera mikrobiell odling för kvantitativ sporräkning (<100 CFU/g).

- [ ] **Dimensionsstabilitet:** Mät om blocken sväller eller krymper vid kraftiga skiftningar i luftfuktighet.  
  **Δ TILLÄGG:** Mät linjär svällning (<1% vid 20–80% RH-skift); testa med digital kalibrering för precision.

---

## 4. Tekniska Gränssnitt (Reset-kontroll)
Hur isoleringen samverkar med husets övriga "organ".  
**Δ TILLÄGG:** Testa i prototypens kontext för att säkerställa cirkulär ekonomi (t.ex. fukt från avfall återvinns utan läckage).

- [ ] **FTX-respons:** Mät hur snabbt ventilationen sänker fuktnivån i isoleringsnära zoner efter en "fuktchock" (t.ex. vid vattenbyte i fiskdammarna).  
  **Δ TILLÄGG:** Mät responstid (<30 min till <60% RH); integrera med M-OS-R för automatisk justering (opt-in, ingen ständig övervakning).

- [ ] **Läckage-simulering:** Medvetet introducera en fuktskada i en testmodul för att se hur myceliet torkar ut och om dess strukturella styrka påverkas efter torkning.  
  **Δ NY PUNKT:** **Integration med Aquaponics-flöden:** Simulera fuktöverföring från vattenkatedraln (t.ex. 95% RH-zon) till isolering; verifiera ingen migration av mikroorganismer (t.ex. via vattenprov).

---

## Δ NY SEKTION: 5. Dokumentation, Kostnad & M-OS-R-Integration
För att checklistan ska vara användbar i prototypfasen och fullskalig projektering, lägg till spårbarhet och hållbarhet. Detta säkerställer att tester stödjer L × S × I (t.ex. data som frigör tid istället för skapar stress).

- [ ] **Dokumentationsprotokoll:** Samla all data i digitalt format (t.ex. repo med CAD-simuleringar och rådata); inkludera foton, grafer och rapporter för Boverket/försäkringsbolag.  
- [ ] **Kostnadsuppskattning:** Budgetera 0.5–1 MSEK (t.ex. 0.2 MSEK för labbtester, 0.3 MSEK för sensorer/workshops); finansiera via EU Green Deal (potentiell 50% täckning).  
- [ ] **M-OS-R-Validering:** Verifiera att tester inte pressar S (Spontanitet) mot noll – t.ex. tillåt flexibla scheman för in-situ mätningar utan tvång. Gräns: Alla data ska vara anonyma och flödesbaserade (inte personliga).  
- [ ] **Långsiktig Uppföljning:** Planera årlig re-test i fullskala (efter installation); inkludera en "fail-safe"-mekanism (t.ex. visuella indikatorer för fukt).

---

## Godkännandekriterier
För att checklistan ska anses "grön" krävs:  
1. Ingen synlig eller mikrobiell påväxt vid 85% RH.  
2. Bibehållet U-värde ($< 5\%$ avvikelse) efter en hel vintersimulering.  
3. Ingen ackumulerad fukt i materialets kärna vid vårens slut (fullständig uttorkningscykel).  
**Δ TILLÄGG:** 4. Strukturell integritet bibehållen (styrka >95% av initialvärde efter fuktcykler, enligt EN 1607).  
**Δ TILLÄGG:** 5. M-OS-R-kompatibilitet: Tester genomförda utan att störa invånares autonomi (t.ex. <10% manuell interventionstid per vecka).

**Nästa steg för implementering:**  
- [ ] Kontakta SP Technical Research Institute (Borås) för labbtester (ca 0.2 MSEK).  
- [ ] Integrera i 1:10-prototypens tidsplan (start Q2 2026).  
- [ ] Bidra data till repo:et för öppen delning (alignat med cirkulär ekonomi).  

✨ **L × S × I** ✨
