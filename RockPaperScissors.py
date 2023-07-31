import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [rock, paper, scissors]
print("Type 0 for Rock, 1 for Paper, and 2 for Scissors.")
your_choice = int(input("Your choice: "))
computers_choice = random.randint(0, 2)

# Checking for invalid choice
if your_choice > 2 or your_choice < 0:
    print(f"You chose: {your_choice}")
else:
    print("You chose:\n" + choices[your_choice])

print("Computer chose:\n" + choices[computers_choice])

# Ultimate gameplay logic starts here
if your_choice == computers_choice:
    print("It's a Draw!")
elif your_choice > 2 or your_choice < 0:
    print("You chose an invalid number. You lose!")
elif your_choice == 0 and computers_choice == 2:
    print("You win!")
elif computers_choice == 0 and your_choice == 2:
    print("You lose! Better luck next time.")
elif your_choice > computers_choice:
    print("You win!")
elif computers_choice > your_choice:
    print("You lose! Better luck next time.")
