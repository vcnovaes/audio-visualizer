from visual.elements import Canvas, AnimationSetting, DisplayElementStyle
import yaml

DEFAULT_CONFIG = "visual_config.yaml"


class VisualConfig:

    def __init__(self, configfile):

        with open(configfile, "r") as f:
            self.config = yaml.safe_load(f)

        self.canvas = Canvas(
            self.config["canvas"]["width"], self.config["canvas"]["height"]
        )

        self.element_style = DisplayElementStyle(
            self.config["colors"]["background"], self.config["colors"]["bar"]
        )

        self.animation = AnimationSetting(
            self.config["audio"]["chunk_size"], self.config["animation"]["fps"]
        )

        pass
