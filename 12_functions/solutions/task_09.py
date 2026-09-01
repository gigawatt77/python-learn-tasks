def average(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total / len(numbers)


grades = [5, 4, 5, 3, 4, 5]
print(average(grades))
