import pygame

import constants
import game.gameclass


class GameEngine:
    def __init__(self):
        pygame.init()
        self._clock = Clock()
        self.screen = Screen()
        self._input_processor = InputProcessor()
        self._input_catcher = InputCatcher()
        self._input_catcher.add_binding('quit', self.stop)
        self.is_running = False

        self._game = game.gameclass.Game()

    def start(self):
        self._game.set_active_scene('gui')

        self.is_running = True
        self.loop()

    def stop(self):
        self.is_running = False

    def loop(self):
        while self.is_running:
            lag = self._clock.tick()
            code = self._input_processor.read()
            self._input_catcher.execute(code)

            while lag >= constants.PHYSICS_TIMESTEP_MS:
                # Physics update / catch-up
                self._game.update()
                lag -= constants.PHYSICS_TIMESTEP_MS

            # Rendering
            self._game.draw(self.screen.surface)
            self.screen.flip()


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

    @property
    def surface(self):
        return self._screen

    @staticmethod
    def flip():
        pygame.display.flip()

    def blit(self, *args):
        self._screen.blit(*args)

class InputProcessor:
    def __init__(self):
        self._events = []

    def read(self):
        self._events = pygame.event.get()
        for event in self._events:
            if event.type == pygame.QUIT:
                return 'quit'
        return None

class InputCatcher:
    def __init__(self):
        self._binding = {}

    def add_binding(self, action, command):
        self._binding.update({action: command})

    def execute(self, action):
        if action:
            self._binding[action]()