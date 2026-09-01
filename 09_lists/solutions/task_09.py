numbers = [7, 22, 3, 45, 19, 8]
biggest = numbers[0]

for number in numbers:
    if number > biggest:
        biggest = number

print("Самое большое число:", biggest)
