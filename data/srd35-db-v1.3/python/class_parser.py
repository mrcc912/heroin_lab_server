from pymongo import MongoClient
from bs4 import BeautifulSoup
import re

client = MongoClient('localhost', 27017)
db = client.dnd
klassCollection = db.klass

f = open("../class.xml", "r")
soup = BeautifulSoup(f.read())

easy_grabs = ["name", "type", "hit_die", "skill_points", "skill_points_ability", "epic_feat_base_level", "epic_feat_interval"]

csv_grabs = ["alignment", "class_skills", "epic_feat_list"]
klasses = []

for klass in soup.find_all("class"):
    klasses.append(klass)

#for klass in klass:
for i in range(0, 1):
    klass = klasses[i]
    klassObject = {}
    for index in easy_grabs:
        if klass.find(index) != None:
            klassObject[index] = klass.find(index).text.encode("utf-8")
    for index in csv_grabs:
        if klass.find(index) != None:
            arr = []
            for val in klass.find(index).text.encode("utf-8").split(","):
                arr.append(val.strip())
            klassObject[index] = arr
    if klass.find("full_text") != None:
        tableArr = []
        text = klass.find("full_text")

        specials = {}
        for div in text.findAll("div"):
            topic = div.get("topic").encode("utf-8")
            found = topic.find("table") and topic.find("Table")
            if found == -1:
                specials[topic] = div.text.encode("utf-8").strip()
        klassObject["specials"] = specials

        table = text.find("table")
        rows = table.findAll("tr")
        headers = [];
        #Gather the row headers
        for td in rows[1].findAll("td"):
            headers.append(td.text.encode("utf-8").strip())
        #populate the rows/mongofied table
        for i in range(2, len(rows)):
            row = {}
            cells = rows[i].findAll("td")
            for j in range(0, len(cells)):
                if headers[j] != "Level":
                    row[ headers[j] ] = cells[j].text.encode("utf-8").strip()
                else:
                    row[ headers[j] ] = re.sub("[^0-9]", "", cells[j].text.encode("utf-8").strip())
            tableArr.append(row)
        klassObject["progression_table"] = tableArr
        #klassObject["full_text"] = klass.find("full_text").prettify()
    if klass.find("epic_full_text") != None:
        text = klass.find("epic_full_text")
        specials = {}
        print len(div)
        for div in text.findAll("div"):
            topic = div.get("topic").encode("utf-8")
            found = topic.find("table") and topic.find("Table")
            if found == -1:
                print "================================================"
                specials[topic] = div.text.encode("utf-8").strip()
               ## print "adding topic: " + topic
               ##print div.text.encode("utf-8").strip()
        klassObject["epic_specials"] = specials
        table = text.find("table")
        rows = table.findAll("tr")
        tableArr = []
        #Gather the row headers
        for i in range(1, len(rows)):
            row = {}
            cells = rows[i].findAll("td")
            row["Level"] = re.sub("[^0-9]","", cells[0].text.encode("utf-8").strip())
            row["Special"] = cells[1].text.encode("utf-8").strip()
            tableArr.append(row)
        klassObject["epic_progression_table"] = tableArr
"""
        for key in klassObject.keys():
            print key + " : "
            print klassObject[key]
"""
    	#klassObject["epic_full_text"] = klass.find("epic_full_text").prettify()
        #klassCollection.insert(klassObject)
