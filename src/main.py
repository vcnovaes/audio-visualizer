from audio.audio_factory import AudioFactory
from audio.audio_segment import Audio
from controller.controller import Controller
from interface import pprint
from interface.execution_queue import get_execution_queue
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

    execution_queue = get_execution_queue(file)
    pprint.print_execution_queue(execution_queue)
    configuration = VisualConfig(config)
    drawing = Drawing(
        configuration,
        controller=Controller(execution_queue, AudioFactory()),
        audio_transform_strategy=configuration.get_transformation_strategy(),
    )
    drawing.run()

    exit(0)


if __name__ == "__main__":
    app()
