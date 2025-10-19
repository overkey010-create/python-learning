class Bird:
    def move(self):
        return "Птица летит"

class Fish:
    def move(self):
        return "Рыба плывёт"

animals = [Bird(), Fish()]
for a in animals:
    print(a.move())



import math
class Shape:
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

class Cirle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)
    
shapes = [Square(4), Square(3)]
for s in shapes:
    print(s.area())
