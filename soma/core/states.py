# states.py
"""
Defines SOMA's central state object, which stores and updates its internal variables,
including sensory inputs, internal drives, and planned actions.
"""

class SomaState:
    def __init__(self):
        """
        Initialize SOMA's internal state.
        """
        self.tick = 0
        self.state = {
            "sensory": {},
            "drives": {},
            "dominant_drive": None,
            "planned_action": None,
            "self_notes": []
        }

    def tick_forward(self):
        """
        Simulates the passage of cognitive time for SOMA.
        """
        self.tick += 1

    def set(self, key, value):
        """
        Update a top-level state key (e.g., sensory input, planned action).
        """
        self.state[key] = value

    def get(self, key):
        """
        Retrieve a top-level state value.
        """
        return self.state.get(key, None)

    def append_note(self, note):
        """
        Store a reflection or observation as part of SOMA's self-awareness.
        """
        self.state["self_notes"].append(note)

    def debug_summary(self):
        """
        Print a summary of SOMA’s state for inspection.
        """
        return (
            f"Tick: {self.tick}\n"
            f"Dominant Drive: {self.get('dominant_drive')}\n"
            f"Planned Action: {self.get('planned_action')}\n"
            f"Self-Notes: {self.get('self_notes')}"
        )
