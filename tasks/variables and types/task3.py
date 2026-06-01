# **Описание**: Создайте переменные с использованием подсказок типов (type hints) и выведите их значения с типами
# **Входные данные**: Нет (используйте встроенные значения)
# **Выходные данные**: Значения переменных и их типы через type()
# **Ограничения**: Обязательно используйте подсказки типов при объявлении переменных (например, name: str = "value")
# **Примеры**:
# Output: 42 <class 'int'>
#         3.14 <class 'float'>
#         Python <class 'str'>
#         False <class 'bool'>

# Ваш код здесь

name: str = "Michail"
age: int = 29
is_developer: bool = True
experience: float = 5.5

print(name, type(name))
print(age, type(age))
print(is_developer, type(is_developer))
print(experience, type(experience))

#Для более компактного вывода

print(f"{name} {type(name)}")