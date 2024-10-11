# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as invitee_data:
    all_names = invitee_data.readlines()
    print(all_names)

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()
    for name in all_names:
        stripped_name = name.strip()
        inv_letter = letter.replace(PLACEHOLDER, stripped_name)

        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as replaced_letter:
            replaced_letter.write(inv_letter)

