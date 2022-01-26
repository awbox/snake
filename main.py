from snake import Snake
from food import Food
from scoreboard import Scoreboard
from turtle import Screen
from time import sleep

if __name__ == '__main__':

    # initialize screen
    screen = Screen()
    screen.setup(width=700, height=700)
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

        # whenever Snake eats Food, it extends,
        # new food object is generated, score is added
        if snake.head.distance(food.position()) < 5:
            snake.extend()
            scoreboard.increase_score()
            food.refresh()

        # whenever Snake hits the wall, game is over
        if (abs(snake.head.xcor()) >= 360) \
                or abs(snake.head.ycor()) >= 360:
            game_is_on = False

        # or its own body
        for segment in snake.segments[2:]:
            if snake.head.distance(segment.position()) < 0.1:
                game_is_on = False

    # final score is presented
    scoreboard.show_final_score()
    screen.exitonclick()
