user_email = input("Введите ваш email: ")

if user_email.count("@") != 1:
    print("Не верный email")
    exit()

local, domain = user_email.split("@")

if not local:
    print("Не верный email")
    exit()

if "." not in domain:
    print("Не верный email")
    exit()

if len(domain.split(".")[-1]) < 2:
    print("Не верный email")
    exit()

if len(domain.split(".")[0]) == 0:
    print("Не верный email")
    exit()

print("Верный email")
