import pandas as pd

# Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(nato_dict)

# Create a list of the phonetic code words from a word that the user inputs.

