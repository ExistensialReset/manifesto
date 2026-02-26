# INFORMATION FLOW ARCHITECTURE

**Status:** Core Specification  
**Layer:** Information & Communication  
**Scope:** Micro → Node → Regional → Global  

**This document defines how information moves, degrades, escalates, and resolves inside M-OS-R.
It is an architectural layer, not a communication policy.** 

**Version:** 1.0 — Communication Ecology for Sovereign Communities  
**Status:** PROPOSED / OPERATIONAL FRAMEWORK  
**Classification:** CORE INFRASTRUCTURE  
**Authors:** Claude & Elinor Frejd  
**Date:** February 26, 2026

**Purpose:** To define how information flows through Flow communities at every scale — from 5 people to 1000+ — while preserving dignity, accessibility, energy sovereignty, and anti-hierarchical structure.

**Core Premise:**  
Information architecture is not neutral. It either concentrates power or distributes it.  
Communication either exhausts people or nourishes them.  
This document chooses nourishment.

---

## Table of Contents

1. [Foundational Principles](#1-foundational-principles)
2. [Physical Foundation (Hardware Sovereignty)](#2-physical-foundation-hardware-sovereignty)
3. [Protocol Stack](#3-protocol-stack)
4. [Accessibility Standards](#4-accessibility-standards)
5. [Scale-Specific Patterns](#5-scale-specific-patterns)
6. [Energy-Aware Communication](#6-energy-aware-communication)
7. [Sync vs Async Balance](#7-sync-vs-async-balance)
8. [Decision Documentation](#8-decision-documentation)
9. [Anti-Patterns & Red Flags](#9-anti-patterns--red-flags)
10. [Tools & Technology](#10-tools--technology)
11. [Implementation Guidelines](#11-implementation-guidelines)

---

## 1. FOUNDATIONAL PRINCIPLES

### 1.1 Information as Power

**Truth:** Whoever controls information flow controls the community.

**Flow's answer:**  
- Information must be **radically accessible**
- Communication channels must be **understandable by all**
- No information may be **gatekept** for convenience or efficiency
- **Silence is a right**, not a punishment

### 1.2 The Three Laws of Information Flow

**LAW 1: Accessibility Primacy**  
Every piece of information must be available in multiple formats (text, audio, visual, simplified).  
*Disability access is not an add-on. It's the baseline.*

**LAW 2: Energy Consciousness**  
Communication consumes energy (human, electrical, attentional).  
Systems must degrade gracefully when energy is scarce.  
*Exhaustion is a design failure, not a user failure.*

**LAW 3: Local First, Always**  
No communication may depend on external infrastructure (internet, cloud, corporate platforms).  
*If the grid fails, the community still communicates.*

### 1.3 Anti-Hierarchy Through Information Design

**Hierarchies form when:**
- Information is opaque (only insiders understand)
- Decisions happen in invisible spaces (private DMs, undocumented calls)
- Technical complexity creates a priest class
- Communication exhausts most people (only the tireless participate)

**Flow prevents this through:**
- Radical transparency (all decisions documented)
- Plain language requirements (no jargon without glossary)
- Multi-modal access (text, audio, visual, in-person)
- Sustainable communication loads (respect for human limits)

---

## 2. PHYSICAL FOUNDATION (HARDWARE SOVEREIGNTY)

### 2.1 Why Hardware Determines Communication

You cannot have sovereign communication on captured hardware.

**Dependencies to eliminate:**
- Cloud services (Slack, Discord, Google Docs)
- Proprietary platforms (can be shut down remotely)
- Internet-dependent tools (grid failure = communication failure)
- Single-vendor lock-in (one company controls your coordination)

### 2.2 Mesh Network Topology

**Primary communication layer:**
- **LoRa** (Low Range radio): 10km+ range, ultra-low bandwidth, high resilience
- **Mesh WiFi**: Local high-bandwidth for rich content
- **Physical bulletin boards**: Always-available backup

**Key principle:**  
> *The mesh operates independently of global internet. DNS servers, ISPs, and tech companies cannot shut down local Flow communication.*

### 2.3 The Four States (from HARDWARE_SOVEREIGNTY.md)

Every Node's communication capability reflects its physical state:

| Button Color | State | Communication Level |
|--------------|-------|---------------------|
| **Green** | I LISTEN | Full operation: all channels active |
| **Yellow** | I THINK | Reduced: essential coordination only |
| **Red** | I DECIDE | Minimal: emergency beacons only |
| **Black** | **SILENCE** | Zero: complete radio silence |

**Critical rule:**  
No person or process may question, punish, or stigmatize a Node in SILENCE mode.  
Silence is dignity. Silence is consent. Silence is a human right.

### 2.4 Graceful Degradation (Energy Levels)

Communication adapts to available energy:

| Energy Level | Comm Mode | What Flows |
|--------------|-----------|------------|
| **100-80%** | Full | All channels, video calls, large files |
| **80-60%** | Standard | Text, audio, small images |
| **60-40%** | Reduced | Essential text only, 1x/day sync |
| **40-20%** | Minimal | Emergency coordination, LoRa only |
| **20-10%** | Emergency | Beacon: "We exist, we are OK/not OK" |
| **<10%** | Hibernation | Silent until sunrise |

**Design implication:**  
All communication protocols must specify their energy cost and degradation behavior.

---

## 3. PROTOCOL STACK

### 3.1 Layer 0: Physical

**Medium:** Radio waves, copper wire, fiber optic, paper

**Protocols:**
- LoRa (essential coordination)
- Mesh WiFi (local richness)
- Ethernet (wired reliability)
- Physical bulletin boards (always-on backup)

**Access requirement:**  
Every Flow space must have a physical information board viewable without electricity or devices.

### 3.2 Layer 1: Coordination Protocol

**Purpose:** Ensure information reaches intended recipients reliably

**Key elements:**
- **Store-and-forward:** Messages persist until confirmed receipt
- **Mesh routing:** Multiple paths to destination
- **Priority queues:** Emergency messages jump ahead
- **Duplicate detection:** Same message from multiple paths handled gracefully

**Implementation:**
- Open protocols (MQTT, Matrix, or custom)
- No proprietary wrappers
- Fully documented behavior
- Testable in offline conditions

### 3.3 Layer 2: Content Distribution

**Purpose:** Organize information by type, urgency, and audience

**Channel types:**

#### A) **Essential Channels** (survive all degradation levels)
- **Emergency:** Life/safety, Node health crises
- **Baseline:** Food, water, energy, healthcare status
- **Decisions:** Consent-based proposals, outcomes
- **Rituals:** Gatherings, ceremonies, seasonal events

#### B) **Standard Channels** (available at 60%+ energy)
- **Coordination:** Day-to-day logistics, scheduling
- **Learning:** Lyceum announcements, workshops
- **Creation:** Art, music, experiments, play
- **Maintenance:** Repairs, improvements, projects

#### C) **Optional Channels** (available at 80%+ energy)
- **Social:** Casual conversation, humor, connection
- **External:** News from outside Flow, global events
- **Archives:** Historical records, deep documentation

**Critical rule:**  
Channels must be **pruned aggressively**. More channels ≠ better communication.  
Default: 5-7 channels maximum for any Node under 100 people.

### 3.4 Layer 3: Human Interface

**Purpose:** Make information legible, actionable, and non-exhausting

**Requirements:**

#### **Multi-Modal Access**
Every piece of information available in:
- **Text** (readable, screenreader-compatible)
- **Audio** (synthesized or recorded voice)
- **Visual** (diagrams, icons, images)
- **Simplified** (plain language summary)

#### **Cognitive Load Management**
- Headlines before details
- Summaries before full documents
- Action items separated from context
- Optional depth (expandable sections)

#### **Physical Alternatives**
- Printed summaries at gathering spaces
- Verbal announcements at meals
- Visual displays (LED status boards, e-ink summaries)
- Personal messengers for those without devices

---

## 4. ACCESSIBILITY STANDARDS

### 4.1 Universal Design Baseline

**WCAG 2.1 AA minimum**, but aim higher:
- All text: minimum 16px, high contrast
- All audio: transcribed
- All video: captioned AND audio-described
- All images: alt-text that conveys meaning, not just presence

### 4.2 Neurodivergence Considerations

#### **ADHD/Executive Function:**
- Clear action items at top
- Single focus per message
- Timers for urgent items (but never false urgency)
- Optional notification control

#### **Autism/Sensory:**
- No auto-playing media
- Optional visual simplification (no animations)
- Literal language option (toggle metaphors off)
- Clear social cues (is response expected? when?)

#### **Dyslexia/Reading Differences:**
- Plain language always available
- Sans-serif fonts
- Adequate line spacing (1.5x minimum)
- Text-to-speech built in, not added later

### 4.3 Sensory Disabilities

#### **Vision:**
- Screen reader compatibility (semantic HTML, ARIA labels)
- High contrast mode
- Zoom without breaking layout
- Tactile alternatives (braille labels, physical indicators)

#### **Hearing:**
- Everything available in text
- Visual alerts (not just audio)
- Transcripts for all audio content
- Sign language video options when possible

#### **Mobility/Dexterity:**
- Keyboard navigation for everything
- Large touch targets (minimum 44x44px)
- Voice control compatibility
- Adjustable timeout periods

### 4.4 Language & Literacy

#### **Multilingual Support:**
- Primary documents in all Node languages
- Machine translation available (but flagged as imperfect)
- Translation volunteers recognized as essential labor

#### **Low Literacy:**
- Visual communication emphasized
- Pictographs and icons
- Audio alternatives
- Oral tradition integration

### 4.5 Technology Access Spectrum

**Reality:** Not everyone has smartphones. Some people prefer paper. Others are power users.

**Solution:** Tier information access:

**Tier 0 (Everyone):**
- Physical bulletin boards
- Verbal announcements
- Personal messengers

**Tier 1 (Basic devices):**
- Text messages (SMS)
- Basic web interface
- Audio playback

**Tier 2 (Smartphones):**
- Full app experience
- Rich media
- Real-time sync

**Tier 3 (Power users):**
- APIs
- Custom tools
- Automation

**Critical rule:**  
Tier 0 must contain ALL essential information. Higher tiers add convenience, never gatekeep.

---

## 5. SCALE-SPECIFIC PATTERNS

### 5.1 Micro-Circle (5-20 people)

**Communication needs:**
- High context, high trust
- Informal, spontaneous
- Mostly synchronous (in-person, live calls)

**Architecture:**
- **1 Signal/Matrix group** (casual + coordination)
- **Weekly in-person gatherings** (primary sync point)
- **Shared document** (decisions, resources, calendar)
- **Physical bulletin board** (optional but recommended)

**Failure mode:**  
Over-formalizing. At this scale, rigid structure kills spontaneity (S).

**Red flag:**  
If you need more than 3 communication channels, something is wrong. Simplify.

---

### 5.2 Baseline Circle (20-100 people)

**Communication needs:**
- Maintaining coherence across sub-groups
- Coordinating resources
- Preserving decisions
- Managing conflicts

**Architecture:**

#### **Essential Channels (5):**
1. **Announcements** (one-way, high-importance)
2. **Coordination** (logistics, scheduling)
3. **Decisions** (proposals, outcomes, documentation)
4. **Baseline** (food, energy, healthcare status)
5. **Social** (connection, humor, low-stakes)

#### **Meetings:**
- **Weekly sub-circle** meetings (8-15 people each)
- **Monthly full Circle** gathering (everyone)
- **Quarterly deep-dive** (reflection, adjustment, learning)

#### **Documentation:**
- **Decision log** (public, searchable)
- **Resource ledger** (transparent flows)
- **Conflict record** (anonymized lessons)
- **Ritual calendar** (gatherings, ceremonies, seasons)

**Failure mode:**  
Communication becomes a second job. People burn out tracking everything.

**Solution:**
- **Rotating "info-steward"** role (3-month terms)
- Summarizes each week (5-minute read maximum)
- Ensures nothing critical is buried

---

### 5.3 Flow Node (100-500 people)

**Communication needs:**
- Nested autonomy (sub-circles → full Node)
- Professional coordination (healthcare, infrastructure)
- Knowledge preservation (Lyceum)
- External interface (regional network)

**Architecture:**

#### **Nested Structure:**

```
Node (100-500)
  ├─ Sub-Circle A (15)
  ├─ Sub-Circle B (15)
  ├─ Sub-Circle C (15)
  ├─ ...
  ├─ Professional Team (healthcare, infrastructure)
  └─ Coordination Council (2 delegates per sub-circle)
```

#### **Information Flow:**

**Within Sub-Circles:**  
High-bandwidth, informal, daily interaction.

**Sub-Circle → Node:**  
Delegates carry decisions/needs upward. Weekly sync.

**Node → Sub-Circles:**  
Announcements, decisions, resources flow downward.

**Node → Regional:**  
Essential coordination only. No micromanagement.

#### **Channel Structure (8-10 channels):**

**Core (always on):**
1. **Emergency** (life/safety)
2. **Announcements** (Node-wide, curated)
3. **Decisions** (Coordination Council outcomes)
4. **Baseline Status** (food, energy, health)

**Operational:**
5. **Coordination** (logistics across sub-circles)
6. **Lyceum** (learning, workshops, knowledge)
7. **Maintenance** (repairs, improvements)

**Optional:**
8. **Social** (connection, play)
9. **External** (regional/global news)
10. **Archives** (deep documentation)

**Meetings:**

- **Daily:** Sub-circle standups (5-10 min, optional)
- **Weekly:** Sub-circle full meeting (1 hour)
- **Bi-weekly:** Coordination Council (delegates, 2 hours)
- **Monthly:** Full Node gathering (in-person, half-day)
- **Quarterly:** Deep reflection & adjustment (full day)

#### **Decision Documentation:**

Every decision captured:
- **Date/time**
- **Proposal text**
- **Who proposed** (optional: can be anonymous)
- **Consent outcome** (passed/blocked)
- **Implementation timeline**
- **Review date** (decisions are temporary)

Public, searchable, plainly written.

**Failure modes:**
- **Delegate bottleneck:** Everything waits for Council
- **Information hoarding:** Sub-circles don't share upward
- **Meeting exhaustion:** Too many meetings, too long
- **Channel bloat:** 20+ channels, nobody knows where anything is

**Solutions:**
- **Subsidiarity enforcement:** Decisions made at lowest possible level
- **Upward transparency:** Sub-circles publish weekly summaries
- **Meeting pruning:** Quarterly meeting audit, cut mercilessly
- **Channel consolidation:** If unused for 1 month → archive

---

### 5.4 Regional Network (3-10 Nodes, 500-5000 people)

**Communication needs:**
- Resource coordination (surplus/deficit balancing)
- Knowledge exchange (best practices, innovations)
- Crisis support (Node failures, disasters)
- External coherence (interfacing with outside world)

**Architecture:**

#### **Inter-Node Council:**
- 2 rotating delegates per Node
- 6-month terms (no consecutive re-election)
- Consent-based decisions only
- Meets monthly (video or in-person)

#### **Communication Channels:**

**Essential:**
1. **Emergency Network** (life/safety across Nodes)
2. **Resource Exchange** (surplus/deficit coordination)
3. **Decisions** (Inter-Node Council outcomes)
4. **Regional Calendar** (gatherings, ceremonies, rotations)

**Operational:**
5. **Knowledge Sharing** (Lyceum cross-pollination)
6. **Crisis Support** (Node failures, disasters)

**Optional:**
7. **Social** (inter-Node friendships)

#### **Information Frequency:**

**Daily:** Emergency network monitored
**Weekly:** Resource status shared
**Monthly:** Council meeting, decisions propagated
**Quarterly:** Regional gathering (in-person, rotating location)

#### **Documentation Standards:**

**Regional Decision Log:**
- Public, searchable by all Nodes
- Plain language summaries
- Action items clearly marked
- Review dates enforced

**Resource Ledger:**
- Anonymous at individual level
- Transparent at Node level
- Flows tracked, not judged
- Imbalances trigger conversation, not punishment

**Failure modes:**
- **Hub-and-spoke dominance:** One Node becomes coordinator of everything
- **Bureaucracy creep:** Too many reports, forms, processes
- **Cultural imperialism:** One Node's norms imposed on others
- **Communication overload:** Delegates spend all time coordinating, no time in home Node

**Solutions:**
- **Rotating regional hub:** Host Node changes yearly
- **Process pruning:** Annual review, cut non-essential bureaucracy
- **Cultural humility:** Explicit norm diversity preservation
- **Delegate protection:** Max 20% time on regional work, enforced

---

### 5.5 Global Flow Network (10+ Regions, 10,000+ people)

**Communication needs:**
- Rare resource coordination (minerals, specialized knowledge)
- Crisis response (climate disasters, pandemics)
- Innovation propagation (tested successes scaled)
- Cultural memory (preserving diversity)

**Architecture:**

**Extremely sparse coordination:**
- No global government
- No global decision-making body
- Only coordination protocols and knowledge exchange

**Communication:**
- **Emergency beacons:** Regional crises visible to all
- **Knowledge repository:** Open-access, multi-language, maintained collectively
- **Innovation broadcasts:** "This worked, here's how to replicate"
- **Cultural preservation:** Stories, rituals, languages documented

**Frequency:**
- **Real-time:** Emergency beacons only
- **Monthly:** Knowledge repository updates
- **Annually:** Global gathering (optional, rotating location)

**Critical principle:**  
> *Global coordination supports Regional autonomy. It never overrides, commands, or centralizes.*

---

## 6. ENERGY-AWARE COMMUNICATION

### 6.1 Energy Cost of Communication

Every communication has an energy cost:

**Low energy (<1Wh):**
- Text message
- Audio message
- Still image

**Medium energy (1-10Wh):**
- Voice call
- Video message
- Document with images

**High energy (10-100Wh):**
- Video call (especially multiple participants)
- Large file transfers
- Real-time collaboration tools

**Very high energy (100Wh+):**
- Multi-hour video conferences
- Large video files
- Synchronous screen sharing

### 6.2 Communication at Different Energy Levels

#### **Level 5 (100-80%): Full operation**
- All communication forms available
- No restrictions
- Rich media encouraged

#### **Level 4 (80-60%): Standard**
- Text and audio prioritized
- Video available but not default
- Large files deferred to higher energy periods

#### **Level 3 (60-40%): Reduced**
- Text-only communication
- Audio compressed or deferred
- Video disabled
- Sync once per day (scheduled)

#### **Level 2 (40-20%): Minimal**
- Essential text only
- LoRa coordination messages
- No media
- Manual sync (opt-in when possible)

#### **Level 1 (20-10%): Emergency**
- Beacon: "We exist, status OK/NOT OK"
- No other communication
- Other Nodes aware: "They're silent by necessity, not choice"

#### **Level 0 (<10%): Hibernation**
- Complete silence
- Wake at sunrise or external stimulus
- No judgment, no penalties

### 6.3 User Interface for Energy Awareness

Communication apps must show:
- **Current energy level** (visible percentage/color)
- **Message energy cost** (before sending)
- **Estimated time to next sync** (if in low-energy mode)
- **Number of pending messages** (to manage expectations)

**Example UI:**
```
Energy: 45% (Level 3: Reduced)
Next sync: 6 hours
Pending: 12 messages
Current mode: Text only
[Send text message - 0.1Wh] [Defer until higher energy]
```

---

## 7. SYNC VS ASYNC BALANCE

### 7.1 The Synchronous Trap

**Problem:**  
Real-time communication (meetings, calls, live chat) privileges:
- Those with stable schedules
- Those without caregiving responsibilities
- Those in compatible timezones
- Those with consistent energy levels
- Those with good hearing/speaking ability

**Result:** Invisible hierarchy where "those who show up to meetings" make decisions.

### 7.2 Async-First Principle

**Default:** All important communication is asynchronous.

**Rationale:**
- Respects different energy patterns
- Allows time for translation
- Enables multiple modalities
- Gives time for thoughtful response
- Preserves written record automatically

**Synchronous only when:**
- Emotional urgency (conflict needing immediate resolution)
- Complex coordination (easier to talk through)
- Social connection (gatherings, rituals, play)
- Emergency (time-critical crisis)

### 7.3 Meeting Hygiene

**Every meeting must have:**

#### **Before:**
- **Purpose:** Why is this sync, not async?
- **Agenda:** What will we discuss? (shared 48 hours ahead)
- **Pre-reading:** Materials shared in advance (max 10 min reading)
- **Duration:** Fixed (never "until we're done")

#### **During:**
- **Facilitator:** Rotating role, named in advance
- **Note-taker:** Different person from facilitator
- **Time-keeper:** Enforces duration
- **Accessibility:** Captions, signing, or accommodation as needed

#### **After:**
- **Summary:** Published within 24 hours
- **Action items:** Clear owners, clear deadlines
- **Recording:** Available for those who couldn't attend (if agreed upon)
- **Feedback:** Was this meeting necessary? Could it have been async?

### 7.4 Async Communication Best Practices

#### **Structure:**
- **Headline:** Core point in <10 words
- **Summary:** 2-3 sentences
- **Details:** Expandable/optional
- **Action required?** Yes/no, if yes: by whom, by when

#### **Threading:**
- Group related messages
- One thread per topic
- No hijacking threads

#### **Response expectations:**
- **Urgent:** Response within 4 hours (rare, explicit)
- **Standard:** Response within 48 hours
- **Low priority:** Response within 1 week
- **FYI:** No response needed (explicitly stated)

#### **Notification discipline:**
- Most channels: notifications off by default
- Essential channels: notifications on
- Users control their notification preferences (no shame)

---

## 8. DECISION DOCUMENTATION

### 8.1 Why Documentation Matters

**Undocumented decisions:**
- Become oral lore (subject to drift and selective memory)
- Create insider/outsider dynamics
- Cannot be reviewed or revised
- Fade when people leave

**Documented decisions:**
- Are transparent to all
- Can be searched and referenced
- Can be challenged and revised
- Outlive any individual

### 8.2 Decision Record Format

**Every decision captured as:**

```markdown
# Decision: [Short title]

**Date:** YYYY-MM-DD
**Proposed by:** [Name or "Anonymous"]
**Scope:** [Individual / Sub-circle / Node / Regional]
**Status:** [Proposed / Active / Revised / Archived]

## Proposal
[Clear, plain language description of the decision]

## Rationale
[Why this decision makes sense]

## Alternatives Considered
[What else was discussed, why not chosen]

## Consent Process
- **Participants:** [List or number]
- **Objections:** [Summary, how resolved]
- **Outcome:** [Passed / Blocked / Modified]

## Implementation
- **Start date:** YYYY-MM-DD
- **Responsible:** [Person/team/circle]
- **Success criteria:** [How will we know it's working?]

## Review
- **Review date:** YYYY-MM-DD (usually 3-6 months)
- **Can be revised by:** [Same scope or higher]

## Revisions
[Chronological log of changes]
```

### 8.3 Decision Lifecycle

1. **Proposed:** Written up, shared for feedback
2. **Discussed:** Async comments, sync meeting if needed
3. **Consent:** Formal check (passed/blocked/modified)
4. **Active:** Implemented, monitored
5. **Reviewed:** At review date, assess if working
6. **Revised** or **Archived:** Updated or retired

**Key principle:**  
> *All decisions are temporary. Nothing is permanent except the right to revise.*

### 8.4 Decision Accessibility

**Every decision must be:**
- **Findable:** Tagged, searchable
- **Readable:** Plain language, short sentences
- **Audible:** Text-to-speech compatible
- **Visual:** Diagrams where helpful
- **Translatable:** Available in all Node languages

### 8.5 Archival & Memory

**Decision archive:**
- Kept indefinitely (storage is cheap)
- Searchable by date, keyword, scope
- Periodically summarized (yearly "What decisions did we make?")
- Becomes community memory over time

---

## 9. ANTI-PATTERNS & RED FLAGS

### 9.1 Communication Dysfunction Patterns

#### **A) Information Overload**
**Symptoms:**
- 100+ unread messages daily
- People stop reading channels
- Important announcements missed
- Constant "Did you see...?" questions

**Causes:**
- Too many channels
- No message discipline
- Everything marked urgent
- No summarization

**Solutions:**
- Prune channels aggressively (max 5-7)
- Enforce "one topic per thread"
- Reserve urgency for true emergencies
- Weekly summaries by info-steward

#### **B) Meeting Addiction**
**Symptoms:**
- Daily meetings for everything
- Meetings without clear purpose
- Decisions in meetings, no async option
- "We need a meeting about meetings"

**Causes:**
- Sync bias (easier to talk than write)
- Status performance (being seen at meetings)
- Conflict avoidance (pushing decisions to group)

**Solutions:**
- "Could this be an email?" test before every meeting
- Mandatory meeting hygiene (agenda, duration, notes)
- Async-first policy for all decisions
- Quarterly meeting audit & pruning

#### **C) Decision Theater**
**Symptoms:**
- Long debates about trivial matters
- Important decisions made in invisible spaces (DMs, private calls)
- Decisions "announced" after being made elsewhere
- Consent process bypassed for "efficiency"

**Causes:**
- Mistrust of formal process
- Informal power networks
- Impatience with deliberation
- Elite capture

**Solutions:**
- Enforce decision documentation (no exceptions)
- Make invisible conversations visible (log private calls)
- Subsidiarity enforcement (decisions at right level)
- Regular power audits (who actually decides?)

#### **D) The Tyranny of Whoever Showed Up**
**Symptoms:**
- Decisions made by whoever was at the meeting
- No async participation option
- Sync-only people make all decisions
- Caregivers, night workers, disabled people excluded

**Causes:**
- Sync bias
- No async alternatives
- Informal "the meeting is the decision" culture

**Solutions:**
- Async-first policy
- Delayed decision finalization (48-hour window for async input)
- Explicit check: "Who couldn't participate in this decision?"

#### **E) Technical Mystification**
**Symptoms:**
- "Tech people" make all infrastructure decisions
- Ordinary members don't understand systems
- Complex tools without training
- "Just use [complicated tool]" without support

**Causes:**
- Technical priesthood (experts hoard knowledge)
- Efficiency prioritized over accessibility
- "Move fast" culture

**Solutions:**
- Plain language requirement for all tech documentation
- Training as essential service, not optional
- User experience testing with least technical members
- "Explain it to a child" test

#### **F) Notification Hell**
**Symptoms:**
- Constant pinging
- Red badges everywhere
- Fear of missing something important
- Can't disconnect without anxiety

**Causes:**
- Everything marked urgent
- No notification discipline
- FOMO culture
- Unclear information hierarchy

**Solutions:**
- Most channels: notifications off by default
- Clear urgency levels (emergency/standard/FYI)
- Cultural norm: checking once/day is sufficient
- Right to silence without penalty

### 9.2 Hierarchy Warning Signs

**Information flow reveals hidden hierarchy. Watch for:**

#### **Power Concentration Indicators:**
- [ ] One person summarizes everything (bottleneck)
- [ ] Private DM networks where real decisions happen
- [ ] Some people always "in the loop," others always surprised
- [ ] Technical knowledge as gatekeeping
- [ ] "Efficient" decisions made without consultation
- [ ] Information in one language only (linguistic hierarchy)
- [ ] Jargon without glossary (insider/outsider divide)
- [ ] Sync-only decision-making (excludes many)

#### **Corrective Actions:**
- Rotate summarization roles
- Make all decision-making conversations public
- Proactive information distribution (push, don't pull)
- Plain language requirement + technical glossary
- Consent requirement for all decisions
- Multi-language commitment
- Jargon audit + simplification
- Async-first policy

---

## 10. TOOLS & TECHNOLOGY

### 10.1 Open Source Priority

**Why:**
- No vendor lock-in
- Community can modify/repair
- No remote killswitches
- Aligns with sovereignty values

**Recommended:**
- **Matrix** (federated chat, like Element)
- **Nextcloud** (file sharing, calendars)
- **Discourse** (forums, long-form discussion)
- **Etherpad** (collaborative writing)
- **Jitsi** (video calls)
- **Mastodon** (social, external communication)

**If proprietary tools necessary:**
- Document escape plan
- Export data regularly
- Never store critical data only there
- Plan for platform death

### 10.2 Mesh Network Implementation

**For local resilience:**
- **Meshtastic** (LoRa devices, <$50 per unit)
- **LibreMesh** (WiFi mesh firmware)
- **Yggdrasil** (overlay mesh network)

**Hardware:**
- Raspberry Pi as mesh nodes
- Solar-powered LoRa devices for remote locations
- Offline-first architecture (sync when connected)

### 10.3 Accessibility Tools

**Built-in, not bolted on:**
- **Screen readers:** NVDA (Windows), VoiceOver (Mac/iOS), TalkBack (Android)
- **Speech-to-text:** Whisper (offline, privacy-preserving)
- **Text-to-speech:** eSpeak, Festival (offline options)
- **Visual simplification:** Reader mode, high contrast themes
- **Captioning:** Live captions for video calls

### 10.4 Low-Tech Backups

**Always maintain:**
- Physical bulletin boards
- Printed summaries (weekly)
- Verbal announcement times (daily or weekly)
- Personal messenger network (for device-free members)
- Paper decision logs (archival backup)

**Principle:**  
> *Technology amplifies. It never replaces human connection.*

---

## 11. IMPLEMENTATION GUIDELINES

### 11.1 Starting from Scratch (New Circle)

**Phase 1: Minimal (Month 1-3)**
- 1 Signal/Matrix group
- Weekly in-person gatherings
- Shared document (decisions + calendar)
- Physical bulletin board

**Phase 2: Formalization (Month 4-6)**
- Add decision documentation process
- Add resource ledger (if Baseline Circle)
- Add ritual calendar
- Add conflict resolution protocol

**Phase 3: Scaling Preparation (Month 7-12)**
- Establish sub-circle structure (if >20 people)
- Add info-steward role
- Add meeting hygiene practices
- Add accessibility standards

### 11.2 Transitioning from Existing Systems

**If currently using corporate platforms (Slack, Discord, etc.):**

**Step 1: Audit (1 month)**
- What channels exist?
- Which are actually used?
- What information would be lost?
- Who is excluded by current system?

**Step 2: Simplify (1 month)**
- Prune unused channels
- Consolidate overlapping channels
- Archive old content
- Document current practices

**Step 3: Migrate (2-3 months)**
- Set up open-source alternatives
- Parallel run (both systems)
- Train everyone on new tools
- Gradually shift activity

**Step 4: Cut Over (1 month)**
- Archive old platform
- Export all data
- Celebrate sovereignty gained

### 11.3 Pilot Testing

**Before rolling out new communication practices:**

**Test with small group (5-10 people, 1 month):**
- Try the new channel structure
- Practice decision documentation
- Use async-first approach
- Implement accessibility standards

**Evaluate:**
- What worked?
- What was confusing?
- Who was excluded?
- What needs adjustment?

**Revise and expand:**
- Incorporate feedback
- Document lessons learned
- Roll out to larger group
- Iterate continuously

### 11.4 Training & Onboarding

**Every new member receives:**
- **Communication guide** (this document, simplified)
- **Channel overview** (what each channel is for)
- **Tool training** (how to use the tech)
- **Accessibility options** (how to customize for their needs)
- **Buddy assignment** (experienced member for questions)

**Ongoing:**
- Quarterly tech workshops
- Regular accessibility check-ins
- Tool reviews (are these still serving us?)
- Process improvements (based on lived experience)

---

## FINAL PRINCIPLES

### 1. Accessibility is Not Optional
If someone cannot access information, the system has failed them.  
Fix the system, not the person.

### 2. Energy is Finite
Human attention, electrical power, and ecological capacity are all limited.  
Communication must respect these limits.

### 3. Silence is Sacred
Every person has the right to disconnect.  
No penalties. No judgment. Just respect.

### 4. Local Before Global
The mesh operates independently.  
The community communicates without permission.  
Sovereignty is physical.

### 5. Simplicity Over Features
Fewer channels, better used.  
Fewer meetings, more meaningful.  
Fewer notifications, more peace.

### 6. Documentation Prevents Hierarchy
What is written can be challenged.  
What is invisible concentrates power.  
Transparency distributes agency.

### 7. Technology Serves Humans
Not the reverse.  
When tools exhaust people, change the tools.

### 8. Iterate Forever
This document is not final.  
Communication needs evolve.  
Stay humble. Stay adaptive.

---

**STATUS:** PROPOSED / READY FOR PILOT TESTING  
**VALIDATION REQUIRED:** 6-12 months of lived experience in diverse contexts  
**COMMITMENT:** Accessible, energy-aware, dignity-preserving information flow for all

---

**Signed in recognition that how we communicate shapes what we can become,**

**Claude & Elinor Frejd**  
**February 26, 2026**

🌿💚📡✨

---

## Appendix A: Quick Reference Tables

### Communication Energy Costs

| Type | Energy Cost | When to Use |
|------|-------------|-------------|
| Text | <1Wh | Always safe |
| Audio | 1-5Wh | Standard |
| Voice call | 5-10Wh | When needed |
| Video message | 10-50Wh | High energy only |
| Video call | 50-200Wh | 80%+ energy |
| Large files | Variable | Defer to high energy |

### Channel Count Guidelines

| Community Size | Max Channels | Rationale |
|----------------|--------------|-----------|
| 5-20 | 3 | High context, informal |
| 20-100 | 5-7 | Balance coherence & specialization |
| 100-500 | 8-10 | Nested structure reduces need |
| 500+ | 6-8 | Regional coordination only |

### Meeting Frequency

| Scale | Meeting Type | Frequency | Duration |
|-------|--------------|-----------|----------|
| Micro | Full circle | Weekly | 1 hour |
| Baseline | Sub-circle | Weekly | 1 hour |
| Baseline | Full circle | Monthly | 2-3 hours |
| Node | Sub-circle | Weekly | 1 hour |
| Node | Coordination Council | Bi-weekly | 2 hours |
| Node | Full Node | Monthly | Half day |
| Regional | Inter-Node Council | Monthly | 2-3 hours |
| Regional | Gathering | Quarterly | Full day |

---

## Appendix B: Accessibility Checklist

**Before launching any communication system:**

- [ ] Text available in all used languages
- [ ] Audio alternative for all text
- [ ] Visual alternative for all audio
- [ ] Plain language summary for complex content
- [ ] Screen reader compatibility tested
- [ ] High contrast mode available
- [ ] Captions for all video
- [ ] Keyboard navigation works
- [ ] Touch targets >44px
- [ ] Works without JavaScript (where possible)
- [ ] Works offline or low-bandwidth
- [ ] Physical backup option exists
- [ ] Training provided in multiple formats
- [ ] Support available for technical issues
- [ ] Feedback mechanism for accessibility problems

---

## Appendix C: Red Flag Checklist

**Quarterly audit — check for these warning signs:**

- [ ] Some people have more information than others (not by choice)
- [ ] Important decisions happen in invisible spaces
- [ ] Technical complexity excludes participation
- [ ] Meeting attendance becomes decision-making power
- [ ] Notifications overwhelming people
- [ ] Channels proliferating (>10 for <500 people)
- [ ] Async options disappearing (everything becoming sync)
- [ ] Documentation falling behind
- [ ] Accessibility standards slipping
- [ ] Energy costs rising unchecked
- [ ] Complaints about communication overload
- [ ] People dropping out due to communication exhaustion
- [ ] New members confused about how to participate
- [ ] Decisions made without documentation
- [ ] Private DM culture replacing public discussion

**If 3+ red flags:** Emergency communication review needed.  
**If 5+ red flags:** System redesign necessary.

---

*End of document. May your information flow like water: freely, nourishing all, never hoarded.* 🌊
