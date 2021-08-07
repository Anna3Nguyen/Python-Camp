# Import libraries
import pygame

pygame.init()

# screen size
WIDTH = 1200
HEIGHT = 1000
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
VEL = 5

# title
pygame.display.set_caption('Space Game')
# LOSER_FONT =

# code for background image
BACKGROUND_WIDTH = 1200
BACKGROUND_HEIGHT = 1000
SPACE_BACKGROUND = pygame.image.load('space_background.png')
SCREEN.blit(SPACE_BACKGROUND, (0,0))
SCREEN = pygame.transform.rotate(pygame.transform.scale(
    SPACE_BACKGROUND, (BACKGROUND_WIDTH, BACKGROUND_HEIGHT)), 45)
pygame.display.update()

# music
pygame.mixer.music.load('Music.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play()

# spaceship alien image is loaded and resized
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
PLAYER_SPACESHIP_IMAGE = pygame.image.load('alien.png')
PLAYER_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    PLAYER_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 0)

BLUE = (0,0,255)
pygame.draw.rect(SCREEN, BLUE, (200, 150, 100, 50))
pygame.display.update()

def alien_controls(keys_pressed, alien):
    if keys_pressed[pygame.K_LEFT]:  # LEFT
        alien.x -= VEL
    if keys_pressed[pygame.K_RIGHT]:  # RIGHT
        alien.x += VEL
    if keys_pressed[pygame.K_UP]:  # UP
        alien.y -= VEL
    if keys_pressed[pygame.K_DOWN]:  # DOWN
        alien.y += VEL




is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

pygame.quit()
# if __name__ == '__main__':
#     main()



