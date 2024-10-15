import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}


# Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        output = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output)


generate_phonetic()
