ranges = open("Advent_of_code/day2/input.txt").read().split(",")
total_invalid_nums=0

for r in ranges:
    invalid_nums=0
    start, end = map(int, r.split("-"))
    for number in range(start, end+1):
        valido = True
        for lenght in range(1, (len(str(number))//2)+1):
            if len(str(number))%lenght != 0 or len(str(number)) == 1:
                continue
            i=0
            x=lenght
            inital_sequence=str(number)[i:lenght]
            second_sequence=str(number)[i+lenght:lenght*2]
            valido = True
            for subnumbers in range(1,int(len(str(number)))//lenght+1):
                if second_sequence != inital_sequence:
                    valido=False
                    break
                i+=lenght
                x+=lenght
                second_sequence=str(number)[i:x]
            
            if valido:
                break
            
        if valido and len(str(number)) != 1:
            total_invalid_nums += number

print(f"Adding up all the invalid IDs in this example produces {total_invalid_nums}")                



