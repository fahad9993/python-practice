import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# Drawing a dashed line
# for _ in range(15):
#     timmy.pendown()
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)

# Drawing multiple overlying shapes, each with different color, on the go
# shapes_list = [3, 4, 5, 6, 7, 8, 9, 10, 11]
#
#
# def change_color():
#     r = random.random()
#     g = random.random()
#     b = random.random()
#
#     timmy.pencolor((r, g, b))
#
#
# def draw_shapes(num_sides):
#     angle = 360/num_sides
#
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     draw_shapes(shape_side_n)
#     change_color()

# Random walk with various pen color


def change_color():
    r = random.random()
    g = random.random()
    b = random.random()

    timmy.pencolor((r, g, b))


def change_direction():
    directions = [0, 90, 180, 270]
    current_direction = random.choice(directions)
    timmy.seth(current_direction)


timmy.pensize(15)
timmy.speed("fastest")
for _ in range(200):
    change_direction()
    timmy.forward(30)
    change_color()

screen = Screen()
screen.exitonclick()
