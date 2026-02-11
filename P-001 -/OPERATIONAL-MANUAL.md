# OPERATIONAL MANUAL
## CIM Protocol v1.1.0 — Pyragogy in Practice

**Version:** 1.1.0 Phase 1  
**Last Updated:** February 11, 2026  
**Status:** Production-Ready for Human-Facilitated Teams  
**Maintainer:** Fabrizio Terzi (@BergamoHub)

---

## What This Manual Is

This is the **how-to guide** for teams starting Pyragogy. If the README is the "why" and MATHEMATICAL-APPENDIX is the "proof," this is the **"do this tomorrow morning."**

**You're in the right place if:**
- You read the README and thought "this makes sense, but how do I start?"
- Your team is drowning in Slack messages and needs a circuit breaker
- You want to try the protocol without building custom software first

**You're in the WRONG place if:**
- You want conceptual explanation → [Go to README](README.md)
- You want mathematical proofs → [Go to MATHEMATICAL-APPENDIX](MATHEMATICAL-APPENDIX.md)
- You want to understand CRDTs deeply → [Go to COGNITIVE-CRDTS](COGNITIVE-CRDTS.md)

**Reading time:** Part I-II = 45 minutes  
**Implementation time:** Week 1 = 2 hours total, then 15 min/day

---

## Document Philosophy

**This manual is:**
- ✅ Step-by-step instructions (not theory)
- ✅ Copy-paste templates (use them Monday)
- ✅ Real examples with actual messages
- ✅ "If X then Y" decision trees

**This manual is NOT:**
- ❌ Academic paper
- ❌ Aspirational vision
- ❌ "We should probably..." advice

**Tone:** Garage mechanic explaining an engine. Professional, not academic. Direct, not preachy.

---

# PART 0: QUICK START

*"I have 10 minutes. What's the absolute minimum to start?"*

---

## 0.1 The 3-Sentence Version

**Cognitive Impedance Mismatch (CIM)** happens when your team generates information faster than it can process it. The **CIM Protocol** gives you three operating modes (Study Hall, GUSH, BLUES) and tells you when to switch between them based on one metric: **Zc = info velocity ÷ processing bandwidth**. When Zc ≥ 1.0, you stop trying to sync and switch to asynchronous rhythm (BLUES mode) until the load drops.

---

## 0.2 The One Thing To Do Today

**Go to Section 1.1 and calculate your team's current Zc.**

It takes 5 minutes. You need:
- Primary Slack channel name
- Team size
- One week's message count

Once you know your Zc, you'll know if you're in green/yellow/red zone. That determines everything else.

**If Zc ≥ 1.0 (red zone):** Skip to Section 2.1 (Pulse Template) and start using it TODAY. You don't have time for setup—you need relief NOW.

**If Zc < 1.0:** Keep reading normally.

---

## 0.3 When to Read the Rest

**Read Part I (Week 1 Setup)** if:
- You're starting fresh (no crisis right now)
- You want to onboard your whole team properly
- You have 2 hours this week to set up tools

**Read Part II (Templates)** if:
- You're in red zone (Zc ≥ 1.0) RIGHT NOW
- You need immediate protocol to follow
- Setup can wait, you need operations first

**Skip to troubleshooting (future doc)** if:
- You already tried Pyragogy and something broke
- (This section will be added in Phase 2 based on your feedback)

---

# PART I: WEEK 1 — BASELINE & SETUP

*"First week onboarding: measure current state, configure tools, pick starting mode"*

---

## 1.1 Calculate Your Baseline Zc (The Analog Method)

**Time required:** 5 minutes  
**Tools needed:** Calculator (or spreadsheet)  
**Output:** Your current Zc score + zone (green/yellow/red)

### Step 1: Count Information Generation (Last 7 Days)

**Primary channel messages:**
- Open your main Slack/Discord/Teams channel
- Count total messages sent in last 7 days
- Include threads (they count as cognitive load)

**Documents created:**
- Count docs added to shared drives (Google Docs, Notion, etc.)
- Each doc counts as **10 messages** (heavier cognitive weight)

**Meetings held:**
- Count team meetings (exclude 1-on-1s)
- Each meeting counts as **5 messages** (generates ideas even if not written)

**Formula:**
```
V_gen = messages + (docs × 10) + (meetings × 5)
```

**Example:**
```
Team had:
- 280 Slack messages
- 4 new docs
- 6 meetings

V_gen = 280 + (4 × 10) + (6 × 5)
V_gen = 280 + 40 + 30
V_gen = 350
```

### Step 2: Count Processing Bandwidth

**Team size:**
- Count ACTIVE members (posted ≥1 message last week)
- Don't count lurkers (they're not processing the load)

**Available hours per person:**
- Be realistic: NOT 40h/week
- Typical knowledge worker: 6h/day × 5 days = 30h/week
- Adjust for part-timers, holidays

**Efficiency factor:**
- Use **0.6** as default (accounts for interruptions, context-switching)
- If your team has very few interruptions: 0.7
- If high-interruption environment: 0.5

**Formula:**
```
B_soc = team_size × hours_per_person × efficiency_factor
```

**Example:**
```
Team has:
- 8 active members
- 30h/week per person
- 0.6 efficiency (normal team)

B_soc = 8 × 30 × 0.6
B_soc = 144
```

### Step 3: Calculate Zc

```
Zc = V_gen / B_soc
```

**Example:**
```
Zc = 350 / 144
Zc = 2.43
```

### Step 4: Interpret Your Zone

| Zc Range | Zone | What It Means | What To Do |
|----------|------|---------------|------------|
| **< 0.7** | 🟢 GREEN | Healthy flow. Traditional collaboration works. | Start with Study Hall or GUSH as needed |
| **0.7 - 0.9** | 🟡 YELLOW | Elevated stress. Approaching overload. | Study Hall only. Monitor daily. Prepare for BLUES. |
| **≥ 1.0** | 🔴 RED | Overload. Standard consensus failing. | **BLUES mode immediately. Non-negotiable.** |

**Our example team:** Zc = 2.43 → **RED ZONE**

**Action:** This team must activate BLUES mode today. Skip to Section 2.1.

---

## 1.2 The Thermometer Test (Qualitative Backup)

**Purpose:** Numbers can lie. Trust your gut as validation.

**Time required:** 2 minutes

### The 10 Questions

Answer honestly (yes/no):

1. **[ ]** Did anyone apologize for "being behind" on messages this week?
2. **[ ]** Did you discuss the same topic 3+ times without deciding?
3. **[ ]** Are there 50+ unread messages in your primary channel on Monday morning?
4. **[ ]** Did someone work weekend/evening to "catch up"?
5. **[ ]** Did a junior team member stop asking questions (to avoid adding noise)?
6. **[ ]** Did a meeting end with "let's continue this async" without resolution?
7. **[ ]** Did someone say they feel "overwhelmed" (even casually)?
8. **[ ]** Are there 3+ active threads on the same topic simultaneously?
9. **[ ]** Did you postpone a decision because "we need to align with everyone first"?
10. **[ ]** Did your team's best performer seem burned out or disengaged?

