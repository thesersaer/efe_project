import game.scenes.scene as scene
from game.objects import Object
from game.gameobject import Actor


class Game:
    def __init__(self):
        self.scene_manager = SceneManager()
        self.map = Map()

        # map_obj = Actor(self.map.group)
        # map_obj.maths.velocity.update(0, -0.2, -0.3)
        # self.map.add_object(map_obj)
        # self.scene_manager.add('Ship')
        # self.scene_manager.switch('Ship')


    def update(self):
        if self.scene_manager.scene:
            self.scene_manager.scene.update()

    def draw(self, display):
        if self.scene_manager.scene:
            self.scene_manager.scene.draw()
            display.blit(self.scene_manager.scene.surface, (0, 0))


class Map(scene.Scene):

    def __init__(self):

        scene.Scene.__init__(self)


    def add_object(self, obj: Object):

        self.group.add(obj)


class SceneManager:

    def __init__(self):

        self.scenes = {}
        self.scene = None

    @staticmethod
    def exists(scene_key: str):
        return scene_key in scene.__all__


    def add(self, scene_key: str):

        if self.exists(scene_key) and scene_key not in self.scenes.keys():

            self.scenes[scene_key] = scene.__dict__.get(scene_key)()


    def remove(self, scene_key: str):

        if self.exists(scene_key) and scene_key in self.scenes.keys():

            self.scenes.pop(scene_key)


    def switch(self, scene_key: str):

        if self.exists(scene_key) and scene_key in self.scenes.keys():
            if self.scene:
                self.scene.exit()

            self.scene = self.scenes[scene_key]
            self.scene.enter()