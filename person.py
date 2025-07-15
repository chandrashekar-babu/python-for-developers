class Person:
    def __init__(self, name):
        self.name = name  # Instance attribute
        
john = Person("John")
mary = Person("Mary")
print(john.name)  # "John"
print(mary.name)  # "Mary"