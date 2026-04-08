# OpenStartupLab 🚀

## Overview

OpenStartupLab is a **multi-agent, real-world simulation environment** where an AI agent autonomously manages a startup’s operations.

It simulates:

* Customer support systems
* Engineering workflows (PR reviews)
* Task prioritization
* Business metrics (revenue, users, satisfaction)
* Dynamic real-world events (crashes, growth spikes)

---

## Why This Matters

This environment models **real operational complexity**, not toy problems.

It evaluates:

* Long-horizon reasoning
* Multi-objective optimization
* Memory-aware decision making
* Tool usage and delegation

---

## Features

* Multi-agent system (CEO, Engineer, Support)
* Long-term + short-term memory
* Dynamic stochastic events
* Tool execution system
* Delayed reward shaping
* Deterministic reproducibility

---

## Tasks

### 1. Email Management (Easy)

Handle customer emails correctly.

### 2. Engineering Management (Medium)

Review PRs and prevent bugs/security issues.

### 3. Startup Survival (Hard)

Balance:

* Revenue growth
* User satisfaction
* Engineering quality

---

## Action Space

* reply_email
* approve_pr
* reject_pr
* schedule
* ignore

---

## Observation Space

* Emails
* PRs
* Tasks
* Metrics
* Memory

---

## Reward Design

Dense + delayed:

* Immediate rewards for good actions
* Penalties for ignored issues
* Long-term memory penalties
* Business performance rewards

---

## Setup

```bash
pip install -r requirements.txt
python inference.py
```

---

## Docker

```bash
docker build -t osl .
docker run osl
```

---

## Baseline Performance

Deterministic baseline produces reproducible reward scores across runs.

---

## Deployment

Deployable on Hugging Face Spaces with Docker support.

---

## Novelty

Unlike existing environments, this combines:

* Multi-agent simulation
* Real business dynamics
* Memory + delayed rewards

This makes it a **mini AGI operations benchmark**.
