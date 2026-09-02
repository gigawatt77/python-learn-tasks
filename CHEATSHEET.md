# Шпаргалка по Python 🐍

Короткая справка по синтаксису всех тем курса — держи открытой рядом,
пока решаешь задачи. Подробности и объяснения смотри в `theory_*.md`
внутри каждой темы.

## 1. print() и комментарии
```python
print("Привет!")            # печатает текст
print("a", "b", sep="-")    # печать с разделителем: a-b
# это комментарий, компьютер его не выполняет
```

## 2. Переменные и типы
```python
name = "Миша"     # str — текст
age = 12          # int — целое число
height = 150.5     # float — дробное число
is_cool = True     # bool — True/False
print(type(age))  # <class 'int'>
```

## 3. input() и преобразование типов
```python
name = input("Как тебя зовут? ")   # всегда возвращает str
age = int(input("Сколько лет? "))  # превращаем текст в число
```

## 4. Арифметика и операторы
```python
5 + 3    # 8   сложение
5 - 3    # 2   вычитание
5 * 3    # 15  умножение
5 / 3    # 1.666... обычное деление (всегда float)
5 // 3   # 1   целочисленное деление
5 % 3    # 2   остаток от деления
5 ** 3   # 125 возведение в степень
```

## 5. Условия if / elif / else
```python
score = 7
if score >= 8:
    print("Отлично!")
elif score >= 5:
    print("Хорошо")
else:
    print("Надо постараться")
```
Операторы сравнения: `==` `!=` `>` `<` `>=` `<=`

## 6. Логические операторы
```python
age = 12
has_ticket = True
if age >= 10 and has_ticket:
    print("Проходи")
if not has_ticket:
    print("Нужен билет")
```

## 7. Цикл while
```python
n = 3
while n > 0:
    print(n)
    n -= 1
print("Пуск!")
```
`break` — выйти из цикла досрочно. `continue` — пропустить остаток итерации.

## 8. Цикл for и range()
```python
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):     # 1, 2, 3, 4, 5
    print(i)
```

## 9. Списки
```python
items = ["меч", "щит", "зелье"]
items.append("лук")       # добавить в конец
items.remove("щит")       # удалить по значению
print(items[0])            # первый элемент
print(items[-1])           # последний элемент
print(items[0:2])          # срез
for item in items:
    print(item)
```

## 10. Строки
```python
s = "Python"
print(s.upper())           # PYTHON
print(s.lower())            # python
print(s[0], s[-1])          # P n
print(s[0:3])                # Pyt
words = "гол пас удар".split()  # ['гол', 'пас', 'удар']
name = "Миша"
print(f"Привет, {name}!")     # f-строка — вставка значений в текст
```

## 11. Словари
```python
player = {"имя": "Миша", "номер": 10}
print(player["имя"])         # Миша
player["уровень"] = 5         # добавить ключ
del player["номер"]           # удалить ключ
for key, value in player.items():
    print(key, "-", value)
```

## 12. Функции
```python
def goals_total(goals, assists=0):
    return goals + assists

print(goals_total(3, 2))   # 5
print(goals_total(3))       # 3 (assists по умолчанию 0)
```

## 13. Модуль random
```python
import random
random.seed(1)                # для повторяемого результата
print(random.randint(1, 6))   # случайное число от 1 до 6
print(random.choice(["орёл", "решка"]))
```

## 14. Обработка ошибок try/except
```python
try:
    n = int("не число")
except ValueError:
    print("Это не похоже на число!")

try:
    x = 10 / 0
except ZeroDivisionError:
    print("На ноль делить нельзя!")
```

## 15. Файлы
```python
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Привет!\n")

with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
```

## Полезные встроенные функции
```python
len(items)       # количество элементов
type(x)          # тип значения
int(x), float(x), str(x)   # преобразование типов
range(n)         # последовательность чисел от 0 до n-1
sum(numbers)     # сумма чисел в списке
max(numbers)     # максимум
min(numbers)     # минимум
```
