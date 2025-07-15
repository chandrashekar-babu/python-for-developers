class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
        
    def perimeter(self):
        return 2 * (self.width + self.height)
        
    def resize(self, width, height):
        self.width = width
        self.height = height
        
rect = Rectangle(5, 10)
print(rect.area())       # 50
print(rect.perimeter())  # 30
rect.resize(7, 14)
print(rect.area())       # 98