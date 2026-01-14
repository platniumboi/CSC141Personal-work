# Move a card from deck to hand
import random
def draw_card(hand, deck):

    hand.append(deck.pop())  # take last card from deck

 

def main():

    deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    player_hand = []

    dealer_hand = []

 

    # shuffle the deck

    random.shuffle(deck)

    ...

         # more stuff here; draw starting cards and start the game loop
    def draw_card(player):
        player.append(deck[-1])
        deck.pop()
    def calculate_score(hand):
        score = 0
        for i in hand:
            if hand[i] == "J" or hand[i] == "Q" or hand[i] == "K":
                score = score + 10
            elif hand[i] == "A":
                if score > 11:
                    score = score + 1
                else:
                    score = score + 11
            else:
                score = score + hand[i]
    
 

if __name__ == "__main__":

    main()