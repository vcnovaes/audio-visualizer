from numpy import ndarray
from abc import ABC, abstractmethod


class AudioTransformationStrategy(ABC):
    @abstractmethod
    def transform(self, data: ndarray) -> ndarray:
        raise NotImplementedError("transform method not implemented")
