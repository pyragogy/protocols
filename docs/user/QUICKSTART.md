# Quick Start Guide - CIM Pattern

**Time to first value: 15 minutes**

This guide will walk you through your first CIM Pattern implementation, from calculating Zc to running your first GUSH session.

---

## Prerequisites

- Team of 5-20 people
- Using async tools (Slack, Notion, email, AI assistants)
- Experiencing decision slowdown or cognitive overload
- 15 minutes of undistracted time

**Optional:**
- Python 3.8+ for CLI tools
- Slack workspace with webhook access

---

## Step 1: Understand Your Current State (5 min)

### Calculate Baseline Zc

**Method A: The 5-Minute Estimate**

1. **Count information sources** (last 24 hours):
   - Slack messages: ___
   - Notion updates: ___
   - AI outputs (Claude, ChatGPT, Cursor): ___
   - Email threads: ___
   - **Total:** ___

2. **Calculate V_generation:**
   ```
   V_generation = Total items ÷ 24 hours = ___ items/hour
   ```

3. **Estimate B_social:**
   ```
   B_social = Team size × 3 hours = ___ capacity/hour
   ```
   *(3 hours = conservative processing capacity per person per day)*

4. **Calculate Zc:**
   ```
   Zc = V_generation ÷ B_social = ___
   ```

**Method B: Use the Web Calculator**

```bash
cd tools/zc-calculator
open index.html
```

Enter your values → Get instant zone classification

**Method C: Use the CLI**

```bash
python tools/zc-calculator/zc_cli.py --interactive
```

---

## Step 2: Interpret Your Zone (2 min)

### 🟢 Green Zone (Zc < 0.7)

**What it means:**
- Your async-first approach is working
- Team has processing capacity headroom
- No immediate action needed

**What to do:**
- Continue current workflow
- Monitor Zc weekly
- Document what's working

**Success pattern:**
Team ships consistently, low stress, decisions made in 24-48h

---

### 🟡 Yellow Zone (Zc 0.7-1.0)

**What it means:**
- Approaching cognitive overload
- Decisions starting to lag
- Async noise building up

**What to do:**
- Schedule GUSH session within 48 hours
- Identify 3-5 pending decisions
- Prepare pre-read materials

**Warning signs:**
- Slack threads with 20+ messages, no conclusion
- "Let's discuss this in the next meeting" (repeated 3+ times)
- Team asking "What are we prioritizing again?"

---

### 🔴 Red Zone (Zc ≥ 1.0)

**What it means:**
- Standard consensus has broken down
- Information generation outpacing processing
- High risk of decision paralysis

**What to do:**
1. **Declare state of emergency** (literally—tell the team)
2. **Pause new initiatives** for 48h
3. **Activate The Jam:**
   - Declare BHO forks for deep work
   - Implement BLUES rhythm
   - Schedule emergency GUSH for critical decisions

**Emergency pattern:**
- Stop generating, start processing
- Convert async threads to BHO forks
- Force decisions on time-sensitive items

---

## Step 3: Take Immediate Action (8 min)

### If Green Zone:

1. **Set up monitoring:**
   ```bash
   # Create weekly Zc check reminder
   # Add to team calendar: "Weekly Zc Check" (15 min, recurring)
   ```

2. **Document your system:**
   - What async practices are working?
   - How do decisions get made?
   - What's your typical V_generation range?

3. **Share with team:**
   > "We calculated our Zc at 0.5 - we're in the Green Zone! Let's keep doing what we're doing and check again next week."

---

### If Yellow Zone:

1. **Schedule GUSH session:**
   ```
   Subject: GUSH Session - Forced Convergence
   When: [Within 48 hours]
   Duration: 60-90 min
   Who: [Core team]
   ```

2. **Prepare agenda:**
   - Use [GUSH template](../tools/templates/GUSH-SESSION-TEMPLATE.md)
   - List 3-5 decisions that need closure
   - Share pre-read 24h before session

3. **Set expectations:**
   ```
   Team message:

   "Our Zc is 0.85 (Yellow Zone). We're scheduling a GUSH session
   for [DATE] to force convergence on [N] pending decisions.
   
   Rules: Camera ON, no multitasking, decisions MUST be made.
   
   Pre-read: [link]
   Agenda: [link to GUSH template]
   
   See you there."
   ```

---

### If Red Zone:

1. **Send emergency alert:**
   ```
   Subject: 🚨 Cognitive Overload - Activating CIM Pattern
   
   Team,
   
   Our Zc is [X] (Red Zone). Standard async isn't working.
   
   IMMEDIATE ACTIONS:
   - Pause new initiatives for 48h
   - Emergency GUSH: [TIME/DATE]
   - All deep work → BHO forks (declare by EOD)
   
   More context: [link to this guide]
   ```

2. **Declare BHO forks:**
   - Use [BHO template](../tools/templates/BHO-FORK-TEMPLATE.md)
   - Move complex decisions to separate threads
   - Assign single owners

3. **Implement BLUES:**
   - Weekly pulse check-ins
   - Async-only between pulses
   - Force merge every 7-10 days

---

## Step 4: Run Your First Session

### Option A: GUSH Session (Yellow/Red Zone)

