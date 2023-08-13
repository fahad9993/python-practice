import random
from hangman_art import *
from hangman_words import word_list

selected_word = random.choice(word_list)
print(logo)

# Testing code
# print(f'Pssst, the solution is {selected_word}.')

printed_word = []
lives = 6

for _ in selected_word:
    printed_word += "_"
print(printed_word)

end_of_game = False  # For breaking the while loop

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    # Clearing the console
    # For this to work you should enable "Emulate terminal in output console"
    # from Run>Edit Configurations>Add new>Python>Modify option>Emulate terminal in output console
    # Then selecting the script path
    import os
    os.system('cls')

    if guess in printed_word:
        print(f"You have already guessed {guess}")
    for position in range(len(selected_word)):
        letter = selected_word[position]
        if letter == guess:
            printed_word[position] = guess
    if guess not in selected_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
    print(printed_word)

    # Decreasing the number of lives after each wrong guess
    if lives == 0:
        end_of_game = True
        print("You lose!")

    # If all the letters are successfully guess then there would be no blank space
    if "_" not in printed_word:
        end_of_game = True
        print("You win.")

    print(stages[lives])
