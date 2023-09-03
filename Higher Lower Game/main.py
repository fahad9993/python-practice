from art import logo, vs
from game_data import data
import random


def compare():
    return random.sample(range(1, len(data)), k=2)


values = compare()
a_info = data[values[0]]
b_info = data[values[1]]
print(a_info, b_info)

print(logo)
print(f"Compare A: {a_info['name']}, a {a_info['description']}, from {a_info['country']}.")
print(vs)
print(f"Against B: {b_info['name']}, a {b_info['description']}, from {b_info['country']}.")
# users_choice = input("Who has more followers? Type 'A' or 'B': ").upper()
