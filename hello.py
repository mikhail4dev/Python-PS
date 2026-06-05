word = str(input("Введите слово: ")).lower()

word_invert = word[::-1].lower()

if word == word_invert:
    print(f"Слово {word} является палиндромом")
else:
    print(f"Слово {word} НЕ является палиндромом")