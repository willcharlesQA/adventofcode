import numpy as np

file = open('input.txt', 'r')
data=list(file)

"""
#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
"""

massMatrix = np.zeros((1000,1000))
#massMatrix = np.zeros((8,8))

# Find the coordinates from the input data
for line in data:
    xs = line.find('@ ')+2
    xe = line.find(',')
    x = int(line[xs:xe])

    ys = line.find(',')+1
    ye = line.find(':')
    y = int(line[ys:ye])

    ls = line.find(': ')+2
    le = line.find('x')
    l = int(line[ls:le])

    ws = line.find('x')+1
    w = int(line[ws:])

    # small block
    matrix = np.ones((l,w))

    # add to big block
    massMatrix[x:x+l,y:y+w] = massMatrix[x:x+l,y:y+w]  + matrix

print(massMatrix)

crossOvers = np.nonzero(massMatrix>1)

# My answer
print(len(crossOvers[0]))

# Check which one doesn't overlap
for line in data:
    xs = line.find('@ ')+2
    xe = line.find(',')
    x = int(line[xs:xe])

    ys = line.find(',')+1
    ye = line.find(':')
    y = int(line[ys:ye])

    ls = line.find(': ')+2
    le = line.find('x')
    l = int(line[ls:le])

    ws = line.find('x')+1
    w = int(line[ws:])

    # small block
    bigCheck = np.nonzero(massMatrix[x:x+l,y:y+w]<1)
    #print(bigCheck)
    if len(bigCheck[0])==1:
        print(line)

    