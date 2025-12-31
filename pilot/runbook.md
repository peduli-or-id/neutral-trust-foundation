# Pilot Runbook – How-To Demo
Neutral Trust Foundation (NTF)

Network Behavior Oracle & Silent Validator

---

## Document Status

- Status: Pilot Runbook (Simulation-Based)
- Scope: Demonstration & Validation
- Compliance: 3GPP-aligned, GDPR-compliant
- Audience: Operators, Regulators, Auditors, Engineers

---

## 1. Purpose of This Runbook

This runbook documents **how the NTF pilot is executed**, step by step,
using **synthetic behavior indicators only**.

The document is written as:
- A **how-to guide**
- A **simulated execution log**
- A **post-run analysis reference**

No real network, traffic, or subscriber data is involved.

---

## 2. Pre-Execution Checklist

Before running the pilot, verify:

- Repository cloned successfully
- Docker & Docker Compose installed
- No operator network connectivity required
- `.env` file present in `pilot/`

### Directory Confirmation
```text
pilot/
├── .env
├── docker-compose.prebuilt.yml
├── docker-compose.source.yml
├── scenario-library.md
├── indicator-generator/
├── nbo-engine/
└── silent-validator/
```


## 3. Execution Modes

Two execution modes are supported:

| Mode | Purpose |
|---|---|
| Pre-built Image | Fast demo, workshops |
| Source Build | Audit, research, transparency |

This runbook documents **both**, using the same logical flow.


## 4. Pilot Execution – Pre-Built Image Mode

### 4.1 Start Pilot Environment

```bash
cd pilot
docker compose -f docker-compose.prebuilt.yml up
```

Expected Result:
- Three containers start
- No exposed ports
- No external connectivity required

### 4.2 Container Startup Log (Simulated)
```csharp
[indicator-generator] MODE=synthetic
[indicator-generator] Profile=3gpp-aligned
[nbo-engine] Evaluation model: baseline-statistical
[silent-validator] Consensus model: simple-majority
```

## 5. Runtime Behavior Simulation
### 5.1 Indicator Generation Phase

The indicator generator emits **synthetic behavior indicators** at randomized intervals.

Sample Output (STDOUT):
```json
{
  "indicator_type": "control_plane_stability",
  "aggregation_window": "300s",
  "stability_score": 0.91,
  "confidence": "synthetic"
}
```

Interpretation:
- No identifiers
- No signaling
Represents abstract stability behavior

### 5.2 NBO Processing Phase
The NBO engine:
- Normalizes indicators
- Builds behavior vectors
- Evaluates deviation

Sample NBO Output:
```json
{
  "assertion_type": "behavior_deviation_statement",
  "behavior_class": "control_plane",
  "deviation_level": "low",
  "confidence_score": 0.93
}
```
Interpretation:
- This is a Network Behavior Assertion (NBA)
- It is evidentiary, not operational

### 5.3 Silent Validator Phase
Silent Validator:
- Receives NBO assertions
- Simulates consensus
- Anchors trust reference

Sample Validator Output:
```json
{
  "validation_result": "accepted",
  "consensus_confidence": 0.88,
  "anchored": true
}
```
Interpretation:
- Consensus reached
- No enforcement
- Reference available for audit

## 6. Scenario Simulation Walkthrough
### 6.1 Scenario: NORMAL Baseline

Observed Behavior:
- Stability score remains > 0.9
- No deviation asserted
Validator Result:

```makefile
Result: ACCEPTED
Impact: None
```

### 6.2 Scenario: DRIFT

Observed Behavior:
```json
{ "stability_score": 0.88 }
{ "stability_score": 0.82 }
{ "stability_score": 0.79 }
```
**NBO Interpretation:**
- Gradual degradation detected
Validator Result:
```makefile
Result: ACCEPTED (trend recorded)
Impact: None
```
### 6.3 Scenario: ANOMALY

Observed Behavior:
```json

{
  "indicator_type": "temporal_behavior_anomaly",
  "anomaly_score": 0.86
}

```
**NBO Interpretation:**
- Single-window anomaly

Validator Result:
```makefile
Result: ACCEPTED (evidence anchored)
Impact: None
```

### 6.4 Scenario: ASYMMETRY
Observed Behavior:
```json
{
  "indicator_type": "cross_domain_behavior_index",
  "domain_count": 3,
  "variance_index": 0.47
}
```

**NBO Interpretation:**
- Cross-domain inconsistency detected

Validator Result:
```makefile
Result: ACCEPTED (neutral trust reference)
Impact: None
```

## 7. Data Collected During Pilot
### 7.1 Artifact Types
|Artifact|	Purpose|
|---------|---------|
|Synthetic indicators|	Input evidence|
|Behavior assertions|	Abstract interpretation|
|Validator decisions	|Consensus trace|
|Timestamps & hashes	|Auditability|

### 7.2 Example Anchored Record
```json
{
  "assertion_id": "nba-2025-02-20-001",
  "timestamp": "2025-02-20T10:05:00Z",
  "hash": "0xabc123...",
  "confidence": 0.88
}
```

## 8. Post-Run Analysis
### 8.1 What Can Be Analyzed
- Behavioral trends
- Cross-scenario consistency
- Consensus reproducibility
- Model determinism

### 8.2 What Cannot Be Analyzed
- Subscriber behavior
- Traffic patterns
- Protocol-level events
- Individual network elements

## 9. Compliance Validation (During Demo)
During execution, it can be verified that:
- No packets are captured
- No ports are exposed
- No identifiers are processed
- No control actions are taken

This can be demonstrated via:
```bash
docker ps
docker inspect
```

## 10. Pilot Stop Procedure
```bash
docker compose down
```
Result:
- All containers stopped
- No state retained
- No impact on host system

## 11. Failure Handling (Simulated)
|Failure|	Behavior|
|-------|----------|
|Generator stops	|NBO idle|
|NBO stops	|Validator idle|
|Validator stops	|No consensus|
|All stop|	Pilot ends cleanly|
No cascading failure risk.

## 12. Demo Talking Points (For Stakeholders)
- “This system observes behavior, not traffic.”
- “No enforcement, only evidence.”
- “Operators remain fully sovereign.”
- “Privacy is preserved by design.”

## Final Statement
This runbook demonstrates that the NTF pilot:
- Can be executed safely
- Produces interpretable evidence
- Does not interfere with networks
- Supports regulator and operator dialogue
The pilot proves **feasibility, not authority.**









