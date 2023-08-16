from art import logo

print(logo)


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

num1 = int(input("What's the first number?: "))
for operator in operators:
    print(operator)
operation_symbol = input("Pick and operation from the line above: ")
num2 = int(input("What's the second number?: "))
answer = operators[operation_symbol](num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")