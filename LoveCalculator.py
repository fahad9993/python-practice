# Love Calculator

print("Welcome to Love Calculator!")
name1 = input("What is your name? ").lower()
name2 = input("What is their name? ").lower()

# "TRUE LOVE" letters count
t = name1.count("t") + name2.count("t")
r = name1.count("r") + name2.count("r")
u = name1.count("u") + name2.count("u")
e = name1.count("e") + name2.count("e")

true = t + r + u + e

l0 = name1.count("l") + name2.count("l")
o = name1.count("o") + name2.count("o")
v = name1.count("v") + name2.count("v")
e = name1.count("e") + name2.count("e")

love = l0 + o + v + e

score = int(str(true) + str(love))

if score < 10 or score > 90:
    print(f"Your score is {score}. You go together like coke and mentos!")
elif 40 <= score <= 50:
    print(f"Your score is {score}. You are alright together.")
else:
    print(f"Your score is {score}.")
