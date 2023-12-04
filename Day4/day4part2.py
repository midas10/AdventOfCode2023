file1 = open("Day4\\day4.txt", 'r')
lines = file1.readlines()
total = 0

cardMap = {}
i = 1

""" I know there's probably a way to combine this and the recursive function but since I'm just gonna save this for loop from part 1 I'm going to populate the cardMap hashmap with the amount of matching numbers for each game"""
for line in lines:
    currentTotal = 0
    line.strip()
    cardSep = line.split(':')

    numberSep = cardSep[1].strip().split('|')
    winningNumbers = set(numberSep[0].split(' '))

    yourNumbers = numberSep[1].split(' ')
    for number in yourNumbers:
        if number == '':
            continue
        elif number in winningNumbers:
            currentTotal += 1
    cardMap[i] = currentTotal
    i += 1

""" Recursive function that takes in the game number, adds one to the total for each call since that means another game was played/copied, returns 0 if there are no matching numbers for that particular game number, then calls itself for each copy associated with the current game in the hasmap"""
def findCopies(gameNum):
    global total
    total += 1

    if cardMap[gameNum] == 0:
        return 0

    copies = cardMap[gameNum]
    #print(gameNum, copies, total)

    for j in range(gameNum+1, gameNum+copies+1):
        #print("Iteration ", gameNum, j)
        findCopies(j)

# Basic for loop to call findCopies on each game
for j in range(1, i):
    findCopies(j)

print(total)
