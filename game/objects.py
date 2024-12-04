import constants
import game.sprite as sprite
import game.maths as m


class BaseObject(sprite.Sprite):

    def __init__(self, source, *groups):

        sprite.Sprite.__init__(self, source, *groups)

        self.maths = m.BaseLogic(self.rect)

        self.action_group: sprite.Group = sprite.Group()

    def update(self, *args, **kwargs):

        self.maths.update(*args, **kwargs)


class StaticObject(BaseObject):

    def __init__(self, source, *groups):

        BaseObject.__init__(self, source, *groups)

        self.maths = m.IMaths(self.rect)


class DynamicObject(BaseObject):

    def __init__(self, source, *groups):

        BaseObject.__init__(self, source, *groups)

        self.maths = m.IPhysics(self.rect)


    def bind(self, obj: 'DynamicObject'):
        """
        Fixes the object to the provided object's movement
        """
        self.maths.bind(obj.maths)


class TriggerObject(DynamicObject):

    def __init__(self, size: tuple[int, int], *groups):

        DynamicObject.__init__(self, size, *groups)

        self.trigger_function = None


    def is_within(self, obj: BaseObject) -> bool:
        """
        Checks if passed object is within the camera boundaries
        :param obj: Object to be tested
        :return: Either True if is within or False otherwise
        """
        return self.maths.is_within(obj.maths)


    def check_group(self, group):
        """
        Checks if any object of the defined seek group is within the trigger boundaries
        :return: A list of the objects which satisfy the condition
        """
        ret_list = []

        for obj in group:

            if self.is_within(obj):

                ret_list.append(obj)

        return ret_list

    def update(self, check_group, *args, **kwargs):

        super().update(*args, **kwargs)
        # Checks if any object is within its area
        sprites = self.check_group(check_group)

        # Removes all objects in group
        self.action_group.empty()

        # Adds objects within the trigger's area
        self.action_group.add(*sprites)
        print(f'within cam: {sprites}')

        # Performs the trigger action onto the group
        for obj in self.action_group:
            self.trigger_function(obj)
