from turtle import Turtle


class Scoreboard(Turtle):
    """
    Creates Scoreboard object, displaying score, aligned to the top center of the screen.
    """
    DATA_FILE = 'data.txt'

    def __init__(self):
        super().__init__()

        # draw the scoreboard on the screen
        self.color('black')
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.reset()

    def update_scoreboard(self):
        """
        Update Scoreboard object with score retrieved from data.txt
        :return: None
        """
        with open(Scoreboard.DATA_FILE, 'r') as score_file:
            score_file.seek(0)
            new_score = score_file.read()
        self.clear()
        self.write(f"Current score: {new_score}", align='center', font=('Courier', 24, 'normal'))

    def reset(self):
        """
        Reset scoreboard object to score 0. Overwrite data.txt file to 0.
        """
        with open(Scoreboard.DATA_FILE, 'w') as score_file:
            score_file.seek(0)
            print('0', file=score_file)
        self.update_scoreboard()

    def increase_score(self):
        """
        Increase score stored in data.txt by 10.
        """
        with open(Scoreboard.DATA_FILE, 'r') as score_file:
            score_file.seek(0)
            score = int(score_file.read())
            score += 10

        with open(Scoreboard.DATA_FILE, 'w') as score_file:
            score_file.seek(0)
            print(score, file=score_file)

        self.update_scoreboard()

    def final_score(self):
        self.clear()
        with open(Scoreboard.DATA_FILE, 'r') as score_file:
            score_file.seek(0)
            new_score = score_file.read()
        self.goto(0, 0)
        self.write(f"GAME OVER\nYour score: {new_score}", align='center', font=("Arial", 30, "normal"))
