from turtle import Turtle, Screen 

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Welcome to the Snake Game")


## we want to make a snake body - three squares- three sqaures 20px apart
segment_1 = Turtle(shape="square")
segment_1.color("white")

segment_2 = Turtle(shape="square")
segment_2.color("white")
segment_2.goto(-20,0)

segment_3 = Turtle(shape="square")
segment_3.color("white")
segment_3.goto(-40,0)

screen.exitonclick()