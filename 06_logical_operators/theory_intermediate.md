# Тема 6: логические операторы and, or, not

В Scratch ты мог видеть блоки "и"/"или"/"не" внутри условных блоков.
В Python это операторы **`and`**, **`or`** и **`not`**, которые
работают с булевыми значениями (`bool`: `True`/`False`) и позволяют
объединять несколько условий в одно.

```python
uroki_sdelany = True
net_dozhdya = False

mozhno_guljat = uroki_sdelany and net_dozhdya
print(mozhno_guljat)   # False, т.к. одно из условий False
```

## Таблица истинности

| a     | b     | a and b | a or b | not a |
|-------|-------|---------|--------|-------|
| True  | True  | True    | True   | False |
| True  | False | False   | True   | False |
| False | True  | False   | True   | True  |
| False | False | False   | False  | True  |

## Приоритет операторов

`not` выполняется раньше `and`, а `and` — раньше `or`. Чтобы не
запутаться, используй скобки — они делают код нагляднее:

```python
vozrast = 15
est_bilet = True
so_vzroslym = False

mozhno = (vozrast >= 12 and est_bilet) or so_vzroslym
print(mozhno)   # True
```

## Ленивые вычисления (short-circuit)

Python вычисляет `and`/`or` "лениво": если левая часть `and` уже
False — правая часть даже не проверяется (результат и так False).
Если левая часть `or` уже True — правая часть не проверяется. Это
удобно, например, для проверки, что переменная не пустая, перед
использованием:

```python
imya = ""

if imya and len(imya) > 0:
    print("Привет,", imya)
else:
    print("Имя не указано")
```

## Запомни

- `and`, `or`, `not` объединяют и переворачивают логические условия.
- `and` — True только если оба операнда True; `or` — True если хотя бы
  один операнд True; `not` — переворачивает значение.
- Приоритет: сначала `not`, потом `and`, потом `or`. Используй скобки
  для ясности.
- Python вычисляет `and`/`or` лениво (short-circuit evaluation).
