from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, player):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.a_score = 0
        self.b_score = 0
        self.__create_score(player)

    def __create_score(self, player):
        if player == 'a':
            self.goto(-40, 270)
            self.write_score(self.a_score,'A')
        if player == 'b':
            self.goto(40, 270)
            self.write_score(self.b_score,'B')

    def write_score(self,score,player):
        self.write(f"Score{player}: {score}", font=("Verdana", 15, "normal"), align="center")

    def update_score(self,player):
        if player == 'a':
            self.__increase_a_score()
            self.write_score(self.a_score,'A')
        elif player == 'b':
            self.__increase_b_score()
            self.write_score(self.b_score,'B')

    def __increase_a_score(self):
        self.a_score += 1
        self.clear()

    def __increase_b_score(self):
        self.b_score += 1
        self.clear()

    def compare_scores(self):
        if self.a_score >= 10 :
            return True
        elif self.b_score >= 10:
            return True
        else:
            return False



    def game_over(self,player):
        self.goto(0, 0)
        self.write(f"Game Over!\nThe winner is:Player {player}", move=False, align='center', font=('Arial', 30, 'normal'))

