print("Welcome to Treasure Island.\nYour mission is to find the treasue.")
first_ans = input("You are at a crossroad.Where do you want to go? Type 'left' or'right'")
if first_ans == 'right':
    print("GameOver")
else:
    second_ans =input("You come to a lake.There is an island in the middle of the lake.Type 'wait' to wait for the "
                      "boat or type 'swim'to swim across.")
    if second_ans == 'swim':
        print("GameOver")
    else:
        third_ans = input('You arrived at he island unharmed.There is a house with 3 doors.One red,one yellow and one'
                          ' blue.Which colour do you choose?')
        if third_ans == 'yellow':
            print("You win!")
        else:
            print("Gameover")