from enum import Enum
from audio.audio_factory import AudioFactory
from pygame import mixer
from pygame import K_p, K_n, K_q

from interface import pprint


class Controller:
    class State(Enum):
        PLAYING = 0
        PAUSED = 1
        STOPPED = 2
        UPDATING = 3

    def __init__(self, execution_queue: list[str], audio_factory: AudioFactory):
        self.execution_queue: list[str] = execution_queue
        self.audio_factory: AudioFactory = audio_factory
        self.current_audio_path = None
        self.current_audio = None
        self.state = Controller.State.STOPPED

    def load_next_audio(self):
        while len(self.execution_queue) > 0:
            self.state = Controller.State.UPDATING
            path = self.execution_queue.pop(0)
            self.current_audio_path = path
            self.current_audio = self.load_audio(path)
            pprint.print_current_song(path)
            mixer.music.play()
            self.state = Controller.State.PLAYING
            return self.current_audio
        self.state = Controller.State.STOPPED
        return None

    def load_audio(self, path: str):
        audio = self.audio_factory.get_audio(path)
        mixer.init(frequency=audio.frame_rate)
        mixer.music.load(self.current_audio_path)
        return audio

    def execute_command(self, command_key):

        if command_key == K_p:
            if self.state == Controller.State.PLAYING:
                mixer.music.pause()
                self.state = Controller.State.PAUSED
            elif self.state == Controller.State.PAUSED:
                mixer.music.unpause()
                self.state = Controller.State.PLAYING
            return self.current_audio
        if command_key == K_n:
            mixer.music.stop()
            return self.load_next_audio()
        if command_key == K_q:
            mixer.music.stop()
            self.state = Controller.State.STOPPED
            return None
        else:
            print(ValueError("Invalid command key", command_key))
