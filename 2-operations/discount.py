price:float = float(input("Стоимость товара"))
discount:int = int(input("Процент скидки"))

price_for_dicount = price - (price * discount / 100)

print(f"Цена товара со скидкой: {price_for_dicount}")