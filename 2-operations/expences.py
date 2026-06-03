food_costs:float = float(input("Введите затраты на еду"))
transportation_costs:float = float(input("Введите затраты на транспорт"))
entertainment_costs:float = float(input("Введите затраты на развлечния"))

total_costs = food_costs + transportation_costs + entertainment_costs
average_value = total_costs / 3

print(f"Cумма всех затрат: {total_costs} руб., среднее значение всех затрат: {average_value} руб.505")