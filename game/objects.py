import game.sprite as sprite
import game.maths as physics


class Object(sprite.Sprite):

    def __init__(self, source, *groups):

        sprite.Sprite.__init__(self, source, *groups)


class StaticObject(Object):

    def __init__(self, source, *groups):

        Object.__init__(self, source, *groups)


class DynamicObject(Object):

    def __init__(self, source, *groups):

        Object.__init__(self, source, *groups)

        self.physics = physics.Physics()


    def update(self, *args, **kwargs):
        self.physics.update()


class TriggerObject(DynamicObject):

    def __init__(self, size: tuple[int, int], *groups):

        DynamicObject.__init__(self, size, *groups)
