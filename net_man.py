import turtle
import time
from playsound3 import playsound


NET_MAN_PATH = "imgs/Net_Man_v3.png"
CATCHER_SOUND = "audios/catchersound.mp3"


turtle.addshape(NET_MAN_PATH)

class netMan(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape(NET_MAN_PATH)
        self.penup()
        self.setposition(x=-360, y=-400)
        # 
        self.direction = 1 

    # control the movement of the bird catcher
    def movement_path(self):
        self.goto(x=self.xcor() + self.direction * 20, y=self.ycor())


    def trying_to_catch(self):
        """
        Trying to catch the bird : when the xcor()>360 we set the direction to -1 and we move backward 
        If the xcor() < -360  we move forward
        """
        print("=====================>",self.xcor())
        if self.xcor() > 360:
            self.direction = -1
            playsound(sound=CATCHER_SOUND, block=False)
        elif self.xcor() <-360:
            self.direction = 1
            playsound(sound=CATCHER_SOUND, block=False)


        self.movement_path()    




