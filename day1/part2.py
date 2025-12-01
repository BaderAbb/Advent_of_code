def retroceder(actual, movements, contador):
    contador += movements//100

    movements = movements%100

    if (actual - movements) <= 0 and actual != 0:
        contador+=1 
    
    return (actual - movements)%100, contador

def avanzar(actual, movements, contador):
    contador += movements//100

    movements = movements%100

    if (actual + movements) >= 100:
        contador+=1 

    return (actual + movements)%100, contador

actual=50
contador=0
file = open("input.txt")

for f in file:
    move = f[0]
    movements = int(f[1:])

    if move == "L":
        actual, contador = retroceder(actual, movements, contador)
    else:
        actual, contador = avanzar(actual, movements, contador)

    

    print(f"The dial is rotated {move}{movements} to position {actual}.")

print(f"The dial has passed through 0 a total of {contador} times.")
    

    

    
    

