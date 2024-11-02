import pygame

from constants import PHYSICS_TIMESTEP_MS as DT


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


class MathI:

    def __init__(self, rect: pygame.Rect):

        self.rect = rect

        self.position = Position()


    def update(self):

        self.rect.center = (self.position.y, self.position.z)


class Physics(MathI):

    def __init__(self, rect):

        MathI.__init__(self, rect)

        self.velocity = Velocity()


    def update(self) -> tuple[int, int]:
        pass


class Logic(MathI):

    def __init__(self, rect):

        MathI.__init__(self, rect)

if __name__ == '__main__':
    foo = Physics()
    bar = foo.position.yz
    print("end")