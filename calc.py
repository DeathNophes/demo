def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def get_numbers():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return get_numbers()

def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    operations = {
        '1': add,
        '2': subtract,
        '3': multiply,
        '4': divide
    }

    while True:
        choice = input("Enter choice (1/2/3/4): ")
        if choice not in operations:
            print("Invalid choice. Please try again.")
            continue

        num1, num2 = get_numbers()
        result = operations[choice](num1, num2)
        print(f"The result is: {result}")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ").lower()
        if next_calculation != 'yes':
            print("Goodbye!")
            break

calculator()
