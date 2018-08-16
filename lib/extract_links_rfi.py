from urllib import urlretrieve
import re, urllib2
import pickle

# textfile = file('depth_1.txt','wt')
print "Enter the URL you wish to crawl.."
print 'Usage  - "http://phocks.org/stumble/creepy/" <-- With the double quotes'
myurl = input("@> ")
root_url = myurl
date_published = "20170201"
request = urllib2.Request(myurl, headers={'User-Agent' : "Magic Browser"})
response = urllib2.urlopen(request)
html = response.read()
links = []
for i in re.findall('''href=["'](.[^"']+)["']''', html, re.I):
    # for radio okapi
    links.append(i)
print links
with open('2017-02-01-rfi.txt', 'wb') as fp:
    pickle.dump(links, fp)
print "the file has been created"


#         for ee in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(i).read(), re.I):
#                 print ee
#                 textfile.write(ee+'\n')
# textfile.close()

# with open ('outfile', 'rb') as fp:
#     itemlist = pickle.load(fp)with open ('outfile', 'rb') as fp:
#     itemlist = pickle.load(fp) ;:
