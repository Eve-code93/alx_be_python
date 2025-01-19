def safe_divide(numerator, denominator):
    """Safely performs division while handling errors."""
    try:
        num = float(numerator)
        denom = float(denominator)
        
        if denom == 0:
            return "Error: Cannot divide by zero."
        
        return f"The result of the division is {num / denom:.1f}"
    except ValueError:
        return "Error: Please enter numeric values only."
