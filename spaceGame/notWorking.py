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

    # Configures the x and y coordinate starting position
    x = 700
    y = 500

    # Configure the size of the green block
    width = 40
    height = 40

    while True:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            x -= vel

        if keys[pygame.K_RIGHT]:  # keeps movement of green block inside size of window
            x += vel

        if keys[pygame.K_UP]:
            y -= vel

        if keys[pygame.K_DOWN]:
            y += vel

        if keys[pygame.K_LEFT]:
            sys.exit()

        if keys[pygame.K_RIGHT] and x == 0:
            sys.exit()

        if keys[pygame.K_DOWN] and y == 0:
            sys.exit()

        if keys[pygame.K_UP] and y == 0:
            sys.exit()

        DISPLAY.fill([0, 0, 0])
        DISPLAY.blit(SPACE_BACKGROUND, (0, 0))

        pygame.draw.rect(DISPLAY, MAGENTA, (300, 200, 900, 100))
        pygame.draw.rect(DISPLAY, MAGENTA, (100, 400, 400, 100))
        pygame.draw.rect(DISPLAY, GREEN, (x, y, width, height))
        pygame.display.update()


if __name__ == '__main__':
    main()