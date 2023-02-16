# Step 1
import random
import HangmanWord_List
from HangMan_Stages import stages
from HangMan_Stages import logo
from HangMan_Stages import youLose

print(logo)
chosen_word = random.choice(HangmanWord_List.word_list)
print(chosen_word)

blank_array = []

for letter in chosen_word:
    blank_array.append("_")
print("Word = ",blank_array)
game_end = False
lives = 6
while not game_end:
    deduct_live = False
    guess = input("Guess a letter: ").lower()
    if str(guess) != '':

        if guess not in blank_array:
            if guess not in blank_array:
                for letter in range(0, len(chosen_word)):
                    if chosen_word[letter] == guess:
                        blank_array[letter] = guess
        else:
            deduct_live = True

        if guess not in chosen_word or deduct_live == True:
            lives -= 1
            if lives == 0:
                game_end = True
                print(youLose)
            print(stages[lives])

        print(blank_array)
        if '_' not in blank_array:
            print("YOU WIN !")
            break
    else:
        print("Please Enter Correct Choice")