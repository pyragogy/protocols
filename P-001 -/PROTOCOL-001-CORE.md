# The CIM Protocol
## Cognitive Impedance Mismatch & Dynamic Mode Switching in Hybrid Teams

**Created by:** Fabrizio Terzi (@BergamoHub)  
**Version:** 2.0 – February 2026  
**License:** MIT – Open Source Cognitive Infrastructure

---

## Before You Read This

If you've ever closed Slack feeling exhausted without knowing what you actually decided—this protocol is for you.

If your team has the same conversation three times and still can't move forward—this protocol is for you.

If your smartest people are burning out while your simplest decisions take weeks—this protocol is for you.

**Don't read this whole document.** Choose your entry point:

- **Just want to try it?** → [Quick Start](#part-vi-implementation-guide) (Week 1: 30 minutes)
- **Need the one-pager?** → [Quick Reference Card](#quick-reference-card) (print, post, use)
- **Want to understand why?** → [Part I: The Problem](#part-i-understanding-cognitive-impedance-mismatch-cim)
- **Skeptical? Good.** → [Common Questions](#part-vii-common-questions) first

This is version 2.0. It's not finished. It's a working hypothesis that needs your real-world testing to evolve.

---

> *"The problem isn't that your team is slow. The problem is that you're generating insights faster than anyone can integrate them."*

---

## Introduction: The Collaboration Paradox

Here's what nobody tells you about modern teamwork: the better your team gets at thinking, the worse it gets at deciding.

You hire smart people. They generate ideas constantly. They spot patterns, propose solutions, share articles, debate approaches. Your Slack is alive with intelligence. And yet somehow, nothing moves forward. Meetings multiply. The same conversations repeat. Decision paralysis sets in. Your best people start looking exhausted.

This isn't a people problem. It's not a tools problem. It's a **topology problem**.

Your team is trying to run a synchronous collaboration model on an asynchronous information load. It's like trying to have a conversation in a nightclub—everyone's shouting, nobody's hearing, and the music just keeps getting louder.

We call this **Cognitive Impedance Mismatch**, and once you see it, you can't unsee it.

---

## Part I: Understanding Cognitive Impedance Mismatch (CIM)

### The Core Concept

**Cognitive Impedance Mismatch occurs when the rate at which a team generates information exceeds its collective capacity to process and integrate that information.**

Think of it like electrical impedance. When you plug a high-power device into a circuit that can't handle it, something breaks. Either the device doesn't work, or the circuit fries. In teams, the same thing happens—either good ideas get lost, or good people burn out.

### The Mathematics of Overload

**The Cognitive Impedance Formula:**

$Z_c = \frac{V_{generation}}{B_{social}}$

Where:
- **Zc** = Cognitive Impedance (system stress level)
- **V_generation** = Velocity of information entering the system
- **B_social** = Team's actual capacity to process and integrate

**Visual Representation:**

```
Information Generated (V_gen)
        ÷
Team Processing Capacity (B_social)
        =
Cognitive Impedance (Zc)

If Zc < 0.7  → GREEN ZONE (Healthy)
If Zc 0.7-0.9 → YELLOW ZONE (Caution)  
If Zc ≥ 1.0  → RED ZONE (Overload)
```

### The Three Zones

| Zone | Zc Range | System State | What You Feel | What To Do |
|:-----|:---------|:-------------|:--------------|:-----------|
| **Green** | < 0.7 | Healthy flow | Engaged, not overwhelmed | Study Hall or GUSH |
| **Yellow** | 0.7-0.9 | Elevated stress | Slightly behind, manageable | Study Hall only, monitor |
| **Red** | ≥ 1.0 | Overload | Drowning, backlog growing | BLUES (mandatory) |

### How to Recognize CIM in Your Team

**Communication Symptoms:**
- Your primary channel feels like a fire hose
- People apologize for "being behind" on messages
- Important threads get buried before anyone responds
- Someone asks "Can anyone summarize where we are on X?"

**Decision Symptoms:**
- Same topic discussed three times without resolution
- Meetings end with "let's continue this conversation async"
- People avoid decisions: "we need to align with everyone first"
- Decisions made, then quietly unmade as new information surfaces

**Social Symptoms:**
- Best people working nights/weekends to "catch up"
- Junior members stop asking questions (don't want to add noise)
- Sub-channels proliferate as people create "actual work" spaces
- Team members describe exhaustion despite shipping less

If you're nodding your head, you have CIM. The question is: what do you do about it?

---

## Part II: The Framework—Three Modes, One Principle

### Why Traditional Responses Fail

Most teams respond to overload in predictable, destructive ways:

**❌ Response 1: More Meetings**
- Increases synchronization cost
- Decreases time for actual work
- **Result:** Higher cognitive load, worse performance

**❌ Response 2: New Tools**
- Changes the interface, not the problem
- Same overload, different platform
- **Result:** No improvement, just adaptation fatigue

**❌ Response 3: "Work Harder"**
- Pushes through for ~2 weeks
- Then burnout hits hard
- **Result:** Productivity collapse, team damage

**None address the root cause:** You're using a fixed collaboration topology for a variable cognitive load.

### The Core Insight

**Your collaboration mode should be a function of your cognitive impedance.**

- **Low load** → Synchronous convergence works beautifully
- **High load** → Forcing synchronization destroys value

This isn't about async vs sync. It's about **dynamic mode switching** based on system state.

### The Three Modes

```mermaid
graph TB
    Start{Measure Current<br/>Cognitive Impedance}
    
    Start -->|Low Load<br/>Zc < 0.7| Decision{Need Immediate<br/>Decision?}
    Decision -->|No| ModeA[Mode A: STUDY HALL<br/><br/>Independent parallel work<br/>Passive presence signals<br/>AI as personal tutor]
    Decision -->|Yes| ModeB[Mode B: GUSH<br/><br/>Forced synchronous convergence<br/>Time-boxed decision making<br/>AI as semantic moderator]
    
    Start -->|High Load<br/>Zc ≥ 1.0| ModeC[Mode C: BLUES<br/><br/>Asynchronous rhythm maintenance<br/>Fork and explore independently<br/>AI as context bridge]
    
    ModeA --> OutA[Output:<br/>✓ Individual progress<br/>✓ Maintained presence<br/>✓ Deep work protected]
    ModeB --> OutB[Output:<br/>✓ Committed decision<br/>✓ Documented rationale<br/>✓ Clear accountability]
    ModeC --> OutC[Output:<br/>✓ Parallel explorations<br/>✓ Maintained coherence<br/>✓ Reduced processing load]
    
    style ModeA fill:#e8eaf6,stroke:#3949ab,stroke-width:3px
    style ModeB fill:#e1f5fe,stroke:#0277bd,stroke-width:3px
    style ModeC fill:#e8f5e9,stroke:#2e7d32,stroke-width:3px
    style Start fill:#fff9c4,stroke:#f9a825,stroke-width:3px
```

---

## Part III: The Three Modes in Practice

### Mode A: Study Hall

> **"We're here together, working in parallel."**

Think of a university library during finals week. Everyone's present. The room has energy. But nobody's interrupting anyone. You're alone together, and that's exactly the point.

#### When to Use This Mode

**Use Study Hall when:**
- ✅ Zc < 0.7 (cognitive load is manageable)
- ✅ Team members have clear, independent work streams
- ✅ You're in exploration phase before convergence
- ✅ Deep work is the primary need

#### Operating Principles

| Principle | What It Means | Example |
|:----------|:--------------|:--------|
| **Presence Over Content** | Signal you're working, don't demand processing | "Researching OAuth. Available 2pm for questions." |
| **Interruptions Are Expensive** | A "quick question" costs 23 minutes (interruption + refocus) | Async questions in threads, not DMs |
| **Async-First** | Write it down for later engagement | Updates in docs, questions in threads |
| **AI as Personal Tutor** | AI helps individuals, doesn't broadcast | Private Claude conversations for research |

#### What This Looks Like

**Monday 9am:**
```
Sarah: Deep work on payment gateway integration.
       Async questions welcome in #payments-thread.
       Back at 1pm.
```

Marcus is simultaneously researching database options. He's having a conversation with Claude about PostgreSQL vs MongoDB trade-offs. No one else sees this—they don't need to yet.

**Monday 1pm:**
```
Sarah: Payment integration progressing well.
       Hit one blocker on error handling → ticket #127
       Will have proposal tomorrow.
```

This is Study Hall. Parallel progress. Maintained presence. Minimal coordination overhead.

---

### Mode B: GUSH (Generative Unified Semantic Harmonization)

> **"We need a decision now, and we're going to make it together."**

GUSH is forced convergence. It's when you take asynchronous exploration and collapse it into synchronous decision-making. Done right, it's extraordinarily powerful. Done wrong, it's just another wasteful meeting.

#### When to Use This Mode

**Decision Tree for GUSH:**

1. **Do you need a decision?** → If NO, use Study Hall
2. **Is Zc < 0.7?** → If NO, don't GUSH (use BLUES instead)
3. **Can team do pre-work?** → If NO, fix trust first
4. **Multiple stakeholders needed?** → If NO, consider delegation
5. **All YES?** → Use GUSH

**Critical Rules:**
- ✅ Use when: Low impedance + urgent decision + multiple stakeholders
- ❌ Never GUSH when: High impedance (Zc ≥ 1.0) - use BLUES instead
- ⚠️ Warning: If team can't respect pre-work, you have a trust problem, not a decision problem

#### The GUSH Protocol

**Session Timeline (45 minutes maximum):**

| Time | Phase | Purpose |
|:-----|:------|:--------|
| **Pre-Session** | Materials shared 24-48h before | All context provided in advance |
| | Team confirms pre-work complete | No one shows up unprepared |
| **0-5 min** | Context Refresh | Quick review (already read) |
| **5-10 min** | AI Synthesis | Present options, agreements, disagreements |
| **10-35 min** | Structured Discussion | Clarify, surface concerns, test assumptions |
| **35-40 min** | Decision Point | Commit to X, not Y or Z, with reasoning |
| **40-45 min** | Documentation | AI generates decision doc in real-time |

**Pre-Session (24-48h before):**

All materials shared:
- Specific decision to be made
- Background context and research
- Options being considered
- Evaluation criteria
- Relevant data/examples

Every participant confirms they've reviewed materials. If someone hasn't done pre-work, session is postponed. Non-negotiable.

> **⚠️ CRITICAL WARNING**  
> If your team cannot respect pre-work commitments, you do not have a decision problem. You have a trust problem. Fix that first. GUSH will fail spectacularly in cultures where people show up unprepared expecting to be caught up during the meeting.

**Session Structure (45 min max):**

| Time | Phase | Purpose |
|:-----|:------|:--------|
| 0-5 min | Context Refresh | Quick review (already read, just refreshing) |
| 5-10 min | AI Synthesis | AI presents: options, agreements, disagreements |
| 10-35 min | Structured Discussion | Clarify, surface concerns, test assumptions |
| 35-40 min | Decision Point | Commit to X, not Y or Z, with clear reasoning |
| 40-45 min | Documentation | AI generates decision doc in real-time |

#### Why This Works

GUSH respects cognitive economics:

- **Pre-work** → Everyone arrives informed, not ignorant
- **Time box** → Urgency to decide, not drift
- **AI synthesis** → Shared understanding from the start
- **Mandatory docs** → Decision doesn't evaporate post-meeting

It's not a meeting. It's a **decision ceremony**.

---

### Mode C: BLUES (Rhythmic Asynchrony)

> **"We can't converge right now, so we maintain rhythm and explore in parallel."**

BLUES is what you do when the system is overloaded. When cognitive impedance is high, forcing synchronous alignment doesn't create clarity—it creates chaos.

**The insight:** Sometimes the best way to maintain team coherence is to reduce coordination demands.

#### When to Use This Mode (MANDATORY Triggers)

**Switch to BLUES immediately if ANY of these:**

1. **Zc ≥ 1.0** - Cognitive impedance in red zone
2. **Overload symptoms visible** - Team showing stress signals
3. **Problem too complex** - Cannot resolve in single session
4. **Multiple valid approaches** - Need parallel exploration
5. **Burnout signals appearing** - Team energy depleted

**In Red Zone conditions, BLUES isn't optional. It's triage.**

#### Protocol 1: BHO (Branching for High-Output)

**Central Idea:** When you can't agree, don't argue—fork.

**The Fork Process:**

1. **Discussion reaches impasse** → Team stuck on decision
2. **Developer declares fork** → Creates fork with unique ID
3. **Independent exploration** → No justification needed during work
4. **Document findings** → Capture learnings (success or failure)
5. **Present results** → Team reviews and decides path forward

**Fork Declaration Template:**

```markdown
FORK DECLARATION

Fork ID: auth-pattern-exploration-2026-02
Forked by: Marcus Chen
Origin: #tech-architecture thread from Feb 8
Question: Can JWT replace our entire OAuth flow?
Approach: Build working prototype with test coverage
Merge Promise: Friday Feb 14, with comparison doc
Collaboration: Open to anyone interested, coord in #fork-auth-jwt
Status: Active exploration
```

**What This Does:**

| Benefit | How It Works |
|:--------|:-------------|
| **Converts argument to exploration** | Build prototype instead of debating hypotheticals |
| **Creates space** | Explore deeply without constant justification |
| **Maintains coherence** | Fork has ID, team knows it's happening, merge promised |
| **Reduces cognitive load** | Others can safely ignore until merge time |

**The Deal:**

When you fork:
- Explore thoroughly, not half-heartedly
- Document learnings (success or failure)
- Merge back by specific date
- Don't be defensive if your approach isn't chosen

When others fork:
- Don't judge during exploration
- Don't demand status updates
- Review merged results fairly
- Value negative results equally

#### Protocol 2: BLUES (The Pulse)

**Central Idea:** When overloaded, send rhythm instead of semantics.

**The Problem:**
- Person disappears → Team loses track
- Person over-communicates → Adds to collective load

**The Solution: Send pulse, not content**

| ❌ Wrong Approach | ✓ Right Approach |
|:-----------------|:-----------------|
| "Team, I've been analyzing our architecture and I have concerns about the microservices approach. I've been seeing latency issues in the metrics that suggest we might want to reconsider. I've drafted a 10-page analysis..." | "BLUES: Still here. Making progress on architecture analysis. About 60% through. Need another 2 days before ready to share." |
| **Effect:** Demands processing from everyone | **Effect:** Maintains connection without cognitive load |

**Valid BLUES Signals:**

- Status pulses: "BLUES: Progressing on X"
- Progress indicators: "60% complete"
- Time estimates: "Ready to share in 2 days"
- Simple acknowledgments: "Seen. Will respond when processed."
- Presence checks: "Still jamming on this"

**The Goal:**

BLUES signals maintain team coherence during high-load periods. They prevent the anxiety of silence ("where did Marcus go?") without creating the burden of content ("now I have to read and respond to this").

> **💡 CRITICAL DISTINCTION**  
> BLUES is not silence. It is not disengagement. It is not avoiding responsibility.  
> **BLUES is accountability without interruption.**  
> It says: "I'm working, I'm making progress, I'll deliver what I promised."

If someone uses BLUES to hide or avoid commitments, that's not BLUES. That's absence with better branding.

**The Jazz Metaphor:**

Orchestra: Perfect synchrony every moment  
Jazz: Rhythm section maintains pulse while soloists explore

As long as everyone can feel the rhythm, the ensemble stays coherent even as individuals diverge. That's BLUES.

---

## Part IV: The AI Integration Principle

Throughout this protocol, AI plays different roles in different modes. This is intentional and critical.

### The Golden Rule

> **AI must reduce cognitive impedance, never increase it.**

**The Test:**
Before using AI for team output, ask: *"Will this require MORE team processing time?"*

- **If YES** → Wrong use (content amplifier)
- **If NO** → Right use (impedance transformer)

**Impact on Cognitive Impedance:**

| AI Use | Effect | Zc Impact |
|:-------|:-------|:----------|
| ❌ Generate 10 ideas | More to read, discuss, decide | Zc INCREASES |
| ✓ Extract 3 key disagreements | Less to read, clearer signal | Zc DECREASES |
| ❌ Write comprehensive proposal | 20+ pages to process | Zc INCREASES |
| ✓ Synthesize 4 threads into matrix | 4 docs → 1 comparison | Zc DECREASES |

### Right Use vs. Wrong Use

| ❌ WRONG: Content Generator | ✓ RIGHT: Noise Filter |
|:---------------------------|:----------------------|
| "Generate 10 alternative approaches" | "Extract the 3 key disagreements from 200 messages" |
| "Write comprehensive proposal" | "Synthesize 4 research threads into comparison matrix" |
| "Give pros and cons for each option" | "What questions haven't been addressed?" |
| **Result:** 10 more things to evaluate, 20 pages to read, 30 decision points | **Result:** 200 messages → 3 points, 4 docs → 1 comparison, scattered thinking → focused questions |

### Mode-Specific AI Roles

| Mode | AI Role | Functions | Broadcast? |
|:-----|:--------|:----------|:-----------|
| **Study Hall** | Personal Tutor | Individual research assistant, answers questions privately, synthesizes information | ❌ No team broadcasting |
| **GUSH** | Semantic Moderator | Real-time transcription, conflict mapping, synthesis suggestions, decision documentation | ✓ Yes, to all participants |
| **BLUES** | Context Bridge | Tracks active forks, onboards new members without bothering humans, synthesizes parallel learnings | ✓ Yes, but only when needed |

---

## Part V: Measuring Impedance in Practice

You don't need precision. You need awareness.

### The Qualitative Approach

Daily team pulse (10 seconds per person):

**"How overloaded did you feel today? (1-5)"**

| Rating | Zone | Feeling | Action |
|:-------|:-----|:--------|:-------|
| **1-2** | Green | Comfortable pace, could handle more | Study Hall or GUSH OK |
| **3-4** | Yellow | Getting stressed, near capacity | Study Hall only, monitor closely |
| **5** | Red | Drowning, can't keep up | BLUES mandatory |

**Rule:** If team average is consistently 4 or above, you're in high impedance. Switch to BLUES.

### The Quantitative Proxy

**Simple weekly calculation:**

1. **Count:** Total messages sent in primary channels
2. **Count:** Average messages each person actually processed
3. **Calculate:** Zc = Total / (Average × Team Size)

**Interpret the result:**

| Zc Result | Zone | Status | Action |
|:----------|:-----|:-------|:-------|
| < 0.7 | Green | Healthy | Study Hall or GUSH safe |
| 0.7-0.9 | Yellow | Approaching overload | Study Hall only, monitor |
| ≥ 1.0 | Red | Overload | BLUES mandatory |

**Example:**  
Team of 6 sent 240 messages last week. Each person processed ~50 messages.

Zc = 240 / (50 × 6) = 240 / 300 = **0.8** (Yellow Zone)

### Leading Indicators

**Watch for these warning signs:**

**Communication Patterns:**
- Response times lengthening
- More "sorry for late response" messages
- "Did you see my message about X?" questions

**Decision Quality:**
- Same topics discussed repeatedly
- Decisions quietly reversed
- "Let's table this" becoming common

**Team Energy:**
- Night/weekend work to "catch up"
- Active channels going silent
- Increased irritability in discussions

When you see these, check impedance formally. You'll probably find Yellow or Red.

---

## Part VI: Implementation Guide

Understanding the framework is one thing. Using it is another.

### Implementation Timeline

**4-Week Rollout Plan:**

| Week | Focus | Key Activities | Duration |
|:-----|:------|:---------------|:---------|
| **Week 1** | Foundation | Team meeting (30 min) → Baseline measurement (2 days) → Practice mode declaration (2 days) | 5 days |
| **Week 2** | First GUSH | Schedule real decision → Run full GUSH protocol → Debrief session | 5 days |
| **Week 3** | First Fork | Identify disagreement → Declare BHO fork → Independent exploration → Fork review | 5 days |
| **Week 4** | High-Impedance | Practice BLUES mode → Test both protocols → Month 1 retrospective | 5 days |

### Week 1: Foundation

**Day 1 - Introduction (30 minutes):**

Share this document. Everyone reads Part I & II beforehand.

In meeting, discuss:
1. "Which CIM symptoms do we recognize?"
2. "What would mode switching mean for us?"
3. "Will we experiment for 4 weeks?"

**Days 2-3 - Baseline:**

Each person tracks privately:
- Team messages sent
- Messages they actually processed
- How they felt (1-5 scale)

Share anonymously end of Day 3. Calculate rough impedance.

**Days 4-5 - Practice Declaration:**

Every team interaction starts with mode:

```
Slack: "Mode: Study Hall - Researching databases, available 3pm"
Calendar: "Mode: GUSH - Deployment decision, pre-work in link"
Email: "Mode: BLUES - Fork ongoing, merge Friday"
```

### Week 2: First Real GUSH

Choose a real decision. Use full protocol:
- Materials shared 24h advance
- Everyone confirms pre-read
- 45-minute session
- Decision doc generated
- Published immediately

**Debrief:** What worked? What felt forced? Adjustments needed?

### Week 3: First Real Fork

Identify current disagreement. Someone declares fork using BHO protocol.

Let them explore. Everyone else practices not interrupting.

**Week end:** Fork creator shares findings. Discuss: Better than endless debate?

### Week 4: First High-Impedance Response

Watch metrics. When impedance → 1.0, call BLUES explicitly.

Practice both protocols:
- Someone forks complex topic (BHO)
- Everyone sends pulse signals, not detailed updates (BLUES)

**Retrospective:**
1. What's better than before?
2. What still feels awkward?
3. Continue for another month?

### Month 2-3: Refinement & Integration

By Month 3, mode switching should feel natural. You're not "doing CIM"—you're just working.

**Success indicators:**
- People spontaneously call mode switches
- Fork declarations happen without ceremony
- BLUES signals understood and respected
- Team feels less overwhelmed despite same workload

---

## Part VII: Common Questions

**"What about truly urgent emergencies?"**

Real emergencies override the protocol. Deal with the emergency. But notice: most "urgent" things aren't emergent—they're just loud. The protocol helps you distinguish.

**"How does this work with distributed timezones?"**

GUSH becomes harder, which is why you need BLUES more. When synchronous alignment is expensive, lean into asynchronous exploration. GUSH happens less frequently, requires more planning.

**"What if someone refuses to follow mode rules?"**

First ask why. Often violations signal wrong mode selection, not difficult people. If someone keeps interrupting in Study Hall, maybe the team needs GUSH to make a decision.

If genuinely not respecting protocol, that's a team norms conversation.

**"Isn't this just Agile/Scrum renamed?"**

No. Traditional Agile assumes static communication patterns (daily standups, sprint planning). It doesn't adapt to cognitive load or address AI integration.

CIM is topology-aware and load-responsive. Tomorrow's mode depends on today's impedance.

**"How is this different from 'work async more'?"**

Because async isn't always better. When impedance is low and you need a decision, GUSH (synchronous) is more efficient than endless async back-and-forth.

The insight: "match topology to load," not "async good, sync bad."

**"Won't this create silos?"**

Only if you never merge. Fork protocol requires merge-back with documentation. BLUES maintains rhythm. GUSH forces alignment when needed.

Done right: parallel exploration with intentional convergence. Not silos—productive divergence.

---

## Part VIII: What We Don't Know Yet

This protocol is version 2.0, which means it's incomplete. Open questions:

**On Measurement:**
- Are 0.7 and 1.0 thresholds universal, or team-dependent?
- Can real-time impedance dashboards help or become ignored metrics?
- What's the right sampling frequency—daily, weekly, per-project?

**On Mode Transitions:**
- How long until teams get comfortable with switching?
- Are there team compositions where GUSH fundamentally doesn't work?
- What happens when sub-teams are in different modes simultaneously?

**On BLUES Specifically:**
- How do you know when a fork has explored too long?
- What's the right balance between protective async and productive isolation?
- Can BLUES work in hierarchical organizations or does it require flat culture?

**On AI Integration:**
- Which AI capabilities actually reduce impedance vs. just sound good?
- How do teams prevent AI "context debt" (AI knows things humans forgot)?
- What's the failure mode of over-relying on AI as context bridge?

**We need your data.** If you try this protocol, document what worked and what broke. Open an issue at github.com/pyragogy/protocols with your findings.

**Especially valuable:**
- "We tried X and it failed because..."
- "We're in industry Y and had to adapt Z..."
- "The thresholds didn't work for us, we found..."
- "Here's a case we couldn't categorize into three modes..."

Failed experiments teach us more than successful ones. Share both.

---

## Conclusion: The Shift

The CIM Protocol isn't complicated. Three modes. One metric. Dynamic switching.

What makes it powerful isn't complexity—it's the shift in perspective.

**Stop thinking:** Collaboration as fixed state ("we're async" or "we do standups")  
**Start thinking:** Dynamic system that responds to load

**Stop using:** AI to generate more content  
**Start using:** AI to reduce noise

**Stop forcing:** Synchronous alignment when drowning  
**Start maintaining:** Rhythm while exploring in parallel

The teams that thrive won't be the ones with the best tools or smartest people. They'll be the ones who understand cognitive economics—who treat attention as scarce and design collaboration accordingly.

That's what CIM gives you: operating at the edge of your team's cognitive capacity without crossing into overload.

Not by working less. By **working in the right mode for the current load**.

**Now go try it.** Pick one thing from the Quick Reference. Use it tomorrow. See what breaks. Tell us what you learned.

This isn't finished. It needs your experimentation to evolve.

---

## Attribution & License

### Intellectual Property

**Cognitive Impedance Mismatch (CIM)** – Concept originated and defined by **Fabrizio Terzi** (@BergamoHub), February 2026.

**Three-Mode Framework & Dynamic Switching** – Designed by **Fabrizio Terzi**, building on foundational work in collaborative learning taxonomies and peer-to-peer pedagogy.

**Semantic Operators (GUSH, BHO, BLUES)** – Designed by the Pyragogy Collective, led by **Fabrizio Terzi**.

### License

This protocol is released under the MIT License. Free to use, adapt, and distribute with attribution.

### Citation

**Academic/Formal:**
```
Terzi, F. (2026). The CIM Protocol: Cognitive Impedance Mismatch 
and Dynamic Mode Switching in Hybrid Human-AI Teams. 
Pyragogy Collective. https://github.com/pyragogy/protocols
```

**Informal:**
```
Based on the CIM Protocol by Fabrizio Terzi
https://github.com/pyragogy/protocols
```

### Contributing

**Share your experience:** github.com/pyragogy/protocols/discussions  
**Report issues:** github.com/pyragogy/protocols/issues  
**Built something useful?** Submit a pull request  
**Questions?** @BergamoHub

---

**Version 2.0 – February 2026**  
*Fabrizio Terzi*

---

## Quick Reference Card

**For printing and posting where your team can see it**

---

### THE CIM PROTOCOL – ESSENTIAL GUIDE

**Core Concept:** Cognitive Impedance Mismatch (CIM)  
When information generation exceeds team processing capacity, collaboration breaks.

**Core Metric:**  
Zc = Information Generated / Team Processing Capacity

| Zone | Range | Action |
|:-----|:------|:-------|
| Green | Zc < 0.7 | Sync work safe |
| Yellow | 0.7-0.9 | Monitor closely |
| Red | Zc ≥ 1.0 | Switch to async |

---

**MODE A: STUDY HALL**  
*When: Default state, parallel work*

- Work independently
- Signal presence only
- No interruptions
- AI helps individually

Example: "Study Hall mode: Researching auth patterns. Available 2pm."

---

**MODE B: GUSH**  
*When: Need decision NOW (only if Zc < 0.7)*

Required:
- Pre-work shared 24h before
- Everyone confirms they've read it
- 45 minute maximum
- Must produce committed decision
- AI transcribes and synthesizes

Structure:
- 0-5 min: Context (already read)
- 5-35 min: Discussion
- 35-45 min: Decision + documentation

---

**MODE C: BLUES**  
*When: Zc ≥ 1.0 (MANDATORY) or high complexity*

**BHO (Fork It):**
When stuck: don't debate, fork and explore.

```
Fork: [topic-name]
By: [your-name]
Merge promise: [date]
Status: Active exploration
```

**BLUES (Send Rhythm):**
When overloaded: don't send content, send pulse.

"BLUES: Still progressing on X. 60% done. Ready in 2 days."

---

**AI GOLDEN RULE:**

AI reduces impedance, never increases it.

Test: "Will this AI output require MORE team processing?"
- If YES → Wrong use
- If NO → Correct use

---

**EMERGENCY OVERRIDE:**

Anyone can call "BLUES MODE" when drowning.  
Team switches immediately. No explanation needed.

---

*Version 2.0 – Fabrizio Terzi – MIT License*  
*github.com/pyragogy/protocols*
