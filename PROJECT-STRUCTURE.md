# CIM Pattern - Project Structure

**Version:** 3.0  
**Last Updated:** February 14, 2026

This document explains the complete project organization, designed for clarity and scalability across multiple development milestones.

---

## Directory Structure

```
cim-pattern/
│
├── README.md                 # Main entry point (practical, concise)
├── VISION.md                 # The big picture, manifesto, philosophy
├── CHANGELOG.md              # Version history
├── CONTRIBUTING.md           # How to contribute
├── ROADMAP.md                # Future plans
├── LICENSE                   # MIT License
│
├── core/                     # 🧠 FOUNDATIONAL THEORY & VISION
│   ├── theory/               # Academic foundation
│   │   ├── MATHEMATICAL-APPENDIX.md    # Formal proofs, equations
│   │   ├── COGNITIVE-CRDTS.md          # Distributed consensus theory
│   │   └── ACTIVE-INFERENCE.md         # Friston integration
│   │
│   └── manifesto/            # Vision & philosophy
│       ├── PROTOCOL-001-CORE.md        # Original conceptual framework
│       └── WHY-CIM-PATTERN.md          # Problem statement, motivation
│
├── tools/                    # 🛠️ PRODUCTION-READY TOOLS
│   ├── calculators/          # Zc calculation tools
│   │   ├── web/
│   │   │   ├── index.html              # Web calculator
│   │   │   ├── style.css
│   │   │   └── calculator.js
│   │   ├── cli/
│   │   │   ├── zc_cli.py               # Command-line tool
│   │   │   └── README.md
│   │   └── api/                        # (Milestone 2)
│   │       └── zc_api.py
│   │
│   ├── integrations/         # Platform integrations
│   │   ├── slack/
│   │   │   ├── bot.py                  # (Milestone 2)
│   │   │   └── webhook.py
│   │   ├── notion/                     # (Milestone 3)
│   │   ├── linear/                     # (Milestone 3)
│   │   └── discord/                    # (Milestone 2)
│   │
│   ├── curator-ai/           # AI monitoring system
│   │   ├── monitor.py                  # (Milestone 2)
│   │   ├── recommender.py
│   │   └── config.yaml
│   │
│   ├── dashboard/            # Metrics visualization
│   │   ├── frontend/                   # (Milestone 2)
│   │   │   ├── src/
│   │   │   └── package.json
│   │   └── backend/
│   │       └── api.py
│   │
│   └── templates/            # Ready-to-use templates
│       ├── GUSH-SESSION.md
│       ├── BHO-FORK.md
│       ├── BLUES-PULSE.md
│       └── notion/
│           └── database-template.json
│
├── docs/                     # 📖 DOCUMENTATION
│   ├── user/                 # For end users
│   │   ├── QUICKSTART.md               # 15-min onboarding
│   │   ├── INSTALLATION.md             # Setup guide
│   │   ├── MODE-REFERENCE.md           # Study Hall, GUSH, The Jam
│   │   ├── FAQ.md
│   │   └── TROUBLESHOOTING.md
│   │
│   ├── developer/            # For contributors
│   │   ├── ARCHITECTURE.md
│   │   ├── API-REFERENCE.md
│   │   ├── TESTING.md
│   │   └── DEPLOYMENT.md
│   │
│   └── research/             # Academic & validation
│       ├── VALIDATION-METHODOLOGY.md
│       ├── PILOT-RESULTS.md
│       └── RELATED-WORK.md
│
├── examples/                 # 💡 REAL-WORLD USAGE
│   ├── case-studies/
│   │   ├── startup-8-people.md
│   │   ├── open-source-25.md
│   │   └── enterprise-50.md
│   │
│   └── calculations/
│       ├── ZC-CALCULATIONS.md          # 7 scenarios
│       └── sample-metrics.json
│
├── tests/                    # 🧪 TEST SUITE
│   ├── unit/
│   │   ├── test_zc_calculation.py
│   │   └── test_mode_detection.py
│   ├── integration/
│   │   └── test_slack_integration.py
│   └── e2e/
│       └── test_full_workflow.py
│
├── scripts/                  # 🚀 AUTOMATION
│   ├── deploy.sh                       # Quick deployment
│   ├── setup-dev.sh                    # Dev environment
│   ├── run-tests.sh
│   └── generate-docs.sh
│
└── .github/                  # 🤖 CI/CD & COMMUNITY
    ├── workflows/
    │   ├── tests.yml
    │   └── deploy.yml
    ├── ISSUE_TEMPLATE/
    │   ├── bug_report.md
    │   └── feature_request.md
    └── PULL_REQUEST_TEMPLATE.md
```

---

## Design Principles

### 1. **Separation of Concerns**

**Theory ≠ Tools ≠ Docs**

- `core/` = Timeless concepts (rarely changes)
- `tools/` = Implementation (evolves rapidly)
- `docs/` = User guidance (updated frequently)

