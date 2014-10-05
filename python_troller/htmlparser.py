from HTMLParser import HTMLParser
import urllib2

base_url = 'http://www.imarvintpa.com'
itemURLs = []
items = []

class ItemListHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            link = attrs[0][1]
            if link.find("items.php") != -1:
                itemURLs.append(base_url + attrs[0][1])

class ItemHTMLParser(HTMLParser):
    header_name = ""
    curr_attr = []
    curr_tag = ""
    table_open = False
    def handle_starttag(self, tag, attrs):
        self.curr_tag = tag
        self.curr_attr = attrs
        if tag == "table":
            table_open = True
    def handle_endtag(self, tag):
        if tag == "table":
            table_open = False
    def handle_data(self, data):
        if self.curr_tag == "th":
            self.header_name = data
            print(self.header_name)
        if  (self.curr_tag == "a" and self.table_open == True):
            self.header_name = self.curr_attr[0][1] 
            print(self.header_name)
        else:
            if self.curr_tag == "td":
                if self.header_name != "":
                    temp_obj = self.header_name, data
                    items.append(temp_obj)
                    self.header_name = ""
                    print(temp_obj)
        
itemListParser = ItemListHTMLParser()
itemParser = ItemHTMLParser()

#finding all of the item URLs
for number in xrange(ord('A'), ord('A')+1):
    req = urllib2.Request(base_url + '/dndlive/Index_Items_Let.php?Letter=' + chr(number))
    res = urllib2.urlopen(req)
    itemListParser.feed(res.read())

req = urllib2.Request(itemURLs[0])
res = urllib2.urlopen(req)
itemParser.feed(res.read())
#print(res.read())

#for string in itemURLs:
#    print(string)
