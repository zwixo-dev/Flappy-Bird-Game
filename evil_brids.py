import turtle
import random


EVIL_BRID = "imgs/evil_bird.png"
turtle.addshape(EVIL_BRID)

class EVILBRIDS(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.evil_birds_list = []
        self.evil_x_pos = 300
        
    # manage evil birds
    def gen_new_evil_bird(self):
        rand_chance = random.randint(0, 10)
        print("CHNACE =====> ", rand_chance)
        if rand_chance == 5:
            new_evil_bird = turtle.Turtle()
            new_evil_bird.shape(EVIL_BRID)
            new_evil_bird.penup()
            new_evil_bird.setheading(180)
            rand_y_pos = random.randint(-270, 270)
            new_evil_bird.goto(x=self.evil_x_pos, y= rand_y_pos)
            self.evil_birds_list.append(new_evil_bird)

    # mange evil birds movement
    def evil_birds_movement(self):
        rand_y = random.randint(2, 5)
        for evil_bird in self.evil_birds_list:
            evil_bird.forward(10)
            # evil_bird.goto(x=self.xcor(), y=rand_y)
