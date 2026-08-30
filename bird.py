import turtle

BIRD_IMG_PATH ="imgs/v2.png"

turtle.addshape(BIRD_IMG_PATH)

class Bird(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape(BIRD_IMG_PATH)
        self.width(20)
        self.penup()

    # gravity control
    def gravity_control(self):
        current_y_pos = self.ycor()
        self.goto(x=0, y=current_y_pos-5)

    # controle the movements
    def up(self):
        current_y_pos = self.ycor()
        self.goto(x=0, y=current_y_pos+30)
