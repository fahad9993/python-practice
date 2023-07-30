print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? (S, M or L) ").upper()
add_pepperoni = input("Do you want to add pepperoni? (Y or N) ").upper()
extra_cheese = input("Do you want extra cheese? (Y or N) ").upper()

bill = 0

if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
else:
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
print(f"Your order:\nPizza size: {size}\nPepperoni: {add_pepperoni}\nExtra Cheese: {extra_cheese}")
print("=" * 20)
print(f"Total bill: ${bill}")
