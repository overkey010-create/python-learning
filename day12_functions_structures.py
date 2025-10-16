def max_in_list(lst): # Максимум в списке
    maximum = max(lst)
    return maximum

print(max_in_list([1, 7, 3, 9, 2])) 


grades = {
    "Иван": [5, 4, 3],
    "Мария": [5, 5, 4],
    "Андрей": [3, 4, 4]
}

def find_student(grades, name):
    return grades.get("Мария")   # получаем оценки по имени

print(find_student(grades, "Мария"))  # ожидаем [5, 5, 4]

