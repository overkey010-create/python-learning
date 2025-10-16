class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    
    def info(self):
        print("Марка:", self.brand, "Год:", self.year)
car1 = Car("Toyota", 2020)
car1.info()
    

class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        print("Гав-гав, я", self.name)
dog1 = Dog("Карл")
dog1.bark()


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
rect = Rectangle(2, 4)
print("Площадь: ", rect.area())