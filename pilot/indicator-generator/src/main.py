import time
import random
import json
import os

interval_min = int(os.getenv("INDICATOR_INTERVAL_MIN", "20"))
interval_max = int(os.getenv("INDICATOR_INTERVAL_MAX", "90"))

while True:
    indicator = {
        "indicator_type": "control_plane_stability",
        "aggregation_window": "300s",
        "stability_score": round(random.uniform(0.5, 0.95), 2),
        "confidence": "synthetic"
    }
    print(json.dumps(indicator))
    time.sleep(random.randint(interval_min, interval_max))
