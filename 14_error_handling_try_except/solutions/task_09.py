этапы = ["15", "0", "abc", "30", "-5"]

for значение in этапы:
    try:
        топливо = int(значение)
        print(100 / топливо)
    except ValueError:
        print("Повреждённые данные:", значение)
    except ZeroDivisionError:
        print("Топливо закончилось!")
