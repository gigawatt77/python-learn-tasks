chislo = 27
shagi = 0

while chislo != 1:
    if chislo % 2 == 0:
        chislo = chislo // 2
    else:
        chislo = chislo * 3 + 1
    shagi += 1

print(shagi)
