from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')
SCOREBOARD_POSITION = (0, 260)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(SCOREBOARD_POSITION)
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.show_score()


    def increase_score(self):
        self.score += 1
        self.show_score()
