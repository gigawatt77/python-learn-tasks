mobs = ["зомби", "крипер", "зомби", "скелет", "крипер", "зомби"]
counts = {}

for mob in mobs:
    if mob in counts:
        counts[mob] = counts[mob] + 1
    else:
        counts[mob] = 1

print(counts)
