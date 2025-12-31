import sys, json

for line in sys.stdin:
    try:
        i = json.loads(line)
        assertion = {
            "assertion_type": "network_behavior_assertion",
            "behavior_class": i["indicator_type"],
            "deviation_level": "low" if i["stability_score"] > 0.8 else "moderate",
            "confidence_score": i["stability_score"]
        }
        print(json.dumps(assertion))
    except:
        pass
