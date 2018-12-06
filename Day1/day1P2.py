
total = 0
freqs = []
done = False

def frequency(stringIn):
    intIn = int(stringIn)

    return total + intIn


file = open('input.txt', 'r') 


for loop in range(147):
    #print('Size of freqs is ',len(freqs))
    print('Loop ',loop)

    file = open('input.txt', 'r') 
    for line in file: 
        total = frequency(line)
        
        # Check it exists in freqs
        if total in freqs:
            print('Answer is ',total)
            done = True
            break
        if done:break
        freqs.append(total)
    if done: break


print('Size of freqs is ',len(freqs))

