shelves = []

with open("Advent_of_code/day4/input.txt") as f:
    for line in f:
        row = [ grid for grid in line.strip() ]

        shelves.append(row)


def checkAdjacent(row, column):
    adjacentRolls=0

    if shelves[row][column] != '@':
        return False

    for df, dc in movements:
        newRow = row + df
        newColumn = column + dc

        if 0 <= newRow < totalRows and 0 <= newColumn < totalColumns:
            if shelves[newRow][newColumn] == '@' or shelves[newRow][newColumn] == 'x':
                adjacentRolls += 1

    return adjacentRolls < 4 

def removeMarked():
    for row in range(totalRows):
        for element in range(totalColumns):
            if shelves[row][element] == 'x':
                shelves[row][element] = '.'


movements = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
totalRows = len(shelves)
totalColumns = len(shelves[0])
validRolls = 0


while True:
    changeMade = False
    for row in range(totalRows):
        for element in range(totalColumns):
            if(checkAdjacent(row, element)):
                changeMade = True
                shelves[row][element] = 'x'
                validRolls+=1
    
    removeMarked()
    
    if not changeMade:
        break

print(f"{validRolls}")