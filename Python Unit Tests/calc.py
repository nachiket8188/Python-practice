def add(x, y):
    """Add function"""
    return x + y


def subtract(x, y):
    """subtract function"""
    return x - y


def multiply(x, y):
    """Multiply function"""
    return x * y


def divide(x, y):
    """Division function"""
    if y == 0:
        return ValueError("Cannot divide by zero!")
    else:
        return x / y
