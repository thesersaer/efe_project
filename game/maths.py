import pygame
from PIL.ImageOps import scale

from constants import GRID_SIZE, GRID_MEASURE, PHYSICS_TIMESTEP_MS


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

    scaling_factor = GRID_SIZE / GRID_MEASURE

    """
    Base 3-component vector used to describe object information in spacetime.
    x -> t
    y -> x
    z -> y
    """

    def screen_coordinates(self):
        """
        Returns the vector's components in screen coordinates. The vector must have a coinciding origin with the screen.
        """
        vector: pygame.math.Vector3 = self.copy()
        vector = vector.elementwise() * self.scaling_factor
        return vector


class Position(Vector3):
    pass


class Velocity(Vector3):
    pass


class BaseLogic:

    scaling_factor = GRID_MEASURE / GRID_SIZE

    def __init__(self, sprite_rect: pygame.Rect):

        """
        :param sprite_rect: Rectangle of the sprite in screen coordinates
        """

        self.sprite_rect = sprite_rect

        size_x = self.scaling_factor * sprite_rect.size[0]
        size_y = self.scaling_factor * sprite_rect.size[1]

        self.rect = pygame.Rect(0., 0., size_x, size_y)


    def update(self, *args, **kwargs):

        pass


    def copy(self):

        imath = BaseLogic(self.sprite_rect.copy())
        return imath


    def is_within(self, obj_math: 'BaseLogic') -> bool:

        return self.rect.colliderect(obj_math.rect)


class IPhysics(BaseLogic):

    def __init__(self, sprite_rect):

        BaseLogic.__init__(self, sprite_rect)

        self.position = Position()
        self.velocity = Velocity()


    def update(self, *args, **kwargs):

        self.position += self.velocity * PHYSICS_TIMESTEP_MS
        print(self.position)


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


class IMaths(BaseLogic):

    def __init__(self, sprite_rect):

        BaseLogic.__init__(self, sprite_rect)


    def update(self, *args, **kwargs):

        pass


if __name__ == '__main__':

    foo = Vector3(5, 5, 5)
    print([int(x) for x in foo.xyz])