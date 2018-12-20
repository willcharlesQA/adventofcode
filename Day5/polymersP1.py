#done = True
#if done: break

file = open('input.txt', 'r')

alphbt = 'abcdefghijklmnopqrstuvwxyz'
bigString = str(list(file))
bigString = bigString[2:-2]
#print(bigString)
# Loop through alphabet (just lowercase?)
bigStringLength = len(bigString)
maxIter = 400

for i in range(maxIter):
    #print(i)
    for letter in alphbt:
        #if letter+letter.upper() in bigString:
        bigString = bigString.replace(letter+letter.upper(), "")
        bigString = bigString.replace(letter.upper()+letter, "")
    if len(bigString) == bigStringLength:
        print('Number found after %d loops' %i)
        break
    bigStringLength = len(bigString)

print(len(bigString))


# Keep looping until everything is destroyed
# Needed less than 400 loops