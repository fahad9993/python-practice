from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(logo)


def caesar(txt, sft, choice):
    end_text = ""
    sft %= 26
    if choice == "decode":
        sft *= -1
    for char in txt:
        if char in alphabet:
            letter_index = alphabet.index(char)
            shift_index = letter_index + sft
            end_text += alphabet[shift_index]
        else:
            end_text += char
    print(f"{choice.capitalize()}d text is:\n{end_text}")


run_again = True
while run_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(txt=text, sft=shift, choice=direction)
    user_input = input("Do you want to run again the program? (Y/N)\n").upper()
    if user_input == "N":
        run_again = False
        print("Goodbye!")
