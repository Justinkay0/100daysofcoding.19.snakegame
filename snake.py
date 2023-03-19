from turtle import Turtle


class Snake:

    def __init__(self):
        self.snake_list = []
        for _ in range(3):
            s = Turtle(shape='square')
            s.penup()
            s.color('white')
            s.setposition(y=0, x=0 - _ * 20)
            self.snake_list.append(s)

    def move(self):
        for segments in range(len(self.snake_list) - 1, 0, -1):
            position = self.snake_list[segments - 1].pos()
            self.snake_list[segments].goto(x=position[0], y=position[1])
        self.snake_list[0].forward(20)
