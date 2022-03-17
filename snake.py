from turtle import Turtle

STARTING_POSITION = ((0, 0))
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake_start_length = 3
        self.snake = list()
        self.create_snake()
        self.snake_head = self.snake[0]

    def reset_snake(self):
        for segment in self.snake:
            segment.goto(1000,1000)
        self.snake.clear()
        self.create_snake()
        self.snake_head = self.snake[0]

    def create_snake_segment(self):
        snake_segment = Turtle(shape='square')
        snake_segment.penup()
        snake_segment.color('white')
        return snake_segment


    def create_snake(self):
        for i in range(0, self.snake_start_length):
            new_segment = self.create_snake_segment()
            self.snake.append(new_segment)
            self.snake[i].setposition(STARTING_POSITION[0] - (i * 20), STARTING_POSITION[1])


    def extend(self):
        new_segment = self.create_snake_segment()
        new_segment.goto(self.snake[-1].position())
        self.snake.append(new_segment)

    def move(self):
        for segment_number in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[segment_number - 1].xcor()
            new_y = self.snake[segment_number - 1].ycor()
            self.snake[segment_number].goto(new_x, new_y)
        self.snake[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake[0].heading() != DOWN:
            self.snake[0].setheading(UP)

    def down(self):
        if self.snake[0].heading() != UP:
            self.snake[0].setheading(DOWN)

    def right(self):
        if self.snake[0].heading() != LEFT:
            self.snake[0].setheading(RIGHT)

    def left(self):
        if self.snake[0].heading() != RIGHT:
            self.snake[0].setheading(LEFT)


    def __iter__(self):
        self.n = 0
        return self


    def __next__(self):
        if self.n < len(self.snake):
            index = self.n
            self.n += 1
            return(self.snake[index])
        else:
            raise StopIteration
