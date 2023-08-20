from art import logo
import random

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play = True
while play:
    play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play_again == "n":
        play = False
    else:
        your_cards = random.choices(cards, k=2)
        current_score = sum(your_cards)
        if current_score > 21 and 11 in your_cards:
            your_cards[your_cards.index(11)] = 1
            current_score = sum(your_cards)
        print(f"Your cards: {your_cards}, Current score: {current_score}")
        computer_cards = random.choices(cards, k=2)
        computers_score = sum(computer_cards)
        if computers_score > 21 and 11 in computer_cards:
            computer_cards[computer_cards.index(11)] = 1
            computers_score = sum(computer_cards)
        print(f"Computer's first card: {computer_cards[0]}")
        want_another_card = True
        while current_score < 21 and want_another_card:
            get_another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if get_another_card == 'y':
                your_cards += random.choices(cards, k=1)
                current_score = sum(your_cards)
                if current_score > 21 and 11 in your_cards:
                    your_cards[your_cards.index(11)] = 1
                    current_score = sum(your_cards)
                # computer_cards += random.choices(cards, k=1)
                # computers_score = sum(computer_cards)
                print(f"Your cards: {your_cards}, Current score: {current_score}")
                print(f"Computer's first card: {computer_cards[0]}")
            else:
                want_another_card = False
        while computers_score <= 16:
            computer_cards += random.choices(cards, k=1)
            if computers_score > 21 and 11 in computer_cards:
                computer_cards[computer_cards.index(11)] = 1
                computers_score = sum(computer_cards)
            computers_score = sum(computer_cards)
        print(f"Your final hand: {your_cards}, final score: {current_score}")
        print(f"Computers final hand: {computer_cards}, final score: {computers_score}")
        if current_score > computers_score:
            if current_score <= 21:
                print("You win!")
            else:
                print("You lose.")
        elif current_score == computers_score:
            print("It's a draw.")
        else:
            if computers_score <= 21:
                print("You lose.")
            else:
                print("You win.")
