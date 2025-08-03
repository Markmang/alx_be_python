def safe_divide(numerator, denominator):
    
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        if denominator == 0:
            raise ZeroDivisionError
        if numerator != float(numerator) or denominator != float(denominator):
            raise ValueError
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")
    else:
        result = numerator / denominator
        print(f"The result of the division is {result:.1f}")