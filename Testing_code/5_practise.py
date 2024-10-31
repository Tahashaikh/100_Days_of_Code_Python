def check_prime(num):

    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0 :
            return False
    return True

number = 9
if check_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
