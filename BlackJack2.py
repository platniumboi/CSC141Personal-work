

from ast import main
from concurrent.futures import wait

import pygame
import random
import sys
import pygame_widgets
from pygame_widgets.button import Button

#constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 30

pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Blackjack")
clock = pygame.time.Clock()

class Card:
    def __init__(self, rank):
        self.rank = rank
    
    def __str__(self):
        return f"{self.rank}"
    
class Deck:
    def __init__(self):
        self.cards = [Card(rank) for rank in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]]
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw_card(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.stood = False
    
    def draw_card(self, deck):
        self.cards.append(deck.draw_card())

    def stand(self):
        self.stood = True

class Player:
    def __init__(self):
        self.hand = Hand()

    def calculate_score(self, hand):
        score = 0
        for i in range(len(hand)):
            if hand[i].rank == "J" or hand[i].rank == "Q" or hand[i].rank == "K":
                score = score + 10
            elif hand[i].rank == "A":
                if score > 11:
                    score = score + 1
                else:
                    score = score + 11
            else:
                score = score + int(hand[i].rank)
        if score > 21:
            return False
        else:
            return score

class Dealer(Player):
    def __init__(self):
        super().__init__()
    
    def play(self, deck):
        while self.calculate_score(self.hand.cards) < 17:
            self.hand.draw_card(deck)
        self.hand.stand()
        

class Human(Player):
    def __init__(self):
        super().__init__()
 
class Game:
    def __init__(self):
        self.mainDeck = Deck()
        self.mainDeck.shuffle()
        self.player = Human()
        self.dealer = Dealer()
        for i in range(2):
            self.player.hand.draw_card(self.mainDeck)
            self.dealer.hand.draw_card(self.mainDeck)
        
    def draw(self, surface):
        self.drawtext(surface, "Player's Hand:", 50, 50, BLACK)
        for i in range(len(self.player.hand.cards)):
            self.drawtext(surface, str(self.player.hand.cards[i]), 50, 80 + i * 30, BLACK)
        self.drawtext(surface, "Dealer's Hand:", 350, 50, BLACK)
        for i in range(len(self.dealer.hand.cards)):
            self.drawtext(surface, str(self.dealer.hand.cards[i]), 350, 80 + i * 30, BLACK) 
        
    def drawtext(self, surface, text, x, y, color, font_size=24):
        text_font = pygame.font.SysFont(None, font_size)
        text_surface = text_font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        surface.blit(text_surface, text_rect)

    def current_turn(self):
        if self.player.hand.stood == False:
            return True
        else:
            return False

    def reset(self):
        self.__init__()

Hit_button = Button(window, 100, 300, 100, 50, text="Hit", fontSize=30, margin=20, onClick=lambda: game.player.hand.draw_card(game.mainDeck))
Stand_button = Button(window, 250, 300, 100, 50, text="Stand", fontSize=30, margin=20, onClick=lambda: game.player.hand.stand())
Reset_button = Button(window, 400, 300, 100, 50, text="Reset", fontSize=30, margin=20, onClick=lambda: game.reset())
    
    
game = Game()

playing = True
events = pygame.event.get()
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False

    if game.current_turn() == False:
        game.dealer.play(game.mainDeck)

    window.fill(GREEN)

    Hit_button.draw()
    Stand_button.draw()
    Reset_button.draw()
    game.draw(window)

    if game.player.calculate_score(game.player.hand.cards) == False:
        game.drawtext(window, "Dealer wins!", 200, 400, BLACK, font_size=40)
    elif game.dealer.calculate_score(game.dealer.hand.cards) == False:
        game.drawtext(window, "Player wins!", 200, 400, BLACK, font_size=40)
    elif game.player.calculate_score(game.player.hand.cards) > game.dealer.calculate_score(game.dealer.hand.cards) and game.player.hand.stood == True and game.dealer.hand.stood == True:
        game.drawtext(window, "Player wins!", 200, 400, BLACK, font_size=40)
    elif game.dealer.calculate_score(game.dealer.hand.cards) > game.player.calculate_score(game.player.hand.cards) and game.player.hand.stood == True and game.dealer.hand.stood == True:
        game.drawtext(window, "Dealer wins!", 200, 400, BLACK, font_size=40)

    pygame_widgets.update(events)
    pygame.display.update()
    clock.tick(FRAMES_PER_SECOND)