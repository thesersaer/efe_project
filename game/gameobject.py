import pygame

from constants import RESOLUTION_X, RESOLUTION_Y, GRID_SIZE, GRID_COLOR
from game.objects import DynamicObject, StaticObject


class Actor(DynamicObject):

    def __init__(self, *groups):

        DynamicObject.__init__(self,'game/sprites/shipBig.png', *groups)


class Grid(StaticObject):

    def __init__(self, *groups):

        StaticObject.__init__(self,(RESOLUTION_X, RESOLUTION_Y), *groups)

        for xx in range(0, RESOLUTION_X, GRID_SIZE):
            start_pos = (xx, 0)
            end_pos = (xx, RESOLUTION_Y)
            pygame.draw.line(self.image, GRID_COLOR, start_pos, end_pos)

        for yy in range(0, RESOLUTION_Y, GRID_SIZE):
            start_pos = (0, yy)
            end_pos = (RESOLUTION_X, yy)
            pygame.draw.line(self.image, GRID_COLOR, start_pos, end_pos)
