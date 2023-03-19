from turtle import Screen, Turtle
from time import sleep
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Da snake game')
screen.tracer(0)

snake = Snake()

screen.update()

game_state = True
while game_state:
    snake.move()
    screen.update()
    sleep(0.15)

screen.exitonclick()
