def echo_generator():
    response = yield
    while True:
        response = yield f"Echo: {response}"

gen = echo_generator()
next(gen)  # Prime the generator
print(gen.send("Hello"))  # "Echo: Hello"
print(gen.send("World"))  # "Echo: World"