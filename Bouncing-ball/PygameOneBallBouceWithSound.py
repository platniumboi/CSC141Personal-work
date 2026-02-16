# pygame demo 4(c), one image, bounce around the window - with sound

# 1 - Import packages
import pygame
from pygame.locals import *
import sys
import random

# 2 - Define constants
BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
N_PIXELS_PER_FRAME = 3

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
 
# 4 - Load assets: image(s), sound(s),  etc.
ballImage = pygame.image.load('images/ball.png')
bounceSound = pygame.mixer.Sound('sounds/boing.wav')
pygame.mixer.music.load('sounds/background.mp3')
pygame.mixer.music.play(-1, 0.0)


# 5 - Initialize variables
ballRect = ballImage.get_rect()
MAX_WIDTH = WINDOW_WIDTH - ballRect.width
MAX_HEIGHT = WINDOW_HEIGHT - ballRect.height
ballRect.left = random.randrange(MAX_WIDTH)
ballRect.top = random.randrange(MAX_HEIGHT)
xSpeed = N_PIXELS_PER_FRAME
ySpeed = N_PIXELS_PER_FRAME
SCORE = 0
TIMER = 0
 
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
        # Clicked the close button? Quit pygame and end the program  
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if ballRect.collidepoint(pygame.mouse.get_pos()):
                SCORE += 1
                bounceSound.play()
                ballRect.left = random.randrange(MAX_WIDTH)
                ballRect.top = random.randrange(MAX_HEIGHT)
                ballRect.left = ballRect.left + xSpeed + random.randint(-5, 5)
                ballRect.top = ballRect.top + ySpeed + random.randint(-5, 5)
                
    
    # 8 - Do any "per frame" actions
    if (ballRect.left < 0) or (ballRect.right >= WINDOW_WIDTH):
        xSpeed = -xSpeed  # reverse X direction
        bounceSound.play()

    if (ballRect.top < 0) or (ballRect.bottom >= WINDOW_HEIGHT):
        ySpeed = -ySpeed  # reverse Y direction
        bounceSound.play()

    if pygame.time.get_ticks() - TIMER > 1000:  # every second
        TIMER = pygame.time.get_ticks()

    if SCORE >= 5:
        window.fill(BLACK)
        draw_text(window, 'You win!', 250, 200, (255, 255, 0), font_size=50)
        draw_text (window, f"Time: {TIMER // 1000} seconds", 250, 260, (255, 255, 255), font_size=30)
        pygame.display.update()
        pygame.time.wait(3000)  # Wait for 3 seconds before quitting
        pygame.quit()
        sys.exit()

    # Update the rectangle of the ball, based on the speed in two directions
    ballRect.left = ballRect.left + xSpeed
    ballRect.top = ballRect.top + ySpeed 

    # 9 - Clear the window before drawing it again
    window.fill(BLACK)
    
    # 10 - Draw the window elements
    window.blit(ballImage, ballRect)

    draw_text(window, f'Score: {SCORE}', 10, 10, (255, 255, 255), font_size=30)

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
