import random
print("This program will give you a choice randomly that who will pay today!")
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

random_name = random.randint(0, len(names) - 1)

print(f"{names[random_name]} is going to buy the meal today!")
