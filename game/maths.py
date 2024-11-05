import numpy as np
import pygame

from constants import GRID_SIZE, GRID_MEASURE


class ISpace:
    """
    Default implementation of a reference system
    """

    def __init__(self):

        pass


    def rotate(self, vector):

        pass


    def translate(self, vector):

        pass

    def scale(self, vector):

        pass


class BaseSpace(ISpace):

    def __init__(self):

        ISpace.__init__(self)


class Vector3(pygame.math.Vector3):
    """
    Base 3-component vector used to describe object information in spacetime.
    x -> t
    y -> x
    z -> y
    """
    pass


class Position(Vector3):
    pass


class Velocity(Vector3):
    pass


class IMath:

    scaling_factor = GRID_MEASURE / GRID_SIZE

    def __init__(self, sprite_rect: pygame.Rect):

        """
        :param sprite_rect: Rectangle of the sprite in screen coordinates
        """

        size_x = self.scaling_factor * sprite_rect.size[0]
        size_y = self.scaling_factor * sprite_rect.size[1]

        self.rect = pygame.Rect(0., 0., size_x, size_y)

        self.position = Position()


    def update(self):

        self.rect.center = (self.position.y, self.position.z)


class Physics(IMath):

    def __init__(self, rect):

        IMath.__init__(self, rect)

        self.velocity = Velocity()


    def update(self) -> tuple[int, int]:
        pass


class Logic(IMath):

    def __init__(self, rect):

        IMath.__init__(self, rect)

if __name__ == '__main__':
    foo = Physics()
    bar = foo.position.yz
    print("end")