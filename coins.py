import turtle
import random


GOLD_COIN = "imgs/coin.png"
turtle.addshape(GOLD_COIN)

class COIN(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        # store coins
        self.coins_list = []
        # fix coin pos to start from
        self.coin_y_position = 400

    def gen_coin(self):
        chance_of_gen = random.randint(0, 19)
        if chance_of_gen == 14:
            new_fallen_coin = turtle.Turtle()
            new_fallen_coin.shape(GOLD_COIN)
            new_fallen_coin.penup()
            new_fallen_coin.setheading(270)
            rand_y_pos = random.randint(-480, 480)
            new_fallen_coin.goto(x=rand_y_pos, y=self.coin_y_position)
            self.coins_list.append(new_fallen_coin)

    def falling_coins(self):
        for fallen_coin in self.coins_list:
            print(fallen_coin)
            fallen_coin.forward(10)