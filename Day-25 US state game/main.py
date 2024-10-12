import pandas
import turtle

FONT = ("Arial", 10, "normal")

screen = turtle.Screen()
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

data = pandas.read_csv("50_states.csv")
all_states = data["state"].tolist()

game_is_on = True
while game_is_on:
    answer_state = turtle.textinput(title="Guess the State", prompt="What's another state's name?")
    # Getting the x and y coordinate by matching state
    answer_state_x = int(data[data.state == answer_state].x.iloc[0])
    answer_state_y = int(data[data.state == answer_state].y.iloc[0])
    print(f"x: {answer_state_x}, y: {answer_state_y}")

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(answer_state_x, answer_state_y)
        t.write(answer_state, align="center", font=FONT)


screen.exitonclick()