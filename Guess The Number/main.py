from art import logo
import random
import os


def random_number():
    """Generates a random number between 1 and 100."""
    return random.randint(1, 100)


def lives_remaining(lives, answer):
    """Generates custom print messages based on remaining lives and random number, which is guessed."""
    if lives == 0:
        print("You have ran out of guesses. You lose.")
        print(f"The correct answer is {answer}.")
    else:
        var = "s" if lives > 1 else ""
        print(f"You have {lives} attempt{var} remaining to guess the number.")


def guess_number():
    """Ask the player to choose easy or hard mode. After that receives guess from the player.
    Also, checks the answer with the guess."""
    print(logo)
    print("Welcome to the Number Guessing Game.")
    print("I am thinking of a number between 1 and 100.")
    answer = random_number()
    print(f"Psst, the correct answer is {answer}.")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        lives = 10
    else:
        lives = 5

    while lives > 0:
        guessed_number = int(input("Make a guess: "))
        if guessed_number == answer:
            print(f"You got it! The answer was {guessed_number}.")
            break
        elif guessed_number > answer:
            print("Too high.")
            print("Guess again.")
            lives -= 1
            lives_remaining(lives, answer)
        else:
            print("Too low.")
            print("Guess again.")
            lives -= 1
            lives_remaining(lives, answer)


guess_number()
while input("Play again? Type 'y' for yes, 'n' for no. ").lower() == "y":
    os.system('cls')
    guess_number()
