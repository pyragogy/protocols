# Real-World Zc Calculation Examples

This document shows how to calculate Zc in different team scenarios with actual numbers.

---

## Example 1: Early-Stage Startup (8 people, remote)

### Scenario

**Team:** 8 engineers, fully remote, using Slack + Notion + Claude

**Measured over:** Last 24 hours (typical Tuesday)

### Data Collection

**Information Generation:**
- Slack messages: 180
- Notion page updates: 15
- Claude conversations (saved): 25
- Email threads: 10
- GitHub PRs + comments: 20
- **Total:** 250 items

**Processing Capacity:**
- Team size: 8 people
- Effective processing hours/person/day: 3 hours
  *(Conservative estimate: most time spent coding/building, not processing info)*

### Calculation

```
V_generation = 250 items / 24 hours = 10.4 items/hour

B_social = 8 people × 3 hours = 24 capacity/hour

Zc = 10.4 / 24 = 0.43
```

### Interpretation

**Zone:** 🟢 Green (Zc < 0.7)

**Status:** Healthy - async-first is working

**Action:** Continue current workflow. Monitor weekly.

### Actual Outcome

Team shipped 2 features in 3 weeks with no major blockers. Decision latency averaged 36 hours.

---

## Example 2: Open Source Project (25 contributors)

### Scenario

**Team:** 25 active contributors, distributed globally, async-heavy

**Measured over:** Last 7 days (normalized to 24h)

### Data Collection

**Information Generation:**
- GitHub issues opened: 35
- PR comments: 180
- Discord messages: 420
- RFC documents posted: 8
- **Total (7 days):** 643 items
- **Per day:** 643 / 7 = 92 items
- **Per hour:** 92 / 24 = 3.8 items/hour

