from snake import Snake
from food import Food
from scoreboard import Scoreboard

if __name__ == '__main__':
    # initialize Scoreboard, Food and Snake objects
    scoreboard = Scoreboard()
    food = Food()
    snake = Snake.create_snake()
    # get current TurtleScreen object as a screen variable
    screen = snake.getscreen()
    # while Snake object exists
    # Snake object moves
    # screen object listens to the keyboard input
    # if keyboard input "up", "down, "right", "left" was provided
    # move Snake object in the specified direction
    # if Snake's head is in the same spot as Food object instance
    # Snake object extends (snake eats apple and grows)
    # score is added
    # if Snake object's head touches Snake's body
    # the game is over
    # score is presented

