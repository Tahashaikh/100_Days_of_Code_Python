rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random

game_images = [rock, paper, scissors]

Checking_Input = True
while Checking_Input:
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if user_choice > 2 or user_choice < 0:
        print("Incorrect Choice please select between 0 ,1 or 3")

    else:
        Checking_Input = False
        print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice == 0 and computer_choice == 2:
    print("YourChoice\nYou win!")
elif computer_choice == 0 and user_choice == 2:
    print("YourChoice\nYou lose")
elif computer_choice > user_choice:
    print("YourChoice\nYou lose")
elif user_choice > computer_choice:
    print("YourChoice\nYou win!")
elif computer_choice == user_choice:
    print("YourChoice\nIt's a draw")

####### Debugging challenge: #########
# Try running this code and type 5.
# It will give you an IndexError and point to line 32 as the issue.
# But on line 38 we are trying to prevent a crash by detecting
# any numbers greater than or equal to 3 or less than 0.
# So what's going on?
# Can you debug the code and fix it?
# Solution: https://repl.it/@appbrewery/rock-paper-scissors-debugged-end
