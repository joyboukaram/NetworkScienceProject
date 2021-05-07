import pandas as pd
import json

# read_file = pd.read_csv (r'2010.txt', delimiter=' ')
#
# read_file.columns = ['ToRemove','Lap','ToRemove','ToRemove','Pass','ToRemove','ToRemove','Passed','ToRemove','ToRemove']
#
# read_file.to_csv (r'2010.csv', index=None)

pd = pd.read_csv('2010.csv')

driver = []
overtakes = {}

for i in pd['Pass']:
    if len(driver) == 0:
        driver.append(i)
    else:
        for j in driver:
            if j == i:
                break
            else:
                if driver.index(j) == len(driver)-1:
                    driver.append(i)

for i in pd['Passed']:
        for j in driver:
            if j == i:
                break
            else:
                if driver.index(j) == len(driver)-1:
                    driver.append(i)


for i in driver:
    overtakes.update({i: {i: ''}})
    for j in driver:
        overtakes[i].update({j: ''})

for j,i in enumerate(pd['Pass']):

    if overtakes[i][pd['Passed'][j]] == '':
        overtakes[i][pd['Passed'][j]] = 0
    overtakes[i].update({pd['Passed'][j]: overtakes[i][pd['Passed'][j]]+1})

with open("overtakes.json", "w") as f:
    json.dump(overtakes, f)

