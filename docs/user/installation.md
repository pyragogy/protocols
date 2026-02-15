# Installation & Deployment Guide

This guide explains how to deploy CIM Pattern v3.0 to your repository.

---

## Quick Deploy (5 minutes)

If you want to **replace** your current repository completely:

### Step 1: Extract Files

```bash
# Unzip the bundle (if received as ZIP)
unzip cim-pattern-v3.0.zip

# Or, if you have the directory
cd protocols-v3
```

### Step 2: Deploy to GitHub

**Option A: New Repository**

```bash
# Initialize git
git init
git add .
git commit -m "v3.0: Production-ready foundation"

# Create repo on GitHub, then:
git remote add origin git@github.com:YOUR_USERNAME/protocols.git
git branch -M main
git push -u origin main
```

**Option B: Update Existing Repository**

```bash
# CAUTION: This will replace your current main branch
cd /path/to/your/current/protocols/repo

# Create backup branch
git checkout -b backup-v2
git push origin backup-v2

# Replace with v3.0
git checkout main
rm -rf *  # Clear everything
cp -r /path/to/protocols-v3/* .  # Copy new files
git add .
git commit -m "v3.0: Complete rewrite - production ready"
git push origin main --force
```

---

## Careful Merge (10 minutes)

If you want to **preserve** some files from your current repository:

### Step 1: Prepare v3.0

```bash
cd protocols-v3
git init
git add .
git commit -m "v3.0: Production-ready foundation"
```

### Step 2: Merge with Existing

```bash
cd /path/to/your/current/protocols/repo

# Add v3.0 as remote
git remote add v3 /path/to/protocols-v3
git fetch v3

# Create merge branch
git checkout -b merge-v3

# Merge (will have conflicts)
git merge v3/main --allow-unrelated-histories
```

### Step 3: Resolve Conflicts

Keep from v3.0:
- `README.md` (completely rewritten)
- `tools/` (new calculator and templates)
- `docs/QUICKSTART.md` (new)
- `CHANGELOG.md` (updated)

Keep from v2.0 (if you want):
- `P-001 -/MATHEMATICAL-APPENDIX.md`
- `P-001 -/COGNITIVE-CRDTS.md`
- Any custom modifications you made

### Step 4: Finalize

```bash
# After resolving conflicts
git add .
git commit -m "Merge v3.0 with v2.0 - keep best of both"
git checkout main
git merge merge-v3
git push origin main
```

---

## File Structure Comparison

### Old (v2.0)
```
protocols/
├── README.md
├── P-001 -/
│   ├── OPERATIONAL-MANUAL.md
│   ├── MATHEMATICAL-APPENDIX.md
│   ├── COGNITIVE-CRDTS.md
│   └── code/
│       ├── pyragogy_engine.py (skeleton)
│       ├── metrics_dashboard.py (empty)
│       └── crdt_prototype.py (empty)
└── [other docs]
```

### New (v3.0)
```
protocols-v3/
├── README.md (completely rewritten)
├── CHANGELOG.md
├── CONTRIBUTING.md
├── ROADMAP.md
├── tools/
│   ├── zc-calculator/
│   │   ├── index.html (web app, working)
│   │   └── zc_cli.py (CLI, working)
│   └── templates/
│       ├── GUSH-SESSION-TEMPLATE.md
│       ├── BHO-FORK-TEMPLATE.md
│       └── slack_notifier.py (working)
├── docs/
│   └── QUICKSTART.md
├── examples/
│   └── ZC-CALCULATIONS.md
└── scripts/
    └── deploy.sh
```

---

## What Changed from v2.0 to v3.0

### Added ✅
- Working Zc calculator (web + CLI)
- Slack integration
- Ready-to-use templates
- Quick start guide
- Real-world examples
- Deployment scripts

### Changed 📝
- README: From manifesto to operational
- Structure: Organized into tools/, docs/, examples/
- Focus: From theory to practice

### Removed ❌
- Empty skeleton files
- Redundant docs (consolidated)
- Overly academic language

---

## Testing Your Installation

After deploying, verify everything works:

### Test 1: Web Calculator

```bash
cd tools/zc-calculator
open index.html  # Or: python -m http.server 8000
```

Should see: Working Zc calculator with examples

### Test 2: CLI Calculator

```bash
python tools/zc-calculator/zc_cli.py --vgen 50 --bsocial 30
```

Should see: Zc calculation with colored output

### Test 3: Slack Integration

```bash
export SLACK_WEBHOOK_URL="your_webhook_url"
python tools/templates/slack_notifier.py --mode GUSH --zc 0.85
```

Should see: "✓ Slack notification sent successfully"

---

## Troubleshooting

### Issue: "No such file or directory"

**Cause:** Running scripts from wrong directory

**Fix:**
```bash
# Always run from project root
cd protocols-v3
python tools/zc-calculator/zc_cli.py --help
```

### Issue: "Permission denied" on deploy.sh

**Fix:**
```bash
chmod +x scripts/deploy.sh
./scripts/deploy.sh
```

### Issue: Git merge conflicts

**Fix:**
```bash
# Accept v3.0 version for most files
git checkout --theirs README.md tools/ docs/

# Then manually review
git status
```

---

## Customization

After installation, you may want to:

### Update README.md

Edit these sections:
- Links (Discord, Twitter - currently "coming soon")
- Team size (currently shows your actual team)
- Pilot results (add your own when available)

### Customize Templates

Edit `tools/templates/*.md` to match your:
- Company culture
- Time zones
- Tool preferences
- Decision-making style

### Add Integrations

Create new files in `tools/templates/`:
- `discord_notifier.py`
- `notion_integration.py`
- `linear_plugin.py`

---

## Migration from v2.0

If you had teams using v2.0:

1. **Communicate change:**
   ```
   Subject: CIM Pattern v3.0 - New Tools Available
   
   We're upgrading to v3.0 with production-ready tools.
   
   New features:
   - Zc Calculator (no more manual math!)
   - Slack integration
   - Better templates
   
   Quick start: [link to QUICKSTART.md]
   ```

2. **Preserve v2.0 docs** (if needed):
   ```bash
   mkdir docs/v2-archive
   mv P-001\ -/* docs/v2-archive/
   ```

3. **Run pilot:**
   - Pick 1-2 teams
   - Use new tools for 2 weeks
   - Collect feedback
   - Roll out to everyone

---

## Next Steps

After successful installation:

1. **Read Quick Start:** `docs/QUICKSTART.md`
2. **Calculate your Zc:** `tools/zc-calculator/`
3. **Run first GUSH:** `tools/templates/GUSH-SESSION-TEMPLATE.md`
4. **Join community:** (Discord link when ready)

---

## Getting Help

- **Issues:** https://github.com/pyragogy/protocols/issues
- **Discussions:** https://github.com/pyragogy/protocols/discussions
- **Email:** protocols@pyragogy.org

---

**Ready to ship! 🚀**

[← Back to README](README.md)
