from art import logo, vs
from game_data import data
import random

# Clearing the console
# For this to work you should enable "Emulate terminal in output console"
# from Run>Edit Configurations>Add new>Python>Modify option>Emulate terminal in output console
# Then selecting the script path
import os

score = 0


def max_follower(a, b):
    if a["follower_count"] > b["follower_count"]:
        return "A"
    else:
        return "B"


run_again = True
while run_again:
    os.system('cls')
    print(logo)
    if score != 0:
        print(f"You're right! Current score: {score}")
    values = random.sample(range(1, len(data)), k=2)
    a_info = data[values[0]]
    b_info = data[values[1]]
    # print(a_info, b_info)

    print(f"Compare A: {a_info['name']}, a {a_info['description']}, from {a_info['country']}.")
    print(vs)
    print(f"Against B: {b_info['name']}, a {b_info['description']}, from {b_info['country']}.")
    users_choice = input("Who has more followers? Type 'A' or 'B': ").upper()

    answer = max_follower(a_info, b_info)

    if users_choice == answer:
        score += 1

    else:
        os.system('cls')
        print(logo)
        print(f"Sorry! That's wrong. Final score: {score}")
        run_again = False
