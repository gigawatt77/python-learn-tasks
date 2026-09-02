kod_shlyuza = "kosmos42"
popytki_koda = ["12345", "qwerty", "kosmos42", "admin"]
indeks = 0
naiden = False

while indeks < len(popytki_koda):
    if popytki_koda[indeks] == kod_shlyuza:
        naiden = True
        print("Код подошёл, шлюз открыт!")
        break
    indeks += 1

if not naiden:
    print("Код не подошёл, шлюз заблокирован")
