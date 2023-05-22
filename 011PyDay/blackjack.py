# Day 11: Blackjack

import random

# Get a random card
def get_card():
    """Returns a random card from the deck."""
    # Infinite deck of cards
    cards = [11, 2, 3, 4, 5, 7, 8, 9, 10, 10, 10, 10]
    
    card = random.choice(cards)

    return card

def calculate_points(cards):
    """Takes a list of cards and returns the sum of its points"""
    # Check if it is a blackjack
    if len(cards) == 2 and sum(cards) == 21:
        return 0 # 0 represents a blackjack

    # Check if an ace can be seen as 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(player_points, computer_points):
    """Takes points as arguments to compare who wins"""
    if player_points > 21 and computer_points > 21:
        return "No one wins..."

    if player_points == computer_points:
        return "It's a draw"
    elif computer_points == 0:
        return "You loose, computer won with a Blackjack."
    elif player_points == 0:
        return "You win with a Blackjack!"
    elif computer_points > 21:
        return "You win! Computer lost."
    elif player_points > 21:
        return "You loose."
    elif player_points > computer_points:
        return "You win!"
    else:
        return "You loose. Computer wins."


# Give two cards to cpu and to player
player_cards = []
computer_cards = []
is_game_over = False


for _ in range(2):
    new_player_card = get_card()
    new_computer_card = get_card()

    player_cards.append(new_player_card)
    computer_cards.append(new_computer_card)


computer_points = calculate_points(computer_cards)

while not is_game_over:
    player_points = calculate_points(player_cards)
    print(f"-Your cards: {player_cards}, total points are {player_points}")
    print(f"-Computer's first card: {computer_cards[0]}")

    if player_points == 0 or computer_points == 0 or player_points > 21:
        is_game_over = True
    else:
        should_get_card = input("Do you want to get a new card? 'y' or 'n' -> ")
        if should_get_card == 'y':
            new_player_card = get_card()
            player_cards.append(new_player_card)
        else:
            is_game_over = True

while computer_points != 0 and computer_points < 17:
    new_computer_card = get_card()
    computer_cards.append(new_computer_card)
    computer_points = calculate_points(computer_cards)


print(f"-Your final hand: {player_cards}, final points are {player_points}")
print(f"-Computer's final hand: {computer_cards}, final score {computer_points}")
print(compare(player_points, computer_points))
