file1 = open("Day4\\day4.txt", 'r')
lines = file1.readlines()
total = 0

""" This for loop just iterates over each game, parses the string to extract the winning numbers (which are put in a hash set) and your numbers (which are put in a list). Then it uses pseudo code language magic to iterate over each number in the yourNumbers list and test if its in winning numbers"""
for line in lines:
    currentTotal = 0
    line.strip()
    cardSep = line.split(':')

    numberSep = cardSep[1].strip().split('|')

    winningNumbers = set(numberSep[0].split(' '))
    yourNumbers = numberSep[1].split(' ')
    for number in yourNumbers:
        # This if statement could've probably been avoided if I trimmed properly but its AoC
        if number == '':
            continue
        # If the number is in winningNumbers but current total is 0 we can't double it, so make it 1
        elif number in winningNumbers and currentTotal == 0:
            currentTotal = 1
        # If the number is in winninNumbers and currentTotal isn't 1, we can just multiply currentTotal by 2
        elif number in winningNumbers:
            currentTotal *= 2
    total += currentTotal
print(total)



