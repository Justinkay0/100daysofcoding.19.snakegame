from turtle import Screen, Turtle
from time import sleep

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Da snake game')
screen.tracer(0)

snake = []

for _ in range(3):
    s = Turtle(shape='square')
    s.color('white')
    s.penup()
    s.setposition(y=0, x=0 - _ * 20)
    snake.append(s)

screen.update()

game_state = True
while game_state:
    for segments in range(len(snake) - 1, 0, -1):
        position = snake[segments -1].pos()
        snake[segments].goto(x=position[0], y=position[1])
    snake[0].forward(20)

    screen.update()
    sleep(0.15)

screen.exitonclick()
