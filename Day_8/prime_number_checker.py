number = int(input("Enter the number"))


def check_for_prime(number):
    is_prime = True
    for num in range(2,number-1):
        if number % num ==0:
            is_prime = False
    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number.")



check_for_prime(number)

