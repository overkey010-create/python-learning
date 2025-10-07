import random

print("Добро пожаловать в игру 'Угадай число'!")
print("Я загадал число от 1 до 10. Попробуй угадать!")

secret = random.randint(1, 10)

while True:
    guess = int(input("Твой вариант: "))

    if guess == secret:
        print("🎉 Поздравляю! Ты угадал!")
        break
    elif guess < secret:
        print("Моё число больше!")
    else:
        print("Моё число меньше!")
