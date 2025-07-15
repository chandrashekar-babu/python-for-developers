class Person:
    species = "Homo Sapiens" # Class attribute
    count = 0 # Class attribute to track 
             # instances
 
    def __init__(self, name):
        self.name = name  # Instance attribute
        Person.count += 1 # Updating class
                          # attribute
 
print(Person.species) # "Homo Sapiens"
print(Person.count) # Number of instances created