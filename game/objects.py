import game.sprite as sprite
import game.maths as m


class Object(sprite.Sprite):

    def __init__(self, source, *groups):

        sprite.Sprite.__init__(self, source, *groups)

        self.maths = m.IMath(self.rect)

        self.action_group = sprite.Group()


class StaticObject(Object):

    def __init__(self, source, *groups):

        Object.__init__(self, source, *groups)


class DynamicObject(Object):

    def __init__(self, source, *groups):

        Object.__init__(self, source, *groups)

        self.maths = m.Physics(self.rect)


    def update(self, *args, **kwargs):
        self.maths.update()


    def bind_to(self, obj: 'DynamicObject'):
        """
        Fixes the current object to the provided object's movement
        """
        self.maths.position  = obj.maths.position
        self.maths.velocity = obj.maths.velocity


class TriggerObject(DynamicObject):

    def __init__(self, size: tuple[int, int], *groups):

        DynamicObject.__init__(self, size, *groups)


    def is_within(self, obj: Object):
        """
        Checks if passed object is within the camera boundaries
        :param obj: Object to be tested
        :return: Either True if is within or False otherwise
        """
        if self.maths.rect.colliderect(obj.maths.rect):

            return True

        else: return False


    def check_group(self):
        """
        Checks if any object of the defined seek group is within the camera boundaries
        :return: A list of the objects which satisfy the condition
        """
        ret_list = []

        for obj in self.action_group.sprites():

            if self.is_within(obj):

                ret_list.append(obj)

        return ret_list
