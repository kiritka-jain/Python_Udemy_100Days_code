import random

number = random.randint(0,1)
if number == 1:
    coin_value = 'Head'
else:
    coin_value = 'Tail'
print(coin_value)