**Before (24h prior):**
- [ ] Share [GUSH template](../tools/templates/GUSH-SESSION-TEMPLATE.md)
- [ ] Distribute pre-read materials
- [ ] Confirm all participants available
- [ ] Test video setup

**During (60-90 min):**
- [ ] Read Zc context aloud
- [ ] Time-box each decision (5-10 min max)
- [ ] Use confidence voting (👍👎👌)
- [ ] Record decisions immediately
- [ ] No "let's table this" allowed

**After (24h):**
- [ ] Share decisions summary
- [ ] Assign action items
- [ ] Re-calculate Zc
- [ ] Document lessons learned

**Success metrics:**
- 70%+ decisions closed
- Zc reduced by 20%+
- Team confidence 7+/10

---

### Option B: BHO Fork Declaration (Red Zone)

**Setup (30 min):**
- [ ] Use [BHO template](../tools/templates/BHO-FORK-TEMPLATE.md)
- [ ] Define scope (what's IN/OUT)
- [ ] Assign single owner
- [ ] Set hard merge deadline
- [ ] Create dedicated channel

**During Fork (3-10 days):**
- [ ] Owner works in isolation
- [ ] Async updates only
- [ ] No pings in main channels
- [ ] Check-ins at day 3, 7

**Merge Preparation (48h before):**
- [ ] Draft findings document
- [ ] Share for async review
- [ ] Collect feedback
- [ ] Prepare 15-min presentation

**Merge Event:**
- [ ] Present findings
- [ ] Make recommendation
- [ ] Force decision (or schedule GUSH)
- [ ] Document lessons learned

---

## Step 5: Measure & Iterate (Ongoing)

### Weekly Check-In (15 min)

Every Friday (or your team's natural rhythm):

1. **Calculate Zc:**
   ```bash
   python tools/zc-calculator/zc_cli.py --interactive
   ```

2. **Review trend:**
   - Is Zc going up or down?
   - What changed this week?
   - Are interventions working?

3. **Adjust mode:**
   - Stay in current mode
   - Switch modes based on new Zc
   - Schedule next intervention

### Monthly Retrospective (30 min)

1. **Zc history:**
   - Plot last 4 weeks
   - Identify patterns
   - Note interventions

2. **Team feedback:**
   - What's working?
   - What's not?
   - Mode preferences?

3. **Calibrate thresholds:**
   - Are 0.7/1.0 thresholds right for you?
   - Should you adjust processing estimates?
   - Tool/workflow changes needed?

---

## Common First-Time Mistakes

### ❌ Mistake 1: Calculating Zc Once and Forgetting

**Why it's bad:** Zc is dynamic. One measurement is a snapshot, not a system.

**Fix:** Set up weekly recurring calculation. Make it a team ritual.

---

### ❌ Mistake 2: Running GUSH Without Pre-Read

**Why it's bad:** First 30 min wasted on context sharing.

**Fix:** Strict 24h pre-read rule. No pre-read = postpone session.

---

### ❌ Mistake 3: BHO Fork Without Hard Deadline

**Why it's bad:** Becomes zombie work that never merges.

**Fix:** Every fork MUST have merge date at declaration. No exceptions.

---

### ❌ Mistake 4: Treating Zc Like a Goal Metric

**Why it's bad:** Zc is diagnostic, not prescriptive. Lower isn't always better.

**Fix:** Target healthy range (0.4-0.7), not minimum possible.

---

### ❌ Mistake 5: Skipping Team Buy-In

**Why it's bad:** GUSH feels authoritarian without context.

**Fix:** Share this guide first. Run trial session. Iterate based on feedback.

---

## Success Checklist

After your first month, you should see:

- [ ] Zc calculated weekly (or when team feels overwhelmed)
- [ ] At least 1 GUSH session run successfully
- [ ] At least 1 BHO fork completed and merged
- [ ] Team understands zone classifications
- [ ] Decision latency reduced by 20%+
- [ ] Reported overwhelm down
- [ ] Team confidence in process 6+/10

If you're seeing these results, you're on the right path.

If not, see [Troubleshooting Guide](TROUBLESHOOTING.md) or [open an issue](https://github.com/pyragogy/protocols/issues).

---

## Next Steps

### Level 2: Automation

- Set up [Slack integration](../tools/templates/slack_notifier.py)
- Automate Zc calculation from Slack analytics
- Build custom dashboard

### Level 3: Advanced Patterns

- The Jam (BLUES rhythm)
- Multi-team coordination
- Curator AI (when released)

### Level 4: Organizational Adoption

- Train facilitators
- Create playbooks
- Measure ROI

[See full documentation →](../docs/)

---

## Getting Help

**Stuck? Confused? Not working?**

1. Check [FAQ](FAQ.md)
2. Read [Troubleshooting Guide](TROUBLESHOOTING.md)
3. [Open a discussion](https://github.com/pyragogy/protocols/discussions)
4. [Join Discord](#) *(coming soon)*
5. Email: protocols@pyragogy.org

**Want to share your experience?**

We're collecting case studies! If you've run CIM Pattern for 30+ days, we'd love to feature your story.

---

**Now go calculate your Zc and ship something.**

[← Back to README](../README.md) | [Next: Deep Dive on Modes →](MODES.md)
