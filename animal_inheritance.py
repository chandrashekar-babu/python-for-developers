class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Some generic animal sound")
        
    def __str__(self):
        return f"{self.name} is a {self.species}"
        
class Dog(Animal):
    def __init__(self, name, breed, age):
        # Call parent's __init__
        super().__init__(name, species="Dog")
        # Add dog-specific attributes
        self.breed = breed
        self.age = age
        
    def make_sound(self):
        # Override parent's method
        print("Woof! Woof!")
        
    def __str__(self):
        # Extend parent's method
        base_str = super().__str__()
        return f"{base_str}, breed is {self.breed}, age is {self.age}"
