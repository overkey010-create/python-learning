def max_in_list(lst): 
    maximum = max(lst)
    return maximum

print(max_in_list([1, 7, 3, 9, 2])) 


grades = {      
    "Иван": [5, 4, 3],
    "Мария": [5, 5, 4],
    "Андрей": [3, 4, 4]
}

def find_student(grades, name):
    return grades.get("name")  

print(find_student(grades, "Мария"))


def count_letters(word):
    counts = {}
    for letter in word:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1
    return counts

print(count_letters("banana"))  

