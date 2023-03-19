from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Da snake game')
snake = []

for _ in range(3):
    s = Turtle(shape='square')
    s.color('white')
    s.penup()
    s.setposition(y=0, x=0 - _ * 20)
    snake.append(s)


screen.exitonclick()
