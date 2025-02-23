def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError:
        return "Error: Unsupported operand type(s)"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# This line might cause an UnboundLocalError if 'result' is not defined in the try block.
print(result)