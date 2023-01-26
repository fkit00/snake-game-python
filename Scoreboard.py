from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        
        self.score =0
        with open("score.txt") as file:
                self.high_score= int(file.read())

        self.color("white")
        self.hideturtle()  
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear() 
        self.write(f"Score:{self.score} High Score:{self.high_score}", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt", mode='w') as file:
                file.write(str(self.high_score))
           
        self.score = 0 
        self.update_scoreboard()    


    def increase_score(self):  
        self.score +=1
        self.update_scoreboard()

