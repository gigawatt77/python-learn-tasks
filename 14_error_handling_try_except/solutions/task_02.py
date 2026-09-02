очки = 10
матчи = 0

try:
    результат = очки / матчи
except ZeroDivisionError:
    print("На ноль делить нельзя!")
