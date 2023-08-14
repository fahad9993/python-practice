# Calculate the number of paint can, required to paint a given area
import math


def paint_calc(height, width, cover):
    area = height * width
    number_of_can = math.ceil(area / cover)
    can_word = "cans" if number_of_can > 1 else "can"
    print(f"You need {number_of_can} paint {can_word}.")


test_h = float(input("Height of the wall (m): "))
test_w = float(input("Width of the wall (m): "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
