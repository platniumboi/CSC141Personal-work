
from random import random

import pygame
from pygame.locals import *
import sys

BLACK = (0, 0, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30
BLUE = (0, 0, 255)

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

class Raindrop:
    __slots__ = ['x', 'y', 'radius']
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 1
    
    def draw(self, window):
        pygame.draw.circle(window, (255, 255, 255), (self.x, self.y), self.radius)

    def update(self):
        self.radius += 0.1

class RaindropsManager:
    RAIN_RATE = 0.01
    MAX_RADIUS = 10
    def __init__(self):
        self.raindrops = []
        self.time_since_last_rain = 0
    
    def run(self, time_passed):
        self.time_since_last_rain += time_passed
        if self.time_since_last_rain > RaindropsManager.RAIN_RATE:
            self.time_since_last_rain = 0
            new_raindrop = Raindrop(random() * WINDOW_WIDTH, random() * WINDOW_HEIGHT)
            self.raindrops.append(new_raindrop)
        
        for raindrop in self.raindrops[:]:
            raindrop.update()
            if raindrop.radius > RaindropsManager.MAX_RADIUS:
                self.raindrops.remove(raindrop)
            else:
                raindrop.draw(window)
            

raindrops_manager = RaindropsManager()

while True:
# 7 - Check for and handle events
    delta_time = clock.tick(FRAMES_PER_SECOND) / 1000.0
    window.fill(BLACK)
    raindrops_manager.run(delta_time)
    for event in pygame.event.get():
# Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()