from turtle import Turtle


class Scoreboard(Turtle):
    """
    Scoreboard displaying user's score, aligned to the top center of the screen.
    Subclass of Turtle, adds the following methods:
    - update_scoreboard() - display current score on board
    - reset() - reset score to 0, then display current score on board
    - increase_score() - increase score by 10, then display current score on board
    - show_final_score() - display final score
    """
    DATA_FILE = 'data.txt'

    def __init__(self):
        """Draw object on screen and reset score to 0."""
        super().__init__()
        self.color('black')
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.reset()

    def update_scoreboard(self):
        """Display current score on board."""
        with open(Scoreboard.DATA_FILE, 'r') as score_file:
            score_file.seek(0)
            new_score = score_file.read()
        self.clear()
        self.write(f"Current score: {new_score}", align='center', font=('Courier', 24, 'normal'))

    def reset(self):
        """Reset score to 0, display the current score on board. """
        with open(Scoreboard.DATA_FILE, 'w') as score_file:
            score_file.seek(0)
            print('0', file=score_file)
        self.update_scoreboard()

    def increase_score(self):
        """Increase score by 10, display current score on board."""
        with open(Scoreboard.DATA_FILE, 'r') as score_file:
            score_file.seek(0)
            score = int(score_file.read())
            score += 10

        with open(Scoreboard.DATA_FILE, 'w') as score_file:
            score_file.seek(0)
            print(score, file=score_file)

        self.update_scoreboard()

    def show_final_score(self):
        """Display final score."""
        self.clear()
        with open(Scoreboard.DATA_FILE, 'r') as score_file:
            score_file.seek(0)
            new_score = score_file.read()
        self.goto(0, 0)
        self.write(f"GAME OVER\nYour score: {new_score}", align='center', font=("Arial", 30, "normal"))
