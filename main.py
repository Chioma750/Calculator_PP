first_number = float(input("Enter the first number: "))
operator = input("Choose an operator (+, -, *, /): ")
second_number = float(input("Enter the second number: "))
# print(f"{first_number} and {second_number}")

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
    result = first_number / second_number
    print(f"{first_number} / {second_number} = {result}")    

else:
    print("Invalid operator")
