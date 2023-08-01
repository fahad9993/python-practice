heights = input("Input a list of height separated by a space: (cm) ").split()

heights = [int(n) for n in heights]
# print(heights)
# print(len(heights))

# Using sum function
# avg_height = sum(heights)/len(heights)

# Using for loop
sum_heights = 0
for n in heights:
    sum_heights += n
number_of_people = 0
for people in heights:
    number_of_people += 1
avg_height = sum_heights / number_of_people

print(f"Average height is {avg_height: .2f} cm.")
