# soma/memory.py

import numpy as np

class MemorySystem:
    def __init__(self):
        self.experiences = []

    def store(self, encoded_input):
        """
        Store a new encoded sensory input.
        """
        self.experiences.append(np.array(encoded_input))

    def similarity_score(self, encoded_input):
        """
        Compute similarity to past experiences using cosine similarity.
        """
        if not self.experiences:
            return 0.0  # Nothing stored yet

        input_vector = np.array(encoded_input)
        similarities = [self._cosine_similarity(input_vector, mem) for mem in self.experiences]
        return max(similarities)  # Return highest similarity to anything remembered

    def is_novel(self, encoded_input, threshold=0.8):
        """
        Determine if this input is new based on similarity to memory.
        """
        score = self.similarity_score(encoded_input)
        return score < threshold

    def _cosine_similarity(self, a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-8)

    def retrieve_snapshot(self):
        """
        Return a copy of the current memory as a snapshot dictionary.
        This allows the reflex or behavior systems to reason over recent memory.
        """
        return {
            "experiences": list(self.experiences)
        }
