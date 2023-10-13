# from turtle import Turtle, Screen
#
# timmy = Turtle()
#
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.speed(1)
# timmy.forward(300)
# timmy.right(135)
# timmy.forward(300)
# timmy.home()
#
# my_screen = Screen()
#
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable, DOUBLE_BORDER

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
table.set_style(DOUBLE_BORDER)
table.add_row(["Testmander", "Air"])

print(table)

