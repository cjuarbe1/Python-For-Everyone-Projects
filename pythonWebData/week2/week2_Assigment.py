import re
hand = open('regex_sum_313224.txt')
listOfNum = list()
for line in hand:
    line = line.rstrip()
    numListInFile = re.findall('[0-9]+', line)
    print(numListInFile)
    if len(numListInFile) <1 :continue
    for x in numListInFile:
        print(x,type(x))
        numHolder = int(x)
        listOfNum.append(numHolder)
sumOfNum = 0
for y in listOfNum:
    sumOfNum += y
print(sumOfNum)
