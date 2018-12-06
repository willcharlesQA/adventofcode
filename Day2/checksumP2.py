import numpy as np


maxSame = 0

file = open('input.txt', 'r')
data=list(file)
for i in range(len(data)):
    line1 = data[i]
    #print(i)
    for j in range(i,len(data)):
        line2 = data[j]
        same = 0
        for s in range(len(line1)-1):
            #print('line1 is %d long. line2 is %d long' %(len(line1),len(line2)))
            if (line1[s] in line2[s] and line1 != line2):
                same = same + 1

        if same > maxSame:
            maxSame = same
            resultLine = [i,j]

print(resultLine)

print(data[resultLine[0]])
print(data[resultLine[1]])