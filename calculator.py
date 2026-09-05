import function

def calculate():
    while True:
        try:
            first_number = float(input("Enter the first number: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        operator = input("Choose an operator (+, -, *, /): ")

        try:
            second_number = float(input("Enter the second number: "))
            print()
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if operator == "+":
            result = function.addition(first_number, second_number)
            print(f"{first_number} + {second_number} = {result}")

        elif operator == "-":
            result = function.subtraction(first_number, second_number)
            print(f"{first_number} - {second_number} = {result}")

        elif operator == "*":
            result = function.multiplication(first_number, second_number)
            print(f"{first_number} * {second_number} = {result}")

        elif operator == "/":
            result = function.division(first_number, second_number)
            if result is None:
                print("Error: Division by zero is not allowed.")
            else:
                print(f"{first_number} / {second_number} = {result}")
        else:
            print("Invalid operator")

        print()
        continue_calc = input("Do you want to calculate again? (yes/no): ")
        if continue_calc.lower() == "yes":
            continue
        else:
            break
