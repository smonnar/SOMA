# File: soma/core/reflex_engine.py

class ReflexEngine:
    """
    The ReflexEngine handles involuntary, pre-programmed reflex behaviors
    that are triggered by specific sensory states. These behaviors correspond
    to Piaget's "Reflexive Schemes" substage, enabling SOMA to automatically
    respond to internal or external stimuli in a machine-native way.
    """

    def __init__(self):
        # Define mappings of sensory triggers to reflex actions
        self.reflex_map = {
            'sensor_overload': self.seek_safety,
            'unfamiliar_noise': self.freeze,
            'low_stability': self.center_self,
        }

    def process_reflexes(self, soma_state):
        """
        Checks the current sensory state in soma_state and triggers
        any appropriate reflex behavior based on hardcoded rules.
        """
        current_sensor_state = soma_state.sensory_input

        if current_sensor_state in self.reflex_map:
            action = self.reflex_map[current_sensor_state]()
            soma_state.append_note(f"Reflex triggered by '{current_sensor_state}': {action}")
            return action

        return None

    def seek_safety(self):
        return 'move_to_familiar_space'

    def freeze(self):
        return 'pause_and_listen'

    def center_self(self):
        return 'recalibrate_sensors'
