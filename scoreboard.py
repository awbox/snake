from turtle import Turtle


class Scoreboard(Turtle):
    """
    Creates Scoreboard object, displaying score, aligned to the top center of the screen.
    """
    DATA_FILE = 'data.txt'

    def __init__(self, score=0):
        super().__init__()
        # initialize score instance variable
        self.score = score

        # draw the scoreboard on the screen
        self.color('black')
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.write(f"Current highscore: {score}", align='center', font=('Courier', 24, 'normal'))

    def update_scoreboard(self):
        """
        Update Scoreboard object with score retrieved from data.txt
        :return: new scoreboard instance
        """
        # open file data.txt for reading
        with open(Scoreboard.DATA_FILE, 'r') as score_file:
            # assign its content to new_score variable
            new_score = int(score_file.read())
            score_file.close()
        # re-initialize object with new_score value
        self.clear()
        new_scoreboard = Scoreboard(score=new_score)
        return new_scoreboard

    def reset(self):
        """
        Reset scoreboard object to score 0. Overwrite data.txt file to 0.
        :return: new scoreboard instance
        """
        # overwrite data.txt with default score
        with open(Scoreboard.DATA_FILE, 'w') as score_file:
            print('0', file=score_file)
            score_file.close()
        # refresh the Scoreboard instance
        self.clear()
        new_scoreboard = Scoreboard()
        return new_scoreboard

    @staticmethod
    def increase_score():
        """
        Increase score stored in data.txt by 10.
        :return: None
        """
        # open file in read mode
        with open(Scoreboard.DATA_FILE, 'r') as score_file:
            # assign current score to variable
            score = score_file.read()
            if score == "":
                score = 0
            else:
                score = int(score)
            score_file.close()
        # increase score by 10
        score += 10
        # write new score to file
        with open(Scoreboard.DATA_FILE, 'w') as score_file:
            print(score, file=score_file)
            score_file.close()

