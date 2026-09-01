анкеты = ["15", "0", "abc", "30", "-5"]

for значение in анкеты:
    try:
        возраст = int(значение)
        print(100 / возраст)
    except ValueError:
        print("Некорректный возраст:", значение)
    except ZeroDivisionError:
        print("Возраст не может быть 0!")
