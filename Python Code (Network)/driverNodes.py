import pandas as pd
import numpy as np
pd = pd.read_csv('allOvertakes.csv')

overtakes = []


for i in pd['Source']:
    if len(overtakes) == 0:
        overtakes.append(i)
    else:
        for j in overtakes:
            if j == i:
                break
            else:
                if overtakes.index(j) == len(overtakes) - 1:
                    overtakes.append(i)

for i in pd['Target']:
    if len(overtakes) == 0:
        overtakes.append(i)
    else:
        for j in overtakes:
            if j == i:
                break
            else:
                if overtakes.index(j) == len(overtakes) - 1:
                    overtakes.append(i)

print(overtakes)
print(len(overtakes))




np.savetxt("DriversNodes.csv",
           overtakes,
           delimiter =", ",
           fmt ='% s')
