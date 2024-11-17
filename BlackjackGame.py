import random

def deal_card():
    """returns a random card from the deck"""
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10] 
    card = random.choice(cards)
    return card

def calculate_cards(cards):
    """take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) == 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(u_score,c_score):
    if u_score == c_score:
        return "it is a draw"
    elif c_score == 0:
        return "you lose, opponent has a blackjack "
    elif u_score == 0:
        return "you win with a Blackjack"
    elif u_score > 21:
        return "you went over, you lose"
    elif c_score > 21:
        return "opponent went over, you win"
    elif u_score > c_score:
        return "you win"
    elif u_score < c_score:
        return "you lose"
def play_game():

    user_cards = []
    computer_cards = []
    is_game_over = False
    user_score = -1
    computer_score = -1

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while is_game_over != True :
        user_score = calculate_cards(user_cards)
        computer_score = calculate_cards(computer_cards)

        print(f"your cards is {user_cards} and your score is {user_score} ")
        print(f"computer first card is {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            should_deal_again = input("type 'y' to get another card or 'n' to end")
            if should_deal_again == "y":
                user_cards.append(deal_card())
            elif should_deal_again == "n":
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_cards(computer_cards)

    print(f"your final cards is {user_cards} and score is {user_score} ")
    print(f"computer cards is {computer_cards} and score is {computer_score} ")
    print(compare(u_score = user_score, c_score = computer_score))

while input("start a new game of Blackjack type 'y' or 'n':") == "y":
    print("\n" * 20)
    play_game()
