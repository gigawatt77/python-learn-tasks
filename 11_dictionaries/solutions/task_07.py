ages = {"Миша": 12, "Максим": 13, "Соня": 11}
total = 0

for name, age in ages.items():
    total = total + age

print("Сумма возрастов:", total)
