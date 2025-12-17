banks = open("Advent_of_code/day3/input.txt").read().splitlines()
total_joltaje=0
print(banks)

for bank in banks:
    print("#### BANK ####")
    highest_joltage=""
    remaining_elimination = len(bank) - 12 
    index=0
    for remaining in range(11, -1, -1):
        highest_batterie = bank[index]

        if remaining_elimination == 0:
            highest_batterie += bank[index:]
            highest_joltage += highest_batterie
            break

        changed = False
        for jumps, batterie in enumerate(bank[index:(index+remaining_elimination+1)]):
            if int(batterie) > int(highest_batterie):
                highest_batterie = str(batterie)
                changed = True
                jump = jumps

        if changed:
            remaining_elimination -= jump
            index+=jump   

        index+=1
        highest_joltage += highest_batterie

    print(highest_joltage)
    total_joltaje += int(highest_joltage)
    
print(f"Voltaje total: {total_joltaje}")



