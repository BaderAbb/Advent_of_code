ranges = open("Advent_of_code/day2/input.txt").read().split(",")
total_invalid_nums=0

for r in ranges:
    invalid_nums=0
    start, end = map(int, r.split("-"))
    for i in range(start, end+1):
        if len(str(i))%2 != 0:
            continue
        if str(i)[:int(len(str(i))/2)] == str(i)[int(len(str(i))/2):]:
            invalid_nums += 1
            total_invalid_nums += i
    print(f"{r} has {invalid_nums} invalid IDs")

print(f"Adding up all the invalid IDs in this example produces {total_invalid_nums}")