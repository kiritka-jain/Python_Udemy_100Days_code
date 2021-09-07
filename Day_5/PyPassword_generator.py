import random

print("Welcome to Pypassword generator!")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
total_letters = int(input("How many letters would you like in your password?\n"))
total_symbols = int(input("How many symbols would you like in your password?\n"))
total_numbers = int(input("How many numbers would you like in your password?\n"))
pasword_char = []
for _ in range(total_letters):
    num = random.randint(0, 51)
    pasword_char.append(letters[num])
for _ in range(total_symbols):
    num = random.randint(0, 9)
    pasword_char.append(symbols[num])
for _ in range(total_numbers):
    num = random.randint(0, 9)
    pasword_char.append(numbers[num])
random.shuffle(pasword_char)
password_string = ''
for character in pasword_char:
    password_string+=str(character)
print(password_string)
