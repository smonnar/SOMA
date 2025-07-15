# soma/curiosity.py

class CuriosityEngine:
    """
    This class computes a 'curiosity score' based on the novelty of sensory input.
    It drives SOMA's desire to explore and engage with unfamiliar stimuli.
    """

    def __init__(self, memory):
        """
        Initialize the curiosity engine with a reference to SOMA's memory system.
        """
        self.memory = memory
        self.last_novelty = 0.0  # Optional: track previous curiosity for smoothing

    def evaluate(self, encoded_input):
        """
        Given an encoded sensory input, determine whether it's novel,
        and return a curiosity score (float between 0 and 1).
        Higher score = more novel = more curious.
        """
        # Check if this input is novel based on similarity threshold
        is_new = self.memory.is_novel(encoded_input)

        # Compute curiosity as binary or graded value
        similarity = self.memory.similarity_score(encoded_input)
        curiosity_score = 1.0 - similarity  # More different = more interesting

        # Store the current input into memory so it's no longer novel next time
        self.memory.store(encoded_input)

        # Return the computed curiosity score
        return curiosity_score
