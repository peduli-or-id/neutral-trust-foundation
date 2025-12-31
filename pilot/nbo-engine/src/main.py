import sys
import json

# NBO engine stub – reads JSON from STDIN
for line in sys.stdin:
    try:
        indicator = json.loads(line.strip())
        nbo_output = {
            "assertion_type": "behavior_deviation_statement",
            "indicator": indicator,
            "confidence_score": indicator.get("confidence", "synthetic")
        }
        print(json.dumps(nbo_output))
    except:
        continue
