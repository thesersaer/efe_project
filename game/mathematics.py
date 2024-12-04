import pygame as pyg
from numpy.random.mtrand import Sequence

from constants import GRID_SIZE, GRID_MEASURE


def to_screen(quantity):

    if isinstance(quantity, Sequence):
        return type(quantity)(x * (GRID_SIZE / GRID_MEASURE) for x in quantity)

    return quantity * (GRID_SIZE / GRID_MEASURE)


def to_world(quantity):

    if isinstance(quantity, Sequence):
        return type(quantity)(x * (GRID_MEASURE / GRID_SIZE) for x in quantity)

    return quantity * (GRID_MEASURE / GRID_SIZE)


class IVector:

    def elementwise(self):

        pass

    def to_screen(self):

        return to_screen(self.elementwise())

    def to_world(self):

        return to_world(self.elementwise())


class Vector2(pyg.Vector2, IVector):

    pass


class Vector3(pyg.Vector3, IVector):

    pass


class BaseLogic:
    """
    Base prototype not intended for direct use. Responsible for operations between coordinate systems.
    """

    def __init__(self, sprite_rect: pyg.Rect, origin: str):

        """
        :param sprite_rect: Reference to the sprite's rectangle in screen coordinates
        :param origin: Reference to the sprite's center point. Either 'center' or a combination of 'top'/'mid'/'bottom'
        + 'top'/'bottom'/'left'/'right'
        """
        self._origin: str = origin
        self._sprite_rect = sprite_rect # Sprite rectangle in screen coordinates


class DynamicLogic(BaseLogic):
    """
    Holds the physical properties of any given object.
    """
    def __init__(self, sprite_rect: pyg.Rect):
        
        super().__init__(sprite_rect, origin='center')

        self.position: Vector3 = Vector3()
        self.velocity: Vector3 = Vector3()

        rect_size = to_world(self._sprite_rect.size)
        self._world_rect = pyg.Rect(0, 0, *rect_size)  # Sprite rectangle in world coordinates


    def set_position(self, x):

        pass


    def set_velocity(self, x):

        pass


    def update_rect(self, position: Vector2):
        """
        Base implementation to update the sprite's rectangle position. Must have subclass implementation
        :param position: The new position
        """


class StaticLogic(BaseLogic):
    """
    TODO
    """
    def __init__(self, sprite_rect: pyg.Rect):

        super().__init__(sprite_rect, origin='topleft')


if __name__ == '__main__':

    foo = (1, 1)
    print(to_world(foo))
