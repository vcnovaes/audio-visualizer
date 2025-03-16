from audio.audio_segment import Audio
from visual.configuration import DEFAULT_CONFIG, VisualConfig
from visual.draw import Drawing
from threading import Thread
import typer


app = typer.Typer()


@app.command()
def main(
    file: str = typer.Argument(
        ..., help="Path to the audio file (e.g., ../assets/song.mp3) [ wav or mp3]"
    ),
    config: str = typer.Option(
        DEFAULT_CONFIG, help="Visual configuration, if not provided, default is used"
    ),
):
    audio = Audio(file)
    configuration = VisualConfig(config)
    drawing = Drawing(configuration, audio)
    player_thread = Thread(target=audio.play)
    player_thread.start()
    drawing.run()
    player_thread.join()


if __name__ == "__main__":
    app()
