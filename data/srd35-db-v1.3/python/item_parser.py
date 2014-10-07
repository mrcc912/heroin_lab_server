from pymongo import MongoClient
from bs4 import BeautifulSoup

client = MongoClient('localhost', 27017)
db = client.dnd
itemCollection = db.items

f = open("../item.xml", "r")
soup = BeautifulSoup(f.read())

easy_grabs = ["name", "category", "subcategory", "special_ability", "caster_level", "price", "cost" , "reference", "weight", "aura"]

items = []

for item in soup.find_all("item"):
    items.append(item)

for item in items:
#for i in range(0, 1):
#    item = items[i]
    itemObject = {}
    for index in easy_grabs:
        if item.find(index) != None:
            itemObject[index] = item.find(index).text.encode("utf-8")
    if item.find("prereq") != None:
        reqs = []
        arr = item.find("prereq").split(",")
        for val in arr:
            optionSet = []
                for option in arr.split("or"):
                    option.strip()
                    optionSet.append(option)
            reqs.append(optionSet)
        itemObject["prereq"] = reqs

    if item.find("full_text") != None:
        itemObject["full_text"] = item.find("full_text").prettify()
    itemCollection.insert(itemObject)

