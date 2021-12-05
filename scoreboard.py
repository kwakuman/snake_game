from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')
SCOREBOARD_POSITION = (0, 260)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(SCOREBOARD_POSITION)
        self.show_score()

    def show_score(self):
        self.write(f'Score: {self.score}', align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.show_score()
