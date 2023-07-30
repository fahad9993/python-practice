print("Welcome to the Roller Coaster Ride")

height = float(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the roller coaster!")

    age = int(input("What is your age? "))

    if age < 12:
        bill = 5
        print(f"Child tickets are ${bill} each.")
    elif age < 18:
        bill = 7
        print(f"Youth tickets are ${bill} each.")
    elif 45 <= age <= 55:
        bill = 0
        print(f"Aged 45-55 will enjoy free ride with {bill} cost.")
    else:
        bill = 12
        print(f"Adult tickets are ${bill} each.")

    wants_photo = input("Do you want to take photos? (Y or N) ")

    if wants_photo.upper() == "Y":
        print("Additional $3 will be added to your bill.")
        bill += 3

    print("=" * 15)
    print(f"Your total bill is ${bill}.")

else:
    print("Sorry, you have to grow taller before you can ride.")
