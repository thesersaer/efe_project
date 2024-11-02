import pygame.sprite

import game.scenes.scene as scene


class Game:
    def __init__(self):
        self.scenes = {}
        self._active_scene = None

        self.scenes.update({'gui': scene.Gui()})

    def set_active_scene(self, scene_key):
        if scene_key in self.scenes.keys():
            self._active_scene = scene_key

    def update(self):
        self.scenes[self._active_scene].update()

    def draw(self, display):
        self.scenes[self._active_scene].draw(display)


class Map:
    def __init__(self):
        pass


class ObjectGroup:
    def __init__(self):
        self.group = []
        self._sprite_group = pygame.sprite.Group()

    def add(self, game_object):
        self.group.append(game_object)
        game_object.add(self._sprite_group)

    def remove(self, game_object):
        self.group.remove(game_object)
        game_object.remove(self._sprite_group)

    def draw(self, surface):
        self._sprite_group.draw(surface)

    def update(self):
        self._sprite_group.update()
