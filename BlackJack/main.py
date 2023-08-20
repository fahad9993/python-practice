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
        # Clearing the console
        # For this to work you should enable "Emulate terminal in output console"
        # from Run>Edit Configurations>Add new>Python>Modify option>Emulate terminal in output console
        # Then selecting the script path
        import os
        os.system('cls')
        # At first two cards are given to the user
        your_cards = random.choices(cards, k=2)
        current_score = sum(your_cards)
        # When the sum is greater than 21 and there are 11 (Ace) in the deck, the Ace (11) can be considered as 1
        # It is a rule of Black Jack game
        # You can find more at https://games.washingtonpost.com/games/blackjack
        if current_score > 21 and 11 in your_cards:
            your_cards[your_cards.index(11)] = 1
            current_score = sum(your_cards)
        print(f"Your cards: {your_cards}, Current score: {current_score}")
        # Two cards are also given to the Dealer (Here Computer)
        # In Black Jack game, the computer is known as Dealer
        computer_cards = random.choices(cards, k=2)
        computers_score = sum(computer_cards)
        # Here the same rule applies, 11 (Ace) can be replaced with 1 if needed
        if computers_score > 21 and 11 in computer_cards:
            computer_cards[computer_cards.index(11)] = 1
            computers_score = sum(computer_cards)
        # Only displaying the first card of the Dealer, the other one is hidden
        # It is also a game rule
        print(f"Computer's first card: {computer_cards[0]}")
        # While loop starts for offering the user get another card up to total score of 21
        want_another_card = True
        # Checks is the user score exceed 21 if not then giving him option to get another card
        # If the total score exceed 21, then the user will not get any option to choose another card
        while current_score < 21 and want_another_card:
            get_another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if get_another_card == 'y':
                your_cards += random.choices(cards, k=1)
                current_score = sum(your_cards)
                if current_score > 21 and 11 in your_cards:
                    your_cards[your_cards.index(11)] = 1
                    current_score = sum(your_cards)
                # printing the current status of the game. The second card of the Dealer is still hidden.
                print(f"Your cards: {your_cards}, Current score: {current_score}")
                print(f"Computer's first card: {computer_cards[0]}")
            else:
                # If the user choose 'n' then this condition is fulfilled
                # In this case, to break the while loop, it is set to False
                want_another_card = False
        # The rule is, the Dealer is bound to get another card until he exceeds total 16
        # But, if the user's score is greater than 21, then the user is already lost the game.
        # So there is no need to choose another card for the Dealer.
        # If the Dealer's total score exceed 16, then he will also not get any chance to choose another card.
        # The rules can be found here: https://games.washingtonpost.com/games/blackjack
        while computers_score <= 16 and current_score <= 21:
            computer_cards += random.choices(cards, k=1)
            computers_score = sum(computer_cards)
            if computers_score > 21 and 11 in computer_cards:
                computer_cards[computer_cards.index(11)] = 1
                computers_score = sum(computer_cards)
            computers_score = sum(computer_cards)
        print(f"Your final hand: {your_cards}, final score: {current_score}")
        print(f"Computers final hand: {computer_cards}, final score: {computers_score}")
        # Here starts the comparing part.
        # The winner of looser of the game will be decided afterward.
        # There could be three possible cases. Those follows:
        # Case 1:
        if current_score > computers_score:
            if current_score <= 21:
                print("You win!")
            else:
                print("You lose.")
        # Case 2:
        elif current_score == computers_score:
            print("It's a draw.")
        # Case 3:
        else:
            if computers_score <= 21:
                print("You lose.")
            else:
                print("You win.")
