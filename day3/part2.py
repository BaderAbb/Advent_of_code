banks = open("Advent_of_code/day3/input.txt").read().split("\n")
total_joltaje=0

for bank in banks:
    highest_joltage=""
    
    index=0
    for remaining in range(12, -1, -1):
        first_baterie=str(bank)[index]
        changed=False
        if remaining == 0:
            for i, baterie in enumerate(str(bank)[index:]):
                if int(first_baterie) < int(baterie):
                    first_baterie = baterie
        else:
            for i, baterie in enumerate(str(bank)[index:-remaining]):
                if int(first_baterie) < int(baterie):
                    first_baterie = baterie
                    index = index + i
                    changed = True
            if not changed:
                    index+=1
            
        highest_joltage += first_baterie
    
    total_joltaje += int(highest_joltage)
    
print(f"{total_joltaje}")



