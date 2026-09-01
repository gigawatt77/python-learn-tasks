import os

путь_к_файлу = os.path.join(os.path.dirname(__file__), "task_02_data.txt")

with open(путь_к_файлу, "w", encoding="utf-8") as файл:
    файл.write("Меня зовут Аня\n")
    файл.write("Мне 12 лет")

with open(путь_к_файлу, "r", encoding="utf-8") as файл:
    содержимое = файл.read()

print(содержимое)
