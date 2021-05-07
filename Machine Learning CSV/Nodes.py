import pandas as pd

drivers = pd.read_csv("drivers.csv")
results = pd.read_csv("results_constructors1.csv")
constructors = pd.read_csv("constructors.csv")
constructorsStanding = pd.read_csv("constructorStandings.csv")
races = pd.read_csv("races.csv")
circuits = pd.read_csv("circuits.csv")
newdrivers = pd.read_csv("DriversNodes_new.csv")

driverName = []
nationality = []

for index, result in results.iterrows():
    print(index)
    if (len(constructorName) == 159):
        break;
    for constructorIndex, constructor in newdrivers.iterrows():
        if (len(constructorName) == 159):
            break;
        if(result['driverName'] == constructor["label"]):
            constructorName.append(result['constructorName'])

            break;


newdrivers["constructorName"] = constructorName

newdrivers.to_csv (r'DriversNodes_new1.csv', index=None)

print(results.head())

for index, result in results.iterrows():
    print(index)
    for driverIndex, driver in drivers.iterrows():
        if(int(result['driverId']) == int(driver["driverId"])):
            driverName.append(driver['driverRef'])
            break;