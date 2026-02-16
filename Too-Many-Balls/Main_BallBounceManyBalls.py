# pygame demo 6(b) - using the Ball class, bounce many balls

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random
from Ball import *  # bring in the Ball class code

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_BALLS = 3
PLAYER_SCORE = 0
LAST_SECONDS = 0
ADDBALLS = pygame.USEREVENT + 1

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()  

# 4 - Load assets: image(s), sounds, etc.

# 5 - Initialize variables
ballList = []
for oBall in range(0, N_BALLS):
    # Each time through the loop, create a Ball object
    oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    ballList.append(oBall)  # append the new Ball to the list of Balls   

def draw_text(surface, text, x, y, color, font_size=24):
    text_font = pygame.font.SysFont(None, font_size)
    text_surface = text_font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)

# 6 - Loop forever
while True:
    
    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()         
        if event.type == pygame.MOUSEBUTTONDOWN:
            for oBall in ballList:
                if oBall.ballRect.collidepoint(pygame.mouse.get_pos()):
                    PLAYER_SCORE += 1
                    break

    LAST_SECONDS = pygame.time.get_ticks() // 1000

    pygame.time.set_timer(ADDBALLS, 1000)  # add a new ball every second
    if event.type == ADDBALLS:
        oBall = Ball(window, WINDOW_WIDTH, WINDOW_HEIGHT)
        ballList.append(oBall)  # append the new Ball to the list of Balls
    
    # 8 - Do any "per frame" actions
    for oBall in ballList:
        oBall.update()  # tell each Ball to update itself

   # 9 - Clear the window before drawing it again
    window.fill(BLACK)
    
    # 10 - Draw the window elements
    for oBall in ballList:
        oBall.draw()   # tell each Ball to draw itself
    draw_text(window, "Score: " + str(PLAYER_SCORE), 10, 10, (255, 255, 255))
    draw_text(window, "Seconds: " + str(LAST_SECONDS), 10, 40, (255, 255, 255))
    # 11 - Update the window
    pygame.display.update()

    if LAST_SECONDS > 15:
        draw_text(window, "Game Over!", 200, 200, (255, 0, 0), font_size=48)
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()
    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait


