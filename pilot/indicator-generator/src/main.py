import time, random, json, os

min_i = int(os.getenv("INDICATOR_INTERVAL_MIN", 20))
max_i = int(os.getenv("INDICATOR_INTERVAL_MAX", 90))

while True:
    indicator = {
        "indicator_type": "control_plane_stability",
        "aggregation_window": "300s",
        "stability_score": round(random.uniform(0.75, 0.95), 2),
        "confidence": "synthetic"
    }
    print(json.dumps(indicator))
    time.sleep(random.randint(min_i, max_i))
