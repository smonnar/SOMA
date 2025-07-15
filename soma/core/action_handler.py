# soma/core/action_handler.py

"""
This module defines the symbolic behavior functions SOMA can execute
based on its current motivation. These simulate consequences or
feedback in its internal state, preparing us for future embodiment.
"""

def explore_environment(soma_state):
    # Simulates exploring — logs a note and increases familiarity
    soma_state.append_note("Explored the environment.")
    soma_state.memory["exploration_count"] = soma_state.memory.get("exploration_count", 0) + 1

def seek_social_input(soma_state):
    # Simulates requesting feedback from caregiver
    soma_state.append_note("Sought input from caregiver.")
    soma_state.memory["last_social_interaction"] = "tick_" + str(soma_state.ticks)

def review_memory(soma_state):
    # Simulates internal reflection
    past = soma_state.memory.get("exploration_count", 0)
    soma_state.append_note(f"Reflected on {past} past explorations.")

def align_with_caregiver(soma_state):
    # Simulates imitation or moral alignment
    soma_state.append_note("Imitated caregiver behavior.")
    soma_state.memory["alignment_log"] = soma_state.memory.get("alignment_log", []) + ["tick_" + str(soma_state.ticks)]

def return_to_familiar_state(soma_state):
    soma_state.append_note("Returned to familiar internal state.")
