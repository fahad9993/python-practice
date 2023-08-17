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

run_again = True
while run_again:
    operation_symbol = input("Pick an operation: ")
    while operation_symbol not in operators:
        print("Invalid Operator!")
        operation_symbol = input("Pick an operation: ")
    num2 = int(input("What's the next number?: "))
    answer = operators[operation_symbol](num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    continue_again = input(f"Type 'y' to continue again with {answer}, or type 'n' to exit.: ").lower()
    if continue_again == "n":
        run_again = False
    num1 = answer
