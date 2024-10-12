# with open("weather-data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     temperature = []
#
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#
#     print(temperature)

import pandas

data = pandas.read_csv("weather-data.csv")
# print(data["temp"])

# temp_list = data["temp"].to_list()
# print(temp_list)
# avg_temp = sum(temp_list)/len(temp_list)
# print(f"Average temperature: {avg_temp}")

# average_temp = data["temp"].mean()
# print(f"Average temperature: {average_temp}")
# max_temp = data["temp"].max()
# print(f"Maximum temperature: {max_temp}")


def convert_to_fahrenheit(temp):
    """This function converts any temperature from Celsius to Fahrenheit"""
    return (9 * temp + 160) / 5


# Get data in a row
# print(data[data.temp == data.temp.max()])
monday_temp = data[data.day == "Monday"].temp
print(convert_to_fahrenheit(int(monday_temp.iloc[0])))
