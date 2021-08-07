import pygame, sys

pygame.init()

DISPLAY = pygame.display.set_mode((900, 700))  # sets the size of window
pygame.display.set_caption('Space Game')

# dimensions of green rect
x = 800
y = 600
width = 40
height = 40

vel = 5

MAGENTA = (255, 0, 255)
GREEN = (0, 255, 0)

# music
pygame.mixer.music.load('Music.mp3')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()

# background imaging
BACKGROUND_WIDTH = 900
BACKGROUND_HEIGHT = 700
SPACE_BACKGROUND = pygame.image.load('space_background.png')
SCREEN = pygame.transform.rotate(pygame.transform.scale(SPACE_BACKGROUND, (BACKGROUND_WIDTH, BACKGROUND_HEIGHT)),
                                     45)
run = True
while run:
    pygame.time.delay(50)

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
    DISPLAY.blit(SPACE_BACKGROUND, (0, 0))

    pygame.draw.rect(DISPLAY, (0, 255, 0), (x, y, width, height))
    pygame.draw.rect(DISPLAY, MAGENTA, (300, 200, 900, 100))
    pygame.draw.rect(DISPLAY, MAGENTA, (100, 400, 700, 100))
    pygame.draw.rect(DISPLAY, MAGENTA, (100, 100, 100, 600))
    pygame.display.update()

pygame.quit()