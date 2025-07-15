def function_a():
    try:
        function_b()
    except ValueError:
        print("Caught ValueError in function_a")

def function_b():
    function_c()  # Will propagate exceptions

def function_c():
    raise ValueError("Error in function_c")

function_a()  # Prints "Caught ValueError in function_a"