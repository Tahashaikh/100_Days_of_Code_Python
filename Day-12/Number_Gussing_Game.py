start_heading = '''
███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗      ██████╗ ██╗   ██╗███████╗███████╗██╗ ██████╗ ███╗   ██╗     ██████╗  █████╗ ███╗   ███╗███████╗
████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗    ██╔════╝ ██║   ██║██╔════╝██╔════╝██║██╔════╝ ████╗  ██║    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝    ██║  ███╗██║   ██║███████╗███████╗██║██║  ███╗██╔██╗ ██║    ██║  ███╗███████║██╔████╔██║█████╗  
██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗    ██║   ██║██║   ██║╚════██║╚════██║██║██║   ██║██║╚██╗██║    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║    ╚██████╔╝╚██████╔╝███████║███████║██║╚██████╔╝██║ ╚████║    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝     ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                                                                                                                                                          
'''
import random
print(start_heading)

def generate_random_number(min_number, max_number):
    return random.randint(min_number, max_number)

def Number_Gussing(secret_number):
    print("I am thinking of a number between 1 and 20")
    guess = 0
    while guess != secret_number:
        guess = int(input("Take a guess: "))
        if guess < secret_number:
            print("Your guess is too low")
        elif guess > secret_number:
            print("Your guess is too high")
        else:
            print("Good job, you guessed it!")
            break


def difficulty_level():
    level = input("Choose a difficulty level:(easy ,medium, hard) ")
    if level == "easy":
        Number_Gussing(generate_random_number(1, 20))
    elif level == "medium":
        Number_Gussing(generate_random_number(1, 30))
    elif level == "hard":
        Number_Gussing(generate_random_number(1, 40))
    else:
        print("Invalid input")


def play_Again():
    play_again = input("Would you like to play again? ").lower()
    if play_again == "yes":
        return True
    elif play_again == "no":
        return False
    else:
        print("Invalid input")


def keep_playing():
    difficulty_level()
    while play_Again():
        difficulty_level()



keep_playing()

keep_playing()