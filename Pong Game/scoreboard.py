from turtle import Turtle
WINNING_SCORE = 10


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

        # Showing name of the players
        self.goto(-270, 240)
        self.write("Player A", align="center", font=("Courier", 30, "normal"))
        self.goto(270, 240)
        self.write("Player B", align="center", font=("Courier", 30, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def show_winner(self):
        if self.l_score == WINNING_SCORE:
            self.goto(0, 50)
            self.write("Player A won", align="center", font=("Courier", 80, "normal"))
            return True

        elif self.r_score == WINNING_SCORE:
            self.goto(0, 50)
            self.write("Player B won", align="center", font=("Courier", 80, "normal"))
            return True

    def restart(self):
        # self.goto(0, -50)
        # self.write("Play again? (Y/N)", align="center", font=("Courier", 40, "normal"))
        self.l_score = 0
        self.r_score = 0
        return self.screen.textinput("Play again?", "(Y/N) : ")
