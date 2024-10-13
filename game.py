import typing
import numpy as np
import pygame

from speedArrow import LorentzTransformation

import constants
from constants import PHYSICS_TIMESTEP_MS, GRID_SIZE, GRID_MEASURE, PLAYER_SIZE, PLAYER_Y_RATIO


def Render_Text(what, color, where):
    font = pygame.font.Font(None, 30)
    text = font.render(what, 1, pygame.Color(color))
    screen.blit(text, where)


def render_player():
    screen_size = screen.get_size()
    rect = (
        screen_size[0]/2 - PLAYER_SIZE[0],
        screen_size[1]/constants.PLAYER_Y_RATIO - PLAYER_SIZE[1],
        PLAYER_SIZE[0], PLAYER_SIZE[1])
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), rect)


def render_grid():
    for xx in range(0, screen.get_width(), constants.GRID_SIZE):
        for yy in range(0, screen.get_height(), constants.GRID_SIZE):
            pygame.draw.rect(
                screen,
                (35, 35, 35),
                (xx - 2, yy - 2, constants.GRID_SIZE, constants.GRID_SIZE), 1)


class PhysicsEngine:
    def __init__(self):
        self.objects = []

    def load_objects(self, object_list):
        self.objects = object_list

    def update(self):
        for physics_object in self.objects:
            physics_object.update()


class PhysicsObject:
    @staticmethod
    def wrap_around(r_vector):
        width = screen.get_width()/GRID_SIZE * GRID_MEASURE
        height = screen.get_height()/GRID_SIZE * GRID_MEASURE
        s_x = r_vector[1]
        s_y = r_vector[2]
        if abs(s_x) > width:
            s_x = abs(s_x % width)
        elif s_x < 0:
            s_x += width
        if abs(s_y) > height:
            s_y = abs(s_y % width)
        elif s_y < 0:
            s_y += height
        return r_vector

    def __init__(self, s_x = 0., s_y = 0.):
        self._s_vector = np.array([
            [0.],
            [s_x],
            [s_y]
        ])

        self._v_vector = np.array([
            [0.],
            [0.]
        ])

    @property
    def s_vector(self):
        return self._s_vector

    @property
    def v_vector(self):
        return self._v_vector

    def boost(self, v_x, v_y):
        self._v_vector = np.array([
            [1],
            [v_x],
            [v_y]
        ])

    def update(self):
        self._s_vector += PHYSICS_TIMESTEP_MS * self._v_vector
        self._s_vector = self.wrap_around(self._s_vector)

    def interpolate(self, factor):
        self._s_vector += factor * PHYSICS_TIMESTEP_MS * self._v_vector
        return self.wrap_around(self._s_vector)


class Renderer:
    @staticmethod
    def physics_to_render_field(s_vector):
        r_vector = s_vector * GRID_SIZE / GRID_MEASURE
        return r_vector

    def __init__(self, physics: PhysicsEngine, lorentz_transformer: LorentzTransformation = None):
        self.objects = physics.objects
        self.lorentz_transformer = lorentz_transformer

    def render(self, interpol_factor: float, apply_lorentz = False):
        for physics_object in self.objects:
            s_vector = physics_object.s_vector
            s_vector = physics_object.interpolate(interpol_factor)
            if apply_lorentz:
                s_vector = self.lorentz_transformer.transpose_vector(s_vector)
            print(physics_object.v_vector)
            r_vector = self.physics_to_render_field(s_vector)
            s_x = r_vector[1] - PLAYER_SIZE[0]
            s_y = r_vector[2] - PLAYER_SIZE[1]
            rect = (
                s_x[0],
                s_y[0],
                PLAYER_SIZE[0], PLAYER_SIZE[1])
            pygame.draw.rect(screen, pygame.Color(255, 255, 255), rect)


# pygame setup
pygame.init()
screen = pygame.display.set_mode(constants.DISPLAY_RESOLUTION)
clock = pygame.time.Clock()
lag = 0.
running = True

physics_engine = PhysicsEngine()
test_object = PhysicsObject(screen.get_width()/2 * GRID_MEASURE/GRID_SIZE,
                            (screen.get_height()/PLAYER_Y_RATIO + 20) * GRID_MEASURE/GRID_SIZE)
object_velocity = (-.01, -0.05)
test_object.boost(*object_velocity)
physics_engine.load_objects([test_object])

lorentz_transformator = LorentzTransformation(*object_velocity)

render_engine = Renderer(physics_engine, lorentz_transformator)

while running:
    elapsed = clock.tick(constants.RENDER_FRAME_RATE)
    lag += elapsed

    # EVENT PROCESSING
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    while lag >= constants.PHYSICS_TIMESTEP_MS:
        # PHYSICS UPDATE
        # here
        physics_engine.update()
        lag -= constants.PHYSICS_TIMESTEP_MS

    # RENDERING
    interpolation_factor = lag / constants.PHYSICS_TIMESTEP_MS
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    Render_Text(str(int(clock.get_fps())), (255, 0, 0), (0, 0))

    render_grid()
    render_player()
    render_engine.render(interpolation_factor, False)

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()
