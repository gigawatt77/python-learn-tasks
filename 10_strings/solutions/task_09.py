text = "Гоночная машина мчалась по трассе на максимальной скорости"
counter = 0

for letter in text:
    if letter == "а":
        counter = counter + 1

print(f"Буква 'а' встречается {counter} раз")
