def calculator():
    """Performs basic arithmetic operations based on user input."""

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter operation (+, -, *, /): ")

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            return "Division by zero!"
        else:
            result = num1 / num2
    else:
        return "Invalid operator!"

    print(f"{num1} {op} {num2} = {result}")

if __name__ == "__main__":
    calculator()
