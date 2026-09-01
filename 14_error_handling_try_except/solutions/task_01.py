текст = "привет"

try:
    число = int(текст)
except ValueError:
    print("Это не число!")
