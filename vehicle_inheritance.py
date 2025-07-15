class Vehicle:
 def __init__(self, make, model, year):
   self.make = make
   self.model = model
   self.year = year
   self.is_running = False
 
 def start(self):
   self.is_running = True
   print(f"{self.make} {self.model} started")
 
 def stop(self):
   self.is_running = False
   print(f"{self.make} {self.model} stopped")
 
class Car(Vehicle):
 def __init__(self, make, model, 
              year, fuel_type):
   # Initialize the parent class
   super().__init__(make, model, year)
   # Add car-specific attributes
   self.fuel_type = fuel_type
   self.doors = 4
 
 def honk(self):
   print("Beep beep!")
