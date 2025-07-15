# main.py
"""
Main loop for SOMA's cognitive cycle.
This simulates one 'tick' of cognition by updating perception, motivation, and selecting a drive-based action.
"""

from soma.core.states import SomaState
from soma.core.motivation import MotivationManager
from soma.core.behavior import BehaviorPlanner

def main():
    # Initialize SOMA's internal components
    soma_state = SomaState()
    motivation = MotivationManager()
    behavior = BehaviorPlanner()

    # Simulate 5 cognitive ticks
    for _ in range(5):
        soma_state.tick_forward()

        # Simulate new perceptual input (placeholder for future vision/audio/touch systems)
        soma_state.set("sensory", {"vision": "blurry_shapes"})

        # Update SOMA’s motivational state
        motivation.update_drive_levels(soma_state)
        motivation.select_dominant_drive(soma_state)

        # 🔧 NEW: Extract the dominant drive to pass it to behavior planner
        dominant_drive = soma_state.get("current_dominant_drive")

        # Plan and log behavior
        behavior.plan_behavior(soma_state, dominant_drive)

        # Output state
        print("=" * 40)
        print(soma_state.debug_summary())

if __name__ == "__main__":
    main()
