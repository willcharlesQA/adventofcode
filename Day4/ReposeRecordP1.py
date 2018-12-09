import numpy as np
import pandas as pd

file = open('test.txt', 'r')
data=list(file)

guard = []

df = pd.DataFrame(columns=['time','event'])

"""  Example data ""
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
"""

# Find the coordinates from the input data
for i in range(len(data)):
    print('Loop ',i)
    line = data[i]
    timeS = line.find('[1518-')+6
    timeE = line.find(']')
    
    time = pd.to_datetime( '2018-'+line[timeS:timeE], format='%Y-%m-%d %H:%M')

    guardExists = line.find('Guard')
    sleepExists = line.find('asleep')
    wakeExists = line.find('wakes')

    if guardExists != -1:
        guardS = line.find('#')
        guardE = line.find('begins')-1
        #guard.append( int(line[guardS:guardE]))
        df.append( {'time': time,'event':line[guardS:guardE] }, ignore_index=True )
    elif sleepExists != -1:
        df.append( {'time': time,'event':'sleep'}, ignore_index=True )
        print('asleep!')
    elif wakeExists != -1:
        df.append( {'time': time,'event':'wake'}, ignore_index=True )
        print('awake!')


print(len(df),type(df) )



    