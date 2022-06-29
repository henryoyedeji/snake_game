from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0

        with open("data.txt", mode="r+") as self.recordscore:
            self.record = int(self.recordscore.read())


        # self.record_score = str(self.highscore)
        self.highscore = self.record
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.record}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score

        self.score = 0
        self.update_scoreboard()

    def update_record(self):
        if self.highscore > self.record:
            self.record = self.highscore
            with open("data.txt", mode="w") as record:
                record.write(f"{self.highscore}")
            self.update_scoreboard()
    #
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
