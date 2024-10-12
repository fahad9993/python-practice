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
guessed_states = []

while len(guessed_states) < 50:
    answer_state = turtle.textinput(title=f"{len(guessed_states)}/50 States correct", prompt="What's another state's "
                                                                                             "name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        missing_data = pandas.Series(missing_states)
        missing_data.to_csv("states_to_learn.csv")
        break
    # Getting the x and y coordinate by matching state
    answer_state_x = int(data[data.state == answer_state].x.iloc[0])
    answer_state_y = int(data[data.state == answer_state].y.iloc[0])
    # print(f"x: {answer_state_x}, y: {answer_state_y}")

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(answer_state_x, answer_state_y)
        t.write(answer_state, align="center", font=FONT)
