def function_with_uncommon_error(a, b):
    result = None  # Initialize the variable outside the try block
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError:
        return "Error: Unsupported operand type(s)"
    except Exception as e:
        return f"An unexpected error occurred: {e}"
    finally:
        return result # Return result even if no exception was raised

# The result variable is now correctly defined before being used
print(function_with_uncommon_error(10, 2)) #prints 5.0
print(function_with_uncommon_error(10, 0)) #prints Error: Division by zero
print(function_with_uncommon_error(10, 'a')) #prints Error: Unsupported operand type(s)