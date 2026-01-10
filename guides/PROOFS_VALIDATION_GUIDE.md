# PROOFS_VALIDATION_GUIDE

**Status:** Active guidance  
**Intended location:** `guides / practical_implementation / validation`  
**Purpose:** Validate that the technical assumptions behind Flow remain true when checked against updated real‑world data.  
**Core idea:** Evidence is not ideology. Verification is not obedience. Reality decides.

---

This document explains how the Flow model is validated using updated data and a simple verification script. It exists to prevent self‑deception, myth‑building, and accidental Mammonization through wishful thinking.

> **Flow does not ask to be believed.** > **Flow asks to be checked.**

The validation process connects three layers:

1.  **TECHNICAL_ANNEX data** (assumptions about food, waste, surplus, recovery, energy drain)
2.  **Updated external data** (FAO, IMF, WPP, 2025–2026)
3.  **The Life = L × S × I model**

If these layers remain coherent under validation, Flow remains grounded.

---

### Core model reminder

Life = L x S x I 

* **L** = Baseline calm and security (food, water, shelter, clothing, health, connectivity)
* **S** = Spontaneity (freedom to act without fear or coercion)
* **I** = Involvement (social trust, relational presence, cooperation)

The system is considered minimally viable for Flow when total recovery exceeds **20 percent**. Below that, scarcity logic dominates cognition and behavior.

---

### Validation tool overview

The script `verify_proofs.py` is located in `core / data_validation`.

**Its purpose is to:**
* Compare **TECHNICAL_ANNEX** assumptions with updated 2025 data.
* Adjust multipliers conservatively (no optimistic jumps).
* Calculate effective food capacity under Flow conditions.
* Calculate total recoverable human energy.
* Confirm whether recovery remains above the **20 percent threshold**.

The script intentionally uses simple math and transparent assumptions. This is a feature, not a limitation.

> Complex models hide bias.  
> Simple models expose it.

#### What the script actually checks, in plain language:
* How much food humanity already produces.
* How much is lost to waste.
* How much surplus exists when waste is reduced.
* How much human energy is currently burned on non‑life‑producing activities.
* Whether reducing that drain frees enough capacity to cross the post‑scarcity threshold.

If the answer is **yes**, Flow is not utopian. It is logistically possible.

---

### How to use this validation

1.  Run the script in a Python environment.
2.  Read the printed output and the generated text file.
3.  **Confirm three things:**
    * Food multiplier remains approximately stable.
    * Flow food capacity still exceeds population needs.
    * Total recovery is greater than 20 percent.

**No interpretation gymnastics are allowed.**

If recovery drops below threshold:
* Update the annex.
* Adjust assumptions.
* Re‑run validation.
* **Accept the result.**

**Reality is the authority.**

---

### How this connects to the rest of the system

This guide exists to support:
* **THE_EVIDENCE** documentation.
* Honest iteration of **TECHNICAL_ANNEX**.
* Protection against ideological drift.
* Psychological safety for implementers.

Validation is not meant to convince skeptics. It is meant to protect builders.

---

### Final principle

Flow does not win by rhetoric. Flow survives by staying falsifiable. When the numbers stop supporting life, we stop and redesign.

That is not weakness. **That is integrity.**
