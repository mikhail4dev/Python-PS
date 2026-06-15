# cost = input("Введите стоимость покупки в формате <руб> руб <коп> коп: ").strip()
cost = '159 руб 10.10 коп'

if 'руб' not in cost:
    print("Некорректный формат суммы")
    exit()

list_cost = cost.split(" ")
rubles = list_cost[0]
penny = "0"

if 2 < len(list_cost) <= 4:
    penny = list_cost[2]

if not rubles.isdigit() and not penny.isdigit():
    print((
        "Некорректный формат суммы\n"
        f"Значение в переменной rebles: {rubles}\n"
        f"Значение в переменной penny: {penny}"
        ))
    exit()

final_cost = float(rubles + "." + penny)
rub_symbol = chr(8381)

print(f"{final_cost:.2f} {rub_symbol}")