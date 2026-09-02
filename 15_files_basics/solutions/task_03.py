import os

путь_к_файлу = os.path.join(os.path.dirname(__file__), "task_03_data.txt")
строки = ["Список для крафта:", "- дерево", "- камень", "- алмазы"]

with open(путь_к_файлу, "w", encoding="utf-8") as файл:
    for строка in строки:
        файл.write(строка + "\n")

with open(путь_к_файлу, "r", encoding="utf-8") as файл:
    содержимое = файл.read()

print(содержимое)
