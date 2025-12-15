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
            if shelves[newRow][newColumn] == '@':
                adjacentRolls += 1

    return adjacentRolls < 4 


movements = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
totalRows = len(shelves)
totalColumns = len(shelves[0])
validRolls = 0
for row in range(totalRows):
    for element in range(totalColumns):
        if(checkAdjacent(row, element)):
            validRolls+=1


print(f"{validRolls}")