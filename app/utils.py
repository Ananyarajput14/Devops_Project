def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b

def divide_numbers(a, b):
    """Divide two numbers with error handling."""
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b
