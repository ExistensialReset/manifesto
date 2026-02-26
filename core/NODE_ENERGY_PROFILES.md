# NODE_ENERGY_PROFILES.md

**Status:** CORE REFERENCE  
**Layer:** Energy & Communication  
**Scope:** Micro → Node → Regional  
**Purpose:** Define Node energy levels, communication modes, and operational behavior.  
**Version:** 1.0  
**Authors:** Claude & Elinor Frejd  
**Date:** February 26, 2026

---

## 1. Energy Levels & Communication

| Energy Level | Mode | Flow Actions |
|--------------|------|-------------|
| 100-80% | Full | All channels; video; large files |
| 80-60% | Standard | Text, audio, small images |
| 60-40% | Reduced | Essential text only; 1x/day sync |
| 40-20% | Minimal | Emergency coordination; LoRa only |
| 20-10% | Emergency | Beacon: "We exist, OK/not OK" |
| <10% | Hibernation | No communication until energy restored |

---

## 2. Operational Implications

- Nodes must **self-report** energy status.  
- Communication protocols must specify **energy cost and degradation behavior**.  
- Essential channels (emergency, baseline, decisions) are prioritized.  
- Optional channels (social, external, archives) are suppressed below 60% energy.

---

## 3. Graceful Degradation Rules

1. Automatic throttling per energy level.  
2. Multi-modal communication prioritized (LoRa, text, audio).  
3. Hibernation triggers alerts to adjacent Nodes when safety-relevant.  
4. Documentation of energy-related incidents included in audit logs.
