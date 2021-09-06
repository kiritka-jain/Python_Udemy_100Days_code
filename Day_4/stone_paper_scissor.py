import random

player_input = int(input("What do you choose? Type '0' for rock,1 for paper and 2 for scissors"))
computer_input = random.randint(0,2)
if player_input == computer_input:
    print("Game Draw.")
elif (player_input == 0 and computer_input ==1) or (player_input == 1 and computer_input ==2) \
        or (player_input == 2 and computer_input ==1):
    print("Computer wins")
elif (player_input == 1 and computer_input ==0) or (player_input == 2 and computer_input ==1) \
        or (player_input == 1 and computer_input ==2):
    print("You win!")

