from bs4 import BeautifulSoup
import urllib2

"""
client = MongoClient('localhost', 27017)
db = client.dnd
itemCollection = db.items
"""

base_url = 'http://dndtools.eu'
itemURLs = []
items = []


#finding all of the skill URLs
req = urllib2.Request(base_url + '/skills/?page_size=1000')
res = urllib2.urlopen(req)
soup = BeautifulSoup(res.read())
for row in soup.findAll('tr'):
    for link in row.findAll('a'):
        itemURL = link.get('href')
        if itemURL.find("/skills/") != -1:
            itemURLs.append(base_url + itemURL)


#for string in itemURLs:
#    print(string)

"""
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
#itemCollection.insert(curr_item)
#items.append(curr_item)
"""

url = itemURLs[0]
req = urllib2.Request(url)
res = urllib2.urlopen(req)
soup = BeautifulSoup(res.read())
curr_item = {}
tables = soup.findAll("table")
for div in tables[0].findAll("div"):
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
