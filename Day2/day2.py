file1 = open('Day2\day2.txt', 'r')
lines = file1.readlines()
possibleGames = []
currentGame = 1
total = 0

for line in lines:
    # set game to possible by default
    gamePossible = True
    newLines = line.split(':')
    
    cubes = newLines[1]
    sets = cubes.split(';')
    # split games into individuals sets then into individual colors
    for s in sets:
        colors = s.split(',')
        # oops this is literally n^3 but who cares
        for color in colors:
            separationYetAgain = color.split()
            num = separationYetAgain[0]
            
            # if current num for associated color is higher than limit, game is impossible and we can break out of all loops
            if "blue" in color and int(num) > 14:
                gamePossible = False
                break
            elif "green" in color and int(num) > 13:
                gamePossible = False
                break
            elif "red" in color and int(num) > 12:
                gamePossible = False
                break
        if not gamePossible:
            break
    # if the games possible, add game number to total
    if gamePossible:
        total += currentGame
    currentGame += 1
print(total)
