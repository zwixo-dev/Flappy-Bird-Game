import turtle

NET_MAN_PATH = "imgs/Net_Man_v3.png"

turtle.addshape(NET_MAN_PATH)

class netMan(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape(NET_MAN_PATH)
        self.penup()
        self.setposition(x=-340, y=-400)

    # control the movement of the bird catcher

    def move_forward(self):
        catcher_x_pos = self.xcor()
        self.goto(x=catcher_x_pos+20, y=self.ycor())

    def move_backward(self):
        catcher_x_pos = self.xcor()
        self.goto(x=catcher_x_pos-20, y=self.ycor())

    # 
    






