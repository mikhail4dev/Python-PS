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

print(f"{final_cost:.2f} {rub_symbol}")  """

def is_valid_cost_format(input_cost:str) -> bool:
    if 'руб' not in input_cost:
        print("Некорректный формат суммы")
        return False
                
    list_cost = input_cost.split(" ")
    rubles = list_cost[0]
    penny = "0"

    if 2 < len(list_cost) <= 4:
        if 'коп' not in input_cost:
            print("Некорректный формат суммы")
            return False
        else:
            penny = list_cost[2]
            
    if not rubles.isdigit() or not penny.isdigit():
        print((
            "Некорректный формат суммы\n"
            f"Значение в переменной rebles: {rubles}\n"
            f"Значение в переменной penny: {penny}"
            ))
        return False
    
    return True

def is_index_valid(index):
    if type(index) is int:
        print("Индекс должен быть целым числом")
        return False
    if index <= 0:
        print("Индекс не может быть меньше или равен 0")
        return False
    return True

def add_expense(expenses: list, value:str):
    value_list = value.split(" ")
    value_float = None

    if 2 < len(value_list) <= 4:
        value_float = float(value_list[0] + "." + value_list[2])
    else:
        value_float = float(value_list[0])

    return expenses.append(value_float)

def delete_expence(expenses, index):
    if len(expenses) > 0:
        format_index = index - 1
        del expenses[format_index]
        return expenses
    else:
        print("Нечего удалять, список расходов пустой")

def get_total(expenses) -> float:
    return sum(expenses)

def get_average(expenses) -> float:
    return sum(expenses) / len(expenses)

def print_total_and_average(expenses):
    print(f"Сумма всех расходов: - {get_total(expenses)} RUB")
    if len(expenses) == 0:
        print("Список расходов пустой")
    else:
        print(f"Средний расход: - {get_average(expenses)} RUB")

def print_report(expenses):
    print_total_and_average(expenses)
    print(f"{"-" * 20}")
    if len(expenses) > 0:
        for i,cost in enumerate(expenses):
            print(f"Расход №{i} - {cost} RUB")
    


MENU_LIST = ("Добавить расход", "Показать все расходы", "Показать сумму и средний расход", "Удалить расход по номеру", "Выход")
expenses_list = []
is_active_menu = True

while is_active_menu:
    print(f"{"=" * 30}")
    for i, item in enumerate(MENU_LIST):
        if i + 1 == len(MENU_LIST):
            print(f"{(i + 1) - len(MENU_LIST)} - {item}")
        else:
            print(f"{i + 1} - {item}")
            print(f"{"-" * 30}")
    print(f"{"=" * 30}")
    user_select = int(input("Выберите действие из меню(укажите только цифру): "))
    match user_select:
        case 0:
            is_active_menu = False
            print("Программа закрыта")
        case 1:
            input_is_valid = True
            user_input = None
            while input_is_valid:
                user_input = input("Введите стоимость покупки в формате <руб> руб <коп> коп: ").strip().lower()
                input_is_valid = not is_valid_cost_format(user_input)
            add_expense(expenses_list, user_input)
        case 2:
            print_report(expenses_list)
        case 3:
            print_total_and_average(expenses_list)
        case 4:
            index_input_is_valid = True
            user_index = None
            while index_input_is_valid:
                user_index = int(input("Укажите номер расхода который хотите удалить: "))
                index_input_is_valid = is_index_valid(user_index)
            expenses_list = delete_expence(expenses_list, user_index)
        case _:
             print("Не известная опция")
