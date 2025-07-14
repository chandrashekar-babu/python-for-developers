color = "white"

class Car:
    color = "blue" # class attribute

    def __init__(self):
        color = "red" # local variable
        self.color = "green"
        
    def drive(self):
        print("Driving a", color, "car")
        print("Car.color =", Car.color)
        print("self.color =", self.color)


c = Car()
c.drive()
