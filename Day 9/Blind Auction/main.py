from art import logo

print(logo)
bidder_info = {}

print("Welcome to the secret auction program.")


def highest_bidder(bidder_information):
    max_bidder_amount = 0
    max_bidder_name = ""

    for bidder in bidder_information:
        next_bidder_amount = bidder_information[bidder]
        if next_bidder_amount > max_bidder_amount:
            max_bidder_amount = next_bidder_amount
            max_bidder_name = bidder

    print(f"The winner is {max_bidder_name} with a bid of ${max_bidder_amount}.")


run_again = True
while run_again:
    bidder_name = input("What is your name?: ")
    bid_amount = int(input("What is your bid?: $"))

    bidder_info[bidder_name] = bid_amount

    user_input = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if user_input == "no":
        run_again = False
        highest_bidder(bidder_info)
    else:
        # Clearing the console
        # For this to work you should enable "Emulate terminal in output console"
        # from Run>Edit Configurations>Add new>Python>Modify option>Emulate terminal in output console
        # Then selecting the script path
        import os

        os.system('cls')

print(bidder_info)
