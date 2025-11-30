def safe_divide(numerator, denominator):
    """
    Perform division of numerator by denominator with robust error handling.

    Args:
        numerator: The number to be divided.
        denominator: The number to divide by.

    Returns:
        A string with the result or an error message.
    """
    try:
        # Convert inputs to floats
        num = float(numerator)
        denom = float(denominator)
        # Perform division
        result = num / denom
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
