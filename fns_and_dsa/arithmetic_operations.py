def perform_operation(num1, num2, operation):
    num1 = float(num1)
    num2 = float(num2)
    match operation:
        case "add" :
            result = num1 + num2
        case "subtract" :
            result = num1 - num2
        case "multiply" :
            result = num1 * num2
        case "divide" :
            if num2 != 0:
                result = num1 / num2
            else:
                print("Cannot divide by zero.")
        case _:
            print("Invalid operation. Please choose +, -, *, or /.")
    return result
