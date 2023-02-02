print("Welcome to the tip calculator!")
amount = float(input("What was the total bill? $"))
Percentageoftip = float(input("How much tip would you like to give? 10, 12, or 15?"))/100
people = int(input("How many people to split the bill?"))

total_amount = amount + Percentageoftip
perperson = total_amount/ people

print(f"Each person should pay: ${round(perperson,2)}")