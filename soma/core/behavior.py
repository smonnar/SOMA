# soma/core/behavior.py

"""
Handles the planning and execution of SOMA's behaviors based on dominant drives.
"""

from soma.core.states import SomaState
from soma.core.action_handler import (
    explore_environment,
    seek_social_input,
    review_memory,
    align_with_caregiver,
    return_to_familiar_state,
)

class BehaviorPlanner:
    def __init__(self):
        self.behavior_map = {
            "curiosity": explore_environment,
            "social_proximity": seek_social_input,
            "cognitive_integrity": review_memory,
            "caregiver_alignment": align_with_caregiver,
            "stability": return_to_familiar_state,
        }

    def plan_behavior(self, soma_state: SomaState):
        dominant_drive = soma_state.current_dominant_drive
        planned_action = self.behavior_map.get(dominant_drive)

        if planned_action:
            # Execute the behavior (side effects on memory/state)
            planned_action(soma_state)
            soma_state.append_note(
                f"Chose action '{planned_action.__name__}' in response to drive '{dominant_drive}'."
            )
        else:
            soma_state.append_note(f"No action mapped for drive '{dominant_drive}'.")
