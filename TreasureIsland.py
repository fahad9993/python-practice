# ascii.co.uk/art
print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
''')
print("Welcome to the treasure island.")
print("Your mission is to find the treasure.")

choice = input("Type \"left\" or \"right\" to choose your direction. ").lower()

if choice == "left":
    print("You have came to a well of snakes. Game Over!!!")
else:
    choice = input("Type \"swim\" or \"wait\" for your next move. ").lower()
    if choice == "swim":
        print("You have fell into the mouth of a shark. Game Over!!!")
    else:
        print("Ok. You have came in front of three doors colored Red, Green, and Blue.")
        choice = input("Type \"red\" or \"green\" or \"blue\" to select which door to enter. ").lower()
        if choice == "red":
            print("You won. Congratulation!!!")
        elif choice == "green":
            print("You have fell into fire. Game Over!!!")
        else:
            print("You have fell from a cliff. Game Over!!!")
