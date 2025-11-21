import json, os

ROOT = os.path.dirname(os.path.dirname(__file__))
DATA_PATH = os.path.join(ROOT, "data", "rules.json")

with open(DATA_PATH, "r") as f:
    RULES = json.load(f)

def get_rule_for(sign):
    sign = sign.lower()
    return RULES.get(sign, ["No guidance available."])[0]
