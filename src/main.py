from audio.audio_segment import Audio
from visual.configuration import DEFAULT_CONFIG, VisualConfig
from visual.draw import Drawing
from threading import Thread
import typer
from visual.strategies.default_strategy import NoTransformStrategy
from visual.strategies.fft_strategy import FFTStrategy
from visual.strategies.time_domain_envelope_strategy import TimeDomainEnvelopeStrategy

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
    drawing = Drawing(configuration, audio, TimeDomainEnvelopeStrategy())
    player_thread = Thread(target=audio.play)
    player_thread.start()
    drawing.run()
    player_thread.join()
    exit(0)


if __name__ == "__main__":
    app()
