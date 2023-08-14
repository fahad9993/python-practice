alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(txt, sft, choice):
    end_text = ""
    if choice == "decode":
        sft *= -1
    for letter in txt:
        letter_index = alphabet.index(letter)
        shift_index = letter_index + sft
        end_text += alphabet[shift_index]
    print(f"{choice.capitalize()}d text is:\n{end_text}")


caesar(txt=text, sft=shift, choice=direction)
