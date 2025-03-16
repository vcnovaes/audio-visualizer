import numpy as np
from pydub import AudioSegment
import pygame
from pydub.playback import play
from audio.audio_segment import Audio
import threading
import time

saudio = Audio("./assets/capitain.mp3")
samples = saudio.samples
audio = saudio.audio
# Pygame setup
WIDTH, HEIGHT = 1200, 800
FPS = 60
CHUNK_SIZE = 500  # Number of samples to display at a time

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Audio Waveform Animation")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)


def draw_waveform(screen, samples, chunk_start, chunk_size):
    """
    Draws a chunk of the waveform on the screen.

    Parameters:
        screen (pygame.Surface): The Pygame screen to draw on.
        samples (np.ndarray): The audio samples.
        chunk_start (int): The starting index of the chunk.
        chunk_size (int): The number of samples in the chunk.
    """
    screen.fill(BLACK)  # Clear the screen
    chunk = samples[chunk_start : chunk_start + chunk_size]
    bar_width = max(WIDTH // chunk_size, 5)  # Ensure bar_width is at least 1
    center_y = HEIGHT // 2

    for i, sample in enumerate(chunk):
        bar_height = int(sample * (HEIGHT // 2))  # Scale sample to screen height
        bar_height = max(
            min(bar_height, HEIGHT // 2 - 1), -(HEIGHT // 2 - 1)
        )  # Clamp to screen height

        x = i * bar_width
        pygame.draw.rect(
            screen,
            ((255 - abs(bar_height)) % 255, 0, 0),
            (x, center_y - bar_height, bar_width - 1, bar_height * 2),
        )


running = True
chunk_start = 0

audio_thread = threading.Thread(target=saudio.play)

start_time = time.time()
audio_thread.start()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the current chunk of the waveform

    elapsed_time = time.time() - start_time
    current_sample = int(elapsed_time * audio.frame_rate)

    # Calculate the chunk_start based on the current playback position
    chunk_start = current_sample
    # Update the chunk start to animate
    chunk_start += CHUNK_SIZE // 10  # Move forward by a fraction of the chunk size
    if chunk_start >= len(samples):
        chunk_start = 0  # Loop back to the start

    draw_waveform(screen, samples, chunk_start, CHUNK_SIZE)
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
audio_thread.join()
