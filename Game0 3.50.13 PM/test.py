# # Import libraries
# import pygame
# import random
#
# # Generate random numbers for random background color
# r = random.randint(0,255)
# g = random.randint(0,255)
# b = random.randint(0,255)
# background_colour = (r,g,b)
#
# # Set window size
# (width, height) = (900, 700)
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption('F18 Window') # Set window caption
#
# screen.fill(background_colour) # Set the background color
# pygame.display.flip()
#
# # Load the F18 image and scale it
# SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40
# F18_SPACESHIP_IMAGE =  pygame.image.load('plane1.jpg') # Load the images
# F18_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
#     F18_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 45)
#
# # Function to render the F18
# def r_key_press(keys_pressed):
#
#     # Check to see if the r key has been pressed
#     if keys_pressed[pygame.K_r]:
#         # Blit will render the object to the screen
#         screen.blit(F18_SPACESHIP, (300, 300))
#
#     elif keys_pressed[pygame.K_d]:
#         screen.fill(background_colour) # Reset the background to original color
#
#     pygame.display.update() # Update the window display
#
# running = True
#
# while running:
#
#   keys_pressed = pygame.key.get_pressed() # Get all keys that have been pressed
#
#   r_key_press(keys_pressed) # Function to render the F18
#
#   # To close the window
#   for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#       running = False

import pygame, sys

pygame.init()

win = pygame.display.set_mode((900, 700))
pygame.display.set_caption("First Game")

x = 800
y = 600
width = 40
height = 40
vel = 5
MAGENTA = (255, 0, 255)
GREEN = (0, 255, 0)
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

    win.fill((0, 0, 0))  # Fills the screen with black
    pygame.draw.rect(win, (0, 255, 0), (x, y, width, height))
    pygame.draw.rect(win, MAGENTA, (300, 200, 900, 100))
    pygame.draw.rect(win, MAGENTA, (100, 400, 400, 100))
    pygame.draw.rect(win, MAGENTA, (100, 400, 400, 100))
    pygame.display.update()

pygame.quit()