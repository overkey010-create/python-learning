import json

movie = {
    "title": "Матрица",
    "year": 1999,
    "genre": "Фантастика"
}

with open("movie.json", "w", encoding="utf-8") as f:
    json.dump(movie, f, ensure_ascii=False, indent=4)


with open("movie.json", "r", encoding="utf-8") as f:
    data = json.load(f)
print(data["title"])





def save_students(students, filename):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(students, f, ensure_ascii=False, indent=4)

students = {
    "Андрей" : [5,4,3],
    "Марго" : [8,7,6]
}

save_students(students, "students.json")

def load_students(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

print(load_students("students.json"))