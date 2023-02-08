def check_if_number_is_prime(number):
    for i in range(1, number):
        prime = True
        if number % i == 0 and i != number:
            prime = False
            break
    if prime:
        return "Number is a Prime Number"
    else:
        return "Number is not a Prime Number"


print(check_if_number_is_prime(int(input("Enter Number you want to check :"))))
