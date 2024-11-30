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

        self.sprite_rect = sprite_rect

        size_x = self.scaling_factor * sprite_rect.size[0]
        size_y = self.scaling_factor * sprite_rect.size[1]

        self.rect = pygame.Rect(0., 0., size_x, size_y)

        self.position = Position()


    def update(self, *args, **kwargs):

        pass


    def copy(self):

        imath = IMath(self.sprite_rect.copy())
        imath.position = self.position.copy()
        return imath


    def is_within(self, obj_math: 'IMath') -> bool:

        return self.rect.colliderect(obj_math.rect)


class IPhysics(IMath):

    def __init__(self, sprite_rect):

        IMath.__init__(self, sprite_rect)

        self.velocity = Velocity()


    def update(self, *args, **kwargs):

        pass


    def copy(self) -> 'IPhysics':

        iph = IPhysics(self.sprite_rect)
        iph.position = self.position.copy()
        iph.velocity = self.velocity.copy()
        return iph


    def bind(self, obj_physics: 'IPhysics'):
        """
        Binds the object's motion to that of obj_physics
        :param obj_physics: IPhysics to be "followed"
        """
        self.position = obj_physics.position
        self.velocity = obj_physics.velocity


    def relative_to(self, obj_physics: 'IPhysics'):
        """
        Returns a copy of itself with its frame shifted with respect to the obj_physics frame
        :param obj_physics: Reference Object
        :return: IPhysics relative object
        """
        relative_frame = self.copy()
        relative_frame.position -= obj_physics.position
        relative_frame.velocity -= obj_physics.velocity
        return relative_frame


class ILogic(IMath):

    def __init__(self, sprite_rect):

        IMath.__init__(self, sprite_rect)


    def update(self, *args, **kwargs):

        pass


if __name__ == '__main__':

    foo = IPhysics()
    bar = foo.position.yz
    print("end")