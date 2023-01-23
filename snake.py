from turtle import Turtle, Screen 

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Welcome to the Snake Game")
screen.tracer(0)

game_is_on = True 

starting_positons=[(0,0),(-20,0),(-40,0)]

segments=[]

## we want to make a snake body - three squares- three sqaures 20px apart

for position in starting_positons:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

screen.update()

game_is_on = True

while game_is_on:
    for seg in segments:
        seg.forward(20)    


screen.exitonclick()