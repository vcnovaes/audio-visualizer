from audio.audio_segment import Audio


class AudioFactory:

    def __init__(self):
        pass

    def get_audio(self, path: str) -> Audio:
        return Audio(path)
