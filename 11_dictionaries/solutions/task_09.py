animals = ["кот", "пёс", "кот", "хомяк", "пёс", "кот"]
counts = {}

for animal in animals:
    if animal in counts:
        counts[animal] = counts[animal] + 1
    else:
        counts[animal] = 1

print(counts)
