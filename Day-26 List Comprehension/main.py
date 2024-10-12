with open("file1.txt") as file_1:
    data_1 = file_1.readlines()
    num_list_1 = [int(num.strip()) for num in data_1]
    # print(num_list_1)

with open("file2.txt") as file_2:
    data_2 = file_2.readlines()
    num_list_2 = [int(num.strip()) for num in data_2]

result = [num for num in num_list_1 if num in num_list_2]
print(result)