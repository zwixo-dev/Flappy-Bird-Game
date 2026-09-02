from turtle import Screen
from bird import Bird
from evil_brids import EVILBRIDS
import time

GAME_IS_ON = True


screen = Screen()
screen.title("Flappy Brid Game!")
screen.setup(width=500, height=600)
screen.tracer(0)
# path image
img_path = "imgs/bg_game.png"
screen.bgpic(img_path)

bird = Bird() # bird player
evils = EVILBRIDS() #bird evils

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

    # if the bird touch the top or bottom edges
    if(bird.ycor() > 280 or bird.ycor() < -280):
        print("I hit the edges")
        GAME_IS_ON = False
    
    # if the bird touch any evil bird
    for evil_bird in evils.evil_birds_list:
        if evil_bird.distance(bird) < 20:
            GAME_IS_ON = False
            print("==== I touch the Evil Birsd =====")




# screen.exitonclick()
