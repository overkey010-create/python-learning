class BankAccount:
    def __init__(self, balance=0):
        self.___balance = balance

    def deposit(self, amount):
        self.___balance += amount

    def withdraw(self, amount):
        if amount <= self.___balance:
            self.___balance -= amount
        else:
            print("Недостаточно средств")

    def get_balance(self):
        return self.___balance
    
acc = BankAccount(100)
acc.deposit(50)
acc.withdraw(30)
print(acc.get_balance())   # 120


class Student:
    def __init__(self, name):
        self.name = name
        self.___grade = None   # приватный атрибут для оценки

    def set_grade(self, grade):
        if 1 <= grade <= 5:
            self.___grade = grade
        else:
            print("Оценка должна быть от 1 до 5")

    def get_grade(self):
        return self.___grade
    
s = Student("Анна")
s.set_grade(5)
print(s.get_grade())   # 5
s.set_grade(10)        # Ошибка



class PasswordManager:
    def __init__(self, password):
        self.___password = password   # приватный пароль

    def check_password(self, input_password):
        return self.___password == input_password


pm = PasswordManager("qwerty")
print(pm.check_password("qwerty"))   # True
print(pm.check_password("1234"))     # False



    