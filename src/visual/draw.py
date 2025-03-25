import numpy as np
from pydub import AudioSegment
import pygame
from pydub.playback import play
from audio.audio_segment import Audio
import time
from numpy.fft import fft

from visual.configuration import VisualConfig
from visual.strategies.audio_transform_strategy import AudioTransformationStrategy


class Drawing:

    def __init__(
        self,
        config: VisualConfig,
        audio: Audio,
        audio_transform_strategy: AudioTransformationStrategy,
    ):
        self.audio = audio
        self.config = config
        pygame.init()

        self.screen = pygame.display.set_mode(
            (self.config.canvas.width, self.config.canvas.height)
        )
        self.clock = pygame.time.Clock()
        self.transform_strategy = audio_transform_strategy
        self.virtual_axis = self.config.canvas.height // 2

        self.bar_width = self.__calculate_bar_width()

    def __calculate_bar_width(self):
        return max(self.config.canvas.width // self.config.animation.chunk_size, 5)

    def draw_wavebar(self, bar_width, bar_height, x_position):
        pygame.draw.rect(
            self.screen,
            self.config.element_style.color_bar_with_gradient(x_position * 0.0008, 0),
            (x_position, self.virtual_axis - bar_height, bar_width - 1, bar_height * 2),
        )

    def __calculate_bar_height(self, sample):

        bar_height = int(
            sample * (self.config.canvas.height // 2)
        )  # Scale sample to screen height
        return max(
            min(bar_height, self.config.canvas.height // 2 - 1),
            -(self.config.canvas.height // 2 - 1),
        )  # Clamp to screen height

    def draw_waveform(self, chunk_start):
        self.screen.fill(self.config.element_style.background_color)  # Clear the screen

        chunk_end = chunk_start + self.config.animation.chunk_size

        chunk = self.transform_strategy.transform(
            self.audio.get_chunk(chunk_start, chunk_end)
        )
        self.__draw_audio_chunk(chunk)

    def __draw_audio_chunk(self, chunk):
        for i, sample in enumerate(chunk):
            self.bar_height = self.__calculate_bar_height(sample)
            x_position = i * self.bar_width
            self.draw_wavebar(self.bar_width, self.bar_height, x_position)

    def run(self):
        running = True
        chunk_start = 0
        start_time = time.time()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Draw the current chunk of the waveform

            elapsed_time = time.time() - start_time
            current_sample = int(elapsed_time * self.audio.frame_rate)

            # Calculate the chunk_start based on the current playback position
            chunk_start = current_sample
            # Update the chunk start to animate
            chunk_start += (
                self.config.animation.chunk_size // 10
            )  # Move forward by a fraction of the chunk size

            if chunk_start >= self.audio.n_samples():
                chunk_start = 0  # Loop back to the start

            self.draw_waveform(chunk_start)

            pygame.display.flip()

            self.clock.tick(self.config.animation.fps)

        pygame.quit()
