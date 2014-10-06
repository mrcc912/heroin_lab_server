from pymongo import MongoClient
from bs4 import BeautifulSoup

client = MongoClient('localhost', 27017)
db = client.dnd
powerCollection = db.powers

f = open("../power.xml", "r")
soup = BeautifulSoup(f.read())

easy_grabs = ["name", "discipline", "display", "manifesting_time", "range", "target", "duration", "power_points", "short_description", "reference", "effect", "power_resistance", "saving_throw", "descriptor", "augment", "area", "subdiscipline", "xp_cost"]

powers = []

for power in soup.find_all("power"):
    powers.append(power)

for power in powers:
#for i in range(0, 1):
#    power = powers[i]
    powerObject = {}
    for index in easy_grabs:
        if power.find(index) != None:
            powerObject[index] = power.find(index).text.encode("utf-8")
    if power.find("description") != None:
        powerObject["description"] = power.find("description").find("p").text.encode("utf-8")
    else:
        powerObject["description"] = ""
    if power.find("level") != None:
        powerLevels = []
        for powerLevel in power.find("level").text.encode("utf-8").split(","):
            powerLevelObject = {}
            powerLevelSplit = powerLevel.split(" ")
            powerLevelObject["class"] = powerLevelSplit[0]
            powerLevelObject["level"] = powerLevelSplit[1]
            powerLevels.append(powerLevelObject)
            powerObject["level"] = powerLevels
    if power.find("full_text") != None:
        powerObject["full_text"] = power.find("full_text").prettify()
    powerCollection.insert(powerObject)