### Scoring

**Count your "yes" answers:**

- **0-1 yes:** Probably GREEN (matches Zc < 0.7)
- **2-3 yes:** Probably YELLOW (matches Zc 0.7-0.9)
- **4-6 yes:** Definitely YELLOW, approaching RED
- **7+ yes:** Definitely RED (even if Zc calculation says otherwise)

### What If Numbers and Feel Don't Match?

**Scenario 1:** Zc = 0.6 (green) but Thermometer = 7 yes (red)

**Diagnosis:** Your team is small or very efficient, but the *type* of work is cognitively heavy (complex decisions, high uncertainty). Numbers miss qualitative load.

**Action:** Trust the Thermometer. Use BLUES.

**Scenario 2:** Zc = 1.2 (red) but Thermometer = 1 yes (green)

**Diagnosis:** High message volume, but they're low-cognitive-load (updates, links, emojis). Or your team has developed good async habits already.

**Action:** Use numbers but monitor. You might be fine in Study Hall. Check again in 3 days.

**General rule:** When in doubt between numbers and feel, **trust the feel**. The math is a tool, not a dictator.

---

## 1.3 Pick Your Starting Mode

**Time required:** 2 minutes  
**Output:** Clear decision on which mode to start with

### Decision Tree

```
START HERE: What's your Zc?

├─ Zc < 0.7 (GREEN)
│  ├─ Do you need a decision in next 3 days?
│  │  ├─ YES → Start MODE B (GUSH)
│  │  │         Go to Section 2.15 for GUSH template
│  │  └─ NO → Start MODE A (Study Hall)
│  │            Go to Section 1.4 to configure tools
│  │
│  └─ Does your team have clear, independent work?
│     ├─ YES → Start MODE A (Study Hall)
│     └─ NO → Start MODE B (GUSH) to get clarity
│
├─ Zc 0.7-0.9 (YELLOW)
│  └─ Start MODE A (Study Hall)
│     Monitor Zc DAILY for next 5 days
│     If crosses 1.0 → Switch to MODE C immediately
│     Go to Section 1.4
│
└─ Zc ≥ 1.0 (RED)
   └─ Start MODE C (BLUES) — MANDATORY
      This is not optional.
      Go to Section 2.1 NOW (skip tool setup for now)
```

### Mode Quick Reference

