def perform_operation(num1, num2, operation):
    num1 = float(num1)
    num2 = float(num2)
    if operation == "add" :
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Cannot divide by zero.")
    else:
        print("Invalid operation. Please choose +, -, *, or /.")
    return result
