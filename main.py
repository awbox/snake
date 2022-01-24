from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen
from time import sleep

if __name__ == '__main__':

    # initialize screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('white')
    screen.tracer(0)

    # initialize Scoreboard, Food and Snake objects
    scoreboard = Scoreboard()
    food = Food()
    snake = Snake()

    # bind the snake moves to screen events (keyboard input)
    screen.listen()
    screen.onkey(snake.move_up, "Up")
    screen.onkey(snake.move_down, "Down")
    screen.onkey(snake.move_right, "Right")
    screen.onkey(snake.move_left, "Left")

    # while game is on
    game_is_on = True
    while game_is_on:
        # Snake object moves
        screen.update()
        snake.move()
        sleep(0.1)
        # screen object listens to the keyboard input
        # if Snake's head is in the same spot as Food object instance
        # Snake object extends (snake eats apple and grows)
        # score is added
        # if Snake object's head touches Snake's body
        # the game is over
        # score is presented

