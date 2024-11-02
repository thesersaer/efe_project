import pygame

from game.gameobject import Grid, Actor


class Scene:
    """
    Stores objects belonging to a scene
    """
    def __init__(self):

        self.group = pygame.sprite.Group()


    def update(self):

        self.group.update()


    def draw(self, display: pygame.Surface):

        self.group.draw(display)


    def handle_inputs(self):
        pass


class Gui(Scene):

    def __init__(self):

        Scene.__init__(self)

        Grid(self.group)
        Actor(self.group)