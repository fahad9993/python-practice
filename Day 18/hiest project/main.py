# import colorgram
#
# num_of_ext_color = 30
# colors_obj = colorgram.extract("image.jpg", num_of_ext_color)
# colors = []
#
# for index in range(num_of_ext_color):
#     color = colors_obj[index].rgb
#     r = color.r
#     g = color.g
#     b = color.b
#
#     colors.append((r, g, b))
#
# print(colors)

from turtle import Turtle, Screen
import random

tim = Turtle()
Screen().colormode(255)
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [(225, 233, 227), (207, 160, 82), (54, 89, 130), (145, 91, 40), (140, 27, 49), (222, 206, 109),
              (132, 177, 203), (45, 55, 104), (158, 46, 83), (169, 160, 39), (129, 189, 143), (83, 20, 44),
              (38, 43, 67), (186, 94, 107), (186, 140, 170), (85, 120, 180), (59, 39, 31), (88, 157, 92),
              (79, 153, 165), (195, 79, 72), (161, 201, 219), (45, 74, 77), (79, 74, 44), (58, 125, 121),
              (218, 176, 187), (167, 206, 168), (220, 182, 168)]


def draw_circle(dia):
    tim.dot(dia, random.choice(color_list))


tim.seth(225)
tim.forward(300)
tim.seth(0)

for _ in range(10):
    current_position = tim.position()
    for _ in range(10):
        # tim.pendown()
        draw_circle(20)
        # tim.penup()
        tim.forward(50)
        # tim.pencolor(random.choice(color_list))

    tim.setpos(current_position)
    tim.seth(90)
    # tim.penup()
    tim.forward(50)
    tim.seth(0)

# print(random.choice(color_list))


screen = Screen()
screen.exitonclick()
