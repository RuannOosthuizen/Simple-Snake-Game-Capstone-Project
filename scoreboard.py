# Imported Libraries:
from turtle import Turtle


# Defined constents
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


# Defined scoreboard class:
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scorebaord()

    # The scoreboard is written here:
    def update_scorebaord(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    # Here the score is tracked and kept:
    def increase_score(self):
        self.score += 1
        self.clear() # clears previous score.
        self.update_scorebaord()

    # Defined game over text:
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align=ALIGNMENT, font=FONT)
