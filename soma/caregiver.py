# soma/caregiver.py

class CaregiverInterface:
    """
    This module represents SOMA's communication with a human caregiver.
    Initially, it supports simple interactions via the console.
    """

    def __init__(self):
        pass  # Placeholder for future extension (e.g., API keys, LLM hooks)

    def receive_feedback(self, encoded_input):
        """
        Display what SOMA has experienced and ask the caregiver for insight.
        """
        print("\n👶 SOMA says:")
        print("  > I encountered something new. I don't recognize it.")
        print("  > Can you tell me what this might be or what it's called?")

        label = input("👤 Caregiver, please enter your response: ")
        return label.strip()

    def confirm_familiarity(self):
        """
        SOMA acknowledges something it already knows.
        """
        print("\n👶 SOMA says:")
        print("  > I recognize this. It's familiar to me.")
