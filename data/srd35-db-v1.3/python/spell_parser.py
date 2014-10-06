from pymongo import MongoClient
from bs4 import BeautifulSoup

client = MongoClient('localhost', 27017)
db = client.dnd
spellCollection = db.spells

f = open("../spell.xml", "r")
soup = BeautifulSoup(f.read())

easy_grabs = ["name", "school", "descriptor", "material_components", "casting_time", "range", "effect", "duration", "saving_throw", "spell_resistance"]

spells = []

for spell in soup.find_all("spell"):
    spells.append(spell)

for spell in spells:
#for i in range(0, 1):
#    spell = spells[i]
    spellObject = {}
    for index in easy_grabs:
        if spell.find(index) != None:
            spellObject[index] = spell.find(index).text.encode("utf-8")
        else:
            spellObject[index] = ""
    if spell.find("description") != None:
        spellObject["description"] = spell.find("description").find("p").text.encode("utf-8")
    else:
        spellObject["description"] = ""
    if spell.find("components") != None:
        spellObject["components"] = spell.find("components").text.encode("utf-8").replace(" ","").split(",")
    else:
        spellObject["components"] = ""
    if spell.find("level") != None:
        spellLevels = []
        for spellLevel in spell.find("level").text.encode("utf-8").split(","):
            spellLevelObject = {}
            spellLevelSplit = spellLevel.split(" ")
            spellLevelObject["class"] = spellLevelSplit[0]
            spellLevelObject["level"] = spellLevelSplit[1]
            spellLevels.append(spellLevelObject)
            spellObject["level"] = spellLevels
    else:
        spellObject["level"] = ""
    if spell.find("full_text") != None:
        spellObject["full_text"] = spell.find("full_text").prettify()
    else:
        spellObject["full_text"] = ""
    spellCollection.insert(spellObject)
