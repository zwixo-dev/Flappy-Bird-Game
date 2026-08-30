import turtle

EVIL_BRID = "imgs/"
turtle.addshape(EVIL_BRID)

class EVILBRIDS(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape(EVIL_BRID)
        
