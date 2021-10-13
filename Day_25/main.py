import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S state Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 correct guess',
                                    prompt="What's another state's name").title()
    if answer_state == 'Exit':
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        timmy = turtle.Turtle()
        timmy.penup()
        timmy.hideturtle()
        state_cordinate = data[data.state == answer_state]
        x_cordinate = int(state_cordinate.x)
        y_cordinate = int(state_cordinate.y)
        timmy.goto(x_cordinate, y_cordinate)
        timmy.write(answer_state)



# States to learn
missed_states =[]
for state in all_states:
    if state not in guessed_states:
        missed_states.append(state)

states_to_learn = pandas.DataFrame(missed_states)
states_to_learn.to_csv("missed_states.csv")