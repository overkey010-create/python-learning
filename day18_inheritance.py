class Bird:
    def fly(self):
        print("Птица летит")

class Eagle(Bird):
    def fly(self):
        print("Орел парит высоко")

b = Bird()
b.fly()       # Птица летит

e = Eagle()
e.fly()       # Орел парит высоко


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
     def bonus(self):
         return self.salary * 0.1 # бонус к зарлпате в виде 10%
     
m = Manager("Андрей", 25000)

print(m.name)
print(m.salary)
print(m.bonus())