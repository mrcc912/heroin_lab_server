from pymongo import MongoClient
from bs4 import BeautifulSoup

client = MongoClient('localhost', 27017)
db = client.dnd
skillsCollection = db.skills

f = open("../skill.xml", "r")
soup = BeautifulSoup(f.read())

easy_grabs = ["name", "key_ability", "psionic", "trained", "action", "try_again", "special", "synergy", "untrained", "restriction", "reference"]

skills = []

for skill in soup.find_all("skill"):
    skills.append(skill)

for skill in skills:
#for i in range(0, 2):
#    skill = skills[i]
    skillObject = {}
    for index in easy_grabs:
        if skill.find(index) != None:
            skillObject[index] = skill.find(index).text.encode("utf-8")
        else:
            skillObject[index] = ""
    if skill.find("description") != None:
        skillObject["description"] = skill.find("description").find("p").text.encode("utf-8")
    else:
        skillObject["description"] = ""
    if skill.find("full_text") != None:
        skillObject["full_text"] = skill.find("full_text").prettify()
    else:
        skillObject["full_text"] = ""
    skillsCollection.insert(skillObject)


""" IGNORING SKILL CHECKS FOR NOW, THE TABLE IS FUCKED UP
    checks = []
    if skill.find("skill_check") != None:
        for check in skill.find("skill_check").find("p"):
            checks.append(check.text.encode("utf-8"))                       
    skillObject["skill_check"] = checks
"""
