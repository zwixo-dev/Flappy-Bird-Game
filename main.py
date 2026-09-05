from turtle import Screen
from bird import Bird
from evil_birds import EVILBRIDS
from net_man import netMan
from coins import COIN
from Huntingdog import SavageDog
import time

GAME_IS_ON = True


screen = Screen()
screen.title("Flappy Brid Game!")
screen.setup(width=800, height=1000)
screen.tracer(0)
# path image
img_path = "imgs/bg_game.png"
screen.bgpic(img_path)

bird = Bird() # bird player
evils = EVILBRIDS() #bird evils
bird_catcher = netMan() #net man
earn_coins = COIN() #Coins
dog_hunted = SavageDog()

screen.listen()
screen.onkey(bird.move_up,"Up")
screen.onkey(bird.move_left,"Left")
screen.onkey(bird.move_right,"Right")


#--------------------- Main Loop to run the game ---------------------

while GAME_IS_ON:
    time.sleep(0.1)
    screen.update()

    # --------- manage the bird player gravity ---------
    bird.gravity_control()

    # --------- generate evil birds randomly with movement ---------
    evils.gen_new_evil_bird()
    evils.evil_birds_movement()

    # --------- coins earning ---------
    earn_coins.gen_coin()
    earn_coins.falling_coins()

    # --------- bird_catcher movement ---------
    bird_catcher.trying_to_catch()


    # --------- bird player conditions  ---------
    # if the bird touch the top or left or right edges
    if bird.ycor() > 480 or bird.xcor() > 380 or bird.xcor() < -380:
        print("I touch the edges (Top or Left or Right)")
        GAME_IS_ON = False

    # If the bird is very close to the ground, it will be catched
    if bird.ycor() < -380:
        print("m gonna be catched :/")
        dog_hunted.catch_the_bird(bird.xcor(), bird.ycor())
        screen.update()
        GAME_IS_ON = False

    # if the bird touch bird_catcher
    if bird_catcher.distance(bird) < 70:
        print("m catched by the bird_catcher")
        GAME_IS_ON = False

    # if the bird touch any evil bird
    for evil_bird in evils.evil_birds_list:
        if evil_bird.distance(bird) < 20:
            GAME_IS_ON = False
            print("==== I touch the Evil Birsd =====")

    # if the bird touch a coin remove it and increse the score
    for coin in earn_coins.coins_list:
        if coin.distance(bird) < 20:
            print("coin touched Index ====> ", coin)
            coin.hideturtle()

screen.exitonclick()