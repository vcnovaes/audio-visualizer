import numpy as np
from pydub import AudioSegment
import pygame
from pydub.playback import play
import threading
import time


def play_audio(audio):
    play(audio)



# Load WAV file
audio = AudioSegment.from_file("assets/capitain.wav", format="wav")
samples = np.array(audio.get_array_of_samples())

# Convert stereo to mono (if needed)
if audio.channels == 2:
    samples = samples.reshape((-1, 2))
    samples = samples.mean(axis=1)

# Normalize samples to range (-1, 1)
samples = samples / np.max(np.abs(samples))

# Pygame setup
WIDTH, HEIGHT = 800, 400
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
    chunk = samples[chunk_start:chunk_start + chunk_size]
    bar_width = max(WIDTH // chunk_size, 1)  # Ensure bar_width is at least 1
    bar_width = 3
    center_y = HEIGHT // 2

    for i, sample in enumerate(chunk):
        bar_height = int(sample * (HEIGHT // 2))  # Scale sample to screen height
        x = i * bar_width
        pygame.draw.rect(screen, RED, (x, center_y - bar_height, bar_width - 1, bar_height * 2))

running = True
chunk_start = 0

audio_thread = threading.Thread(target=play_audio, args=(audio,))

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