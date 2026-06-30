#Функция - генератор паролей принимающий:
#lenght
#use_symbol

import string
import random

def generate_password(lenght: int = 8, use_symbols:bool = True):
    if lenght <= 3:
        return ""
    
    letters = string.ascii_letters
    digits = string.digits
    symbols = "!@#$%&*?"

    pool = letters + digits + (symbols if use_symbols else "")

    password_charts: list[str] = []

    while len(password_charts) < lenght:
        password_charts.append(random.choice(pool))

    return "".join(password_charts)


print(generate_password(15))
print(generate_password(12, False))
print(generate_password(3))