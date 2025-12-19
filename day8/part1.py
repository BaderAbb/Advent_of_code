positions=[]

with open("Advent_of_code/day8/input.txt") as f:
    for line in f.read().splitlines():
        x, y, z = map(int, line.split(","))
        positions.append([x, y, z])

print(positions)