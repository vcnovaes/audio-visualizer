from audio.audio_segment import Audio
from visual.configuration import DEFAULT_CONFIG, VisualConfig
from visual.draw import Drawing
from threading import Thread


def main():
    audio = Audio("../assets/capitain.mp3")
    config = VisualConfig(DEFAULT_CONFIG)
    drawing = Drawing(config, audio)
    player_thread = Thread(target=audio.play)
    player_thread.start()
    drawing.run()
    player_thread.join()


if __name__ == "__main__":
    main()
