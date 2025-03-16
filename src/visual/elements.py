class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        pass


class DisplayElementStyle:
    def hex_to_tuple(self, hex_color):
        """
        Converts a hex color string to an RGB tuple.

        Parameters:
            hex_color (str): The hex color string (e.g., "#FF0000").

        Returns:
            tuple: A tuple representing the RGB color (e.g., (255, 0, 0)).
        """
        # Remove the '#' if present
        hex_color = hex_color.lstrip("#")

        # Convert the hex string to an RGB tuple
        return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))

    def __init__(self, background_color, bar_color):
        self.background_color = self.hex_to_tuple(background_color)
        self.bar_color = self.hex_to_tuple(bar_color)


class AnimationSetting:
    def __init__(self, chunk_size, fps):
        self.chunk_size = chunk_size
        self.fps = fps
        pass
