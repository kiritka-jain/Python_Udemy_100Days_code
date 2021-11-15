from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR, highlightthickness=0)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text='Some question text',
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))

        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        # score
        self.score = Label(text='Score:', fg='White', bg=THEME_COLOR, highlightthickness=0)
        self.score.grid(column=1, row=0)

        # right button
        self.right_img = PhotoImage(file='images/true.png')
        self.right_button = Button(image=self.right_img, highlightthickness=0, command=self.check_for_true)
        self.right_button.grid(column=0, row=2)

        # wrong button
        self.wrong_img = PhotoImage(file='images/false.png')
        self.wrong_button = Button(image=self.wrong_img, highlightthickness=0, command=self.check_for_false)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        self.score.config(text=f"Score:{self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='You have reached the end.')
            self.right_button.config(state= 'disabled')
            self.wrong_button.config(state= 'disabled')


    def check_for_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def check_for_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right == True:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
