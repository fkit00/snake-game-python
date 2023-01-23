from turtle import Screen
import time
from snake import Snake
from food import Food
from Scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Welcome to the Snake Game")
screen.tracer(0)

game_is_on = True 



## we want to make a snake body - three squares- three sqaures 20px apart

snake= Snake()
food= Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

while game_is_on: 
    screen.update()
    time.sleep(0.1)
    snake.move()
## we need to detect collision with food 
    if snake.head.distance(food) < 15:
        ## we want to food to go to another location 
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    if snake.head.xcor() >280 or snake.head.xcor() < -280 or snake.head.ycor() >280 or snake.head.ycor() < -280:
        #snake has hit the wall
        game_is_on = False
        scoreboard.game_over()
## we now want to detect collision with tail 
 
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
            
  
        

screen.exitonclick()