top = {
    "one": 1,
    "two": 2,
    "three": 3
}

for key in top:
    print(key)

top["four"] = 4
print(top)


shop = {
    "яблоко": 50,
    "банан": 30,
    "груша": 70
}


for key, value in shop.items():
    print(key, "->", value)


item = input("Введите товар: ")

if item in shop:
    print("Цена:", shop[item])
else:
    print("Такого товара нет")
