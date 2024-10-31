
print("Give me a number:")
number = input()
print("Type any symbol: \n + \n - \n * \n \\")
checkSymbol = True
while checkSymbol:
    operation = input()
    if operation =="+" or operation =="-" or operation == "*" or operation == "//":
        checkSymbol = False
    else:
        print("Please input correcly!")
print("Give me an other number:")
number2 = input()
