import pygame

def Render_Text(what, color, where):
    font = pygame.font.Font(None, 30)
    text = font.render(what, 1, pygame.Color(color))
    screen.blit(text, where)

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
        lag -= MS_PER_UPDATE

    # RENDERING
    interpolation_factor = lag / MS_PER_UPDATE
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    Render_Text(str(int(clock.get_fps())), (255,0,0), (0,0))

    # flip() the display to put your work on screen
    pygame.display.flip()

pygame.quit()
