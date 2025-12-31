# Reference Architecture
Neutral Trust Foundation (NTF)

Network Behavior Oracle & Silent Validator System

---

## Document Status

- Status: Reference Architecture / Pilot-Ready
- Scope: Cross-Domain, Neutral, Non-Operational
- Compliance: 3GPP-aligned, GDPR-compliant
- Audience: Operators, Regulators, Standards Bodies, Architects

---

## 1. Architectural Objective

This reference architecture defines how **Network Behavior Oracle (NBO)** and **Silent Validator** components are deployed, interconnected, and governed without:

- Accessing subscriber data
- Intercepting traffic
- Violating operator sovereignty
- Circumventing lawful intercept frameworks

The architecture exists **above protocol layers** and **outside enforcement paths**.

---

## 2. High-Level Architectural Principles

### 2.1 Separation of Concerns (3GPP-aligned)

| Plane | Status |
|---|---|
| User Plane (UP) | Untouched |
| Control Plane (CP) | Untouched |
| Management Plane (MP) | Read-only aggregation only |
| Trust Plane (NTF) | External, neutral |

### 2.2 GDPR Alignment

- Data minimization (Art. 5)
- Privacy by design (Art. 25)
- Security of processing (Art. 32)
- No personal data processing

---

## 3. Logical Architecture Overview

<img width="378" height="473" alt="referensi arsitektur" src="https://github.com/user-attachments/assets/a1a54521-f1ea-49e3-842e-3de439820e75" />



---

## 4. Component Breakdown

### 4.1 Local Metric Source (Operator Domain)

Examples:
- OSS counters
- KPI summaries
- Rate-based aggregates

**Constraints:**
- No raw logs
- No signaling traces
- No identifiers

---

### 4.2 Behavior Exporter (Operator-Controlled)

**Function:**
- Aggregate metrics
- Enforce schema
- Apply temporal windows

**Trust Boundary:**
- Fully controlled by operator
- No inbound control from NTF

---

### 4.3 Indicator Transport Layer

- Push-based or pull-based
- TLS encrypted
- Authenticated
- Rate-limited

No real-time dependency.

---

### 4.4 Network Behavior Oracle Engine (NTF)

**Responsibilities:**
- Normalize indicators
- Remove domain bias
- Construct behavior vectors
- Generate Network Behavior Assertions (NBA)

---

### 4.5 Silent Validator Layer

**Responsibilities:**
- Cross-domain consistency check
- Consensus participation
- Evidence anchoring
- Trust reference publication

---

## 5. Data Flow (Step-by-Step)

### Step 1 – Metric Aggregation (Local)

```text
Raw counters → Aggregated metrics (5–15 min window)
```

### Step 2 – Indicator Generation

```text
Aggregated metrics → Behavior Indicators
```
### Step 3 – Indicator Submission
```text
Indicators → Secure Transport → NTF
```

### Step 4 – Behavior Evaluation (NBO)
```text
Indicators → Behavior Vector → NBA
```
### Step 5 – Validation & Anchoring

```text
NBA → Silent Validator → Trust Reference
```

## 6. Trust Boundaries

| Boundary	| Control|
|---|---|
|Operator internal	| Operator|
|Exporter output	| Operator|
|Indicator stream	| Shared|
|NTF processing	| Neutral|
| Enforcement	|Operator only|


## 7. Sample Dummy Data (Safe & 3GPP-Aligned)

> All data below is synthetic, non-identifying, and non-operational.

### 7.1 Behavior Indicator (Registration Procedure)
```json
{
  "indicator_type": "access_procedure_behavior",
  "procedure_family": "registration",
  "aggregation_window": "300s",
  "baseline": "self-historical",
  "delta_ratio": 0.21,
  "confidence": 0.89
}
```
### 7.2 Control Plane Stability Indicator
```json
{
  "indicator_type": "control_plane_stability",
  "time_window": "600s",
  "stability_score": 0.74,
  "trend": "stable"
}

```
### 7.3 Cross-Domain Comparison Indicator

```json
{
  "indicator_type": "cross_domain_behavior_index",
  "domain_count": 4,
  "metric_family": "procedure_rate",
  "variance_index": 0.38
}
```

### 7.4 Network Behavior Assertion (NBA)

```json
{
  "assertion_type": "behavior_deviation_statement",
  "time_window": "UTC-2025-02-10T10:00",
  "behavior_class": "access_procedure",
  "deviation_level": "moderate",
  "confidence_score": 0.87
}
```

## 8. Deployment Modes
### 8.1 Simulation Mode
- Fully synthetic
- Docker-based
- No operator dependency

### 8.2 Pilot Mode
- Real aggregated metrics
- Synthetic anomaly injection
- Observer-only

### 8.3 Production Observer Mode
- Metrics export only
- No enforcement coupling
- Independent validation

## 9. Failure & Degradation Model

|Scenario	|Impact|
|---|---|
| Exporter failure	|Local only|
|NTF outage	|No operator impact|
|Validator failure	|Consensus degraded|
|Network incident|	No interference|


## 10. Audit & Transparency
Artifacts:
- Indicator schemas
- Hashes
- Consensus metadata
- Time proofs
No opaque logic.

## 11. Security Considerations
- No attack surface on user/control planes
- Minimal metadata exposure
- Immutable audit trail
- Zero trust between domains

## 12. Regulatory Narrative (Important)

This architecture:
- Does not intercept traffic
- Does not process personal data
- Does not bypass lawful intercept
- Does not centralize control
It provides evidence, not authority.

## 13. Evolution Path

- Pilot in Indonesia (multi-operator)
- Independent foundation governance
- Open standards discussion
- Possible 3GPP study item proposal


## Final Statement

This reference architecture demonstrates that trust can be built without surveillance.
It enables:
- Shared understanding
- Objective evidence
- Neutral collaboration

Without:
- Interception
- Central control
- Privacy erosion

