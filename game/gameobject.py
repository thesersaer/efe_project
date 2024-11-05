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

    def __init__(self, size: tuple[int, int], zoom: float = 1, *groups):

        TriggerObject.__init__(self, size, *groups)

        self.zoom = None

        self.set_zoom(zoom)


    def seek_group(self, group):

        self.action_group.add(group)


    def set_zoom(self, zoom: float):

        self.maths.rect.width *= zoom
        self.maths.rect.height *= zoom

        self.zoom = zoom


    def update(self, *args, **kwargs):

        self.maths.update()
        self.check_group()


class CameraViewer(StaticObject):

    def __init__(self, size: tuple[int, int], *groups):

        StaticObject.__init__(self, size, *groups)

        self.camera: Optional[Camera] = None


    def set_camera(self, camera: Optional[Camera] = None):

        self.camera = camera


    def draw(self):

        self.action_group.draw(self.image)


    def update(self, *args, **kwargs):

        self.maths.update()
        self.action_group.add(self.camera.check_group())



if __name__ == '__main__':
    foo = Camera()
    print(foo)