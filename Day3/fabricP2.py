import numpy as np

file = open('input.txt', 'r')
data=list(file)

x = []
y = []
l = []
w = []
"""
#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
"""

massMatrix = np.zeros((1000,1000))
#massMatrix = np.zeros((8,8))

# Find the coordinates from the input data
for i in range(len(data)):
    line = data[i]
    xs = line.find('@ ')+2
    xe = line.find(',')
    x.append( int(line[xs:xe]) )

    ys = line.find(',')+1
    ye = line.find(':')
    y.append( int(line[ys:ye]))

    ls = line.find(': ')+2
    le = line.find('x')
    l.append( int(line[ls:le]) )

    ws = line.find('x')+1
    w.append( int(line[ws:]) )

    # small block
    matrix = np.ones((l[i],w[i]))

    # add to big block
    massMatrix[x[i]:x[i]+l[i],y[i]:y[i]+w[i]] = massMatrix[x[i]:x[i]+l[i],y[i]:y[i]+w[i]]  + matrix

#print(massMatrix)

crossOvers = np.nonzero(massMatrix>1)

# My answer
print('Number of cross-overs: ',len(crossOvers[0]))

# Check which one doesn't overlap
for i in range(len(data)):
    
    # small block
    bigCheck = np.nonzero(massMatrix[x[i]:x[i]+l[i],y[i]:y[i]+w[i]] -1)

    #print(bigCheck)
    if len(bigCheck[0])==0:
        print('Fabric with no overlaps: ',data[i])

    