# import day1 puzzle
file1 = open('Day1\day1.txt', 'r')
lines = file1.readlines()
total = 0

# function to check if current character is a number cause I forgot the python built-in function
def isNum(x):
    numSet = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}

    if x in numSet:
        return True
    else:
        return False

# loop through puzzle lines
for line in lines:
    # initiate left and right pointers
    l = 0
    lFound = False
    r = len(line)-2
    rFound = False
    
    # use the left and right pointers to traverse the left side until you hit first number,
    # and same w/ right side
    while (lFound == False or rFound == False):
        if isNum(line[l]) and lFound == False:
            lFound = True
        if isNum(line[r]) and rFound == False:
            rFound = True

        if lFound == False:
            l += 1
        if rFound == False:
            r -= 1
        if lFound == True and rFound == True:
            break
    # add first and last digit into a concatenated string, convert to int, and add to running total
    total += int(line[l] + line[r])

print(total)
