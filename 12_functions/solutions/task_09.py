def average(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total / len(numbers)


ratings = [5, 4, 5, 3, 4, 5]
print(average(ratings))
