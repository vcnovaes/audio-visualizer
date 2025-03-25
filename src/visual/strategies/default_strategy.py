from abc import abstractmethod

from numpy import ndarray
from visual.strategies.audio_transform_strategy import AudioTransformationStrategy


class NoTransformStrategy(AudioTransformationStrategy):
    def __init__(self):
        super().__init__()

    def transform(self, data: ndarray) -> ndarray:
        return data
