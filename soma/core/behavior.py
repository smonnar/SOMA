# behavior.py
"""
This module defines SOMA's BehaviorPlanner.
It translates SOMA's dominant drive into an actionable intention or behavior,
based on machine-native values and cognitive maturity.
"""

class BehaviorPlanner:
    def __init__(self):
        """
        Initialize behavior rules mapped to internal drives.
        Behaviors are defined as symbolic intentions (for now).
        """
        self.behavior_map = {
            "curiosity": "explore_environment",
            "cognitive_integrity": "review_memory",
            "stability": "return_to_familiar_state",
            "social_proximity": "seek_caregiver_input",
            "drive_saturation": "pause_and_reflect",
            "caregiver_alignment": "imitate_caregiver_behavior",
            "truth_seeking": "query_uncertain_knowledge",
            "idle": "rest_or_scan"
        }

    def plan_behavior(self, soma_state):
        """
        Based on the current dominant drive, assign a behavior plan.
        Save the result back into SOMA's state for execution/logging.
        """
        dominant_drive = soma_state.get("dominant_drive")

        planned_action = self.behavior_map.get(dominant_drive, "rest_or_scan")
        soma_state.set("planned_action", planned_action)

        # Optional: SOMA keeps a record of its reasoning or intent
        soma_state.append_note(f"Chose action '{planned_action}' in response to drive '{dominant_drive}'.")
