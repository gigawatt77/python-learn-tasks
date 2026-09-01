значения = ["3", "abc", "0", "8"]

for значение in значения:
    try:
        число = int(значение)
        print(50 / число)
    except ValueError:
        print("Не число:", значение)
    except ZeroDivisionError:
        print("Ноль запрещён!")
