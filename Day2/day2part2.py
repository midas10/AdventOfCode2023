# read in file
file1 = open('Day2\day2.txt', 'r')
lines = file1.readlines()
total = 0

for line in lines:    
    # split strings down to individual sets of plays, then to individual colors
    newLines = line.split(':')

    cubes = newLines[1]
    sets = cubes.split(';')
    # default mins are set to 1 since at least one cube from each color is necessary for the game
    currentBMin = 1
    currentRMin = 1
    currentGMin = 1

    for s in sets:
        colors = s.split(',')
        # oops this is literally n^3 but who cares
        for color in colors:
            separationYetAgain = color.split()
            num = separationYetAgain[0]
            num = int(num)

            # get the max between current minimum and current num associated with color since we need at least this many cubes to play the game
            if "blue" in color:
                currentBMin = max(currentBMin, num)
            elif "green" in color:
                currentGMin = max(currentGMin, num)
            elif "red" in color:
                currentRMin = max(currentRMin, num)
    total += (currentBMin * currentGMin * currentRMin)
print(total)
