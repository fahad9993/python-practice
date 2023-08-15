from art import logo

print(logo)
bidder_info = []

print("Welcome to the secret auction program.")

run_again = True
while run_again:
    bidder_name = input("What is your name?: ")
    bid_amount = input("What is your bid?: $")

    new_bidder = {
        "name": bidder_name,
        "amount": bid_amount,
    }
    bidder_info.append(new_bidder)

    user_input = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if user_input == "no":
        run_again = False
    else:
        # Clearing the console
        # For this to work you should enable "Emulate terminal in output console"
        # from Run>Edit Configurations>Add new>Python>Modify option>Emulate terminal in output console
        # Then selecting the script path
        import os
        os.system('cls')

print(bidder_info)
