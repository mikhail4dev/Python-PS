""" cost = input("Введите стоимость покупки в формате <руб> руб <коп> коп: ").strip().lower()

if 'руб' not in cost:
    print("Некорректный формат суммы")
    exit()

list_cost = cost.split(" ")
rubles = list_cost[0]
penny = "0"

if 2 < len(list_cost) <= 4:
    if 'коп' not in cost:
        print("Некорректный формат суммы")
        exit()
    penny = list_cost[2]


if not rubles.isdigit() or not penny.isdigit():
    print((
        "Некорректный формат суммы\n"
        f"Значение в переменной rebles: {rubles}\n"
        f"Значение в переменной penny: {penny}"
        ))
    exit()

final_cost = float(rubles + "." + penny)
rub_symbol = chr(8381)

print(f"{final_cost:.2f} {rub_symbol}") """

MENU_LIST = ("Добавить расход", "Показать все расходы", "Показать сумму и средний расход", "Удалить расход по номеру", "Выход")
user_select = 1

while user_select:
    print(f"{"=" * 30}")
    for i, item in enumerate(MENU_LIST):
        if i + 1 == len(MENU_LIST):
            print(f"{(i + 1) - len(MENU_LIST)} - {item}")
        else:
            print(f"{i + 1} - {item}")
            print(f"{"-" * 30}")
    print(f"{"=" * 30}")
    user_select = int(input("Выберите действие из меню(укажите только цифру): "))

