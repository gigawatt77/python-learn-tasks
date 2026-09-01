import os

путь_к_файлу = os.path.join(os.path.dirname(__file__), "task_06_data.txt")

with open(путь_к_файлу, "w", encoding="utf-8") as файл:
    файл.write("Готово!")
    print("Готово!")
