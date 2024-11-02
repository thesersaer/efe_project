import pygame

class SpriteI:
    """
    Base Interface for pygame Sprite class
    """
    def __init__(self, source: str | tuple[int, int]):
        """

        :param source: Either the sprite path in str or the size of the rect in px
        """

        if type(source) == str:
            self.image = pygame.image.load(source).convert_alpha()

        else:
            self.image = pygame.Surface(source, pygame.SRCALPHA)

        self.rect = self.image.get_rect()


    def update(self, *args, **kwargs):
        pass


class Sprite(pygame.sprite.Sprite, SpriteI):

    def __init__(self,
                 source: str | tuple[int, int],
                 *groups: pygame.sprite.AbstractGroup):

        pygame.sprite.Sprite.__init__(self, *groups)

        SpriteI.__init__(self, source)


class DirtySprite(pygame.sprite.DirtySprite, SpriteI):

    def __init__(self, source, *groups):

        pygame.sprite.DirtySprite.__init__(self, *groups)

        SpriteI.__init__(self, source)



if __name__ == '__main__':
    foo = Sprite((30, 30))
    print("end")