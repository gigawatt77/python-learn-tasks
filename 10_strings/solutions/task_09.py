text = "Молоко и мороженое очень вкусные продукты"
counter = 0

for letter in text:
    if letter == "о":
        counter = counter + 1

print(f"Буква 'о' встречается {counter} раз")
