file1 = open('Day3\day3.txt', 'r')
lines = file1.readlines()
mapCoordinates = set()
r = 1

numSet = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
total = 0

for line in lines:
    c = 1
    for char in line:
        if (not char in numSet) and (not char == '.') and (not char == "\n"):
            #print(char)
            mapCoordinates.add((r, c))

        c += 1
    r += 1
#print("coords", mapCoordinates)
r = 1
for line in lines:
    c = 1
    i = 0
    while i < len(line):
        currentNum = ""
        while i < len(line) and line[i] in numSet:
            currentNum += line[i]

            if (r+1, c+1) in mapCoordinates or (r, c+1) in mapCoordinates or (r-1, c+1) in mapCoordinates or (r-1, c) in mapCoordinates or (r-1, c-1) in mapCoordinates or (r, c-1) in mapCoordinates or (r+1, c-1) in mapCoordinates or (r+1, c) in mapCoordinates:
                while line[i] in numSet and i < len(line):
                    i+=1
                    c+=1
                    currentNum += line[i]
                total += int(currentNum[0:len(currentNum)-1])
                currentNum = ""
            i+=1
            c+=1
        i+=1
        c+=1
    r += 1
print(total)
