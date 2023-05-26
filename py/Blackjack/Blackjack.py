from art import logo
import random
import os

deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def deal_card():
   card = random.choice(deck)
   return card

def calculate_hand(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 21
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)
    

def determine_winner(player_score, dealer_score):
    if (player_score > 21 and dealer_score):
        return "You are bust! You lose..."
    elif (player_score == dealer_score):
        return "Draw..."
    elif (player_score == 0):
        return "Blackjack! You win..."
    elif (dealer_score == 0):
        return "Blackjack! Dealer wins..."
    elif (player_score > 21):
        return "You are bust! You lose..."
    elif (dealer_score > 21):
        return "Dealer is bust! You win..."
    elif (player_score > dealer_score):
        return "You win..."
    else:
        return "You lose..."

   
def play_game():
    print(logo)
    player_hand = []
    dealer_hand = []
    game = False

    for card in range(2):
        player_hand.append(deal_card())
        dealer_hand.append(deal_card())

    while not game:
        player_score = calculate_hand(player_hand)
        dealer_score = calculate_hand(dealer_hand)
        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Dealer's first card: {dealer_hand[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game= True
        else:
            hit = input("Type 'y' to get another card, type 'n' to pass: ")
            if hit == "y":
                player_hand.append(deal_card())
            else:
                game= True

    while dealer_score != 0 and dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = calculate_hand(dealer_hand)

    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")
    print(determine_winner(player_score, dealer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  os.system('cls')
  play_game()
