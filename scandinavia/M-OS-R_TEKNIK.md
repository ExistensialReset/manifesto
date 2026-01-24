# M-OS-R Cheatsheet för AI/Systemdesign

## Syfte
Snabb referens för ingenjörer: Hur man bygger M-OS-R-kompatibla system.

---

## Basprincip: L × S × I
- **L – Lugn**: Systemet får inte skapa permanent stress. Baslinjen måste alltid vara tryggad.
- **S – Spontanitet**: Systemet måste ge utrymme för improvisation, variation och oförutsedda behov.
- **I – Inkännande**: Systemet ska skydda individens integritet och värdighet.

> Om någon faktor pressas mot noll kollapsar helheten.

---

## Nyckelkrav

1. **Baslinjen måste skyddas**  
   - Mat, värme, skydd, vila och grundläggande vård är ovillkorligt.

2. **Systemet anpassar sig snabbare än användaren**  
   - Justeringar sker automatiskt. Ingen människa ska behöva optimera eller pressa sig.

3. **Fel får inte bli existentiella**  
   - Misstag, långsamhet eller frånvaro ska inte hota trygghet eller tillhörighet.

4. **Ansvar är synligt, makt är inte det**  
   - Alla beslut spåras. Ingen dold hierarki eller kontroll utan ansvar.

5. **Ingen reduceras till resurs**  
   - Systemets effektivitet får inte bygga på mänsklig överbelastning.

6. **Tystnad & återhämtning är inbyggt**  
   - Arkitektur ger utrymme för vila, stillhet och emotionellt återhämtning.

7. **Teknik får aldrig ha egen auktoritet**  
   - Fråga alltid: Vad skyddar du? Inte: Vad optimerar du?

8. **Systemet fungerar vid lågintensivt liv**  
   - Systemet ska fungera utan extra driv, prestanda eller motivation.

9. **Alltid väg tillbaka**  
   - Användare kan lämna, vila och återvända utan skuld eller förlust av värde.

---

## Tips för implementering

- Tänk modulärt: varje flöde ska vara resilient oberoende av andra.  
- Testa “stressfria” scenarier: fungerar systemet när ingen interagerar aktivt?  
- L × S × I som kodpolicy: varje beslut/algoritm ska verifieras mot de tre faktorerna.  
- Dokumentera ansvar och flöden explicit. Inga “hemliga” komponenter.  

---

**Kort sagt:**  
M-OS-R handlar inte om att pressa människor.  
Det handlar om att bygga **system som skyddar L × S × I** – alltid.