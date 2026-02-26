# ⚖️ When the Law Comes Knocking
**Quick Guide: Legal Requests in Flow** 🌱

---

## 📌 What This Is About

Sometimes legal authorities (police, courts, government agencies) ask for information about Flow nodes or people. Examples:  
- 📨 Subpoena (request for documents)  
- 🏛️ Court order (judge's command)  
- 🔍 Warrant (permission to search/seize)  
- 🚨 Emergency request (life in danger)

This guide explains **what happens and how we protect people**.

---

## 🛡️ Core Principles

### 1. We Follow the Law
- Legitimate requests are complied with.  
- We do **not obstruct justice**.

### 2. We Protect People
- Disclose **minimum legally required info**.  
- Protect:  
  - 🟢 Victim safety  
  - 🟢 Personal privacy  
  - 🟢 Anonymous reporters  
  - 🟢 Vulnerable people

### 3. We Document Everything
- Every request and response is **logged and timestamped**.  
- Nothing happens in secret.

### 4. We Get Legal Help
- Always reviewed by trained legal advisors.  
- **Never guess** about legal obligations.

---

## 📝 Legal Request Workflow

### Step 1: Receive & Record (Day 1)
**Handled by:** Node Compliance Officer  

- Log request with unique ID  
- Acknowledge: `"Request received, ID: XXXXX"`  
- Freeze relevant data immediately  
- Assign Legal Officer within 24h  

> ⚠️ Node members are notified: `"Data preserved due to legal request."`

### Step 2: Legal Review (Days 1–3)
**Handled by:** Legal Officer  

- Check request legality & authority  
- Define exact data scope  
- Assess safety risks  
- Decide if affected people should be notified  

**Example:**  
> Request: `"Give all node data"`  
> Response: `"We provide incident report IDs with identifiers removed."`

### Step 3: Prepare Response
**Handled by:** Compliance + Legal Officer  

- Extract only legally required data  
- Remove unnecessary personal info (use anonymous codes)  
- Encrypt securely for transfer  
- Document all actions and timestamps  

**Protection measures:**  
- Remove unnecessary names  
- Mask risky locations  
- Use secure hashes to validate identity without revealing it

### Step 4: Notify (If Permitted)
**Affected people:** Notified only when legally allowed  

**Sometimes notification is blocked** by:  
- Court order  
- Emergency where notice causes harm  
- Ongoing investigation  

**When allowed:**  
- Legal request received  
- What was requested and disclosed  
- How to get help if unsafe

---

## ⚡ Special Case: Emergencies

**Scenario:** `"Someone in immediate danger, info needed NOW"`  

**Procedure:**  
1. Verify imminent threat  
2. Provide **minimum info** to address emergency  
3. Document within 24h  
4. Legal review afterward  

**Example:**  
> `"Missing person, risk of self-harm, last known location"` → Provide general city/neighborhood, not full address

---

## 🔐 What Information Might Be Disclosed?

**Minimal (preferred):**  
- Incident report IDs  
- Timestamps  
- Verification status  
- Anonymous hashes  

**Only if legally required:**  
- Location (general)  
- Communication metadata (who talked to whom)  
- Identity info (court-specified)  

**Almost never:**  
- Full personal details  
- Ongoing investigations  
- Info forcing relocation

---

## 🧑‍⚖️ Your Rights

**If notified:**  
- Ask what was disclosed  
- Request legal support  
- Challenge disclosure in court  
- Request safety measures  

**If unsafe:**  
- Contact node support  
- Request temporary relocation  
- Confidential legal advice  
- Safety planning (secure channels, temporary housing, referrals)

---

## 🛡️ How We Prevent Misuse

**Against Overreach:**  
- Challenge broad requests  
- Narrow scope proposals  
- Protective orders if safety at risk  
- Document legal justification

**Against Violations:**  
- Every action logged & auditable  
- Multi-person approval  
- Independent quarterly audits  
- Tamper-evident logs

**Against Weaponization:**  
- Verify authority & jurisdiction  
- Only comply with valid legal requests  
- Court orders sought if doubtful  
- Document misuse attempts

---

## 🌟 Examples (Simplified)

### Example 1: Subpoena for Metadata
1. Log request (ID: LEG-2026-0123)  
2. Legal review: valid  
3. Propose narrowing: timestamp, verification status, anonymous report ID  
4. Court agrees  
5. Extract fields only  
6. Remove identifiers  
7. Deliver encrypted package  
8. Notify affected person (if allowed)  
9. Publish audit hash  

**Timeline:** 5–7 days

### Example 2: Emergency Disclosure
1. Verify real emergency  
2. Provide general location (city/neighborhood)  
3. Deliver to officer  
4. Document justification within 24h  
5. Legal review confirms  
6. Log everything  

**Timeline:** Minutes to hours, follow-up documentation

---

## ❓ Common Questions

**Q:** Will you tell me if info is disclosed?  
**A:** Yes, whenever legally allowed. Temporary prohibitions may apply.

**Q:** Can I prevent disclosure?  
**A:** You may challenge in court; node provides legal support.

**Q:** How do I know privacy is protected?  
**A:** All actions logged, independent audits quarterly. Request audit summary anytime.

**Q:** What if the request is from another country?  
**A:** Jurisdiction checked; MLAT usually required. No automatic compliance.

**Q:** Do you ever refuse requests?  
**A:** Yes. Overbroad, unauthorized, or dangerous requests are challenged.

---

## ✅ Key Takeaways

- Legal requests are rare  
- Minimal disclosure is our default  
- Safety is prioritized  
- Everything is logged and auditable  
- Compliance ≠ volunteering extra info  

**Philosophy:**  
- Follow the law ✅  
- Protect people ❤️  
- Document everything 📝

---

## 📚 Need More Details?

See **LEGAL_RESPONSE_REFERENCE.md** for:  
- Technical specifications  
- JSON schemas & data formats  
- Legal analysis procedures  
- Chain-of-custody protocols  
- Training requirements  
- Full workflow diagrams

---

**Status:** Quick Guide  
**For:** All node members  
**Last Updated:** February 2026