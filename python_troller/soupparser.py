from pymongo import MongoClient
from BeautifulSoup import BeautifulSoup
import urllib2

client = MongoClient('localhost', 27017)
db = client.dnd
itemCollection = db.items

base_url = 'http://www.imarvintpa.com'
itemURLs = []
items = []

#finding all of the item URLs
for number in xrange(ord('A'), ord('Z')+1):
    req = urllib2.Request(base_url + '/dndlive/Index_Items_Let.php?Letter=' + chr(number))
    res = urllib2.urlopen(req)
    soup = BeautifulSoup(res.read())
    for link in soup.findAll('a'):
        itemURL = link.get('href')
        if itemURL.find("items.php") != -1:
            itemURLs.append(base_url + itemURL)


for url in itemURLs:
    req = urllib2.Request(url)
    res = urllib2.urlopen(req)
    soup = BeautifulSoup(res.read())
    curr_item = {}
    tables = soup.findAll("table")
    for row in tables[0].findAll("tr"):
        row_name = ""
        row_value = ""
        if row.find("a") : 
            row_name = row.find('a').text.encode("utf-8")
        else:
            row_name = row.find("th").text.encode("utf-8").replace(".", "")
        row_value = row.find("td").text.encode("utf-8").replace(".", "")
        curr_item[row_name] = row_value
    print curr_item["Name"]
    if tables[1].find('p') != None:
        curr_item["Description"] = tables[1].find('p').text
    itemCollection.insert(curr_item)          
    items.append(curr_item)
   
     
"""
url = itemURLs[0]
req = urllib2.Request(url)
res = urllib2.urlopen(req)
soup = BeautifulSoup(res.read())
curr_item = {}
tables = soup.findAll("table")
for row in tables[0].findAll("tr"):
    row_name = ""
    row_value = ""
    if row.find("a") : 
        row_name = row.find('a').text.encode("utf-8")
    else:
        row_name = row.find("th").text.encode("utf-8")
    row_value = row.find("td").text.encode("utf-8")
    curr_item[row_name] = row_value
        
curr_item["Description"] = tables[1].find('p').text
#itemCollection.insert(curr_item)      
items.append(curr_item)
     
#for string in itemURLs:
#    print(string)
"""
