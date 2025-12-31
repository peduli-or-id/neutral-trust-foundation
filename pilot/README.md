# Pilot Testbed – Network Behavior Oracle & Silent Validator

This pilot demonstrates the **conceptual operation** of the Network Behavior Oracle (NBO)
and Silent Validator using **synthetic behavior indicators only**.

No live traffic, signaling stacks, or subscriber data are involved.

---

## Objectives

- Demonstrate neutral trust validation
- Validate architecture assumptions
- Support regulator and operator walkthroughs
- Provide reproducible simulation environment

---

## Pilot Variants

Two deployment variants are provided:

1. **Pre-built Image Mode**
   - Fastest
   - Git clone + docker-compose up
   - Suitable for demos and workshops

2. **Source-Build Mode**
   - Full transparency
   - Compile from source
   - Suitable for audits and research

---

## Compliance Statement

This pilot:
- Does not inspect packets
- Does not generate traffic
- Does not interact with telco protocols
- Processes only synthetic data

## 🧩 Common Architecture (Both Versions)
```text
┌───────────────────────────┐
│ synthetic-indicator-gen   │
│ - dummy metrics           │
│ - random / deterministic  │
└────────────┬──────────────┘
             │
┌────────────▼──────────────┐
│ nbo-engine                │
│ - normalization           │
│ - behavior vector         │
│ - assertion generation    │
└────────────┬──────────────┘
             │
┌────────────▼──────────────┐
│ silent-validator          │
│ - consensus simulation    │
│ - anchoring               │
│ - trust reference         │
└───────────────────────────┘
```

## 🟢 VERSION 1
Pre-built Image (Git Clone & Run)
📁 Directory
```text
pilot/
 ├── docker-compose.prebuilt.yml
 └── .env

```
## How To Run
```text
git clone https://github.com/peduli-or-id/neutral-trust-foundation
cd neutral-trust-foundation/pilot
docker compose -f docker-compose.prebuilt.yml up
```
- No build
- No compile
- Demo-ready


## 🔵 VERSION 2
Source-Build (Compile from GitHub)
📁 Directory
```text
pilot/
 ├── docker-compose.source.yml
 ├── indicator-generator/
 │    ├── Dockerfile
 │    └── src/
 ├── nbo-engine/
 │    ├── Dockerfile
 │    └── src/
 └── silent-validator/
      ├── Dockerfile
      └── src/
```


