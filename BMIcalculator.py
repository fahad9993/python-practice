# Calculate your BMI
print("Welcome to the BMI Calculator.")

height = float(input("Enter your height in meter: "))

weight = float(input("Enter your weight in kg: "))

# BMI = round(weight / height ** 2, 0)

BMI = int(weight / height ** 2)

print("Your BMI is " + str(BMI))
