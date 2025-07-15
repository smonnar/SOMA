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

        # Simulate new sensory input (placeholder)
        soma_state.set("sensory", {"vision": "blurry_shapes"})

        # Drive selection process
        motivation.update_drive_levels(soma_state)
        motivation.select_dominant_drive(soma_state)

        # Choose a behavior in response to the selected drive
        behavior.plan_behavior(soma_state)

        # Debugging output
        print("=" * 40)
        print(soma_state.debug_summary())

if __name__ == "__main__":
    main()
