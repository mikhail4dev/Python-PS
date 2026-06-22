# Игра - Камень, Ножницы, Бумага
# Пользователь вводит число раундов
# Для каждого рауна вводит камень / ножницы / бумага
# Компьютер выбирает случайно и считается результат
# Считается у кого больше
# 1.Спрашиваем у пользователя количество раундов
# 2.Для каждого раунда получаем выбор и сравниваем
# 3.Показываем итог
import random

CHOICES = ("камень", "ножницы", "бумага")
rounds = int(input("Введите количество раундов целым числом: "))
user_score = 0
comp_score = 0


for round in range(1, rounds + 1):
    print(f"\nРаунд {round}")
    user_select = ""
    while user_select not in CHOICES:
        user_select = input("Выберите: камень, ножницы или бумага? ").strip().lower()
        if user_select not in CHOICES:
            print("Не корректный выбор")
    comp_select = random.choice(CHOICES)
    print(f"Противник выбрал {comp_select}")

    if user_select == comp_select:
        print("Ничья")
    elif (user_select == CHOICES[0] and comp_select == CHOICES[1]) or \
    (user_select == CHOICES[1] and comp_select == CHOICES[2]) or \
    (user_select == CHOICES[2] and comp_select == CHOICES[0]):
        print("Победа")
        user_score += 1
    else:
        print("Проиграл")
        comp_score += 1

print("-----Итог игры-----")
print(f"Твой счет: {user_score}")
print(f"Счет противника: {comp_score}")

if user_score == comp_score:
    print("Результат игры - НИЧЬЯ")
elif user_score > comp_score:
    print("Результат игры - ПОБЕДА")
else:
    print("Результат игры - ПРОЙГРЫШЬ:(")