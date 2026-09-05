import turtle

DOG_PATH = "imgs/savage_dog (1).png"
turtle.addshape(DOG_PATH)


class SavageDog(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape(DOG_PATH)
        self.penup()
        self.goto(x=-400, y=-600)


    def catch_the_bird(self, x_bird_pos, y_bird_pos):
        self.goto(x=x_bird_pos-60, y=y_bird_pos)