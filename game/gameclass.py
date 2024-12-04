import game.scenes.scene as scene
from game.objects import BaseObject
from constants import GRID_SIZE, GRID_MEASURE


class Game:
    def __init__(self):
        self.scene_manager = SceneManager(self)
        self.world = World(self)

        # map_obj = Actor(self.map.group)
        # map_obj.maths.velocity.update(0, -0.2, -0.3)
        # self.map.add_object(map_obj)
        # self.scene_manager.add('Ship')
        # self.scene_manager.switch('Ship')


    def update(self):

        self.world.update()

        if self.scene_manager.scene:
            self.scene_manager.scene.update()

    def draw(self, display):

        if self.scene_manager.scene:
            self.scene_manager.scene.draw()
            display.blit(self.scene_manager.scene.surface, (0, 0))


class World(scene.Scene):

    def __init__(self, game):

        scene.Scene.__init__(self, game)
        self.size_y = 1280 * GRID_MEASURE / GRID_SIZE
        self.size_z = 720 * GRID_MEASURE / GRID_SIZE


    def add_object(self, obj: BaseObject):

        self.group.add(obj)

    def _set_size(self, s_y: float, s_z: float):

        self.size_y = s_y
        self.size_z = s_z

    def is_out_of_bounds(self, obj: BaseObject):

        ret_list = []

        if abs(obj.maths.position.y) > self.size_y / 2:
            ret_list.append('y')
        if abs(obj.maths.position.z) > self.size_z / 2:
            ret_list.append('z')

        return ret_list


    def _wrap_back(self, obj: BaseObject, coord: str):
        """
        Performs the world wrap-back logic for the object passed
        :param obj: obj outside world boundaries
        :param coord: either 'y' for the horizontal coordinate or 'z' for the vertical
        """
        # Gets the current exceeded coordinate
        current_coord = getattr(obj.maths.position, coord)

        # Gets the sign of the above
        coord_sign = current_coord/abs(current_coord)

        # Gets the size of the world along the dimension
        world_coord_size = getattr(self, f'size_{coord}')

        # Performs the wrap-back
        next_coord = current_coord - coord_sign * world_coord_size

        setattr(obj.maths.position, coord, next_coord)


    def update(self):

        super().update()

        # wrap-back logic
        for obj in self.group:

            # Checks if object is oob
            coord_list = self.is_out_of_bounds(obj)

            # Performs the wrap-back for the appropriate coordinates
            for coord in coord_list:
                self._wrap_back(obj, coord)


class SceneManager:

    def __init__(self, game):

        self.game = game
        self.scenes = {}
        self.scene = None

    @staticmethod
    def exists(scene_key: str):
        return scene_key in scene.__all__


    def add(self, scene_key: str):

        if self.exists(scene_key) and scene_key not in self.scenes.keys():

            self.scenes[scene_key] = scene.__dict__.get(scene_key)(self.game)


    def remove(self, scene_key: str):

        if self.exists(scene_key) and scene_key in self.scenes.keys():

            self.scenes.pop(scene_key)


    def switch(self, scene_key: str):

        if self.exists(scene_key) and scene_key in self.scenes.keys():
            if self.scene:
                self.scene.exit()

            self.scene = self.scenes[scene_key]
            self.scene.enter()
