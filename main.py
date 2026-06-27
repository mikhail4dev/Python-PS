# Калькулятор

from typing import Literal

def calculate(a:float, b:float, operation: Literal["+", "-", "*", "/"]):
    
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

#Star arguments

def avg(*args: int):
    return sum(args) / len(args)

def prints_data(name: str, *data: str):
    print(name, data)

prints_data("Михаил", "fd", "gdfg", "dsfsd")

#Значение по умолчанию

def exp(num: float, e:float = 2, mul:float = 1) -> float:
    return mul * num ** e

print(exp(e=3, num=2))
print(exp(2, mul=3))