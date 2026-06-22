# Таблица умножения от 1 до 10

for i in range(1,11):
    for k in range(1, 11):
        print(f"{i * k:4}", end="")
    print("\n")