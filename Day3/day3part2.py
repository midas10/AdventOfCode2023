file1 = open('Day3\day3.txt', 'r')
lines = file1.readlines()
mapCoordinates = {}
r = 1

numSet = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
total = 0

def coordCheck(r, c):
    if(r+1, c+1) in mapCoordinates:
        return (r+1,c+1)
    elif(r, c+1) in mapCoordinates:
        return (r, c+1)
    elif (r-1, c+1) in mapCoordinates:
        return (r-1, c+1)
    elif (r-1,c) in mapCoordinates:
        return(r-1,c)
    elif (r-1,c-1) in mapCoordinates:
        return (r-1,c-1)
    elif (r, c-1) in mapCoordinates:
        return (r, c-1)
    elif (r+1, c-1) in mapCoordinates:
        return (r+1, c-1)
    elif (r+1, c) in mapCoordinates:
        return (r+1, c)
    else:
        return (0, 0)

for line in lines:
    c = 1
    for char in line:
        if char == '*':
            mapCoordinates[(r, c)] = []

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
            #print(currentNum, r, c)
            res = coordCheck(r, c)
            if not res == (0, 0):
                #print("test")
                while line[i] in numSet and i < len(line):
                    i+=1
                    c+=1
                    currentNum += line[i]
                mapCoordinates[res].append(currentNum[0:len(currentNum)-1])
                currentNum = ""
            i+=1
            c+=1
        i+=1
        c+=1
    r += 1

for val in mapCoordinates.values():
    if len(val) == 2:
        total += (int(val[0]) * int(val[1]))

print(total)

