# day9_files.py
# Пошаговые упражнения по работе с файлами

FILENAME = "notes.txt"

def step1_write_initial():
    lines = ["Первая строка", "Вторая строка", "Третья строка"]
    # "w" — перезапишет файл; encoding="utf-8" — корректная запись русских букв
    with open(FILENAME, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print("Записали 3 строки в", FILENAME)

def step2_read_all():
    with open(FILENAME, "r", encoding="utf-8") as f:
        text = f.read()
    print("\nЧитаем весь файл целиком:")
    print("--------------------")
    print(text, end="")
    print("--------------------")

def step3_append_line():
    with open(FILENAME, "a", encoding="utf-8") as f:
        f.write("Четвёртая строка\n")
    print("Добавили строку в конец файла")

def step4_read_by_lines():
    print("\nЧитаем построчно с номерами:")
    with open(FILENAME, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f, start=1):
            print(f"{idx}: {line.strip()}")

if __name__ == "__main__":
    step1_write_initial()
    step2_read_all()
    step3_append_line()
    step4_read_by_lines()
