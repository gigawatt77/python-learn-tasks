def безопасное_деление(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Ошибка: деление на ноль"


print(безопасное_деление(10, 2))
print(безопасное_деление(10, 0))
