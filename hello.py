floor:int = int(input("Выберите этаж: "))

match floor:
    case -1:
        print("Подвал: здесь находится склад")
    case 1:
        print("Холл и ресепшен")
    case _ if 2 <= floor <= 9:
        if floor % 2 == 0:
            print(f"Офиосный этаж: {floor}")
        else:
            print(f"Жилой этаж: {floor}")
    case 10:
        print("Технической этаж - вход запрещен")
    case _:
        print(f"Такого этажа не существует: {floor}")
