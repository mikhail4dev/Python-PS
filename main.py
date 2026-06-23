# Калькулятор

def calculate(a:float, b:float, operation:str):
    
    match operation:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b if b != 0 else print("Нельзя разделить на 0")
        case _:
            return "Не известная операция"

a_num:float = float((input("Введите первое число: ")))
b_num:float = float((input("Введите второе число число: ")))
operator:str = str((input("Укажите операцию (+, -, *, /): ")))

print(calculate(a_num, b_num, operator))