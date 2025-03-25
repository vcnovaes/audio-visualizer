from visual.elements import Canvas, AnimationSetting, DisplayElementStyle
import yaml
from visual.strategies import *
from visual.strategies.default_strategy import NoTransformStrategy
from visual.strategies.fft_smooth_strategy import FFTSmoothStrategy
from visual.strategies.fft_strategy import FFTStrategy
from visual.strategies.time_domain_envelope_strategy import TimeDomainEnvelopeStrategy

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
            self.config["audio"]["chunk_size"],
            self.config["animation"]["fps"],
            self.config["audio"]["symmetric"],
        )

        self.raw_transformation = self.config["audio"]["transformation"]
        pass

    def get_transformation_strategy(self):
        match self.raw_transformation:
            case "fft":

                return FFTStrategy(self.animation.chunk_size)
            case "time_smooth":

                return TimeDomainEnvelopeStrategy()
            case "none":
                return NoTransformStrategy()
            case "fft_smooth":
                return FFTSmoothStrategy(
                    self.animation.chunk_size, TimeDomainEnvelopeStrategy()
                )
            case _:
                raise ValueError("Invalid or unsupported transformation")
