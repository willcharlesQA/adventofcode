import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file = open('input.txt', 'r')
data=list(file)

df   = pd.DataFrame(columns=['Time','Minutes','Event'])
duty = pd.DataFrame(columns=['ID'])

"""  Example data ""
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
"""

# Extract the data from the input
for i in range(len(data)):
    #print('Loop ',i)
    line = data[i]
    timeS = line.find('[1518-')+6
    timeE = line.find(']')
    
    # Because the year 1218 doesn't work, pretend everything is in 2018
    time = pd.to_datetime( '2018-'+line[timeS:timeE], format='%Y-%m-%d %H:%M')

    guardExists = line.find('Guard')
    sleepExists = line.find('asleep')
    wakeExists = line.find('wakes')

    if guardExists != -1:
        guardS = line.find('#')
        guardE = line.find('begins')-1
        #guard.append( int(line[guardS:guardE]))
        #df = df.append(pd.DataFrame({'Time': time, 'Event':line[guardS:guardE] }, index=[i]))
        duty = duty.append(pd.DataFrame({'ID':line[guardS:guardE] }, index=[time.round('d')]) )
    elif sleepExists != -1:
        df = df.append(pd.DataFrame({'Time': time, 'Minutes':time.minute, 'Event':'sleep'}, index=[time.round('d')]))
        #print('asleep!')
    elif wakeExists != -1:
        df = df.append(pd.DataFrame({'Time': time, 'Minutes':time.minute, 'Event':'wake'}, index=[time.round('d')]))
        #print('awake!')

# Sort by date
df = df.sort_values(by="Time")
duty.sort_index(inplace=True)

# To contruct visual matrix, loop by day then by minute
minutes = range(60)
IDs = duty.iloc[:,0]
visMatrix = np.zeros((len(duty),60))

for i in range(len(duty)):
    # 0 is awake. 1 is asleep.
    event = int(0)
    count = 0
    # If the guard falls asleep during the day
    if duty.index[i] in df.index:
        eachDay = df.loc[duty.index[i],'Minutes']
    else:
        eachDay = []
    for j in minutes:
        if count < len(eachDay):
            if j == int(eachDay[count]):
                event = abs(event-1)
                count = count + 1
        visMatrix[i,j] = event

vis = pd.DataFrame(visMatrix, columns=minutes, index=IDs) #, index=arrayOfDice

#for i in range(len(duty)):
print('0 is awake. 1 is asleep.')
print(vis)
#ax = sns.heatmap(vis) #, linewidths=.5
#plt.show()

IDlist = vis.index.unique().values

for ID in IDlist:
    timetable = vis.loc[ID]
    totalTimeAsleep =  timetable.sum(axis=1).sum(axis=0) 
    print('%s is asleep for %s minutes' %(ID,totalTimeAsleep))
'''
for ID in IDlist:
    timetable = vis.loc[ID]
    print(timetable.as_matrix)
    totalAsleep = len( np.nonzero(timetable.as_matrix) )
    #print('timetable for ',ID,'total asleep',totalAsleep)
    print(totalAsleep)
'''
#print(vis.loc['#99'])




    