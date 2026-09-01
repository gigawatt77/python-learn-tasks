import os

путь_к_файлу = os.path.join(os.path.dirname(__file__), "task_05_data.txt")

with open(путь_к_файлу, "w", encoding="utf-8") as файл:
    файл.write("Первая строка")

with open(путь_к_файлу, "a", encoding="utf-8") as файл:
    файл.write("\nВторая строка")

with open(путь_к_файлу, "r", encoding="utf-8") as файл:
    содержимое = файл.read()

print(содержимое)
