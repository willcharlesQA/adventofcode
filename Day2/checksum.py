import numpy as np

alphbt = 'abcdefghijklmnopqrstuvwxyz'
"""
inputStr = 'abccddzzz'
count = np.zeros((26))

for a in range(len(alphbt)):
    alphLetter = alphbt[a]
    for inputLetter in inputStr:
        if inputLetter in alphLetter:
            count[a] = count[a] + 1

twice  = np.nonzero(count==2)
thrice = np.nonzero(count==3)

numOfTwice  = len(twice[0])
numOfThrice = len(thrice[0])

print('Twos : %d, Threes: %d' %(numOfTwice,numOfThrice))
"""

totalNumOfTwice = 0
totalNumOfThrice = 0

file = open('input.txt', 'r') 
for line in file:
    count = np.zeros((26))
    for a in range(len(alphbt)):
        alphLetter = alphbt[a]
        for inputLetter in line:
            if inputLetter in alphLetter:
                count[a] = count[a] + 1

    twice  = np.nonzero(count==2)
    thrice = np.nonzero(count==3)
    numOfTwice  = len(twice[0])
    numOfThrice = len(thrice[0])

    if numOfTwice != 0:
        totalNumOfTwice = totalNumOfTwice + 1

    if numOfThrice != 0:
        totalNumOfThrice = totalNumOfThrice + 1

print('Twos : %d, Threes: %d' %(totalNumOfTwice,totalNumOfThrice))
print(totalNumOfTwice*totalNumOfThrice)