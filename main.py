while True:
    try:
        first_number = float(input("Enter the first number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    operator = input("Choose an operator (+, -, *, /): ")

    try:
        second_number = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    if operator == "+":
        result = first_number + second_number
        print(f"{first_number} + {second_number} = {result}")    

    elif operator == "-":
        result = first_number - second_number
        print(f"{first_number} - {second_number} = {result}")

    elif operator == "*":
        result = first_number * second_number
        print(f"{first_number} * {second_number} = {result}")    

    elif operator == "/":  
        try:
            result = first_number / second_number
            print(f"{first_number} / {second_number} = {result}") 
        except ZeroDivisionError:
            print("You can't divide by zero because, division by zero is underfined.")   

    else:
        print("Invalid operator")

    continue_calc = input("Do you want to calculate again? (yes/no): ")
    if continue_calc.lower() == "yes":
        continue
    else:
        break
