import game.scenes.scene as scene
from game.objects import Object
from game.gameobject import Actor


class Game:
    def __init__(self):
        self.scenes = {}
        self._active_scene = None
        self.map = Map()

        map_obj = Actor(self.map.group)
        map_obj.maths.velocity.update(0, -0.2, -0.3)
        self.map.add_object(map_obj)

        self.scenes.update({'ship': scene.Ship()})
        self.set_active_scene('ship')
        self.active_scene.map_view.load_seek_group(self.map.group)


    @property
    def active_scene(self):
        return self.scenes[self._active_scene]

    def set_active_scene(self, scene_key):
        if scene_key in self.scenes.keys():
            self._active_scene = scene_key

    def update(self):
        self.scenes[self._active_scene].update()

    def draw(self, display):

        self.active_scene.draw()
        display.blit(self.active_scene.surface, (0, 0))


class Map(scene.Scene):

    def __init__(self):

        scene.Scene.__init__(self)


    def add_object(self, obj: Object):

        self.group.add(obj)