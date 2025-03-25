from audio.audio_formatter import AudioFormatter
from pydub import AudioSegment
from numpy import array
from pydub import playback
from numpy.fft import fft


class Audio:

    def __init__(self, filename: str):
        (wav_filename, err) = AudioFormatter.as_wav(filename).unwrap()
        if err != None:
            raise Exception(err)

        self.filename = wav_filename
        self.audio = AudioSegment.from_file(
            self.filename, format=AudioFormatter.DefaultFormat
        )
        self.samples = self.calculate_samples()

        self.frame_rate = self.audio.frame_rate

    def __convert_samples_to_mono(self, samples):
        if self.audio.channels == 2:
            return samples.reshape((-1, 2)).mean(axis=1)

    def play(self):
        playback.play(self.audio)

    def get_chunk(self, start, end):
        return self.samples[start:end]

    def calculate_samples(self):
        samples = array(self.audio.get_array_of_samples())
        samples = samples / max(abs(samples))
        return self.__convert_samples_to_mono(samples)

    def n_samples(self):
        return len(self.samples)
