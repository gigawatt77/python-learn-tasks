import random

random.seed(4)
счёт = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for _ in range(10):
    бросок = random.randint(1, 6)
    счёт[бросок] += 1

print(счёт)
