import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#FF449F"
RED = "#e7305b"
GREEN = "#77D970"
YELLOW = "#FFF338"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer_reset = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer_reset)
    timer.config(text="Timer", fg=GREEN)
    checkmarks.config(text="")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_brk_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer.config(text='Long break Mode', fg=PINK)
    elif reps % 2 == 0:
        count_down(short_brk_sec)
        timer.config(text='Short break Mode', fg=GREEN)
    else:
        count_down(work_sec)
        timer.config(text='Work Mode', fg=RED)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = '00'
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer_reset
        timer_reset = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session_completed = math.floor(reps / 2)
        for _ in range(work_session_completed):
            marks += '✓'
        checkmarks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=110, pady=70, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 140, text='00:00', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# timer label
timer = Label(text='Timer', font=(FONT_NAME, 35, 'bold'), fg=GREEN, bg=YELLOW)
timer.grid(column=1, row=0)

# start button
start = Button(text='Start', bg=YELLOW, highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

# stop button
stop = Button(text='Stop', bg=YELLOW, highlightthickness=0, command=reset_timer)
stop.grid(column=2, row=2)

# check marks
checkmarks = Label(text='', fg=GREEN, bg=YELLOW)
checkmarks.grid(column=1, row=3)

window.mainloop()
