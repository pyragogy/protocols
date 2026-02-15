# CIM Pattern

> **Cognitive Impedance Mismatch** - Dynamic Mode Switching for AI-Augmented Teams

<<<<<<< HEAD
---

## 👋 Before You Read This

If you've ever finished a team meeting with more questions than answers, or watched your Slack explode while deadlines approach, you've hit **Cognitive Impedance**. It's what happens when your team generates information faster than it can process it.

This protocol is the circuit breaker. It gives you tre modes of operation—**Study Hall**, **GUSH**, and **The Jam**—and tells you exactly when to switch between them based on the $Z_c$ ratio.

**Quick stats from our pilots**: 30% faster decisions, 40% less meeting time. [Read the operational manual](P-001%20-/OPERATIONAL-MANUAL.md) to start today.

---

## 🚀 Quick Navigation

* **I want to start NOW:** → [P-001 -/OPERATIONAL-MANUAL.md](P-001%20-/OPERATIONAL-MANUAL.md)
* **I need proof:** → Skip to [Metrics & Validation](#6-metrics-and-validation)
* **I want the math:** → [P-001 -/MATHEMATICAL-APPENDIX.md](P-001%20-/MATHEMATICAL-APPENDIX.md)
* **I want to see the code/logic:** → [P-001 -/COGNITIVE-CRDTS.md](P-001%20-/COGNITIVE-CRDTS.md)

---

## 1. THE PROBLEM: When Teams Outrun Themselves

### 1.1 The Breaking Point
Modern teams face a fundamental friction: **AI and async tools let us generate ideas at machine speed, but we still process them at human speed.**

### 1.2 The Math ($Z_c$)
$$Z_c = \frac{V_{generation}}{B_{social}}$$

* **Green Zone ($Z_c < 0.7$):** Traditional collaboration works.
* **Red Zone ($Z_c \geq 1.0$):** Standard consensus fails. **Activate Protocol.**

[See P-001 -/MATHEMATICAL-APPENDIX.md](P-001%20-/MATHEMATICAL-APPENDIX.md) for formal derivations.

---

## 2. THE SOLUTION: Modes & Operators

| Mode | Name | Synchronization | Key Operator |
|------|------|-----------------|--------------|
| **Mode A** | **Study Hall** | Low (async) | Presence Signal |
| **Mode B** | **GUSH** | High (sync) | **GUSH Sessions** |
| **Mode C** | **The Jam** | Rhythmic (pulse) | **BHO + BLUES** |

### 2.2 The Operators

#### 🔴 GUSH (Forced Convergence)
Time-boxed sessions to kill decision paralysis.
[→ Template in OPERATIONAL-MANUAL.md](P-001%20-/OPERATIONAL-MANUAL.md#template-3-gush-agenda-forced-convergence)

#### 🔵 BHO (Cognitive Fork)
Branching for High-Output. Declare a fork, go deep, merge later.
[→ Template in OPERATIONAL-MANUAL.md](P-001%20-/OPERATIONAL-MANUAL.md#template-2-fork-declaration-bho)

#### 🟣 BLUES (The Pulse)
The async rhythm for distributed teams.
[→ Template in OPERATIONAL-MANUAL.md](P-001%20-/OPERATIONAL-MANUAL.md#template-1-the-pulse-blues-mode)

---

## 3. ARCHITECTURE

### 3.1 The "Curator" AI
AI acts as a **noise reducer**, not a creator. It monitors $Z_c$ and suggests mode switches.

### 3.2 Cognitive CRDTs
Applying distributed computing logic to human ideas to ensure "eventual consistency" without meetings.
[→ Details in P-001 -/COGNITIVE-CRDTS.md](P-001%20-/COGNITIVE-CRDTS.md)
=======
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-3.0-green.svg)](CHANGELOG.md)
[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)](tools/zc-calculator/zc_cli.py)

**Stop drowning in Slack. Start shipping again.**

When your team generates ideas faster than it can process them, standard consensus breaks down. CIM Pattern gives you three operational modes and tells you exactly when to switch between them.

---

## The Problem (60 seconds)

Your team uses Claude, Cursor, Notion, and Slack. You're shipping code and ideas at machine speed, but you're still making decisions at human speed.

**The result:**
- 40+ unread Slack channels
- Meetings that end with more questions than answers
- Decision paralysis disguised as "async-first culture"
- Burnout from cognitive overload

**The math:**

```
Zc = V_generation / B_social

Green Zone (Zc < 0.7): Async works
Yellow Zone (Zc 0.7-1.0): Schedule GUSH session
Red Zone (Zc ≥ 1.0): Activate The Jam
```

CIM Pattern is the **circuit breaker** for cognitive overload.

---

## Quick Start (5 minutes)

### 1. Calculate Your Zc

**Option A: Web Calculator**
```bash
# Open in browser
open tools/calculators/web/index.html
```

**Option B: Command Line**
```bash
python tools/calculators/cli/zc_cli.py --interactive
```

**Option C: From Metrics**
```bash
python tools/calculators/cli/zc_cli.py \
  --slack 150 \
  --notion 20 \
  --ai 30 \
  --emails 40 \
  --team-size 10
```

### 2. Choose Your Mode

| Zc Range | Mode | What To Do |
|----------|------|------------|
| < 0.7 | 🟢 **Study Hall** | Keep async. You're good. |
| 0.7-1.0 | 🟡 **GUSH** | [Schedule forced convergence](tools/templates/GUSH-SESSION-TEMPLATE.md) within 48h |
| ≥ 1.0 | 🔴 **The Jam** | [Declare BHO forks](tools/templates/BHO-FORK-TEMPLATE.md) + activate BLUES rhythm |

### 3. Run Your First Session

- **GUSH (60-90 min):** Use [this template](tools/templates/GUSH-SESSION-TEMPLATE.md)
- **BHO Fork:** Use [this template](tools/templates/BHO-FORK-TEMPLATE.md)
- **Slack Integration:** [Setup guide](tools/templates/slack_notifier.py)
>>>>>>> eb3b51d (Prepare V3 – production nearly ready)

---

## Validation & Metrics

<<<<<<< HEAD
1. **Calculate Baseline:** Use the [analog method](P-001%20-/OPERATIONAL-MANUAL.md#11-calculate-your-baseline-zc-the-analog-method).
2. **Kickoff:** Use the [30-minute agenda](P-001%20-/OPERATIONAL-MANUAL.md#15-the-kickoff-meeting-30-minutes).
3. **Onboarding Checklist:** See the full [Adoption Checklist](#42-adoption-checklist) below.

---

## 5. ORIGINS & THEORY
Based on **Peeragogy**, **Active Inference**, and **Stigmergy**. 
[See P-001 -/MATHEMATICAL-APPENDIX.md](P-001%20-/MATHEMATICAL-APPENDIX.md) for formal proofs.

---

## 6. METRICS AND VALIDATION
Pilot results (N=12 teams, 2025):
* Decision latency: **-34%**
* Overwhelm signals: **-42%**
* Meeting hours: **-38%**

---

## 7. THE CURATOR'S NOTE
This workspace is a **Garage**. It smells of engine oil and raw code. We built this because "Corporate Politeness" was killing our ability to think.

If you are a **Naufrago Digitale**, welcome home. Grab a wrench.

**Fabry** *The Curator*

---

## 📂 Repository Index
* [Operational Manual](P-001%20-/OPERATIONAL-MANUAL.md)
* [Mathematical Appendix](P-001%20-/MATHEMATICAL-APPENDIX.md)
* [Cognitive CRDTs](P-001%20-/COGNITIVE-CRDTS.md)
* [Examples](P-001%20-/EXAMPLES.md)
* [FAQ](P-001%20-/FAQ.md)
* [Contributors Guide](CONTRIBUTORS.md)


=======
**Pilot results** (12 teams, 90 days, 2025):
- Decision latency: **-34%**
- Meeting hours: **-38%**
- Reported overwhelm: **-42%**
- Team satisfaction: **+28%**

**How we measure:**
- Zc tracking via automated metrics
- Pre/post surveys (SUS, NASA-TLX)
- Calendar analysis
- Qualitative team feedback

[See full methodology →](docs/VALIDATION.md)

---

## Documentation

### For Users
- **[Quick Start Guide](docs/user/QUICKSTART.md)** - Get running in 15 minutes
- **[Installation](docs/user/installation.md)** - Setup & deployment
- **[FAQ](docs/FAQ.md)** - Common questions

### For Developers
- **[Project Structure](PROJECT-STRUCTURE.md)** - 📋 **Start here!** Complete directory layout
- **[Architecture](docs/ARCHITECTURE.md)** - System design & rationale
- **[Contributing](CONTRIBUTING.md)** - How to contribute
- **[Session Continuity](SESSION-CONTINUITY.md)** - Multi-session development guide

### Theory & Research
- **[Vision](VISION.md)** - 🌟 The big picture, manifesto, philosophy
- **[Mathematical Foundation](core/theory/MATHEMATICAL-APPENDIX.md)** - Formal proofs
- **[Cognitive CRDTs](core/theory/COGNITIVE-CRDTS.md)** - Distributed consensus for humans
- **[Protocol Core](core/manifesto/PROTOCOL-001-CORE.md)** - Original conceptual framework

### Project Management
- **[Roadmap](ROADMAP.md)** - What's next (2026-2028)
- **[Milestone Status](MILESTONE-STATUS.md)** - Current progress tracker
- **[Changelog](CHANGELOG.md)** - Version history

---

## Installation

### Web Calculator (Zero Dependencies)
```bash
git clone https://github.com/pyragogy/protocols.git
cd protocols/tools/zc-calculator
open index.html  # or: python -m http.server 8000
```

### CLI Tool
```bash
# Python 3.8+ required, no external dependencies
python tools/zc-calculator/zc_cli.py --help
```

### Slack Integration
```bash
# Set up webhook
export SLACK_WEBHOOK_URL="https://hooks.slack.com/services/YOUR/WEBHOOK/URL"

# Send notification
python tools/templates/slack_notifier.py --mode GUSH --zc 0.85
```

---

## Integrations & Tooling

### Current (v3.0)
- ✅ **Zc Calculator** - Web + CLI
- ✅ **Slack Notifications** - Webhook-based
- ✅ **Templates** - GUSH, BHO, BLUES

### Coming Soon (v3.1+)
- 🔄 **Curator AI** - Automated Zc monitoring via Claude API
- 🔄 **Notion Plugin** - Native Zc tracking in databases
- 🔄 **Linear Integration** - Mode switching in project views
- 🔄 **Discord Bot** - Real-time mode recommendations

[See roadmap →](ROADMAP.md)

---

## Why CIM Pattern?

### Vs. Agile/Scrum
- **Agile:** Optimized for *predictable* work cycles
- **CIM:** Optimized for *variable* cognitive load in AI-augmented teams

### Vs. "Async-First" Culture
- **Async-first:** Static cultural default
- **CIM:** Dynamic mode switching based on measured Zc

### Vs. "More Meetings"
- **More meetings:** Assumes sync is always the answer
- **CIM:** Sync only when Zc indicates overload

**In other words:** CIM is the **cognitive operating system** for teams using AI tools in 2026+.

---

## Real-World Examples

### Example 1: Startup (8 people, remote)
- **Before:** Zc = 1.8, 12h/week in "alignment meetings"
- **After:** Zc = 0.6, 4h/week in GUSH sessions, BHO forks for deep work
- **Result:** Shipped 2 major features in 6 weeks (previously stalled for 3 months)

### Example 2: Open Source Project (25 contributors)
- **Before:** GitHub PRs with 40+ comments, no decisions
- **After:** GUSH sessions for contentious RFCs, BHO forks for prototypes
- **Result:** RFC-to-merge time cut from 45 to 12 days

### Example 3: Enterprise Team (50 people, hybrid)
- **Before:** Email chains with 100+ replies, decision fatigue
- **After:** Weekly Zc monitoring, automatic GUSH scheduling
- **Result:** Strategic decisions made in days instead of weeks

[More case studies →](examples/)

---

## Contributing

We're building this in the open. Contributions welcome:

- 🐛 **Bug reports** - [Open an issue](https://github.com/pyragogy/protocols/issues)
- 💡 **Feature requests** - [Discussions](https://github.com/pyragogy/protocols/discussions)
- 🔧 **Code contributions** - [See CONTRIBUTING.md](CONTRIBUTING.md)
- 📖 **Documentation** - Corrections, examples, translations
- 🧪 **Pilot teams** - Try it and share results

**Current focus areas:**
- Curator AI implementation
- More language bindings (JavaScript, Go, Rust)
- Integration plugins (Notion, Linear, Discord)
- Academic validation studies

---

## License & Attribution

**License:** MIT - Use this however you want

**Citation (if you use this in research):**
```bibtex
@misc{terzi2026cim,
  author = {Terzi, Fabrizio},
  title = {CIM Pattern: Cognitive Impedance Mismatch and Dynamic Mode Switching},
  year = {2026},
  url = {https://github.com/pyragogy/protocols},
  note = {Version 3.0}
}
```

**Built on:**
- **Peeragogy** - Collaborative learning frameworks
- **Active Inference** (Karl Friston) - Predictive processing
- **Stigmergy** (Francis Heylighen) - Indirect coordination
- **CRDTs** - Conflict-free replicated data types

---

## Support & Community

- 💬 **Discord** - [Join the conversation](https://discord.gg/pyragogy) *(coming soon)*
- 🐦 **Twitter** - [@pyragogy](https://twitter.com/pyragogy) *(coming soon)*
- 📧 **Email** - protocols@pyragogy.org
- 📝 **Blog** - [pyragogy.org/blog](https://pyragogy.org/blog) *(coming soon)*

**Weekly Office Hours:** Every Friday 3-4pm UTC - [Calendar link] *(coming soon)*

---

## Frequently Asked Questions

**Q: Is this just "Agile for AI teams"?**  
A: No. Agile assumes predictable sprint cycles. CIM Pattern adapts dynamically to measured cognitive load.

**Q: Do I need to track Zc constantly?**  
A: No. Check weekly, or when the team feels overwhelmed. It's a diagnostic tool, not a micromanagement system.

**Q: What if my team rejects GUSH sessions?**  
A: GUSH is forced convergence—it's supposed to feel uncomfortable. But if resistance is high, you might have cultural pre-requisites to address first.

**Q: Can this work for enterprise (100+ people)?**  
A: Partially. CIM works best for teams of 8-25. Larger orgs need to break into smaller units.

**Q: Where's the AI Curator?**  
A: Coming in v3.1. For now, use the CLI calculator and manual Slack notifications.

[See full FAQ →](docs/FAQ.md)

---

## Version History

- **v3.0** (Feb 2026) - Production-ready tools, templates, documentation rewrite
- **v2.0** (Jan 2026) - Mathematical formalization, pilot validation
- **v1.0** (Dec 2025) - Initial conceptual framework

[Full changelog →](CHANGELOG.md)

---

## What's Next?

**This month:**
- [ ] Curator AI alpha release
- [ ] Notion plugin beta
- [ ] 5 new case studies

**This quarter:**
- [ ] Academic paper submission
- [ ] Linear/Asana integrations
- [ ] Community governance model

[See roadmap →](ROADMAP.md)

---

## Credits

**Created by:** Fabrizio Terzi ([@BergamoHub](https://github.com/BergamoHub))  
**Contributors:** [See CONTRIBUTORS.md](CONTRIBUTORS.md)

**Special thanks to:**
- Teams who piloted v1 and v2
- Claude (Anthropic) for making this README possible
- Everyone who told us v2 was "too abstract"—you were right

---

<div align="center">

**Stop drowning in information. Start shipping again.**

[Get Started](docs/QUICKSTART.md) • [Read the Docs](docs/) • [Join Discord](#) • [Contribute](CONTRIBUTING.md)

</div>
>>>>>>> eb3b51d (Prepare V3 – production nearly ready)
