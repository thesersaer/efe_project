from typing import Optional

import pygame

from game.gameobject import Grid, Player, Camera, CameraViewer
from constants import RESOLUTION_X, RESOLUTION_Y, PLAYER_X_RATIO, PLAYER_Y_RATIO


class Scene:
    """
    Stores objects belonging to a scene
    """
    def __init__(self):

        self.group = pygame.sprite.Group()

        self.surface = pygame.Surface((RESOLUTION_X, RESOLUTION_Y))


    def relative_coord(self, rel_x, rel_y):

        abs_x = int(self.surface.get_width() * rel_x)
        abs_y = int(self.surface.get_height() * rel_y)

        return abs_x, abs_y


    def update(self):

        self.group.update()


    def draw(self):

        self.group.draw(self.surface)


    def blit_scene(self, scene: 'Scene'):
        """
        Draws the passed scene's surface onto this surface
        """
        self.surface.blit(scene.surface, (0, 0))



    def handle_inputs(self):
        pass


class Gui(Scene):

    def __init__(self):

        Scene.__init__(self)

        grid_size = self.relative_coord(0.9, 0.8)

        self.grid = Grid(grid_size, self.group)
        self.grid.rect.center = self.relative_coord(0.5, 0.55)

        self.player = Player(self.relative_coord(PLAYER_X_RATIO, PLAYER_Y_RATIO), self.group)


class MapView(Scene):

    def __init__(self, size: tuple[int, int]):

        Scene.__init__(self)

        self.camera_viewer = CameraViewer(size, self.group)


    def add_camera(self, camera: Camera):

        camera.add(self.group)


    def load_seek_group(self, group):

        self.camera_viewer.camera.seek_group(group)


    def add_viewer(self, camera_viewer: CameraViewer):

        if not self.camera_viewer:
            camera_viewer.add(self.group)
            self.camera_viewer = camera_viewer


class Ship(Gui):

    def __init__(self):

        Gui.__init__(self)

        self.map_view = MapView(self.grid.rect.size)

        camera = Camera(self.grid.rect.size, 1, self.group)
        self.map_view.camera_viewer.set_camera(camera)


    def update(self):

        self.map_view.update()
        Scene.update(self)



    def draw(self):


        # TODO: Fix drawing of instance surfaces onto self surface
        self.map_view.draw()
        self.blit_scene(self.map_view)

        Scene.draw(self)
