from turtle import Turtle


class Scoreboard(Turtle):
    """
    Scoreboard displaying user's score, aligned to the top center of the screen.
    Subclass of Turtle, adds the following methods:
    - display_score() - display current score on board
    - increase_score() - increase score by 10, then display current score on board
    - start_tracking_highscore() - create or open highscore.txt file, return current highscore as int
    - is_new_highscore() - return True if user's score is greater than current highscore
    - save_highscore() - save user's score as highscore
    - show_final_score() - display final score
    """

    def __init__(self):
        """Draw object on screen and reset score to 0."""
        super().__init__()
        self.score = 0
        self.color('black')
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.display_score()
        self.highscore = self.start_tracking_highscore()

    def display_score(self)-> None:
        """Display current score on board."""
        self.clear()
        self.write(f"Current score: {self.score}", align='center', font=('Courier', 24, 'normal'))

    def increase_score(self) -> None:
        """Increase score by 10, display current score on board."""
        self.score += 10
        self.display_score()

    def start_tracking_highscore(self) -> int:
        """
        Create or open highscore.txt file, return current highscore as int.
        :return int highscore
        """
        highscore_file = "highscore.txt"
        try:
            with open(highscore_file, "r") as f:
                highscore = f.read()
        except FileNotFoundError:
            with open(highscore_file, "w") as f:
                print(0, file=f)
                highscore = 0
        return int(highscore)

    def is_new_highscore(self) -> bool:
        """
        Return True if user's score is greater than current highscore.
        :return: bool
        """
        return self.score > self.highscore

    def save_highscore(self) -> None:
        """Save user's score as highscore."""
        if self.is_new_highscore():
            with open("highscore.txt", "w") as f:
                print(self.score, file=f)

    def show_final_score(self) -> None:
        """Display final score on screen."""
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER\nYour score: {self.score}\nCurrent highscore: {self.highscore}", align='center', font=("Arial", 30, "normal"))