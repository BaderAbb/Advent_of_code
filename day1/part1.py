def retroceder(actual, movements):
    return (actual - movements)%100

def avanzar(actual, movements):
    return (actual + movements)%100

actual=50
contador=0
file = open("input.txt")

for f in file:
    move = f[0]
    movements = int(f[1:])

    if move == "L":
        actual = retroceder(actual, movements)
    else:
        actual = avanzar(actual, movements)

    print(f"The dial is rotated {move}{movements} to position {actual}.")

    if actual == 0:
        contador += 1

print(f"The dial has passed through 0 a total of {contador} times.")
    

    

    
    

