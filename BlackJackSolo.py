# Move a card from deck to hand
import random
def draw_card(hand, deck):

    hand.append(deck.pop())  # take last card from deck

def calculate_score(hand):
        score = 0
        for i in range(len(hand)):
            if hand[i] == "J" or hand[i] == "Q" or hand[i] == "K":
                score = score + 10
            elif hand[i] == "A":
                if score > 11:
                    score = score + 1
                else:
                    score = score + 11
            else:
                score = score + int(hand[i])
        if score > 21:
            return "bust"
        else:
            return score

def print_status(player):
    for i in range(len(player)):
        print(player[i])
 
 

def main():

    deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    player_hand = []

    dealer_hand = []

    active = True
    able_to_draw = True
    dealer_wants_to_draw = True

    # shuffle the deck

    random.shuffle(deck)

    # draw starting cards
    draw_card(player_hand, deck)
    draw_card(player_hand, deck)
    draw_card(dealer_hand, deck)
    draw_card(dealer_hand, deck)

    while active == True:
        print("Your hand:")
        print_status(player_hand)
        print("Dealer's hand:")
        print_status(dealer_hand)
        print("")
        if able_to_draw == True:
            player_input = input("Do you want to hit or stand? (h/s): ")
            print("")
            if player_input == "h":
                draw_card(player_hand, deck)
            elif player_input == "s":
                able_to_draw = False
            if calculate_score(player_hand) == "bust":
                print("")
                print("Your hand:")
                print_status(player_hand)
                print("Dealer's hand:")
                print_status(dealer_hand)
                print("")
                print("You busted! Dealer wins!")
                active = False
        elif calculate_score(player_hand) <= 21 and able_to_draw == False:
            print("You chose to stand with a score of", calculate_score(player_hand))
            able_to_draw = False
        
        if dealer_wants_to_draw and calculate_score(dealer_hand) != "bust" and calculate_score(dealer_hand) < 17:
            draw_card(dealer_hand, deck)
        elif calculate_score(dealer_hand) == "bust":
            print("")
            print("Your hand:")
            print_status(player_hand)
            print("Dealer's hand:")
            print_status(dealer_hand)
            print("")
            print("Dealer busted! You win!")
            active = False
        elif calculate_score(dealer_hand) >= 17:
            dealer_wants_to_draw = False
        if able_to_draw == False and dealer_wants_to_draw == False:
            player_score = calculate_score(player_hand)
            dealer_score = calculate_score(dealer_hand)
            if player_score > dealer_score:
                print("You win!")
            elif dealer_score > player_score:
                print("Dealer wins!")
            else:
                print("It's a tie!")
            active = False


    # more stuff here; draw starting cards and start the game loop


if __name__ == "__main__":

    main()