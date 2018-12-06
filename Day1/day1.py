
total = 0

def frequency(stringIn):
    intIn = int(stringIn)

    return total + intIn

file = open('input.txt', 'r') 
for line in file: 
    total = frequency(line)

print(total)