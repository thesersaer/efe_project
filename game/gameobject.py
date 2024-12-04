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

        # Set margins for the camera trigger
        size = tuple(x + 100 for x in size)

        TriggerObject.__init__(self, size, *groups)


class CameraViewer(StaticObject):

    def __init__(self, size: tuple[int, int], *groups):

        StaticObject.__init__(self, size, *groups)

        self.camera = Camera(size)

        self.camera.trigger_function = self.on_camera_trigger


    def draw_view(self):
        """
        Draws what the camera is viewing onto this sprite, then draws the sprite onto the passed surface
        """
        # Clear the surface
        self.image.fill((0, 0, 0))

        # Go through all objects within the viewer's range:
        for obj in self.action_group:
            # Gets the object's math relative to the camera
            relative_frame = obj.maths.relative_to(self.camera.maths)

            # Draw it onto self
            screen_coords = relative_frame.position.screen_coordinates()
            self.image.blit(obj.image, tuple(int(x) for x in screen_coords.yz))


    def update(self, *args, **kwargs):

        # Checks for world objects within the camera's boundary
        self.camera.update(*args, **kwargs)

        # Those in camera range are checked if are in viewer's range via the trigger_function


    def on_camera_trigger(self, obj: DynamicObject):
        # Performed each time the camera registers a new object

        # Fist empty action group
        self.action_group.empty()

        # Detect if object is within viewer's boundary
        if self.maths.is_within(obj.maths):
            # If true, add it to the action group
            self.action_group.add(obj)
            print(f'within viewer: {obj}')


if __name__ == '__main__':
    foo = Camera()
    print(foo)