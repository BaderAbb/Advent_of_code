ranges=[]
values=[]
fresh_food=0


with open("Advent_of_code/day5/input.txt") as f:
    for line in f.read().splitlines():
        if "-" in line:
            start, end = map(int, line.split("-"))
            ranges.append((start, end))
        else:
            if line.strip():
                values.append(int(line))

def is_in_range(start, end, value):
    if start <= value <= end:
        return True
    else:
        return False

for ingredient in values:
    for range in ranges:
        if is_in_range(range[0], range[1], ingredient):
            fresh_food+=1
            break
        

print(f"{fresh_food}")
    
