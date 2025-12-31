import json
import time
import uuid
from datetime import datetime
from pathlib import Path

ARTIFACT_DIR = Path("/app/data/artifacts")
LOG_FILE = Path("/app/logs/indicator-generator.log")

ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

def log(msg):
    timestamp = datetime.utcnow().isoformat()
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {msg}\n")

def generate_indicator():
    return {
        "indicator_id": str(uuid.uuid4()),
        "type": "synthetic_behavior_signal",
        "domain": "synthetic-domain-A",
        "timestamp": datetime.utcnow().isoformat(),
        "confidence": round(0.6 + 0.3 * time.time() % 1, 2),
        "scope": "non-operational"
    }

def main():
    log("Indicator generator started")

    indicator = generate_indicator()
    artifact_path = ARTIFACT_DIR / f"indicator-{indicator['indicator_id']}.json"

    with open(artifact_path, "w") as f:
        json.dump(indicator, f, indent=2)

    log(f"Indicator written: {artifact_path.name}")
    log("Indicator generator completed successfully")

if __name__ == "__main__":
    main()
