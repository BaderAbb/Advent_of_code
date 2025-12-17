lines = []
with open("Advent_of_code/day7/input.txt") as f:
    for line in f.read().splitlines():
        row = [ grid for grid in line.strip() ]

        lines.append(row)

def find_start():
    start=0
    for idx, element in enumerate(lines[0]):
        if element == "S":
            start = idx
    return start

start = find_start()
lines[1][start] = "|"
lenght = len(lines[0])
contador=0

for line in range(2,len(lines)):
    for element in range(lenght):
        if lines[line-1][element] == "|":
            if lines[line][element] == "^":
                contador+=1
                lines[line][element+1] = "|"
                lines[line][element-1] = "|"
            else:
                lines[line][element] = "|"

print(f"{contador}")


