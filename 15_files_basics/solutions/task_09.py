import os

путь_к_файлу = os.path.join(os.path.dirname(__file__), "task_09_data.txt")

with open(путь_к_файлу, "w", encoding="utf-8") as файл:
    файл.write("Миша\n")
    файл.write("Артём\n")
    файл.write("Данил")

with open(путь_к_файлу, "r", encoding="utf-8") as файл:
    содержимое = файл.read()

строки = содержимое.splitlines()
for строка in строки:
    print(строка)

print("Количество строк:", len(строки))
