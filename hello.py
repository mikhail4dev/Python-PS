first_num:float = float(input("Введите первое число"))
second_num:float = float(input("Введите второе число"))
third_num:float = float(input("Введите трете число"))

if first_num >= second_num and first_num >= third_num:
    print(f"Наибольшее число: {first_num}")
elif second_num >= first_num and second_num >= third_num:
    print(f"Наибольшее число: {second_num}")
else:
    print(f"Наибольшее число: {third_num}")