try:
    num = int(input("Введите число: "))
    print("Квадрат: ", num ** 2)
except ValueError:
    print("Ошибка: это не число")


try:
    x = int(input("Введите первое число: "))
    y = int(input("Введите второе число: "))
    result = x / y
    print("Результат: ", result)
except ZeroDivisionError:
    print("На ноль не делится")


try:
    f = open("data.txt", "r")
    text = f.read()
except FileNotFoundError:
    print("Файл не найден")


try:
    a = int("f")
except ValueError:
    print("Ошибка")
finally:
    print("Завершение программы")
    
