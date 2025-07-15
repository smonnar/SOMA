# soma/perception.py

class SensoryInput:
    def __init__(self, color: str, shape: str):
        self.color = color
        self.shape = shape

    def encode(self):
        """
        Encodes sensory input (color, shape) into a simple vector.
        This is a machine-native representation of raw environmental data.
        """
        color_vector = self._encode_color(self.color)
        shape_vector = self._encode_shape(self.shape)
        return color_vector + shape_vector

    def _encode_color(self, color):
        color_map = {
            'red': [1, 0, 0],
            'green': [0, 1, 0],
            'blue': [0, 0, 1],
            'yellow': [1, 1, 0],
            'black': [0, 0, 0],
            'white': [1, 1, 1]
        }
        return color_map.get(color.lower(), [0.5, 0.5, 0.5])  # Unknown = gray

    def _encode_shape(self, shape):
        shape_map = {
            'circle': [1, 0, 0],
            'square': [0, 1, 0],
            'triangle': [0, 0, 1],
            'star': [1, 1, 0]
        }
        return shape_map.get(shape.lower(), [0.3, 0.3, 0.3])  # Unknown = neutral

