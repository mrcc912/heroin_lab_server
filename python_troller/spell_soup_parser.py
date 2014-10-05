from pymongo import MongoClient
from BeautifulSoup import BeautifulSoup
import urllib2

client = MongoClient('localhost', 27017)
db = client.dnd
spellCollection = db.spells

base_url = 'http://www.imarvintpa.com'
URLlist = []
spells = []

#finding all of the item URLs
for number in xrange(ord('A'), ord('A')+1):
    req = urllib2.Request(base_url + '/dndlive/AlphaIndexLet.php?Letter=" + chr(number) + "&Small=1')
    res = urllib2.urlopen(req)
    soup = BeautifulSoup(res.read())
    for link in soup.findAll('a'):
        spellURL = link.get('href')
        if spellURL.find("spells.php") != -1:
            URLlist.append(base_url + spellURL)


for url in URLlist:
    req = urllib2.Request(url)
    res = urllib2.urlopen(req)
    soup = BeautifulSoup(res.read())
    spell = {}
    tables = soup.findAll("table")
    for row in tables[0].findAll("tr"):
        row_name = ""
        row_value = ""
        if row.find("a") : 
            row_name = row.find('a').text.encode("utf-8")
        else:
            row_name = row.find("th").text.encode("utf-8").replace(".", "")
        row_value = row.find("td").text.encode("utf-8").replace(".", "")
        spell[row_name] = row_value
    print spell
    
