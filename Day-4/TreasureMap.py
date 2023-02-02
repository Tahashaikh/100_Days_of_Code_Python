row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
TreasureMap = [row1, row2, row3]


print(f"{row1}\n{row2}\n{row3}")
print("Keep in mind Your area is 3X3 sor dont put greater, \nfirst digit indicate row and second indicate column")
Check_Coordinates = True
while Check_Coordinates:
    position = input("Where do you want to put the treasure? ")
    positions = position.split("x")
    row = positions[0]
    column = positions[1]
    if int(row) > 3 or int(column) > 3:
        print("Please Enter Correct Coordinates")
    else:
        Check_Coordinates = False


TreasureMap[int(row)-1][int(column)-1] = "X"

print(f"{row1}\n{row2}\n{row3}")

