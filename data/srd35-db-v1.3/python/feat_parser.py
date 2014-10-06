from pymongo import MongoClient
from bs4 import BeautifulSoup

client = MongoClient('localhost', 27017)
db = client.dnd
featsCollection = db.feats

f = open("../feat.xml", "r")
soup = BeautifulSoup(f.read())

easy_grabs = ["name", "type", "stack", "multiple", "choice"]

feats = []

for feat in soup.find_all("feat"):
    feats.append(feat)

for feat in feats:
#for i in range(0, 2):
#    feat = feats[i]
    featObject = {}
    for index in easy_grabs:
        if feat.find(index) != None:
            featObject[index] = feat.find(index).text.encode("utf-8")
        else:
            featObject[index] = ""
    if feat.find("description") != None:
        featObject["description"] = feat.find("description").find("p").text.encode("utf-8")
    else:
        featObject["description"] = ""
    
    if feat.find("benefit") != None:
        str = feat.find("benefit").text.encode("utf-8")
        featObject["benefit"] = str[str.find(":")+1:].strip()
    else: 
        featObject["benefit"] = ""
    if feat.find("full_text") != None:
        featObject["full_text"] = feat.find("full_text").prettify()
    else:
        featObject["full_text"] = ""
        
    featsCollection.insert(featObject)

