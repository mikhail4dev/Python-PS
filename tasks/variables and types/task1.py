# **Описание**: Создайте программу для объявления переменных разных типов и вывода их типов данных
#
# **Входные данные**: Нет (используйте встроенные значения)
#
# **Выходные данные**: Значения переменных и их типы
#
# **Ограничения**: Используйте только базовые типы Python (int, float, str, bool)
#
# **Примеры**:
# Output: 25 <class 'int'>
#         19.99 <class 'float'>
#         Alice <class 'str'>
#         True <class 'bool'>

# Ваш код здесь
name = str("Michail")
age = int(29)
is_developer = bool(True)
experience = float(5.5)

print(name, type(name))
print(age, type(age))
print(is_developer, type(is_developer))
print(experience, type(experience))