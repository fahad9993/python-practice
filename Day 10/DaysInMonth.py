def is_leap(your_year):
    """Take a year and check if it is a leap year and return True or False according to the result."""
    if your_year % 4 == 0:
        if your_year % 100 == 0:
            if your_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(check_year, check_month):
    if check_month > 12 or check_month < 1:
        return "Invalid input!"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(check_year) and check_month == 2:
        return 29
    return month_days[check_month - 1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
