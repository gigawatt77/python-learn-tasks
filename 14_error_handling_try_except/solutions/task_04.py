ящиков_для_деления = [2, 0, 5]

for число in ящиков_для_деления:
    try:
        print(20 / число)
    except ZeroDivisionError:
        print("Нельзя делить на 0!")
