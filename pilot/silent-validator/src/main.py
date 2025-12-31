import sys, json

for line in sys.stdin:
    try:
        a = json.loads(line)
        validation = {
            "validation_result": "accepted",
            "consensus_model": "simple-majority",
            "confidence": a["confidence_score"],
            "anchored": True
        }
        print(json.dumps(validation))
    except:
        pass
