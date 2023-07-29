# Calculate Leap year

print("Welcome to Leap Year Calculation Program")
print("*" * 40)

year = int(input("Enter the year: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("This year is a LEAP YEAR.")
else:
    print("This year is not a LEAP YEAR.")
