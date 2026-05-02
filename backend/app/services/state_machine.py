# services/state_machine.py

VALID_TRANSITIONS = {
    "OPEN": ["INVESTIGATING"],
    "INVESTIGATING": ["RESOLVED"],
    "RESOLVED": ["CLOSED"],
}

def can_transition(current, new):
    return new in VALID_TRANSITIONS.get(current, [])

