import pygame

PLAYER_Y_RATIO = 5/4
GRID_SIZE = 32

def Render_Text(what, color, where):
    font = pygame.font.Font(None, 30)
    text = font.render(what, 1, pygame.Color(color))
    screen.blit(text, where)


def render_player():
    screen_size = screen.get_size()
    player_size = (4, 6)
    rect = (screen_size[0]/2 - player_size[0], screen_size[1]/PLAYER_Y_RATIO - player_size[1], player_size[0], player_size[1])
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), rect)


def render_grid():
    for xx in range(0, screen.get_width(), GRID_SIZE):
        for yy in range(0, screen.get_height(), GRID_SIZE):
            pygame.draw.rect(screen, (35, 35, 35), (xx - 2, yy - 2, GRID_SIZE, GRID_SIZE), 1)

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
lag = 0.
MS_PER_UPDATE = 3
FRAME_RATE = 60
running = True

while running:
    elapsed = clock.tick(FRAME_RATE)
    lag += elapsed

    # EVENT PROCESSING
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    while lag >= MS_PER_UPDATE:
        # PHYSICS UPDATE
        # here
        lag -= MS_PER_UPDATE

    # RENDERING
    interpolation_factor = lag / MS_PER_UPDATE
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    Render_Text(str(int(clock.get_fps())), (255, 0, 0), (0, 0))

    render_grid()
    render_player()

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()
