# List Comprehension

# with open("file1.txt") as file_1:
#     data_1 = file_1.readlines()
#
# with open("file2.txt") as file_2:
#     data_2 = file_2.readlines()
#
# result = [int(num) for num in data_1 if num in data_2]
# print(result)

# Dictionary Comprehension - 01

# sentence = "What is the Airspeed Velocity of an unladen Swallow?"
#
# words = sentence.split()
# result = {word:len(word) for word in words}
#
# print(result)

# Dictionary Comprehension - 02

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}


def to_fahrenheit(c):
    """Converts temperature in Celsius to Fahrenheit"""
    return (c * 9 / 5) + 32


weather_f = {day: to_fahrenheit(temp_c) for (day, temp_c) in weather_c.items()}

print(weather_f)
