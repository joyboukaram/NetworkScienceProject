import pandas as pd
#driverId, driverRef, dob, nationality,
drivers = pd.read_csv("drivers.csv")
#raceid(to get date => driver age)
#driverId to get the name
# constructorId to get the constructor name
# position
results = pd.read_csv("results.csv")
constructors = pd.read_csv("constructors.csv")
constructorsStanding = pd.read_csv("constructorStandings.csv")
races = pd.read_csv("races.csv")
circuits = pd.read_csv("circuits.csv")
overtakes = pd.read_csv("overtakes_merged.csv")
# im gonna loop on results replace
#
# drivername = []
# age = []
# nationality = []
# for index, result in results.iterrows():
#     print(index)
#     for driverIndex, driver in drivers.iterrows():
#         if int(result['driverId']) == int(driver["driverId"]):
#             drivername.append(driver['driverRef'])
#             try:
#                 age.append((driver['dob'].split("/"))[2])
#             except:
#                 age.append("111900")
#             nationality.append(driver['nationality'])
#             break;
# results["driver_name"] = drivername
# results["driver_dob"] = age
# results["driver_nationality"] = nationality
#
#
# results.to_csv(r"results.csv", index=None)
#
# print(results.head())

# raceYear = []
# circuitCountry=[]
# circuitRef = []
# driverAge = []
# for index, result in results.iterrows():
#     print(index)
#     for raceIndex, race in races.iterrows():
#         if int(result['raceId']) == int(race["raceId"]):
#             raceYear.append(race['year'])
#             if int(result["driver_dob"]) != 111900:
#                 driverAge.append(int(race['year'])-int(result["driver_dob"]))
#             else:
#                 driverAge.append(111900)
#             for circuitIndex, circuit in circuits.iterrows():
#                 if int(race['circuitId']) == int(circuit['circuitId']):
#                     circuitRef.append(circuit['circuitRef'])
#                     circuitCountry.append(circuit['country'])
#                     break;
#             break;
#
# results["race_year"] = raceYear
# results["circuit_country"] = circuitCountry
# results["circuit_ref"] = circuitRef
# results["driver_age"] = driverAge
#
# results.to_csv(r"results.csv", index=None)
#
# print(results.head())

overtakesArr = []
missingRacers = []
for index, result in results.iterrows():
    print(index)
    count = 0
    for overtakeIndex, overtake in overtakes.iterrows():
        if result["driver_name"] == overtake["driver"] and result["race_year"] == overtake["date"]:
            count = overtake["overtakes"]
            break;

    if count == 0:
        missingRacers.append(result["driver_name"])

    overtakesArr.append(count)
results["overtakes"] = overtakesArr
results.to_csv(r"results.csv", index=None)

print(results.head())
print(missingRacers)
#

# arr = []
# date = "1982"
# driver = 'watson'
# count = 0
# for overtakeIndex, overtake in overtakes.iterrows():
#     print(overtakeIndex)
#     if overtake["Source"] == driver and overtake["Date"] == date:
#         count = count +1
#     else:
#         arr.append({"driver":driver,"date": date,"overtakes": count})
#         count = 1
#         driver = overtake["Source"]
#         date = overtake["Date"]
#
#
# print(arr)
#
#





