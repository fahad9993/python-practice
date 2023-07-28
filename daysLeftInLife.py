print("Life is too short to be counted but we live as if we will not die.\n"
      "Let's calculate your remaining life if you are about to live 90 years on earth.")
print("*" * 30)

age = int(input("Your age: "))

age_remaining = 90 - age

days_left = age_remaining * 365
weeks_left = age_remaining * 52
months_left = age_remaining * 12

print(f"You have {days_left} days or, {weeks_left} weeks, or {months_left} months, or {age_remaining} years left.")
