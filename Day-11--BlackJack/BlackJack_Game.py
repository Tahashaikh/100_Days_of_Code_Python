import random

cards = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10,
         "A", "A", "A", "A", "K", "K", "K", "K", "Q", "Q", "Q", "Q", "J", "J", "J", "J"]
random.shuffle(cards)
User_cards = []
computer_cards = []


def assign_card():
    card_index = random.randint(0, len(cards) - 1)
    selected_card = (cards[card_index])
    cards.remove(selected_card)
    return selected_card


def calculate_score(list):
    list1 = list
    for index in range(0, len(list1)):
        if list1[index] == 'K' or list1[index] == 'Q' or list1[index] == 'J':
            list1[index] = 10
    for index in range(0, len(list1)):
        if list1[index] == 'A':
            list1[index] = 11
            if sum(list1) > 21:
                list1[index] = 1
    return sum(list1)



def check_winner(another_card):
    if another_card == 'y':
        User_cards.append(assign_card())
        current_score = calculate_score(User_cards)
        if current_score[0] > 21:
            print(f"Your Cards are ----{User_cards}")
            print(f"Computer Cards are ----{computer_cards}")
            print(f"YOUR SCORE = {current_score[0]} and COMPUTER SCORE IS = {current_score[1]}")
            print("You Lose")
            return "LOSE"
        else:
            print(f"Your Cards are ----{User_cards}")
            print(f"Computer Cards are ----[{computer_cards[0]},*]")
            print(f"YOUR SCORE = {current_score[0]} and COMPUTER SCORE IS = {computer_cards[0]}")
    else:
        while True:
            current_score = calculate_score(User_cards, computer_cards)
            print(f"Your Cards are ----{User_cards}")
            print(f"Computer Cards are ----{computer_cards}")
            print(f"YOUR SCORE = {current_score[0]} and COMPUTER SCORE IS = {current_score[1]}")
            if current_score[1] == current_score[0] <= 21:
                return "DRAW"
            if current_score[1] > 21:
                return "WIN"
            if 21 >= current_score[1] > current_score[0]:
                return "LOSE"
            if 21 > current_score[1] < current_score[0]:
                computer_cards.append(assign_card())


def play_again():
    while True:
        play_game_again = input("Do You Want to play again [Y/N]:")
        if play_game_again == 'y' or play_game_again == 'n':
            if play_game_again == 'n':
                return False

            else:
                return True

        else:
            print("Incorrect Decision")


def play_game():
    while True:
        for i in range(0, 2):
            user_cards.append(assign_card())
            com_cards.append(assign_card())
        print("Game Started")
        print(f"Your Cards are ----{user_cards}")
        print(f"Computer Cards are ----[{com_cards[0]},*]")
        current_score = calculate_score(user_cards, com_cards)
        print(f"YOUR SCORE ={current_score[0]} and COMPUTER SCORE IS = {com_cards[0]}")
        while True:
            another_card = input("Do you want another card [Y/N]: ").lower()
            if another_card == 'y' or another_card == 'n':
                winner = check_winner(another_card)
                if winner == 'WIN':
                    print("Congratulation on Your Winning This is Your Day")
                elif winner == 'DRAW':
                    print("ITS A DRAW PLEASE TRY AGAIN")
                    play_game_again = input("Do You Want to play again [Y/N]")
                elif winner == 'LOSE':
                    print("BETTER LUCK NEXT TIME")
                    play_game_again = input("Do You Want to play again [Y/N]")
            else:
                print("Incorrect Decision")


play_game()
if play_again():
    user_cards = []
    com_cards = []
    play_game()
else:
    print("Good Bye")
