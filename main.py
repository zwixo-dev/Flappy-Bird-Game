from turtle import Screen
from bird import Bird
import time

GAME_IS_ON = True


screen = Screen()
screen.title("Flappy Brid Game!")
screen.setup(width=500, height=600)
screen.tracer(0)
# path image
img_path = "imgs/bg_game.png"
screen.bgpic(img_path)

bird = Bird()



screen.listen()
screen.onkey(bird.up,"Up")

while GAME_IS_ON:
    time.sleep(0.1)
    screen.update()

    bird.gravity_control()
    print(bird.ycor())

    # if the bird touch the top or bottom edges
    if(bird.ycor() > 280 or bird.ycor() < -280):
        print("I hit the edges")
        # GAME_IS_ON = False




# screen.exitonclick()
