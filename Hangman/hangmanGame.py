import random
import hangman_art
import hangman_words

selected_word = random.choice(hangman_words.word_list)
print(selected_word)

printed_word = []
lives = 6

for _ in selected_word:
    printed_word += "_"
print(printed_word)

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(len(selected_word)):
        letter = selected_word[position]
        if letter == guess:
            printed_word[position] = guess
    if guess not in selected_word:
        lives -= 1
    print(printed_word)

    if lives == 0:
        end_of_game = True
        print("You lose!")

    if "_" not in printed_word:
        end_of_game = True
        print("You win.")

    print(hangman_art.stages[lives])
