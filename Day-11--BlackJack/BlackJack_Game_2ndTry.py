import random

cards = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10,
         "A", "A", "A", "A", "K", "K", "K", "K", "Q", "Q", "Q", "Q", "J", "J", "J", "J"]
random.shuffle(cards)

black_Jack = """########  ##          ###     ######  ##    ##          ##    ###     ######  ##    ## 
##     ## ##         ## ##   ##    ## ##   ##           ##   ## ##   ##    ## ##   ##  
##     ## ##        ##   ##  ##       ##  ##            ##  ##   ##  ##       ##  ##   
########  ##       ##     ## ##       #####             ## ##     ## ##       #####    
##     ## ##       ######### ##       ##  ##      ##    ## ######### ##       ##  ##   
##     ## ##       ##     ## ##    ## ##   ##     ##    ## ##     ## ##    ## ##   ##  
########  ######## ##     ##  ######  ##    ##     ######  ##     ##  ######  ##    ## """


def assign_card():
    card_index = random.randint(0, len(cards) - 1)
    selected_card = (cards[card_index])
    cards.remove(selected_card)
    return selected_card


def calculate_score(list1):
    total = 0
    remain = []
    for index in range(0, len(list1)):
        if list1[index] == 'K' or list1[index] == 'Q' or list1[index] == 'J':
            total = total + 10

    for index in range(0, len(list1)):
        if list1[index] != 'K' and list1[index] != 'Q' and list1[index] != 'J' and list1[index] != 'A':
            remain.append(list1[index])

    for index in range(0, len(list1)):
        if list1[index] == 'A':
            total = total + 11
            if (total + sum(remain)) > 21:
                total = total - 10

    return total + sum(remain)


def play_again():
    while True:
        print("-----------------------------------X------------------------------------")
        play_game_again = input("Do You Want to play again [Y/N]:").lower()
        if play_game_again == 'y' or play_game_again == 'n':
            if play_game_again == 'n':
                return False

            else:
                return True

        else:
            print("Incorrect Decision")


def print_info(list_1, list_2, show_all):
    print("---------------------------------------------------------------\n")
    print(f"Your Cards are ----{list_1}")
    if show_all:
        print(f"Your Cards are ----{list_2}")
        print(f"YOUR SCORE ={calculate_score(list_1)} and COMPUTER SCORE IS = {calculate_score(list_2)}")
    else:
        print(f"Computer Cards are ----[{list_2[0]},*]")
        print(f"YOUR SCORE ={calculate_score(list_1)} and COMPUTER CARD IS = {list_2[0]}")
    print("---------------------------------------------------------------")


def check_winner(user_list, comp_list):
    if calculate_score(comp_list) == calculate_score(user_list) <= 21:
        return "DRAW"
    elif 21 >= calculate_score(comp_list) > calculate_score(user_list):
        return "LOSE"

def compare(user_score, computer_score):
  #Bug fix. If you and the computer are both over, you lose.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"


  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"


def Shuffling(user_list, comp_list):
    while True:
        another_card = input("Do you want another card [Y/N]: ").lower()
        if another_card == 'n' or another_card == 'y':
            if another_card == 'y':
                user_list.append(assign_card())
                print_info(user_list, comp_list, True)
                if calculate_score(user_list) > 21:
                    print("-----------------------------------\nYOU LOSE BETTER LUCK NEXT "
                          "TIME\n-----------------------------------")
                    break
            elif another_card == 'n':
                break
        else:
            print("Incorrect decision")
    while True:
        if 21 > calculate_score(comp_list) < calculate_score(user_list):
            comp_list.append(assign_card())
            print_info(user_list, comp_list, True)
            if calculate_score(comp_list) > 21:
                print("-----------------------------------\nYOU WIN! "
                      "Congratulation\n-----------------------------------")
                break
        else:
            if check_winner(user_list, comp_list) == "DRAW":
                print_info(user_list, comp_list, True)
                print(
                    "-----------------------------------\nITS A DRAW\n-----------------------------------")
                break
            elif check_winner(user_list, comp_list) == "LOSE":
                print_info(user_list, comp_list, True)
                print("-----------------------------------\nYOU LOSE BETTER LUCK NEXT "
                      "TIME\n-----------------------------------")
                break
        if check_winner(user_list, comp_list) == "WIN" or check_winner(user_list,
                                                                       comp_list) == "DRAW" or check_winner(
            user_list, comp_list) == "LOSE":
            break


def continue_playing(continue_play, user_list, comp_list):
    print_info(user_list, comp_list, False)
    while continue_play:
        Shuffling(user_list, comp_list)
        continue_play = False


def play_game():
    run = True
    print(black_Jack)
    while run:
        print("Game Started")
        user_list = []
        comp_list = []
        user_list.clear()
        comp_list.clear()

        for i in range(0, 2):
            user_list.append(assign_card())
            comp_list.append(assign_card())
        continue_playing(True, user_list, comp_list)
        run = play_again()


play_game()
