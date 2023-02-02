print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
prize = 0
if size == "S":
    prize = 15
elif size == "M":
    prize = 20
elif size == "L":
    prize = 25

if add_pepperoni == "Y" and size == "S":
    prize = prize + 2

if add_pepperoni == "Y" and size == "M" or size == "L":
    prize = prize + 3

if extra_cheese == "Y":
    prize = prize + 1

print (f"Your final bill is: ${prize}.")


