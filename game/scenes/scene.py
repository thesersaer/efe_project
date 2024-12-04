from typing import Optional

import pygame

from game.gameobject import Grid, Player, Camera, CameraViewer
from constants import RESOLUTION_X, RESOLUTION_Y, PLAYER_X_RATIO, PLAYER_Y_RATIO


class Scene:
    """
    Stores objects belonging to a scene
    """
    def __init__(self, game):

        self.game = game

        self.group = pygame.sprite.Group()

        self.surface = pygame.Surface((RESOLUTION_X, RESOLUTION_Y))

        self.boot()


    def boot(self):
        """
        Executes when the scene is created
        """
        pass


    def enter(self):
        """
        Executes whenever the scene is brought to the screen
        """
        pass


    def exit(self):
        """
        Executes whenever the scene is removed from the screen
        """
        pass


    def update(self, *args, **kwargs):

        self.group.update(*args, **kwargs)


    def draw(self):

        self.group.draw(self.surface)


    def blit_scene(self, scene: 'Scene'):
        """
        Draws the passed scene's surface onto this surface
        """
        self.surface.blit(scene.surface, (0, 0))


    def abs_coord(self, rel_x, rel_y):

        abs_x = int(self.surface.get_width() * rel_x)
        abs_y = int(self.surface.get_height() * rel_y)

        return abs_x, abs_y


class Gui(Scene):

    def __init__(self, game):

        Scene.__init__(self, game)

        grid_size = self.abs_coord(0.9, 0.8)

        self.grid = Grid(grid_size, self.group)
        self.grid.rect.center = self.abs_coord(0.5, 0.55)

        self.player = Player(self.abs_coord(PLAYER_X_RATIO, PLAYER_Y_RATIO), self.group)


class MapView(Scene):

    def __init__(self, game):

        Scene.__init__(self, game)

        self.camera_viewer = CameraViewer(self.surface.get_size(), self.group)


    def update(self, *args, **kwargs):

        super().update(self.game.world.group)


    def draw(self):

        self.camera_viewer.draw_view()
        super().draw()


class Ship(Gui):

    def __init__(self, game):

        Gui.__init__(self, game)

        self.map_view = MapView(game)


    def update(self):

        self.map_view.update()
        super().update()


    def draw(self):


        # TODO: Fix drawing of instance surfaces onto self surface
        self.map_view.draw()
        self.blit_scene(self.map_view)

        super().draw()

__all__ = ['Gui', 'MapView', 'Ship']

if __name__ == '__main__':
    print(dict)