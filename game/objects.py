import game.sprite as sprite
import game.maths as m


class Object(sprite.Sprite):

    def __init__(self, source, *groups):

        sprite.Sprite.__init__(self, source, *groups)

        self.maths = m.IMath(self.rect)

        self.action_group = sprite.Group()

    def update(self, *args, **kwargs):
        self.maths.update(*args, **kwargs)


    def draw(self, surface):

        pass


class StaticObject(Object):

    def __init__(self, source, *groups):

        Object.__init__(self, source, *groups)

        self.maths = m.ILogic(self.rect)


    def draw(self, surface):

        pass


class DynamicObject(Object):

    def __init__(self, source, *groups):

        Object.__init__(self, source, *groups)

        self.maths = m.IPhysics(self.rect)


    def draw(self, surface):

        pass


    def bind(self, obj: 'DynamicObject'):
        """
        Fixes the object to the provided object's movement
        """
        self.maths.bind(obj.maths)


class TriggerObject(DynamicObject):

    def __init__(self, size: tuple[int, int], *groups):

        DynamicObject.__init__(self, size, *groups)


    def is_within(self, obj: Object) -> bool:
        """
        Checks if passed object is within the camera boundaries
        :param obj: Object to be tested
        :return: Either True if is within or False otherwise
        """
        return self.maths.is_within(obj.maths)


    def check_group(self):
        """
        Checks if any object of the defined seek group is within the trigger boundaries
        :return: A list of the objects which satisfy the condition
        """
        ret_list = []

        for obj in self.action_group.sprites():

            if self.is_within(obj):

                ret_list.append(obj)

        return ret_list
