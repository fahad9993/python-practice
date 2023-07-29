# Calculate your BMI
print("Welcome to the BMI Calculator.")

height = float(input("Enter your height in meter: "))

weight = float(input("Enter your weight in kg: "))

# BMI = round(weight / height ** 2, 0)

bmi = int(weight / height ** 2)

# Determining BMI category

category = ""

if bmi <= 18.5:
    category = "underweight"
elif bmi <= 25:
    category = "normal weight"
elif bmi <= 30:
    category = "overweight"
elif bmi <= 35:
    category = "obese"
else:
    category = "clinically obese"

print(f"Your BMI is {bmi} and you are in the \"{category.upper()}\" category.")

