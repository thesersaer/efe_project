import typing
import pygame
import constants

class Game:
    def __init__(self):
        pygame.init()
        self._clock = Clock()
        self._screen = Screen()
        self.is_running = False

    def start(self):
        self.is_running = True

    def stop(self):
        self.is_running = False

    def loop(self):
        while self.is_running:
            self._clock.tick()
            # Event processing
            # Physics update / catch-up
            # Rendering


class Clock:
    def __init__(self):
        self._clock = pygame.time.Clock()
        self._lag = 0

    def tick(self) -> int:
        elapsed = self._clock.tick(constants.RENDER_FRAME_RATE)
        self._lag += elapsed
        return elapsed

class Screen:
    def __init__(self):
        self._screen = pygame.display.set_mode(constants.DISPLAY_RESOLUTION)