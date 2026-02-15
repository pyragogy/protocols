# 🚀 CIM PATTERN v3.0 - START HERE

**Repository completa, production-ready, organizzata.**

---

## ⚡ QUICK START (5 minuti)

```bash
# 1. Setup automatico
chmod +x scripts/setup.sh && ./scripts/setup.sh

# 2. Configura API keys
nano .env  # Aggiungi ANTHROPIC_API_KEY

# 3. Avvia tutto
chmod +x scripts/run.sh && ./scripts/run.sh
```

✅ Dashboard: http://localhost:3000  
✅ API: http://localhost:8000/docs

---

## 📁 STRUTTURA REPOSITORY

```
cim-pattern/
├── 📖 START-HERE.md          ← SEI QUI
├── 📋 PROJECT-STRUCTURE.md   ← Dettagli organizzazione
├── 🌟 VISION.md              ← Manifesto e filosofia
├── 📊 MILESTONE-STATUS.md    ← Progressi
│
├── core/                     🧠 Teoria & Fondamenti
│   ├── theory/               Matematica, CRDTs
│   └── manifesto/            Framework concettuale
│
├── tools/                    🛠️ Strumenti Production
│   ├── curator-ai/           ✅ Monitor + AI Recommender
│   ├── integrations/         ✅ Slack, Discord bots
│   ├── dashboard/            ✅ React + FastAPI
│   ├── calculators/          ✅ Web + CLI
│   └── templates/            ✅ GUSH, BHO
│
├── docs/                     📖 Documentazione
│   ├── user/                 Quick Start, Installation
│   └── developer/            API, Architecture
│
├── tests/                    🧪 Test Suite
│   └── unit/                 Pytest tests
│
└── scripts/                  🚀 Automazione
    ├── setup.sh              Setup completo
    ├── run.sh                Avvia tutto
    └── deploy.sh             Deploy produzione
```

---

## 🎯 COSA PUOI FARE

### 1️⃣ Monitorare Cognitive Load
```bash
python tools/curator-ai/monitor.py
```

### 2️⃣ Dashboard Real-Time
```bash
./scripts/run.sh
# Visita http://localhost:3000
```

### 3️⃣ Bot Slack/Discord
```bash
# Slack
export SLACK_BOT_TOKEN="xoxb-..."
python tools/integrations/slack/bot.py

# Discord
export DISCORD_BOT_TOKEN="..."
python tools/integrations/discord/bot.py
```

### 4️⃣ Calcolare Zc
```bash
# Web
open tools/calculators/web/index.html

# CLI
python tools/calculators/cli/zc_cli.py --interactive
```

---

## 📚 DOCUMENTAZIONE

**Inizia da qui:**
1. `docs/user/QUICKSTART.md` - 15 min onboarding
2. `VISION.md` - Capire il "perché"
3. `docs/developer/ARCHITECTURE.md` - Come funziona

**API:**
- `docs/developer/API-REFERENCE.md` - Tutti gli endpoint
- http://localhost:8000/docs - Swagger live

**Theory:**
- `core/theory/MATHEMATICAL-APPENDIX.md`
- `core/manifesto/PROTOCOL-001-CORE.md`

---

## 🔧 TECNOLOGIE

**Backend:** Python, FastAPI, Anthropic Claude API  
**Frontend:** React, Recharts  
**Bots:** Slack SDK, Discord.py  
**Tests:** Pytest  
**Deploy:** Docker, Docker Compose

---

## ✅ CHECKLIST PRIMO UTILIZZO

- [ ] Run `./scripts/setup.sh`
- [ ] Configura `.env` con API keys
- [ ] Test: `python tools/curator-ai/monitor.py`
- [ ] Avvia dashboard: `./scripts/run.sh`
- [ ] Calcola primo Zc
- [ ] Leggi `docs/user/QUICKSTART.md`

---

## 🆘 TROUBLESHOOTING

**"Module not found"**
→ `pip install -r requirements.txt`

**"Connection refused" nel dashboard**
→ Backend deve essere running su porta 8000

**"API key not set"**
→ Configura `.env` con `ANTHROPIC_API_KEY`

**Frontend non parte**
→ `cd tools/dashboard/frontend && npm install`

---

## 🚀 DEPLOY PRODUZIONE

```bash
# Docker Compose (raccomandato)
docker-compose up -d

# Manuale
./scripts/deploy.sh
```

---

## 📞 SUPPORTO

- GitHub: https://github.com/pyragory/protocols
- Issues: https://github.com/pyragory/protocols/issues
- Docs: Leggi `PROJECT-STRUCTURE.md`

---

## 🎊 COMPLETATO

**Milestone 1:** ✅ Foundation  
**Milestone 2:** ✅ Curator AI  
**Milestone 3:** 🔄 Integrations (Next)

**File totali:** 50+  
**Codice:** ~3,000 linee  
**Docs:** ~20,000 parole  
**Tests:** Unit suite completa

---

**Inizia da `./scripts/setup.sh` e sei operativo in 5 minuti! 🚀**
