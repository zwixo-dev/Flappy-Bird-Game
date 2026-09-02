import turtle

BIRD_IMG_PATH ="imgs/v2.png"

turtle.addshape(BIRD_IMG_PATH)

class Bird(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape(BIRD_IMG_PATH)
        self.penup()

    # gravity control
    def gravity_control(self):
        current_y_pos = self.ycor()
        self.goto(x=self.xcor(), y=current_y_pos-8)

    # controle the movements
    def move_up(self):
        current_y_pos = self.ycor()
        self.goto(x=self.xcor(), y=current_y_pos+30)

    def move_left(self):
        current_x_pos = self.xcor()
        self.goto(x=current_x_pos-30, y=self.ycor())
    def move_right(self):
        current_x_pos = self.xcor()
        self.goto(x=current_x_pos+30, y=self.ycor())

    