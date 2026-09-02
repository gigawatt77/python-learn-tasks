speeds = [180, 240, 210, 260, 195]
fastest = speeds[0]

for speed in speeds:
    if speed > fastest:
        fastest = speed

print("Самая высокая скорость:", fastest)
