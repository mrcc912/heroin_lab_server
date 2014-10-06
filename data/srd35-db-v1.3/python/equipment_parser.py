from pymongo import MongoClient
from bs4 import BeautifulSoup

client = MongoClient('localhost', 27017)
db = client.dnd
equipmentsCollection = db.equipments

f = open("../equipment.xml", "r")
soup = BeautifulSoup(f.read())

easy_grabs = ["name", "family", "category", "subcategory", "reference", "cost", "dmg_s", "dmg_m", "critical", "weight", "type", "range_increment", "armor_check_penalty", "speed_30", "speed_20", "arcane_spell_failure_chance", "maximum_dex_bonus", "armor_shield_bonus"]

equipments = []

for equipment in soup.find_all("equipment"):
    equipments.append(equipment)

for equipment in equipments:
#for i in range(0, 2):
#    equipment = equipments[i]
    equipmentObject = {}
    for index in easy_grabs:
        if equipment.find(index) != None:
            equipmentObject[index] = equipment.find(index).text.encode("utf-8")
    if equipment.find("full_text") != None:
        equipmentObject["description"] = equipment.find("full_text").text.encode("utf-8")
    else:
        equipmentObject["description"] = ""
        
#    print(equipmentObject)        
    equipmentsCollection.insert(equipmentObject)

""" CHECK TO SEE IF WE ARE FORGETTING ANY TYPES
for child in equipment.findChildren():
found = 0
for tag in easy_grabs:
if tag == child.name.encode("utf-8") or child.name.encode("utf-8") =="full_text":
found = 1
if found == 0:
print child.name.encode("utf-8")
"""
