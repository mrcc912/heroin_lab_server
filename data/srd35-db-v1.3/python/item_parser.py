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
    itemObject = {}
    for index in easy_grabs:
        if item.find(index) != None:
            itemObject[index] = item.find(index).text.encode("utf-8")
    if item.find("prereq") != None:
        reqs = []
        arr = item.find("prereq").text.encode("utf-8").split(",")
        for val in arr:
            optionSet = []
            if val.find(" or ") != None:
                for option in val.split(" or "):
                    optionSet.append(option.strip())
            else:
                optionSet.append(val.strip())
            reqs.append(optionSet)
        itemObject["prereq"] = reqs

    if item.find("full_text") != None:
        itemObject["full_text"] = item.find("full_text").prettify()
    itemCollection.insert(itemObject)

