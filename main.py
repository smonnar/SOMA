# main.py

import time
from soma.memory import MemorySystem
from soma.core.motivation import MotivationManager
from soma.core.behavior import BehaviorPlanner
from soma.core.states import SomaState
from soma.core.reflex_engine import ReflexEngine

TICK_DURATION = 1  # seconds

def main():
    memory = MemorySystem()
    motivation = MotivationManager()
    behavior = BehaviorPlanner()
    reflexes = ReflexEngine()
    soma_state = SomaState()

    print("=" * 40)

    for tick in range(1, 6):
        print(f"Tick: {tick}")

        # Update memory
        soma_state.memory_snapshot = memory.retrieve_snapshot()

        # Evaluate dominant drive
        soma_state.current_dominant_drive = motivation.evaluate_drives(soma_state)

        # Check reflexes first
        reflex_action = reflexes.check_for_reflex(soma_state)
        if reflex_action:
            print(f"Reflex Triggered: {reflex_action}")
            soma_state.append_note(f"Reflex action '{reflex_action}' triggered.")
        else:
            # Plan and execute behavior
            dominant_drive = soma_state.current_dominant_drive
            behavior.plan_behavior(soma_state, dominant_drive)

        # Show self-notes
        print(f"Dominant Drive: {soma_state.current_dominant_drive}")
        print(f"Planned Action: {soma_state.planned_action}")
        print(f"Self-Notes: {soma_state.self_notes}")
        print("=" * 40)
        time.sleep(TICK_DURATION)

if __name__ == "__main__":
    main()
