x, y = 5, 0

try:
    # Code that might raise an exception
    result = x / y
except ZeroDivisionError as e:
    # Handle specific exception
    print(f"Error: {e}")
except (TypeError, ValueError) as e:
    # Handle multiple exceptions
    print(f"Input error: {e}")
except Exception as e:
    # Catch-all for other exceptions (use sparingly)
    print(f"Unexpected error: {e}")
else:
    # Execute if no exceptions were raised
    print(f"Result: {result}")
finally:
    # Always execute, regardless of exceptions
    print("Cleanup code")
