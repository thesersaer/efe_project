from typing import Optional

import pygame

from constants import GRID_SIZE, GRID_COLOR
from game.objects import DynamicObject, StaticObject, TriggerObject


class Actor(DynamicObject):

    def __init__(self, *groups):

        DynamicObject.__init__(self,'game/sprites/shipBig.png', *groups)


class Player(Actor):

    def __init__(self, position: tuple[int, int], *groups):

        Actor.__init__(self, *groups)

        self.rect.center = position


class Grid(StaticObject):

    def __init__(self, size: tuple[int, int], *groups):

        StaticObject.__init__(self, size, *groups)

        for xx in range(0, size[0], GRID_SIZE):
            start_pos = (xx, 0)
            end_pos = (xx, size[1])
            pygame.draw.line(self.image, GRID_COLOR, start_pos, end_pos)

        for yy in range(0, size[1], GRID_SIZE):
            start_pos = (0, yy)
            end_pos = (size[0], yy)
            pygame.draw.line(self.image, GRID_COLOR, start_pos, end_pos)

        pygame.draw.rect(self.image, 'white', self.rect, 2)


class Camera(TriggerObject):

    def __init__(self, size: tuple[int, int], *groups):

        TriggerObject.__init__(self, size, *groups)


class CameraViewer(StaticObject):

    def __init__(self, size: tuple[int, int], *groups):

        StaticObject.__init__(self, size, *groups)

        self.camera = Camera(size)


    def draw(self, surface):

        for obj in self.action_group:

            obj.draw()


    def update(self, *args, **kwargs):

        pass


if __name__ == '__main__':
    foo = Camera()
    print(foo)