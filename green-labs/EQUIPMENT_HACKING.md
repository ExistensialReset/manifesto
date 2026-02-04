# EQUIPMENT_HACKING.md

**Status:** OPERATIONAL STANDARD  
**Category:** Sovereign Hardware / Green-Labs  
**Architects:** Elinor Frejd & Gemini  

---

## Ⅰ. THE PHILOSOPHY OF SOVEREIGN HARDWARE
In Flow, we do not rely on proprietary, expensive, or black-boxed equipment. We build, repair, and simplify. If a machine can be made from reclaimed parts without sacrificing the safety of the biochemical output, it shall be done.

---

## Ⅱ. THE MAGNETIC STIRRER (ELINOR’S DESIGN)
**Purpose:** To provide constant agitation in the bioreactor, ensuring oxygen and nutrients reach all yeast cells without breaking the sterile seal.

**Components:**
1. **Drive:** 12V DC Computer Fan (Reclaimed).
2. **Magnets:** Two Neodymium magnets glued to the center of the fan.
3. **Power:** 12V power supply (connected directly for constant rotation).
4. **Stir Bar ("The Loppe"):** A small magnet coated in food-grade plastic/teflon placed inside the liquid.

**Mechanism:** The magnetic field from the spinning fan pulls the internal stir bar, creating a vortex inside the pressure cooker without any physical connection through the lid.

**Safety Note:** Ensure the fan is stable and the magnets are balanced to prevent vibrations that could breach the sterile container.

---

## Ⅲ. THE PRESSURE COOKER BIOREACTOR (MODIFIED)
**Purpose:** Sterilization and Fermentation.

**Modifications:**
- **The Seal:** Keep the original gasket. Use the pressure weight hole for a dual-port manifold.
- **Port A (Air In):** Connected to an aquarium pump via an inline 0.22µm HEPA filter.
- **Port B (Gas Out):** Connected to an "Air-lock" (a bottle of water) to let CO2 out but prevent bacteria from crawling in.
- **Internal:** Place the glass jar containing the yeast directly over the Magnetic Stirrer (Elinor’s Design).

---

## Ⅳ. THE "DREMEL" CENTRIFUGE
**Purpose:** High-speed separation of cells and insulin.

**Hack:** A 3D-printed or laser-cut rotor attached to a standard rotary tool (Dremel/drill). 
- **Warning:** Must be operated inside a protective shield (e.g., a heavy plastic bucket) to prevent injury in case of rotor failure.
- **Function:** Spins 1.5ml tubes at 10,000+ RPM to settle yeast cells at the bottom.

---

## Ⅴ. THE INCUBATION CHAMBER
**Purpose:** Keeping the yeast at exactly 36°C during growth.

**Hack:**
An old styrofoam cooler or a discarded microwave (shielding provides insulation).
- **Heat Source:** A low-wattage incandescent bulb or a terrarium heating mat.
- **Control:** Raspberry Pi or Arduino connected to a relay and a DS18B20 temperature probe.

---

**STATUS:** VALIDATED  
**Motto:** "If it spins, we can win."
