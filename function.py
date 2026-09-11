def addition(first_number, second_number):
    result = first_number + second_number
    return result

def subtraction(first_number, second_number):
    result = first_number - second_number
    return result

def multiplication(first_number, second_number):
    result = first_number * second_number
    return result

def division(first_number, second_number):
    try:
        result = first_number / second_number
    except ZeroDivisionError:
        return None
    return result