# Игра - Камень, Ножницы, Бумага
# Пользователь вводит число раундов
# Для каждого рауна вводит камень / ножницы / бумага
# Компьютер выбирает случайно и считается результат
# Считается у кого больше
# 1.Спрашиваем у пользователя количество раундов
# 2.Для каждого раунда получаем выбор и сравниваем
# 3.Показываем итог
import random

def select_variant():
    user_select = None
    while user_select not in CHOICES:
        user_select = input("Выберите: камень, ножницы или бумага? ").strip().lower()
        if user_select not in CHOICES:
            print("Не корректный выбор")
    return user_select

def compute_game_result(user_ch: str, comp_ch: str):
    if user_ch == comp_ch:
        print("Ничья")
        return (0,0)
    elif (user_ch == CHOICES[0] and comp_ch == CHOICES[1]) or \
    (user_ch == CHOICES[1] and comp_ch == CHOICES[2]) or \
    (user_ch == CHOICES[2] and comp_ch == CHOICES[0]):
        print("Победа")
        return (1,0)
    else:
        print("Проиграл")
        return (0,1)

def print_result(user_res: int, comp_res: int):
    print("-----Итог игры-----")
    print(f"Твой счет: {user_res}")
    print(f"Счет противника: {comp_res}")

    if user_res == comp_res:
        print("Результат игры - НИЧЬЯ")
    elif user_res > comp_res:
        print("Результат игры - ПОБЕДА")
    else:
        print("Результат игры - ПРОЙГРЫШЬ:(")

CHOICES = ("камень", "ножницы", "бумага")
rounds = int(input("Введите количество раундов целым числом: "))
user_score = 0
comp_score = 0


for round in range(1, rounds + 1):
    print(f"\nРаунд {round}")
    user_select = select_variant()
    comp_select = random.choice(CHOICES)
    print(f"Противник выбрал {comp_select}")
    [user_mode, comp_mode] = compute_game_result(user_select, comp_select)
    user_score += user_mode
    comp_score += comp_mode
print_result(user_score, comp_score)
