operands=[]
operators=[]

with open("Advent_of_code/day6/input.txt") as f:
    for line in f.read().splitlines():
        if "+" in line:
            operators = line.split()
        else:
            operands.append(line.split())


grand_total=0
for idx in range(len(operators)):
    if operators[idx] == '+':
        this_total=0
        for element in range(len(operands)):
            this_total += int(operands[element][idx])
    else:
        this_total=1
        for element in range(len(operands)):
            this_total *= int(operands[element][idx])

    grand_total += this_total

print(grand_total)