from game import engineclass as en
from game.gameobject import Actor


class TestEngine(en.GameEngine):
    def __init__(self):
        en.GameEngine.__init__(self)

        self.game.scene_manager.add('MapView')
        self.game.scene_manager.switch('MapView')

        obj1 = Actor(self.game.world.group)
        # obj1.maths.position.update(0., 1280/3.2, 720/3.2)
        self.game.scene_manager.scene.camera_viewer.camera.maths.bind(obj1.maths)
        obj1.maths.velocity.update(0., 0.2, 0.3)

        print('boot end')



if __name__ == '__main__':
    foo = TestEngine()
    foo.start()