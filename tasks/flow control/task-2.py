# **Описание**: Создайте программу для определения статуса покупки в интернет-магазине
# **Входные данные**: Строка - статус заказа
# **Выходные данные**: Строка с соответствующим сообщением о статусе
# **Ограничения**: Программа должна обрабатывать статусы: 'pending', 'processing', 'shipped', 'delivered'
# **Примеры**:
# Input: pending
# Output: Заказ ожидает обработки
# Input: processing
# Output: Заказ обрабатывается
# Input: shipped
# Output: Заказ отправлен
# Input: delivered
# Output: Заказ доставлен
# Input: cancelled
# Output: Неизвестный статус заказа

status = input("Введите статус заказа: ")

# Ваш код здесь

if status == "pending":
    print("Заказ ожидает обработки")
elif status == "processing":
    print("Заказ обрабатывается")
elif status == "shipped":
    print("Заказ отправлен")
elif status == "delivered":
    print("Заказ доставлен")
else:
    print("Неизвестный статус заказа")

match status:
    case "pending":
        print("Заказ ожидает обработки")
    case "processing":
        print("Заказ обрабатывается")
    case "shipped":
        print("Заказ отправлен")
    case "delivered":
        print("Заказ доставлен")
    case _:
        print("Неизвестный статус заказа")