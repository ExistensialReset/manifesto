# LOTUS_PROTOCOL.md

**Version:** 1.0  
**Status:** Core Specification  
**Scope:** Cross-Scale Role Selection  
**Layer:** Governance Infrastructure  
**Author:** Elinor Frejd  
**Date:** 2026-02-26  

LOTUS defines how all cross-scale roles are selected, rotated, and reviewed inside M-OS-R.

It prevents representative power concentration through deterministic lottery selection and mandatory rotation.

LOTUS governs selection.  
It does not govern case outcomes.

---

# 1. PURPOSE

The protocol ensures:

- No representative role is self-appointed
- No election campaigns occur
- No permanent governance class forms
- All selection is auditable
- All roles are temporary

Representation is a function, not a status.

---

# 2. SCOPE

LOTUS applies to:

- Node delegates  
- Regional delegates  
- Inter-Node coordinators  
- Crisis coordination roles (when applicable)  
- Any cross-circle decision-making panel  

No independent selection mechanisms are permitted at any scale.

---

# 3. SELECTION MODEL

## 3.1 Eligibility Pool

The selection pool includes all qualified members at the relevant scale.

Exclusions:

- Direct conflict-of-interest
- Active mandate in the same role
- Exceeded yearly selection limit

Self-recusal is permitted and must be logged.

---

## 3.2 Deterministic Lottery

Selection must be:

- Random
- Deterministic
- Offline-verifiable
- Publicly auditable

The draw must publish:

- Context string  
- Public nonce  
- Hash of the draw result  

Implementation details are defined separately.

---

# 4. MANDATE LIMITS

- Maximum consecutive service: 6 months  
- Maximum selections per calendar year: 2  
- Extended mandates require documented justification  
- Automatic rotation triggers when limits are reached  

No role may become permanent by default.

---

# 5. ROLE BOUNDARIES

Selected individuals:

- Transmit and coordinate  
- Do not accumulate executive authority  
- Do not override documented decisions  
- Must publish written summaries  

All decisions made within a mandate must be logged and reviewable.

---

# 6. DOCUMENTATION REQUIREMENTS

Each selection event must generate a log entry including:

- Event identifier  
- Timestamp  
- Context description  
- Eligibility pool summary  
- Verification reference  

Logs must be:

- Exportable  
- Retained locally  
- Auditable without cloud dependency  

Sensitive data may be anonymized after retention period.

---

# 7. REVIEW & AUDIT

Quarterly review must verify:

- Selection integrity  
- Rotation compliance  
- Documentation completeness  

Discrepancies must be publicly documented and resolved.

---

# 8. FAILURE ASSUMPTION

The protocol assumes:

- Informal power may accumulate  
- Familiar individuals may be repeatedly selected  
- Technical errors may occur  

Therefore:

- Rotation limits are enforced  
- Selection caps exist  
- Logs are mandatory  
- Audit is periodic  

If LOTUS creates status hierarchies, it must be adjusted.

---

# 9. CORE GUARANTEES

LOTUS guarantees:

- No campaign politics  
- No permanent office  
- No hidden selection process  
- No representation outside rotation  
- No scale exempt from lottery  

All cross-scale authority flows through LOTUS. 
