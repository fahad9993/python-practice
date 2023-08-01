scores = input("Input a list of scores separated by a space: ").split()
scores = [int(score) for score in scores]
print(scores)

# Calculating max score
# max_score = max(scores)
max_score = 0
for score in scores:
    if score > max_score:
        max_score = score
print(f"The highest score in the class is: {max_score}")
