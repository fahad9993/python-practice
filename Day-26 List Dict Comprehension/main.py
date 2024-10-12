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

sentence = "What is the Airspeed Velocity of an unladen Swallow?"

words = sentence.split()
result = {word:len(word) for word in words}

print(result)