**Processing Capacity:**
- Active contributors: 25
- Effective processing hours/person/day: 1.5 hours
  *(Lower because it's volunteer work, not full-time)*

### Calculation

```
V_generation = 3.8 items/hour

B_social = 25 people × 1.5 hours = 37.5 capacity/hour

Zc = 3.8 / 37.5 = 0.10
```

### Interpretation

**Zone:** 🟢 Green (Zc < 0.7)

**Status:** Very healthy - distributed async working well

**Action:** Document what's working. Could actually increase V_generation.

### Actual Outcome

Project maintained steady contributions. RFC-to-implementation averaged 14 days. No contributor burnout reported.

---

## Example 3: Scale-up (50 people, hybrid)

### Scenario

**Team:** 50 people, product org, mix of remote/office

**Measured over:** Last 24 hours (Monday - high activity)

### Data Collection

**Information Generation:**
- Slack messages: 800
- Email threads: 120
- Notion updates: 45
- Meeting notes published: 12
- Figma comments: 60
- Linear issues/comments: 80
- **Total:** 1,117 items

**Processing Capacity:**
- Team size: 50 people
- Effective processing hours/person/day: 2.5 hours
  *(Mix of makers and managers, medium estimate)*

### Calculation

```
V_generation = 1,117 / 24 = 46.5 items/hour

B_social = 50 people × 2.5 hours = 125 capacity/hour

Zc = 46.5 / 125 = 0.37
```

### Interpretation

**Zone:** 🟢 Green (Zc < 0.7)

**Status:** Healthy for organization size

**Action:** Continue current practices. Watch for sub-team overload.

### Actual Outcome

Organization-wide healthy, but **Product team (8 people) was in Red Zone** with Zc = 1.8. Lesson: Calculate Zc per team, not just org-wide.

---

## Example 4: Hypergrowth Startup (15 people, AI-heavy)

### Scenario

**Team:** 15 people, using Claude/Cursor extensively for coding

**Measured over:** Last 24 hours (Thursday - peak chaos)

### Data Collection

**Information Generation:**
- Slack messages: 320
- Claude/Cursor outputs (code): 85
- Notion updates: 30
- PRs + comments: 40
- Email threads: 25
- Design feedback (Figma): 35
- **Total:** 535 items

**Processing Capacity:**
- Team size: 15 people
- Effective processing hours/person/day: 2 hours
  *(Lower because AI tools increase generation, not processing)*

### Calculation

```
V_generation = 535 / 24 = 22.3 items/hour

B_social = 15 people × 2 hours = 30 capacity/hour

Zc = 22.3 / 30 = 0.74
```

### Interpretation

**Zone:** 🟡 Yellow (Zc 0.7-1.0)

**Status:** Warning - approaching overload

**Action:** Schedule GUSH session within 48 hours

### Actual Outcome

Team scheduled emergency GUSH. Closed 7 pending decisions in 90 minutes. Zc dropped to 0.52 within 3 days.

---

## Example 5: Crisis Mode (12 people, incident response)

### Scenario

**Team:** 12 engineers, major production incident, war room mode

**Measured over:** 8-hour incident window

### Data Collection

**Information Generation:**
- Slack (incident channel): 450
- Datadog alerts: 80
- GitHub commits: 25
- Postmortems started: 5
- **Total (8h):** 560 items
- **Normalized to 24h:** 560 × 3 = 1,680 items

**Processing Capacity:**
- Team size: 12 people
- Effective processing hours/person/day: 6 hours
  *(Higher during crisis - everyone focused)*

### Calculation

```
V_generation = 1,680 / 24 = 70 items/hour

B_social = 12 people × 6 hours = 72 capacity/hour

Zc = 70 / 72 = 0.97
```

### Interpretation

**Zone:** 🟡 Yellow (Zc 0.7-1.0), **but context matters**

**Status:** High Zc is appropriate for crisis - everyone processing synchronously

**Action:** This is temporary. Post-incident, return to Green Zone.

### Actual Outcome

Incident resolved in 8 hours. Post-crisis Zc returned to 0.45. Team took recovery day.

**Lesson:** High Zc isn't always bad—context matters.

---

## Example 6: Academic Research Team (6 people)

### Scenario

**Team:** 6 researchers, slow-moving, consensus-driven

**Measured over:** Last 24 hours (typical week)

### Data Collection

**Information Generation:**
- Email threads: 12
- Slack messages: 25
- Shared docs (comments): 8
- Literature reviews posted: 2
- **Total:** 47 items

**Processing Capacity:**
- Team size: 6 people
- Effective processing hours/person/day: 4 hours
  *(Higher - academics read/think deeply)*

### Calculation

```
V_generation = 47 / 24 = 1.96 items/hour

B_social = 6 people × 4 hours = 24 capacity/hour

Zc = 1.96 / 24 = 0.08
```

### Interpretation

**Zone:** 🟢 Green (Zc < 0.7)

**Status:** Very low Zc - possibly under-utilizing async

**Action:** Could increase information generation without overload

### Actual Outcome

Team operates slowly but deliberately. No cognitive overload. CIM Pattern not critical for this team.

**Lesson:** Low Zc can indicate healthy pace OR under-utilization.

---

## Example 7: Marketing Team (10 people, campaign launch)

### Scenario

**Team:** 10 marketers, launching major campaign, high creativity mode

**Measured over:** Last 24 hours (campaign launch week)

### Data Collection

**Information Generation:**
- Slack messages: 280
- Figma design iterations: 45
- Notion campaign docs: 20
- Email campaigns sent: 8
- Social media posts drafted: 30
- Analytics reviews: 15
- **Total:** 398 items

**Processing Capacity:**
- Team size: 10 people
- Effective processing hours/person/day: 2.5 hours
  *(Creative work - less time on processing, more on creating)*

### Calculation

```
V_generation = 398 / 24 = 16.6 items/hour

B_social = 10 people × 2.5 hours = 25 capacity/hour

Zc = 16.6 / 25 = 0.66
```

### Interpretation

**Zone:** 🟢 Green (Zc < 0.7), **but close to Yellow**

**Status:** Near threshold - watch carefully

**Action:** Monitor daily. Be ready to GUSH if crosses 0.7.

### Actual Outcome

Campaign launched successfully. Post-launch Zc dropped to 0.35 as creative generation slowed.

---

## Key Patterns Across Examples

### Pattern 1: Team Size ≠ Processing Capacity

Large teams don't automatically have high B_social. Effective processing hours matter more than headcount.

### Pattern 2: AI Tools Increase V_generation Dramatically

Teams using Claude/Cursor/ChatGPT generate 2-3× more information than non-AI teams.

### Pattern 3: Crisis Mode Can Have High Zc (And That's OK)

Temporary high Zc during incidents is fine—everyone's synchronized. Problem is chronic high Zc.

### Pattern 4: Low Zc Can Mean Different Things

- Healthy pace (academic team)
- Under-utilization (could ship faster)
- Post-crisis recovery (intentional slowdown)

### Pattern 5: Calculate Per-Team, Not Org-Wide

Large orgs need Zc per team. Org-wide average hides sub-team problems.

---

## Your Turn: Calculate Your Zc

Use the CLI:

```bash
python tools/zc-calculator/zc_cli.py --interactive
```

Or web calculator:

```bash
open tools/zc-calculator/index.html
```

**Need help?** See [Quick Start Guide](../docs/QUICKSTART.md)

---

[← Back to README](../README.md) | [Next: Templates →](../tools/templates/)
