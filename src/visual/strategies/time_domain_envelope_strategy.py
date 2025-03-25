from numpy import ndarray, abs, convolve, ones
from visual.strategies.audio_transform_strategy import AudioTransformationStrategy


class TimeDomainEnvelopeStrategy(AudioTransformationStrategy):
    def __init__(self, smoothing_window_size: int = 10):
        """
        Initialize the strategy with a smoothing window size.

        Parameters:
            smoothing_window_size (int): The size of the moving average window for smoothing.
        """
        super().__init__()
        self.smoothing_window_size = smoothing_window_size

    def __calculate_envelope(self, samples: ndarray) -> ndarray:
        """
        Calculate the amplitude envelope of the audio signal.

        Parameters:
            samples (ndarray): The audio samples.

        Returns:
            ndarray: The smoothed amplitude envelope.
        """
        # Take the absolute value of the samples to get the amplitude
        absolute_samples = abs(samples)

        # Apply a moving average for smoothing
        window = ones(self.smoothing_window_size) / self.smoothing_window_size
        smoothed_envelope = convolve(absolute_samples, window, mode="same")

        return smoothed_envelope

    def transform(self, data: ndarray) -> ndarray:
        """
        Transform the audio data by calculating its amplitude envelope.

        Parameters:
            data (ndarray): The audio samples.

        Returns:
            ndarray: The transformed audio data (amplitude envelope).
        """
        return self.__calculate_envelope(data)
