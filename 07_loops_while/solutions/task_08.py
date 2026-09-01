parol = "python123"
popytki = ["12345", "qwerty", "python123", "admin"]
indeks = 0
naiden = False

while indeks < len(popytki):
    if popytki[indeks] == parol:
        naiden = True
        print("Пароль верный!")
        break
    indeks += 1

if not naiden:
    print("Пароль не найден")
