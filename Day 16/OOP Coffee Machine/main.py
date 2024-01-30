from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

selected_coffee = input("What would you like? (espresso/latte/cappuccino/): ")

print(selected_coffee)

available_items = Menu().get_items()
print(available_items)

available_ingredients = CoffeeMaker().report()
print(available_ingredients)
