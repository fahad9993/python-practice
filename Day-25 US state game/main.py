import turtle
from turtle import Screen

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


# def get_coordinates(x, y):
#     """This function prints the x and y coordinate of a point when clicked on any point on the screen"""
#     print(x, y)
#
#
# turtle.onscreenclick(get_coordinates)

answer_state = turtle.textinput(title="Guess the state", prompt="What is the another state?")
print(answer_state)

turtle.mainloop()