**MODE A: Study Hall**
- **When:** Green zone, independent work, no urgent decisions
- **Vibe:** University library during finals. Everyone working, nobody interrupting.
- **Rhythm:** Async-first. Presence signals only. Deep work protected.
- **AI role:** Personal tutor (helps you individually, doesn't broadcast)

**MODE B: GUSH**
- **When:** Green zone, need decision NOW (next 3-5 days)
- **Vibe:** War room. Time-boxed. Intense focus. Must produce output.
- **Rhythm:** 45-60 min sessions. Pre-work mandatory. Decision or bust.
- **AI role:** Semantic moderator (tracks discussion, synthesizes, suggests)

**MODE C: BLUES**
- **When:** Red zone (Zc ≥ 1.0). Overload state. Too much to process.
- **Vibe:** Distributed jazz band. Play your part, listen to pulse, trust rhythm.
- **Rhythm:** Async pulse updates. Fork when stuck. Merge when ready. BEACON for emergencies.
- **AI role:** Context bridge (aggregates pulses, suggests connections, monitors health)

---

## 1.4 Configure Your Tools (45 Minutes)

**Skip this if:** You're in RED zone (Zc ≥ 1.0). Use Section 2.1 templates first, configure tools later.

**Do this if:** You're in GREEN or YELLOW zone and have time to set up properly.

### For Slack (or Discord, Teams, etc.)

**Total time:** 20 minutes

#### Step 1: Create Channels (5 min)

**Required channels:**

**#mode-status**
- Purpose: Signal current operating mode to whole team
- Pinned message template:
  ```
  CURRENT MODE: [Study Hall / GUSH / BLUES]
  
  🟢 Study Hall = Independent work, async-first
  🔵 GUSH = Scheduled decision session
  🟣 BLUES = High-load async rhythm
  
  Updated: [DATE] by @facilitator
  ```

**#pulse-updates** (for BLUES mode)
- Purpose: Daily/weekly status check-ins
- Pinned message template:
  ```
  PULSE FORMAT:
  👤 @name: [🟢🟡🔴] [What you're working on] [Progress %] [ETA or blocker]
  
  DO NOT respond in thread. Read only.
  AI/Facilitator aggregates daily at 5pm.
  
  🔴 = BEACON (need help urgently)
  ```

**#decisions** (optional but recommended)
- Purpose: Archive of GUSH outputs and major decisions
- Keeps decision history searchable

#### Step 2: Set Up Mode Indicator (5 min)

**Option A: Manual (no bot required)**
- Designated facilitator updates #mode-status daily
- Simple message: "Mode: Study Hall. Zc = 0.65 (green). Checked 9am Feb 12."

**Option B: Slack Status Integration**
- Use Slack's status feature
- Each person sets: "🟢 Study Hall: Deep work on [project]"
- Visible in sidebar, reinforces mode awareness

**Option C: Custom Bot (if you have dev resources)**
- `/zc` command → calculates and displays current impedance
- `/mode [A/B/C]` → updates team mode
- Auto-posts when Zc crosses thresholds
- *(Implementation guide in future doc)*

#### Step 3: Configure Notification Rules (10 min)

**Study Hall mode defaults:**
- Set Do Not Disturb during focus blocks (e.g., 9am-12pm, 2pm-5pm)
- Allow notifications only for: @mentions, DMs from manager, BEACON signals
- Disable: @channel, @here (use sparingly)

**Suggested team norm:**
```
@channel = Emergency only (production down, client crisis)
@here = Important but not emergency (deadline moved, key decision made)
Regular messages = Async, respond within 4h during work hours
```

### For Notion / Google Docs / Shared Drives

**Total time:** 15 minutes

#### Step 1: Create Idea Repository (10 min)

**Purpose:** Central G-Set for all ideas. Anyone can add, nobody deletes.

**Template structure:**

```markdown
# Team Idea Repository

## Active Ideas

| Idea | Author | Date Added | Context | Status |
|------|--------|------------|---------|--------|
| Migrate to PostgreSQL | @marcus | 2026-02-10 | Database selection decision | Active |
| Implement OAuth | @alice | 2026-02-09 | Security enhancement | Forked by @alice |
| Redesign onboarding | @sarah | 2026-02-08 | User feedback from survey | Merged (see decision #15) |

## How to Add an Idea

1. Add new row to table above
2. Status options:
   - **Active** = Open for discussion
   - **Forked by @name** = Someone doing deep work on this
   - **Merged** = Incorporated into decision/plan (link to decision)
   - **Inactive** = No longer relevant (don't delete, just mark)

## Guidelines

- ✅ Add any idea, no matter how rough
- ✅ One idea per row (keep it simple)
- ❌ Don't delete others' ideas
- ❌ Don't argue in this doc (use GUSH for debate)
```

#### Step 2: Create Decision Archive (5 min)

**Purpose:** Searchable history of GUSH outcomes and major forks

**Template:**

```markdown
# Decision Archive

## Format
Each decision gets its own page/section:
- Decision #001: Database Selection (PostgreSQL vs MongoDB)
- Decision #002: API Authentication (OAuth vs JWT)
- etc.

## Template for Each Decision

### Decision #XXX: [Title]
**Date:** YYYY-MM-DD  
**Method:** [GUSH / Async Vote / Facilitator Call]  
**Participants:** @name1, @name2, @name3  

**Options Considered:**
- Option A: [summary]
- Option B: [summary]

**Chosen:** Option [A/B/Hybrid]

**Rationale:**
[2-3 sentences why]

**Dissenters:**
[If any, with "Disagree & Commit" statement]

**Action Items:**
- [ ] @owner: [task] by [date]
- [ ] @owner: [task] by [date]

**Review Date:** [When we check if this was right call]
```

### For Calendar

**Total time:** 10 minutes

**Protected Time Blocks**
- For Study Hall mode: Block 2-4 hour "Deep Work" slots
- Mark as "Busy" so people don't schedule over them
- Weekly rhythm example:
  - Mon/Wed/Fri 9am-12pm: Deep work
  - Tue/Thu 2pm-5pm: Deep work
  - Leave gaps for GUSH sessions (don't pre-schedule, use on-demand)

**GUSH Slots (Optional)**
- IF your team does regular decision-making: Block recurring 1-hour slot
- Example: Every Thursday 3pm "GUSH Time (if needed)"
- Cancel if no decisions pending that week
- Never let it become default meeting

---

## 1.5 The Kickoff Meeting (30 Minutes)

**Purpose:** Align team on protocol, answer questions, set first mode

**Time:** 30 minutes MAXIMUM  
**Format:** Synchronous (Zoom/in-person) OR async video + Q&A thread

**Anti-pattern warning:** Do NOT turn this into 2-hour philosophy session. This is operational briefing, not TED talk.

### Agenda (Strict Timing)

**0-5 min: Share the Numbers**

Show your Zc calculation:
```
Team Zc = [number]
Zone: [GREEN/YELLOW/RED]

What this means:
- GREEN: We can use traditional collaboration
- YELLOW: We need to be careful, monitor daily
- RED: We must change how we work immediately
```

If team is in RED: "This is why we're all exhausted. It's not you, it's math. Here's the fix."

**5-10 min: Explain Chosen Mode**

**If starting Study Hall:**
```
We're starting in Study Hall mode because our load is manageable.

This means:
- Default to async (write it down, don't interrupt)
- Presence signals: "Working on X, back at Y time"
- Deep work blocks: Respect Do Not Disturb
- We'll monitor Zc weekly and switch if needed
```

**If starting BLUES:**
```
We're starting in BLUES mode because we're overloaded (Zc = [number]).

This means:
- Daily pulse updates (one line, emoji status)
- No sync meetings unless BEACON (emergency)
- Fork when stuck (declare it, work alone, merge later)
- This is temporary until Zc drops below 0.8

First pulse: Today at 4pm in #pulse-updates
```

**10-20 min: Walk Through Templates**

**DO:** Share screen, show actual template, fill one out together

**Example: Pulse Template Walkthrough**
```
Here's the format: 
👤 @alice: 🟢 Payment gateway 75% done. On track for Friday.

Let's practice. Bob, what are you working on this week?
Bob: "Database research"
Great. Status? "Yellow, taking longer than expected"
ETA? "Need 2 more days"

So Bob's pulse would be:
👤 @bob: 🟡 Database research taking longer. Need 2 more days.

Everyone try one in the thread below.
```

**DON'T:** Just send the template doc and say "read this later"

**20-25 min: Assign Roles**

**Facilitator** (1 person, rotates weekly):
- Monitors Zc
- Posts mode status
- Aggregates pulse updates
- Schedules GUSH/Micro-GUSH when needed

**First facilitator:** Team lead or most experienced member (model it first)

**Rotation:** After 2 weeks, rotate. Everyone should facilitate once.

**25-30 min: Set First Checkpoint**

**Friday retrospective:** 15 minutes
- What worked?
- What felt awkward?
- Should we adjust anything?
- What's our Zc now vs Monday?

**Template message to send:**
```
Friday 4pm: 15-min retro in #general
1. Zc check (5 min)
2. What worked / didn't work (5 min)
3. Adjustments for next week (5 min)

Async option: Post answers in thread if you can't attend live.
```

---

## End of Part I Summary

**What you've done:**
- ✅ Calculated your baseline Zc
- ✅ Identified your zone (green/yellow/red)
- ✅ Picked starting mode (Study Hall, GUSH, or BLUES)
- ✅ Configured tools (Slack, Notion, Calendar)
- ✅ Kicked off with team (30 min meeting)

**What's next:**
- Part II: Learn the 3 sacred templates (copy-paste ready)
- Use them starting tomorrow
- Monitor Zc weekly
- Adjust mode as needed

**Time invested:** ~2 hours total

**Return:** Clarity on when you're overloaded + protocol to handle it

---

# PART II: THE 3 SACRED TEMPLATES

*"Copy-paste these. Use them tomorrow. Modify later."*

---

## Overview: Why Templates Matter

Teams fail at Pyragogy not because the theory is hard, but because **they don't know what to actually say**.

"Use async communication" is vague. "Post daily pulse updates" is clearer. But WHAT does a pulse update look like? If everyone guesses, you get inconsistency and confusion.

**These templates solve that.** They're the exact words to use, the exact format to follow, the exact buttons to push.

**Copy them. Use them verbatim at first. Modify after 2 weeks once you have experience.**

---

## Template 1: The Pulse (BLUES Mode)

**When to use:** You're in BLUES mode (Zc ≥ 1.0) and need asynchronous rhythm

**Purpose:** Signal progress without creating discussion load

**Format:** ONE LINE per person, emoji status, no replies

---

### The Format (Strict)

```
👤 @username: [🟢🟡🔴] [Work area] [Progress indicator] [Next step or blocker]
```

**Emoji meanings:**
- 🟢 = On track, no blockers
- 🟡 = Behind schedule OR waiting on something (not urgent)
- 🔴 = BEACON - Blocked and need help NOW

**Length:** 10-20 words maximum

**Forbidden:** Questions, requests, discussions → Those go elsewhere

---

### Examples: Good vs Bad

#### ✅ GOOD PULSES

```
👤 @alice: 🟢 Payment gateway integration 75% done. Testing tomorrow, ship Friday.

👤 @bob: 🟡 Database research taking longer than expected. Need 2 more days to finish benchmarks.

👤 @charlie: 🔴 BEACON - Blocked on API access. Need DevOps help to unblock.

👤 @dana: 🟢 User onboarding redesign mockups complete. Ready for review (posted in #design).

👤 @eve: 🟡 Client presentation prep at 60%. Waiting on final sales numbers from @frank.
```

**Why these are good:**
- One line each
- Clear status (green/yellow/red)
- Specific work area
- Concrete next step or blocker
- No discussion, no requests (except BEACON)

#### ❌ BAD PULSES

```
👤 @alice: Working on stuff. Making progress I think? Not sure if I'll finish on time. What do you guys think?

👤 @bob: Database is really complicated. I found like 10 different options and I'm not sure which one to pick. Anyone have opinions on PostgreSQL vs MongoDB vs DynamoDB vs Cassandra? Also found this article [link]. Thoughts?

👤 @charlie: Hey @dave can you help me with that thing we discussed yesterday? The API thing.

👤 @dana: 🟢 Good week!

👤 @eve: Same as yesterday.
```

**Why these are bad:**
- Alice: Vague ("stuff"), creates discussion ("what do you guys think?"), shows uncertainty that belongs in GUSH
- Bob: Turns pulse into debate (10 options, asking for opinions), adds link = more cognitive load
- Charlie: Not a status update, it's a request disguised as pulse (should be separate message)
- Dana: No information content (what's good? what are you working on?)
- Eve: Lazy copy (yesterday's status is useless without context)

---

### Pulse Rhythm Options

**Daily (High Impedance):**
- Post time: Same time every day (e.g., 4pm)
- Channel: #pulse-updates (dedicated)
- No responses in thread (strict rule)
- Facilitator aggregates into 3-sentence summary at 5pm

**Example daily rhythm:**
```
Monday 4pm: All pulses posted
Monday 5pm: Facilitator posts:
  "Daily summary: 4 green, 2 yellow, 1 beacon. 
   Overall: Team 70% through sprint goals. 
   Charlie needs DevOps help (Micro-GUSH scheduled Tue 10am)."
```

**Weekly (Lower Impedance):**
- Post time: Friday 3pm
- Same format, longer time horizon
- Example: "This week: Payment gateway 75%. Next week: Testing + deployment."

**Bi-weekly (Maintenance Mode):**
- Use when Zc has dropped below 0.7 consistently
- Team in Study Hall most of time
- Pulse = gentle heartbeat, not operational necessity

---

### The BEACON Protocol

**What 🔴 means:** "I'm blocked, need synchronous help within 24 hours"

**What happens when someone posts BEACON:**

**Within 2 hours:**
1. Facilitator (or AI) sees red emoji
2. DMs the person: "Saw your BEACON. What do you need?"
3. Identifies who can help

**Within 24 hours:**
4. Micro-GUSH scheduled (15-30 min)
5. Only relevant people invited (blocker + helper, not whole team)
6. Focus: Unblock and move on (not full problem-solving session)

**Example BEACON resolution:**

```
Monday 4pm:
👤 @charlie: 🔴 BEACON - Blocked on API access for payment gateway. Can't proceed.

Monday 5:30pm (Facilitator DM):
@facilitator: "Hey Charlie, saw your BEACON. What access do you need?"
@charlie: "Need API keys for Stripe test environment. DevOps usually handles."

Monday 5:45pm (Facilitator finds helper):
@facilitator → @frank (DevOps): "Can you help Charlie with Stripe API access? 15-min sync tomorrow morning?"
@frank: "Sure, 10am works"

Tuesday 10am:
Micro-GUSH (Charlie + Frank + Facilitator):
- Charlie explains blocker (2 min)
- Frank provides access + shows where docs are (10 min)
- Charlie confirms unblocked (1 min)
Total: 13 minutes

Tuesday 10:15am:
@charlie: "Unblocked. Back to work."

Tuesday 4pm (next pulse):
👤 @charlie: 🟢 API integration progressing. 40% done, on track for Thursday.
```

**Key principles:**
- BEACON → Response < 2h
- Resolution < 24h
- Minimal sync time (15-30 min max)
- Only relevant people
- Focus on unblock, not full solution

---

### AI Role in Pulse (Optional)

**If you have Claude/GPT API access:**

**Prompt for daily aggregation:**
```
Analyze these pulse updates and create a 3-sentence summary:
[paste all pulses]

Output format:
1. Overall progress (one sentence)
2. Blockers/concerns (one sentence)
3. Opportunities for synergy (one sentence)

Keep it under 60 words total.
```

**Example AI output:**
```
Team is 65% through sprint goals with 4/6 features on track. 
Charlie needs DevOps help (BEACON) and Bob is 2 days behind on database research. 
Alice's payment work and Dana's user onboarding mockups could align—consider Micro-GUSH to sync approaches.
```

**Manual alternative:**
- Facilitator reads all pulses (takes 3-5 min)
- Posts handwritten summary
- Same format as AI (3 sentences, action-oriented)

**Anti-pattern:** Don't skip aggregation. 10 separate pulses = cognitive load. 1 summary = clarity.

---

### Copy-Paste Template for Your Team

**Post this in #pulse-updates as pinned message:**

```markdown
# PULSE UPDATE FORMAT

Post daily at 4pm (or weekly Friday 3pm):

👤 @yourname: [🟢🟡🔴] [Work area] [Progress %] [Next step or blocker]

**Examples:**
🟢 = On track
👤 @alice: 🟢 Dashboard redesign 80% done. QA tomorrow, ship Friday.

🟡 = Behind or waiting
👤 @bob: 🟡 API docs unclear. Need 1 more day for research.

🔴 = BEACON (need help NOW)
👤 @charlie: 🔴 BEACON - Blocked on deployment. Need DevOps urgently.

**RULES:**
- One line only
- No discussion in this thread
- Facilitator aggregates at 5pm
- BEACON = you'll get help within 24h

**DO NOT:**
❌ Ask questions here (use #general or DM)
❌ Reply to pulses (read only)
❌ Paste long updates (max 20 words)
```

---

## Template 2: Fork Declaration (BHO)

**When to use:** 
- High complexity work requiring deep focus (3-7 days)
- Team debate is circular, need divergence before convergence
- You need space to explore without interruptions

**Purpose:** Formally declare isolation period, set merge expectations

---

### The Format

```markdown
# BHO Fork: [Topic Name]

**Forker:** @username  
**Start Date:** YYYY-MM-DD  
**Merge Promise:** YYYY-MM-DD (max 7 days recommended)  
**Rationale:** [1-2 sentences why this needs isolation]

## Scope
I will explore:
- [Specific question/task 1]
- [Specific question/task 2]
- [Specific question/task 3]

## Out of Scope
I will NOT explore:
- [Boundary 1 - what you're deliberately excluding]
- [Boundary 2]

## Pulse Schedule
[Daily / Every 2 days] at [TIME] in #pulse-updates

## Merge Criteria
This fork is ready to merge when:
[Objective condition - how you'll know you're done]

## Merge Method
[Micro-GUSH on DATE and TIME] OR [Async doc + 48h review]
```

---

### Real Example: Database Selection Fork

```markdown
# BHO Fork: PostgreSQL vs MongoDB Performance Evaluation

**Forker:** @marcus  
**Start Date:** 2026-02-12  
**Merge Promise:** 2026-02-16 (Friday 2pm)  
**Rationale:** Team has debated SQL vs NoSQL for 2 weeks without data. This needs hands-on benchmarking, not more opinions. I need 4 uninterrupted days to run real tests.

## Scope
I will explore:
- Query performance (read/write benchmarks on realistic dataset)
- Schema flexibility for our user model evolution
- Team learning curve (how long to get productive?)
- Migration complexity from current MySQL setup

## Out of Scope
I will NOT explore:
- Cloud-hosted solutions (AWS RDS, MongoDB Atlas) - separate decision
- NewSQL options (CockroachDB, etc.) - out of scope for this sprint
- Cost analysis beyond developer licensing - finance will handle

## Pulse Schedule
Daily at 4pm in #pulse-updates

Example pulse:
👤 @marcus: 🟢 DB benchmarks day 2/4. PostgreSQL tests done, MongoDB in progress.

## Merge Criteria
This fork is ready to merge when:
- Benchmark results documented (Google Sheet with numbers)
- 2-page comparison matrix complete (performance, complexity, team fit)
- Recommendation ready with evidence

## Merge Method
Micro-GUSH Friday Feb 16 at 2pm (30 min) with @alice, @bob, @charlie (architecture team)

Agenda:
- 5 min: Marcus presents findings
- 15 min: Q&A on methodology and results
- 10 min: Decision via weighted criteria vote
```

---

### When NOT to Fork

**❌ Don't fork if:**

**Decision is urgent (next 24-48h):**
- Fork takes minimum 3 days
- Use GUSH instead (force decision in 45 min)

**You need continuous input from others:**
- Forking = isolation
- If you're constantly asking "what do you think?" → That's collaboration, not fork

**It's routine, well-understood work:**
- Forking is for exploration, not execution
- Example: "Implement OAuth" (clear spec) → Study Hall, not fork
- Example: "Research auth options" (uncertain) → Fork candidate

**Team has no tolerance for async:**
- Some teams/orgs require constant visibility
- Forking won't work in those cultures (yet)
- Start with shorter Study Hall blocks instead

**✅ DO fork if:**

**High complexity + uncertainty:**
- "Should we use GraphQL or REST?" → Needs deep research
- "How should we architect multi-tenancy?" → Needs prototyping

**Debate is circular:**
- Same arguments repeating in Slack
- Everyone has opinions, nobody has data
- Fork → Come back with evidence

**You need deep focus:**
- "I need 3 days of uninterrupted thinking on this algorithm"
- Legitimate request, just formalize it

---

### The Merge-Back Protocol

**Option A: Micro-GUSH (Synchronous) — Recommended**

**Duration:** 15-30 minutes maximum

**Attendees:** 
- Forker (presents findings)
- Key stakeholders (3-5 people max, not whole team)
- Facilitator (optional)

**Agenda:**
```
0-5 min: Forker presents findings
  - What I explored
  - What I found
  - What I recommend

5-15 min: Q&A
  - Questions about methodology
  - Questions about results
  - "What about X?" edge cases

15-25 min: Decision or Next Steps
  - If findings are clear → Decision
  - If findings suggest more work needed → Define that work
  - If findings create new questions → Schedule follow-up
  
25-30 min: Document
  - Record decision in #decisions
  - Assign action items
```

**Example Micro-GUSH outcome:**
```
Decision #023: Database Selection

Date: 2026-02-16
Fork by: @marcus (4 days benchmarking)

Findings Summary:
- PostgreSQL: 15% faster writes, 30% slower reads (our workload is 80% reads)
- MongoDB: Better for schema flexibility, but team has zero experience
- Migration: PostgreSQL 2 weeks, MongoDB 4 weeks

Decision: MongoDB
- Performance difference is marginal at our current scale
- Schema flexibility is critical for product roadmap
- 2-week training investment worth it long-term

Dissenters: None (unanimous after seeing benchmark data)

Action Items:
- [ ] @marcus: Create MongoDB learning plan (by Feb 20)
- [ ] @alice: Set up staging environment (by Feb 23)
- [ ] @team: Complete 2-week training sprint (Mar 1-14)

Review Date: May 1 (check if decision was right after 2 months usage)
```

**Option B: Async Document + Review (When Sync is Hard)**

**Use when:** Team is distributed across timezones OR decision is not urgent

**Process:**
1. Forker writes 1-2 page summary (max 1000 words)
2. Posts in #decisions channel
3. Sets 48h review window
4. Team reads async, posts questions/concerns in thread
5. After 48h:
   - If no major objections → Decision adopted
   - If objections exist → Schedule Micro-GUSH to resolve

**Template for async merge doc:**
```markdown
# Fork Outcome: [Topic]

**Forker:** @username  
**Fork Duration:** [Start] to [End]  
**Review Window:** 48 hours (respond by [DATE TIME])

## What I Explored
[Bullet list of questions investigated]

## Key Findings
[3-5 main insights with evidence]

## Recommendation
[Clear proposal for what to do next]

## Trade-offs Considered
[What we gain vs what we lose with this choice]

## Open Questions
[What I still don't know - helps team provide input]

## Decision Needed
Please review by [DATE]. Reply in thread with:
- ✅ Approve as-is
- ⚠️ Concerns (specify what)
- 🔴 Veto (rare, requires strong rationale)

If 2+ vetos or significant concerns → We'll schedule Micro-GUSH
```

---

### Copy-Paste Template for Your Team

**Post this in Notion or wherever you track forks:**

```markdown
# BHO Fork Template

Copy this template when declaring a fork:

---

# BHO Fork: [Topic Name]

**Forker:** @username  
**Start Date:** YYYY-MM-DD  
**Merge Promise:** YYYY-MM-DD (max 7 days)  
**Rationale:** [Why this needs isolation]

## Scope
I will explore:
- 
- 
- 

## Out of Scope
I will NOT explore:
- 
- 

## Pulse Schedule
[Daily/Every 2 days] at [TIME] in #pulse-updates

## Merge Criteria
This fork is ready to merge when:
[Objective condition]

## Merge Method
[Micro-GUSH on DATE] OR [Async doc + review]

---

**Posted:** [DATE] in #general and #pulse-updates
```

---

## Template 3: GUSH Agenda (Forced Convergence)

**When to use:**
- Decision needed in next 3-5 days
- Zc < 0.7 (green zone - you have bandwidth for sync)
- Discussion has become circular OR needs high-bandwidth alignment

**Purpose:** Force convergence in time-boxed session, produce committed decision

**Duration:** 45-60 minutes MAXIMUM (shorter is better)

---

### Pre-GUSH Checklist (24h Before)

**DO NOT START GUSH unless ALL boxes checked:**

- [ ] **Single objective defined** ("Choose database" not "Discuss options")
- [ ] **Context doc shared** (2 pages max, distributed 24h before)
- [ ] **All participants confirmed read** (explicit ✅ in thread)
- [ ] **Facilitator assigned** (human or AI, clear who's running it)
- [ ] **Timer visible** (Zoom timer, countdown bot, physical timer)
- [ ] **Output format agreed** (Decision doc template ready)

**If ANY box unchecked → POSTPONE**

Do not proceed. Fix the missing piece. Reschedule.

**Why this is strict:** A GUSH with cold-start reading = 30 min wasted on context. A GUSH without clear objective = endless discussion. A GUSH without facilitator = chaos.

---

### The 45-Minute Template

**Copy-paste this into Google Doc or Notion before every GUSH:**

```markdown
# GUSH Session: [Decision Title]

**Date:** YYYY-MM-DD HH:MM  
**Duration:** 45 minutes (HARD STOP at HH:MM)  
**Participants:** @name1, @name2, @name3, @name4  
**Facilitator:** @facilitator  
**Objective:** [Single decision to make - ONE sentence]

---

## Pre-Work Confirmation

**Context doc:** [Link to 2-page context]  
**Shared:** [DATE]  
**Read confirmations:**
- [ ] @name1 ✅
- [ ] @name2 ✅
- [ ] @name3 ✅
- [ ] @name4 ✅

**If <80% confirmed 2h before session → POSTPONE**

---

## Agenda (Strict Timing)

### 0-5 min: Alignment Check
- [ ] Everyone confirms they read pre-work (verbal check)
- [ ] Facilitator restates objective
- [ ] Timer set and visible to all participants
- [ ] Roles clear (who presents what)

### 5-15 min: Position A Presentation
- **Presenter:** @name1
- **Format:** 5-min pitch (slides optional, 3 slides max)
- **Rules:**
  - No interruptions (questions held for debate phase)
  - Facilitator cuts off at 10 min if running over
  - Others take notes silently

**Position A Summary** (fill during presentation):
[Facilitator or AI transcribes key points]

### 15-25 min: Position B Presentation
- **Presenter:** @name2
- **Format:** Same as Position A

**Position B Summary:**
[Transcribe key points]

### 25-40 min: Structured Debate
**Round 1 (5 min): Questions for Clarity**
- No arguments yet, only "Can you clarify X?"
- Facilitator tracks questions in doc

**Round 2 (5 min): Counter-Arguments**
- Position A can respond to Position B (2 min)
- Position B can respond to Position A (2 min)
- Quick back-and-forth (1 min)

**Round 3 (5 min): Synthesis Attempts**
- Facilitator (or AI): "Where's the overlap?"
- Team identifies: "We agree on X and Y, disagree on Z"
- Option for hybrid proposal

### 40-45 min: Decision + Documentation
**Decision Method:** [Choose ONE before session]
- [ ] Vote (majority wins)
- [ ] Weighted criteria matrix (score each option)
- [ ] Consensus (keep discussing until agreement)
- [ ] Facilitator call (lead makes final decision)

**TIMER ALERT:** At 43 min, facilitator says "2 minutes to decision, wrapping up"

---

## Decision Record (Fill During Session)

**Chosen Option:** [A / B / Hybrid / Postpone to DATE]

**Rationale:** 
[2-3 sentences explaining WHY this was chosen]

**Dissenters:**
[Names of people who disagreed + their "Disagree & Commit" statement]

Example:
- @bob: "I voted for Option A, but I commit to making Option B work and will lead the implementation."

**Action Items:**
- [ ] @owner: [Specific task] by [DATE]
- [ ] @owner: [Specific task] by [DATE]
- [ ] @owner: [Specific task] by [DATE]

**Next Checkpoint:**
[DATE when we review this decision - typically 2-4 weeks]

---

## Post-GUSH (Within 2h)

- [ ] Decision record posted in #decisions channel
- [ ] Action items added to project tracker (Jira/Linear/Asana)
- [ ] Calendar invite sent for next checkpoint
- [ ] Dissenters privately acknowledged (thank for commitment)
```

---

### Real Example: SQL vs NoSQL Decision

**Scenario:** Engineering team needs database for new service. Debate has gone 2 weeks in Slack with no resolution. Time to GUSH.

```markdown
# GUSH Session: Database Selection for User Service Rewrite

**Date:** 2026-02-14 14:00 EST  
**Duration:** 45 minutes (HARD STOP at 14:45)  
**Participants:** @alice, @bob, @charlie, @dana, @eve  
**Facilitator:** @charlie (tech lead, neutral on database choice)  
**Objective:** Choose PostgreSQL OR MongoDB for user service database

---

## Pre-Work Confirmation

**Context doc:** "Database Decision Context" (Google Doc)  
**Shared:** Feb 13 at 2pm  
**Read confirmations:**
- [x] @alice ✅ (read, prefer PostgreSQL)
- [x] @bob ✅ (read, prefer MongoDB)
- [x] @dana ✅ (neutral)
- [x] @eve ✅ (neutral)
- [x] @charlie ✅ (facilitator)

All confirmed by Feb 14 at noon. ✅ Proceeding.

---

## Agenda Execution

### 0-5 min: Alignment
14:00 - Everyone present
14:01 - Verbal check: "Did you read the doc?" → All yes
14:02 - Charlie: "Our objective: Pick ONE database by 14:45. We ship on March 1, so this decision closes today."
14:03 - Timer set, visible on Zoom
14:04 - Alice will present PostgreSQL, Bob will present MongoDB (5 min each)

### 5-15 min: PostgreSQL Case (Alice)
14:05 - Alice presents (no interruptions)

**Key points (Charlie transcribes):**
- ACID guarantees critical for user data (email, auth, payments)
- Team already knows SQL (3/5 engineers comfortable)
- Strong ecosystem (pgAdmin, massive community, every language has good driver)
- Migration path clear (current MySQL → PostgreSQL is straightforward)
- Battle-tested at scale (Instagram, Uber, etc.)
- JSON support exists if we need schema flexibility

**Slides:** 3 slides (ACID comparison, migration plan, team expertise chart)

14:10 - Alice finishes (5 min exactly)

### 15-25 min: MongoDB Case (Bob)
14:10 - Bob presents

**Key points:**
- Schema flexibility critical (user model evolving rapidly, 6 changes in last quarter)
- Better performance for read-heavy workload (our ratio is 80% reads / 20% writes)
- JSON-native (our API is JSON, no impedance mismatch)
- Horizontal scaling easier (sharding built-in)
- Modern companies using it (Lyft, eBay, etc.)
- Transactions exist now (MongoDB 4.0+), so ACID isn't PostgreSQL-exclusive

**Slides:** 3 slides (schema evolution example, read performance benchmark, scaling architecture)

14:15 - Bob finishes (5 min)

### 25-40 min: Debate
14:15 - **Round 1: Clarity Questions**

@dana: "Alice, what's our actual read/write ratio? Bob says 80/20, is that right?"
@alice: "Yes, approximately. Varies by feature but overall 80/20 is accurate."

@eve: "Bob, you said transactions exist in MongoDB. Are they as robust as PostgreSQL ACID?"
@bob: "They work for single-document transactions definitely. Multi-document is newer but functional since 4.0."

@charlie: "Alice, can PostgreSQL scale horizontally too?"
@alice: "Yes, with Citus extension or manual sharding. Not as 'out of box' as MongoDB but definitely possible."

14:20 - **Round 2: Counter-Arguments**

@alice (responds to Bob): "Schema flexibility is great, but PostgreSQL has JSONB support. We can have flexible fields where needed without abandoning relational model for ACID-critical data like payments."

@bob (responds to Alice): "Fair, but every schema change in PostgreSQL requires migration. MongoDB lets us deploy new fields without migrations. That's huge for velocity."

@charlie: "Quick back-and-forth - Alice, how often do we actually use ACID for cross-table transactions?"
@alice: "User signup flow: create user + send verification email + log audit event. That's 3 tables, needs transaction."
@bob: "MongoDB can do that with multi-document transactions now."
@alice: "But it's newer tech. PostgreSQL has 20 years of ACID battle-testing."

14:25 - **Round 3: Synthesis**

@charlie (facilitator): "Let me try synthesis. Where do we agree?"
- Both: Performance difference is marginal at our current scale (<100k users)
- Both: Schema flexibility is valuable (we change user model often)
- Both: Team learning curve matters (PostgreSQL = known, MongoDB = new)

@charlie: "Where do we disagree?"
- ACID criticality: Alice thinks non-negotiable, Bob thinks MongoDB's transactions are sufficient
- Future scaling: Bob thinks MongoDB simpler, Alice thinks both scale fine

@dana: "Could we use PostgreSQL with JSONB for flexible fields?"
@alice: "Yes, that's a hybrid approach."
@bob: "But then we're fighting the tool. Relational DB with JSON bolted on."

14:30 - Charlie: "We have 15 min to decide. Let's use weighted criteria."

### 40-45 min: Decision via Weighted Criteria

14:30 - Charlie screen shares criteria matrix:

| Criterion | Weight | PostgreSQL Score | MongoDB Score | Notes |
|-----------|--------|------------------|---------------|-------|
| **ACID compliance** | 40% | 10 | 7 | Alice: PG proven, MongoDB newer |
| **Read performance** | 30% | 7 | 9 | Bob: MongoDB faster for reads |
| **Team expertise** | 20% | 9 | 5 | Current: 3/5 know SQL, 0/5 know Mongo |
| **Migration cost** | 10% | 8 | 6 | Alice: PG from MySQL easier |

14:35 - Team scores each (1-10 scale):
- PostgreSQL: (10×0.4) + (7×0.3) + (9×0.2) + (8×0.1) = 4.0 + 2.1 + 1.8 + 0.8 = **8.7**
- MongoDB: (7×0.4) + (9×0.3) + (5×0.2) + (6×0.1) = 2.8 + 2.7 + 1.0 + 0.6 = **7.1**

14:40 - Charlie: "Math says PostgreSQL. Anyone object to the weighting?"

@bob: "I think performance should be 40%, not 30%. Our app is read-heavy."

@charlie: "Okay, let's adjust:"

| Criterion | Weight | PostgreSQL | MongoDB |
|-----------|--------|------------|---------|
| ACID compliance | 30% | 10 | 7 |
| Read performance | 40% | 7 | 9 |
| Team expertise | 20% | 9 | 5 |
| Migration cost | 10% | 8 | 6 |

New scores:
- PostgreSQL: (10×0.3) + (7×0.4) + (9×0.2) + (8×0.1) = 3.0 + 2.8 + 1.8 + 0.8 = **8.4**
- MongoDB: (7×0.3) + (9×0.4) + (5×0.2) + (6×0.1) = 2.1 + 3.6 + 1.0 + 0.6 = **7.3**

14:43 - Still PostgreSQL wins.

@charlie: "PostgreSQL wins even with Bob's preferred weighting. Final objections?"

@bob: "I still think MongoDB is better long-term, but the data is clear. I commit to making PostgreSQL work."

14:44 - **DECISION: PostgreSQL**

---

## Decision Record

**Chosen Option:** PostgreSQL

**Rationale:**
ACID compliance is non-negotiable for user data (especially payments and auth). While MongoDB has improved transactions, PostgreSQL has 20+ years of proven ACID reliability. Team already knows SQL (3/5 engineers), reducing risk. Read performance difference is marginal at current scale (<100k users). We can use JSONB for schema flexibility where needed without abandoning relational model.

**Dissenters:**
- @bob: "I disagree with prioritizing ACID over read performance, but I commit to making PostgreSQL work and will lead the performance optimization effort post-launch."

**Action Items:**
- [ ] @alice: Create PostgreSQL migration plan from MySQL (by Feb 17)
- [ ] @dana: Set up PostgreSQL staging environment (by Feb 18)
- [ ] @bob: Lead performance optimization (query analysis, indexing strategy) post-launch
- [ ] @charlie: Schedule architecture review session to confirm schema design (by Feb 20)

**Next Checkpoint:** 
March 15, 2026 (review performance metrics after 2 weeks in production)

---

## Post-GUSH Actions

14:45 - GUSH ends (exactly on time)
14:50 - Charlie posts decision in #decisions channel
15:00 - Action items added to Linear
15:30 - Charlie DMs Bob: "Thanks for committing even though you disagreed. That's what makes this work. Let's chat tomorrow about the optimization plan."

**Total time:** 45 minutes to resolve 2-week debate
```

---

### GUSH Anti-Patterns (What NOT to Do)

**❌ Anti-Pattern 1: The Endless GUSH**

**Symptom:** Session goes 60, 70, 90 minutes

**Why it happens:**
- No hard timer
- "Just 5 more minutes to decide" (never ends)
- Facilitator too passive

**Fix:**
- Hard timer. Non-negotiable stop.
- At 45 min: "We're out of time. Options:"
  - A) Make decision with current info
  - B) Schedule GUSH Part 2 for tomorrow
  - C) Postpone decision to [date] with explicit plan
- NEVER extend in the moment

**❌ Anti-Pattern 2: The Unprepared GUSH**

**Symptom:** People reading docs during session

**Why it happens:**
- Pre-work not shared
- Shared but not enforced
- "We can just catch up real quick" (takes 30 min)

**Fix:**
- 24h rule: Doc must be shared 24h before
- 2h rule: If <80% confirmed read 2h before → POSTPONE
- No exceptions (even for executives)

**❌ Anti-Pattern 3: The Fake GUSH**

**Symptom:** Decision already made privately, GUSH is theater

**Why it happens:**
- Leadership has decided but wants "buy-in"
- One person's mind is made up, wants validation

**Result:** Team resentment, loss of trust in protocol

**Fix:**
- Don't call it GUSH if decision is made
- Instead: "Here's the decision. Here's why. Questions?"
- Honesty > performative participation

**❌ Anti-Pattern 4: The Multi-Objective GUSH**

**Symptom:** Trying to decide 3 things in one session

**Example:** "Let's pick database AND deployment strategy AND API framework"

**Result:** Decides none well, or superficially

**Fix:**
- One objective only (literally one sentence)
- Multiple decisions → Multiple GUSH sessions
- Or: One GUSH to decide decision priority, then focused sessions

**❌ Anti-Pattern 5: The GUSH in Red Zone**

**Symptom:** Trying to run GUSH when Zc ≥ 1.0

**Why it fails:** Team doesn't have bandwidth for sync

**What happens:**
- Half the people don't show up (too busy)
- Those who show haven't read pre-work (no time)
- Discussion is low-quality (everyone's burned out)

**Fix:**
- Check Zc BEFORE scheduling GUSH
- If Zc ≥ 1.0 → Use BLUES (async decision via fork + document)
- GUSH only works in green zone (Zc < 0.7)

---

### Copy-Paste Template for Your Team

**Save this as "GUSH Template.md" in shared drive:**

```markdown
# GUSH Session Template

Copy this before every GUSH:

---

# GUSH Session: [Decision Title]

**Date:** YYYY-MM-DD HH:MM  
**Duration:** 45 minutes (HARD STOP)  
**Participants:** @name1, @name2, @name3  
**Facilitator:** @facilitator  
**Objective:** [One sentence - what decision are we making?]

---

## Pre-Work Checklist (24h before)

- [ ] Context doc shared (2 pages max): [link]
- [ ] All participants confirmed read:
  - [ ] @name1 ✅
  - [ ] @name2 ✅
  - [ ] @name3 ✅
- [ ] Facilitator assigned
- [ ] Timer ready
- [ ] Output template ready

**If ANY unchecked → POSTPONE**

---

## Agenda

**0-5 min:** Alignment check  
**5-15 min:** Position A presentation  
**15-25 min:** Position B presentation  
**25-40 min:** Structured debate  
**40-45 min:** Decision + documentation

---

## Decision Record (Fill During)

**Chosen:** [Option]  
**Rationale:** [Why]  
**Dissenters:** [Names + "Disagree & Commit"]  
**Action Items:**
- [ ] @owner: [task] by [date]

**Next Checkpoint:** [DATE]

---

**Post-GUSH (Within 2h):**
- [ ] Decision posted in #decisions
- [ ] Action items in tracker
- [ ] Checkpoint scheduled
```

---

## End of Part II Summary

**What you now have:**
- ✅ **Pulse Template** (BLUES mode async rhythm)
- ✅ **Fork Declaration** (BHO isolation protocol)
- ✅ **GUSH Agenda** (forced convergence in 45 min)

**How to use them:**

**If Zc < 0.7 (green):**
- Default: Work normally in Study Hall
- When decision needed: Use GUSH template
- When deep focus needed: Use Fork template

**If Zc ≥ 1.0 (red):**
- Activate BLUES immediately
- Use Pulse template daily
- Fork when stuck (use Fork template)
- GUSH only for BEACON emergencies (Micro-GUSH)

**Next steps:**
1. Save these templates to shared drive
2. Post them in relevant Slack channels
3. Use them tomorrow (literally start tomorrow)
4. Adjust after 2 weeks based on what feels awkward

**Common question:** "Can we modify these templates?"

**Answer:** YES, but not yet. Use them verbatim for 2 weeks first. Then modify. Why? Because you need to experience the discipline before relaxing it. Most teams that modify too early end up with vague, ineffective versions.

---

# END OF PHASE 1

**What you've completed:**
- ✅ Part 0: Quick Start (know what to do in 10 min)
- ✅ Part I: Week 1 Setup (calculated Zc, configured tools, kicked off)
- ✅ Part II: Templates (have exact formats for Pulse, Fork, GUSH)

**Total reading time:** 45-60 minutes  
**Total implementation time:** 2 hours (Week 1), then 15 min/day ongoing

**What's NOT in this manual yet** (coming in Phase 2):
- Part III: Mode-specific playbooks (day-by-day operations)
- Part IV: Measurement & calibration (advanced Zc tracking)
- Part V: Troubleshooting (when things break)
- Part VI: Advanced topics (multi-team, nested forks)

**When Phase 2 will be written:**
- After 5-10 teams pilot Phase 1 manual
- Based on real feedback: "We tried X and Y broke"
- Troubleshooting section writes itself from actual failures

---

## What To Do Right Now

**If your Zc < 0.7 (green):**
1. Configure tools (Section 1.4) - 45 min
2. Kick off with team (Section 1.5) - 30 min
3. Use templates when needed (Part II)
4. Check Zc weekly, adjust mode as needed

**If your Zc ≥ 1.0 (red):**
1. Copy Pulse template (Section 2.1) - 5 min
2. Post in Slack: "BLUES mode activated. First pulse at 4pm today."
3. Set daily pulse time (same time every day)
4. Fork when stuck (use Fork template)
5. Check Zc daily until it drops below 0.8

**Either way:**
- Friday: 15-min retrospective
  - What worked?
  - What felt awkward?
  - Zc now vs Monday?
- Adjust based on experience

---

## Feedback & Iteration

**This manual will improve based on YOUR experience.**

**Please report:**
- What broke (issues on GitHub)
- What felt awkward (discussions)
- What we got wrong (be brutally honest)
- What's missing (gaps you discovered)

**Where to share:**
- GitHub: github.com/pyragogy/protocols/issues
- Email: info@pyragogy.org
- Twitter/X: Tag @BergamoHub

**Especially valuable:**
- "We tried X template and it failed because..."
- "We're in industry Y and had to adapt Z..."
- "The Zc calculation didn't work for us because..."
- "Here's a scenario we couldn't categorize into three modes..."

Failed experiments teach more than successful ones. Share both.

---

## License & Citation

**License:** MIT (code) + CC-BY-4.0 (documentation)  
Use freely. Attribute clearly.

**Citation:**
```bibtex
@manual{terzi2026operational,
  title={Operational Manual: CIM Protocol v1.1.0},
  author={Terzi, Fabrizio},
  year={2026},
  organization={Pyragogy.org},
  url={https://github.com/pyragogy/protocol-001-core}
}
```

---

**Document Version:** 1.1.0 Phase 1  
**Last Updated:** February 11, 2026  
**Maintainer:** Fabrizio Terzi (@BergamoHub)  
**Status:** Production-Ready for Human-Facilitated Teams

**The garage is open. Now go use it.** 🔧

---

**Related Documents:**
- [README](README.md) - Conceptual overview and theory
- [MATHEMATICAL-APPENDIX](MATHEMATICAL-APPENDIX.md) - Formal proofs
- [COGNITIVE-CRDTS](COGNITIVE-CRDTS.md) - Technical deep-dive on CRDTs
- [EXAMPLES](EXAMPLES.md) - Real-world scenarios
- [Review Report](CIM_Protocol_Review_Report.md) - Senior architect analysis

[← Back to Repository](https://github.com/pyragogy/protocol-001-core)
