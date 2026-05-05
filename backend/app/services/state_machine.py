VALID = {
    "OPEN": ["INVESTIGATING"],
    "INVESTIGATING": ["RESOLVED"],
    "RESOLVED": ["CLOSED"]
}

def can_transition(current, new):
    return new in VALID.get(current, [])
