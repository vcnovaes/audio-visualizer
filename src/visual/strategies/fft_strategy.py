from numpy import ndarray, fft, array
from visual.strategies.audio_transform_strategy import AudioTransformationStrategy


class FFTStrategy(AudioTransformationStrategy):
    def __init__(self, chunk_size):
        super().__init__()
        if not self.sample_size_allowed(chunk_size):
            raise ValueError("Chunk size must be a power of 2")
        pass

    def __apply_fft(samples, frame_rate):
        fft_result = fft.fft(samples)
        magnitudes = abs(fft_result)
        frequencies = array(range(len(magnitudes))) * (frame_rate / len(magnitudes))

        return frequencies[: len(magnitudes) // 2], magnitudes[: len(magnitudes) // 2]

    def __frequency_weighted_magnitudes(frequencies, magnitudes):
        return frequencies * magnitudes

    def __normalize(array):
        max_val = max(abs(array))
        if max_val == 0:
            return array
        return array / max_val

    def transform(self, data: ndarray):
        (frequencies, magnitudes) = FFTStrategy.__apply_fft(data, 44100)
        weighted_magnitudes = FFTStrategy.__frequency_weighted_magnitudes(
            frequencies, magnitudes
        )
        return FFTStrategy.__normalize(weighted_magnitudes)

    def sample_size_allowed(self, sample_size) -> bool:
        return (sample_size & (sample_size - 1)) == 0
