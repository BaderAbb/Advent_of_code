banks = open("Advent_of_code/day/input.txt").read().split("\n")

total_joltaje=0

for bank in banks:
    first_baterie=str(bank)[0]
    index=0
    for i, baterie in enumerate(str(bank)[1:-1]):
        if int(first_baterie) < int(baterie):
            first_baterie = baterie
            index = i+1  
    
    second_baterie=str(bank)[index+1]
    for baterie in str(bank)[index+2:]:
        if second_baterie < baterie:
            second_baterie = baterie
    
    joltaje = int(first_baterie + second_baterie)
    total_joltaje += joltaje

print(f"{total_joltaje}")

