import os

путь_к_файлу = os.path.join(os.path.dirname(__file__), "task_08_data.txt")
рекорды = [120, 95, 340, 60, 210]

with open(путь_к_файлу, "w", encoding="utf-8") as файл:
    for число in рекорды:
        файл.write(str(число) + "\n")

with open(путь_к_файлу, "r", encoding="utf-8") as файл:
    содержимое = файл.read()

print(содержимое)
