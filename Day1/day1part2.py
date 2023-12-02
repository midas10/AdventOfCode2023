# Hashmap to see which string of letters correlates to which digit
numCorrelations = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

# import day1 puzzle
file1 = open('Day1\day1.txt', 'r')
lines = file1.readlines()
total = 0

# function to check if current character is a number cause I forgot the python built-in function
def isNum(x):
    numSet = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

    if x in numSet:
        return True
    else:
        return False

# new function for part 1 which checks substrings of length 3, 4, and 5 to see if they're in the character to digit hashmap, then returns the string if it is
def replaceAnnoyingNumberStrings(y, i):
    if i+3 <= len(y) and y[i:i+3] in numCorrelations:
        return y[i:i+3]
    elif i+4 <= len(y) and y[i:i+4] in numCorrelations:
        return y[i:i+4]
    elif i+5 <= len(y) and y[i:i+5] in numCorrelations:
        return y[i:i+5]
    else:
        return ""

# loop through puzzle lines
for line in lines:
    # initiate left and right pointers
    l = 0
    r = len(line)-1
    # use the left and right pointers to traverse the left side until you hit first number, same with right
    # Now since we're dealing with an extra function we introduce leftDigit/rightDigit to keep track of answers
    leftDigit = ''
    rightDigit = ''
    while (not leftDigit or not rightDigit):
        testLeft = replaceAnnoyingNumberStrings(line, l)
        testRight = replaceAnnoyingNumberStrings(line, r)
        
        # Goes through each circumstance if left/rigth digits have not been found, first testing for string then testing for straight up digit
        if not leftDigit and testLeft:
            leftDigit = numCorrelations[testLeft]
        if not rightDigit and testRight:
            rightDigit = numCorrelations[testRight]
        if not leftDigit and isNum(line[l]):
            leftDigit = line[l]
        if not rightDigit and isNum(line[r]):
            rightDigit = line[r]

        if not leftDigit:
            l += 1
        if not rightDigit:
            r -= 1
        if leftDigit and rightDigit:
            break
    # add first and last digit into a concatenated string, convert to int, and add to running total
    # print(line[l]+line[r])
    total += int(leftDigit + rightDigit)

print(total)
