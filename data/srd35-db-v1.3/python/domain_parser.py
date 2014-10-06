from pymongo import MongoClient
from bs4 import BeautifulSoup

client = MongoClient('localhost', 27017)
db = client.dnd
domainCollection = db.domains

f = open("../domain.xml", "r")
soup = BeautifulSoup(f.read())

easy_grabs = ["name", "granted_powers", "reference"]

for i in range(1, 10):
    easy_grabs.append("spell_" + `i`)

domains = []

for domain in soup.find_all("domain"):
    domains.append(domain)

for domain in domains:
#for i in range(0, 1):
#    domain = domains[i]
    domainObject = {}
    for index in easy_grabs:
        if domain.find(index) != None:
            domainObject[index] = domain.find(index).text.encode("utf-8")
    if domain.find("full_text") != None:
        domainObject["full_text"] = domain.find("full_text").prettify()
#    print(domainObject)
    domainCollection.insert(domainObject)

