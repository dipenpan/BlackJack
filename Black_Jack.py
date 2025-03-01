import random

# Initialize deck
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4  # J, Q, K as 10, A as 11

# Function to deal a card
def deal_card(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)

# Function to calculate hand total
def calculate_total(hand):
    total = sum(hand)
    ace_count = hand.count(11)

    while total > 21 and ace_count:  # Convert Ace from 11 to 1 if necessary
        total -= 10
        ace_count -= 1

    return total

# Function to reveal the dealer's hand
def reveal_dealer_hand():
    return dealer_hand[0], "X"

# Initialize player and dealer hands
player_hand = []
dealer_hand = []

# Deal two cards to each player
for _ in range(2):
    deal_card(player_hand)
    deal_card(dealer_hand)

player_in = True
dealer_in = True

# Game Loop
while player_in or dealer_in:
    print(f"\nDealer's Hand: {reveal_dealer_hand()}")
    print(f"Your Hand: {player_hand} (Total: {calculate_total(player_hand)})")

    # Player Turn
    if player_in:
        choice = input("1: Stay\n2: Hit\n")
        if choice == "2":
            deal_card(player_hand)
            if calculate_total(player_hand) > 21:
                print(f"\nYour Hand: {player_hand} (Total: {calculate_total(player_hand)})")
                print("You busted! Dealer wins.")
                break
        else:
            player_in = False

    # Dealer Turn
    if dealer_in and calculate_total(dealer_hand) < 17:
        deal_card(dealer_hand)
    else:
        dealer_in = False

    # Dealer Bust Check
    if calculate_total(dealer_hand) > 21:
        print(f"\nDealer's Hand: {dealer_hand} (Total: {calculate_total(dealer_hand)})")
        print("Dealer busted! You win.")
        break

# End Game Results
if calculate_total(player_hand) <= 21 and calculate_total(dealer_hand) <= 21:
    print(f"\nFinal Hands:\nDealer: {dealer_hand} (Total: {calculate_total(dealer_hand)})\nPlayer: {player_hand} (Total: {calculate_total(player_hand)})")
    if calculate_total(player_hand) > calculate_total(dealer_hand):
        print("You win!")
    elif calculate_total(player_hand) < calculate_total(dealer_hand):
        print("Dealer wins.")
    else:
        print("It's a tie!")
