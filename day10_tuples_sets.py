numbers = (1, 2, 3, 4, 5)
print(numbers[0])
print(numbers[-1])


coordinates = (10, 20)
x = coordinates[10]
y = coordinates[20]
print("X = ", x, "Y =", y)

lst = [1, 2, 2, 3, 3, 4]
unique = set(lst)
print(unique)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("объединение: ", a | b)
print("пересечение: ", a & b)
print("разность: ", a - b)