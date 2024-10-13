

class GuiRenderer:
    def __init__(self):
        pass

    def render_text(what, color, where):
        font = pygame.font.Font(None, 30)
        text = font.render(what, 1, pygame.Color(color))
        screen.blit(text, where)

    def render_grid():
        for xx in range(0, screen.get_width(), constants.GRID_SIZE):
            for yy in range(0, screen.get_height(), constants.GRID_SIZE):
                pygame.draw.rect(
                    screen,
                    (35, 35, 35),
                    (xx - 2, yy - 2, constants.GRID_SIZE, constants.GRID_SIZE), 1)