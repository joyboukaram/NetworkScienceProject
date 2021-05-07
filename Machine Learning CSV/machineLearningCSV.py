import pandas as pd
drivers = pd.read_csv("drivers.csv")

results = pd.read_csv("results.csv")
constructors = pd.read_csv("constructors.csv")
constructorsStanding = pd.read_csv("constructorStandings.csv")
races = pd.read_csv("races.csv")
circuits = pd.read_csv("circuits.csv")

constructorName = []
nationality = []

for index, result in results.iterrows():
    print(index)
    for constructorIndex, constructor in constructors.iterrows():
        if(int(result['constructorId']) == int(constructor["constructorId"])):
            constructorName.append(constructor['constructorRef'])
            nationality.append(constructor['nationality'])
            break;

results["constructorName"] = constructorName
results['constructorNationality'] = nationality

results.to_csv (r'results_constructors.csv', index=None)

print(results.head())