alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(txt, sft, choice):
    encoded_text = ""
    decoded_text = ""
    if choice == "encrypt":
        for letter in txt:
            letter_index = alphabet.index(letter)
            shift_index = letter_index + sft
            if shift_index >= 26:
                shift_index -= 26
            encoded_text += alphabet[shift_index]
            # print(encoded_text)
        print(f"Encoded text is:\n{encoded_text}")
    else:
        for letter in txt:
            letter_index = alphabet.index(letter)
            shift_index = letter_index - sft
            if shift_index >= 26:
                shift_index -= 26
            decoded_text += alphabet[shift_index]
            # print(encoded_text)
        print(f"Decoded text is:\n{decoded_text}")


caesar(txt=text, sft=shift, choice=direction)
