# Угадай число

import random

secret_number = random.choice(range(1,11))
guess = 0

print("Угадай число от 1 до 10")

while guess != secret_number:
    guess = int(input("Введите число: "))
    if guess < secret_number:
        print("Загаданное число больше")
    elif guess > secret_number:
        print("Загаданное число меньше")
print("Вы угаладали")