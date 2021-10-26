import random
import time
from tkinter import *

import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn ={}
# ---------------------------- Functionality ------------------------------- #
try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')



def next_card():
    global current_card, flip_timer
    current_card = random.choice(to_learn)
    canvas.itemconfig(title, text='French',fill = 'Black')
    canvas.itemconfig(word, text=current_card['French'],fill = 'Black')
    canvas.itemconfig(canvas_background, image=front_img)
    flip_timer = window.after(3000, func=card_flip)

def card_flip():
    canvas.itemconfig(title, text='English',fill = 'White')
    canvas.itemconfig(word, text=current_card['English'],fill = 'White')
    canvas.itemconfig(canvas_background, image=back_img)

def card_known():
    to_learn.remove(current_card)
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index= False)



# ---------------------------- UI SETUP ------------------------------- #

# window background

window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=card_flip)

# canvas set up

canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas_background = canvas.create_image(400, 263, image=front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
title = canvas.create_text(400, 150, text='', font=('Arial', 40, 'italic'))
word = canvas.create_text(400, 263, text='', font=('Arial', 40, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

# right button
right_img = PhotoImage(file='images/right.png')
right_button = Button(image=right_img, highlightthickness=0, command=card_known)
right_button.grid(column=0, row=1)

# wrong button
wrong_img = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=1, row=1)

next_card()


window.mainloop()