### 2. **Progressive Disclosure**

**README → QUICKSTART → Deep Dive**

Users see complexity only when needed:
1. README: 5-min overview
2. QUICKSTART: 15-min practical guide
3. Theory docs: For those who want to understand deeply

### 3. **Milestone-Friendly**

Each directory can grow independently:

- **Milestone 1** (Current): `tools/calculators/`, `tools/templates/`, `docs/user/`
- **Milestone 2** (Next): `tools/curator-ai/`, `tools/dashboard/`, `tools/integrations/slack/`
- **Milestone 3**: `tools/integrations/notion/`, `tools/integrations/linear/`

### 4. **Academic Rigor + Practical Value**

- **Vision** in `core/manifesto/` (for believers)
- **Math** in `core/theory/` (for researchers)
- **Tools** in `tools/` (for practitioners)

All three coexist without conflict.

---

## File Organization Rules

### Naming Conventions

**Markdown files:**
- `UPPERCASE-WITH-DASHES.md` for important docs (README, CHANGELOG)
- `lowercase-with-dashes.md` for regular docs (installation, troubleshooting)
- `PascalCase.md` for case studies (StartupCaseStudy.md)

**Code files:**
- `snake_case.py` for Python
- `kebab-case.js` for JavaScript
- `PascalCase.tsx` for React components

### File Placement Logic

**"Where does this file go?"**

| Content Type | Location | Example |
|--------------|----------|---------|
| Mathematical proof | `core/theory/` | `MATHEMATICAL-APPENDIX.md` |
| Philosophical essay | `core/manifesto/` | `WHY-CIM-PATTERN.md` |
| Working tool | `tools/*/` | `zc_cli.py` |
| User guide | `docs/user/` | `QUICKSTART.md` |
| Developer doc | `docs/developer/` | `API-REFERENCE.md` |
| Research finding | `docs/research/` | `PILOT-RESULTS.md` |
| Real team story | `examples/case-studies/` | `startup-8-people.md` |
| Deployment script | `scripts/` | `deploy.sh` |
| Test | `tests/*/` | `test_zc_calculation.py` |

---

## Milestone Progression

### Milestone 1 (Current) - Foundation
**Status:** ✅ Complete

Populated directories:
- `tools/calculators/`
- `tools/templates/`
- `docs/user/`
- `examples/calculations/`
- `scripts/`

### Milestone 2 - Automation
**Status:** 🔄 Next

Will populate:
- `tools/curator-ai/`
- `tools/dashboard/`
- `tools/integrations/slack/`
- `tools/integrations/discord/`
- `tests/unit/`

### Milestone 3 - Integration
**Status:** ⏳ Planned

Will populate:
- `tools/integrations/notion/`
- `tools/integrations/linear/`
- `tools/api/`
- `tests/integration/`
- `.github/workflows/`

### Milestone 4 - Validation
**Status:** ⏳ Planned

Will populate:
- `docs/research/`
- `examples/case-studies/` (3+ detailed studies)
- `tests/e2e/`

---

## Navigation Guide

### "I want to..."

**...understand the big idea**
→ `VISION.md` → `core/manifesto/PROTOCOL-001-CORE.md`

**...use it right now**
→ `README.md` → `docs/user/QUICKSTART.md`

**...understand the math**
→ `core/theory/MATHEMATICAL-APPENDIX.md`

**...integrate with my tools**
→ `tools/integrations/[platform]/`

**...contribute code**
→ `CONTRIBUTING.md` → `docs/developer/`

**...see real examples**
→ `examples/case-studies/`

**...validate it works**
→ `docs/research/PILOT-RESULTS.md`

---

## Maintenance

### What Changes Frequently
- `tools/` - New features, bug fixes
- `docs/user/` - Updated guides
- `examples/` - New case studies
- `ROADMAP.md` - Adjusted plans

### What Changes Rarely
- `core/theory/` - Foundational math
- `core/manifesto/` - Core philosophy
- `LICENSE` - Legal terms

### What Never Changes
- `VISION.md` - The original "why"

---

## For Contributors

When adding files, ask:

1. **Is this theory or practice?**
   - Theory → `core/`
   - Practice → `tools/` or `docs/`

2. **Who is the audience?**
   - End users → `docs/user/`
   - Developers → `docs/developer/`
   - Researchers → `docs/research/` or `core/theory/`

3. **Is it conceptual or executable?**
   - Conceptual → `docs/` or `core/`
   - Executable → `tools/` or `scripts/`

4. **Is it documentation or example?**
   - Documentation → `docs/`
   - Example → `examples/`

When in doubt, open a discussion: https://github.com/pyragogy/protocols/discussions

---

## Version History

- **v3.0** (Feb 2026) - Introduced this structure
- **v2.0** (Jan 2026) - Flat structure with P-001 folder
- **v1.0** (Dec 2025) - Single README

---

**This structure is designed to grow with the project while maintaining clarity.**

Last updated: February 14, 2026
