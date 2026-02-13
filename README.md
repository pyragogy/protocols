# The CIM Pattern
## Cognitive Impedance Mismatch & Dynamic Mode Switching in Hybrid Teams

**Created by:** Fabrizio Terzi (@BergamoHub)  
**Version:** 2.0 – February 2026  
**License:** MIT – Open Source Cognitive Infrastructure

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

---

## 4. GETTING STARTED

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


