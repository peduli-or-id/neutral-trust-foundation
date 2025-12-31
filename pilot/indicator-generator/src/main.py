import random
import time
import json

while True:
    indicator = {
        "indicator_type": "control_plane_stability",
        "aggregation_window": "300s",
        "stability_score": round(random.uniform(0.6, 0.95), 2),
        "confidence": "synthetic"
    }
    print(json.dumps(indicator))
    time.sleep(random.randint(20, 90))
