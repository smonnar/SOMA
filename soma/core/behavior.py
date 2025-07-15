# soma/core/behavior.py

"""
Behavior selection logic based on current drive state.
This maps internal drives to actions that SOMA can perform.
"""

class BehaviorPlanner:
    def __init__(self):
        # Define drive-to-action mappings
        self.drive_action_map = {
            "curiosity": "explore_environment",
            "truth_seeking": "query_caregiver",
            "caregiver_alignment": "imitate_caregiver_behavior",
            "social_proximity": "seek_closeness",
            "stability": "return_to_familiar_state",
            "cognitive_integrity": "review_memory",
            "drive_saturation": "pause_and_integrate"
        }

    def plan_behavior(self, soma_state, dominant_drive):
        """
        Determine the best action to take based on the dominant internal drive.
        """
        planned_action = self.drive_action_map.get(dominant_drive, None)

        if planned_action:
            soma_state.set("planned_action", planned_action)
            soma_state.append_note(
                f"Chose action '{planned_action}' in response to drive '{dominant_drive}'."
            )
        else:
            soma_state.set("planned_action", None)
            soma_state.append_note(
                f"No action mapped for drive '{dominant_drive}'."
            )
