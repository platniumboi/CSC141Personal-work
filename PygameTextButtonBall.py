# Pygame demo text and buttons 

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random
import pygwidgets

# 2 - Define constants
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_PIXELS_PER_FRAME = 3

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  

# 4 - Load assets: image(s), sounds,  etc.

# 5 - Initialize variables


# 6 - Loop forever
while True:

    # 7 - Check for and handle events
    for event in pygame.event.get():
        


    # 8 - Do any "per frame" actions
   
   

    # 9 - Clear the window before drawing it again
    window.fill(BLACK)  # draw a background image
                          
    # 10 - Draw the window elements
   

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait




