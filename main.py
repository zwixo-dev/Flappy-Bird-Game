from turtle import Screen
from bird import Bird
from evil_birds import EVILBRIDS
from net_man import netMan
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

screen.listen()
screen.onkey(bird.move_up,"Up")
screen.onkey(bird.move_left,"Left")
screen.onkey(bird.move_right,"Right")


while GAME_IS_ON:
    time.sleep(0.1)
    screen.update()

    # evil birds
    evils.gen_new_evil_bird()
    evils.evil_birds_movement()

    # manage the bird player gravity
    bird.gravity_control()
    print(bird.ycor())

    #bird player conditions
    # if the bird touch the top or bottom or left or right edges
    if bird.ycor() > 480 or bird.ycor() < -400  or  bird.xcor() > 380 or bird.xcor() < -380 :
        print("I hit the edges")
        GAME_IS_ON = False
    
    # if the bird touch any evil bird
    for evil_bird in evils.evil_birds_list:
        if evil_bird.distance(bird) < 20:
            GAME_IS_ON = False
            print("==== I touch the Evil Birsd =====")

    # bird catcher condition 
    bird_catcher.trying_to_catch()




# screen.exitonclick()
