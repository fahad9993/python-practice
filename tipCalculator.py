print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? Taka "))

tip_percentage = float(input("What percentage of tip would you like to give? 10, 12, or 15? "))

number_of_people = int(input("How many people to split the bill? "))

total_tip = total_bill * tip_percentage / 100

total_bill_payable = total_bill + total_tip

bill_per_person = "{:.2f}".format(round(total_bill_payable / number_of_people, 2))

print(f"You have to pay total {total_bill_payable:.2f} taka and each person should pay: Taka {bill_per_person}")
