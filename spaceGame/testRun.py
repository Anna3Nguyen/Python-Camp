import pygame, sys


def main():
    pygame.init()

    DISPLAY = pygame.display.set_mode((900, 700))  # sets the size of window
    pygame.display.set_caption('Space Game')

    # Color codes
    MAGENTA = (255, 0, 255)
    GREEN = (0, 255, 0)

    vel = 5  # controls velocity/speed of object

    # Background pic configuration, should be the same size as window
    BACKGROUND_WIDTH = 900
    BACKGROUND_HEIGHT = 700
    SPACE_BACKGROUND = pygame.image.load('space_background.png')
    SCREEN = pygame.transform.rotate(pygame.transform.scale(SPACE_BACKGROUND, (BACKGROUND_WIDTH, BACKGROUND_HEIGHT)),
                                     45)

    pygame.mixer.music.load('Music.mp3')
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play()

    x = 50
    y = 50
    width = 40
    height = 60
    vel = 5

    run = True

    while run:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            x -= vel

        if keys[pygame.K_RIGHT]:
            x += vel

        if keys[pygame.K_UP]:
            y -= vel

        if keys[pygame.K_DOWN]:
            y += vel

        if keys[pygame.K_LEFT] and x == 0:
            sys.exit()

        if keys[pygame.K_RIGHT] and x == 0:
            sys.exit()

        if keys[pygame.K_DOWN] and y == 0:
            sys.exit()

        if keys[pygame.K_UP] and y == 0:
            sys.exit()

        DISPLAY.fill((0, 0, 0))  # Fills the screen with black
        pygame.draw.rect(DISPLAY, (255, 0, 0), (x, y, width, height))
        pygame.display.update()

    pygame.quit()