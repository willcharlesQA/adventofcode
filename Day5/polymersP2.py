#done = True
#if done: break

file = open('input.txt', 'r')

alphbt = 'abcdefghijklmnopqrstuvwxyz'
bigBigString = str(list(file))
bigBigString = bigBigString[2:-2]
#print(bigString)
# Loop through alphabet (just lowercase?)

maxIter = 400

for removedLetter in alphbt:
    bigString = bigBigString.replace(removedLetter+removedLetter.upper(), "")
    bigString = bigBigString.replace(removedLetter.upper()+removedLetter, "")
    bigStringLength = len(bigString)
    for i in range(maxIter):
        #print(i)
        for letter in alphbt:
            #if letter+letter.upper() in bigString:
            bigString = bigString.replace(letter+letter.upper(), "")
            bigString = bigString.replace(letter.upper()+letter, "")
        if len(bigString) == bigStringLength:
            print('Number found after %d loops with removed %s' %(i,removedLetter))
            break
        bigStringLength = len(bigString)

#print(len(bigString))


# Keep looping until everything is destroyed
# Needed less than 400 loops