class Building():
    total = 0
    def __init__(self):
        Building.total += 1

print(Building.total)

for i in range(40):
    h1 = Building()
    print(h1.total)

print(Building.total)
