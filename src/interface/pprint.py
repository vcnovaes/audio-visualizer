from rich.console import Console
from rich.table import Table
from rich.panel import Panel
import os

console = Console()


def print_execution_queue(queue: list[str]):
    """
    Prints the execution queue in a formatted table.

    Parameters:
        queue (list[str]): List of songs in the execution queue.
    """
    table = Table(title="Execution Queue", style="bold cyan")
    table.add_column("Index", justify="center", style="bold green")
    table.add_column("Song", justify="left", style="bold yellow")
    queue = [os.path.basename(f) for f in queue]
    for index, song in enumerate(queue, start=1):
        table.add_row(str(index), song)

    console.print(table)


def print_current_song(song: str):
    """
    Prints the currently playing song in a styled panel.

    Parameters:
        song (str): The name of the currently playing song.
    """
    song = os.path.basename(song)
    panel = Panel(
        f"[bold yellow]Now Playing:[/bold yellow] [bold green]{song}[/bold green]",
        title="🎵 Music Player",
        border_style="bold magenta",
    )
    console.print(panel)
