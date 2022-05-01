from turtle import Turtle


class Brick(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("brown")
        self.shape("square")
        self.shapesize(stretch_len=3, stretch_wid=0.75)
        self.penup()
        self.goto(position)
