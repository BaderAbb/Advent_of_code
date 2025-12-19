ranges=[]

with open("Advent_of_code/day5/input.txt") as f:
    for line in f.read().splitlines():
        if "-" in line:
            start, end = map(int, line.split("-"))
            ranges.append([start, end])

ranges = sorted(ranges, key=lambda start: start[0])

idx = 0
while idx < len(ranges)-1:
    end = ranges[idx][1]
    next_start = ranges[idx+1][0]
    next_end = ranges[idx+1][1]


    if next_start <= end:
        ranges[idx][1] = max(end, next_end)
        del ranges[idx+1]
    else:
        idx+=1

total_fresh_ID=0
for element in ranges:
    total_fresh_ID += element[1] - element[0] + 1
    
print(total_fresh_ID)           