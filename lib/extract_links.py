#!python2
import requests
import re
import pickle
import datetime

# textfile = file('depth_1.txt','wt')
#print("Enter the URL you wish to crawl..")
#print('Usage  - "http://phocks.org/stumble/creepy/" <-- With the double quotes')
#myurl = input("@> ")
root_url = "https://www.radiookapi.net"
#print("Enter the date for which to get the news..")
#print('Usage  - "2018/02/05"')
date_published = datetime.datetime.now().strftime('%Y/%m/%d')
date_formated = date_published.replace("/", "-")
urls_folder = '/var/jenkins_home/data/readingNewsCongo/assets/urls_text_files/'
filename = urls_folder + date_formated + '.txt'
request = requests.get(root_url)
html = ""
if request.status_code == 200:
    html = request.text
else:
    print("the request was not successful")
    print(request.status_code)

links = []
for i in re.findall('''href=["'](.[^"']+)["']''', html, re.I):
    full_link = root_url + i
    # for radio okapi
    if date_published in full_link:
        links.append(full_link)

    try:
        with open(filename, 'wb') as fp:
            pickle.dump(links, fp)
    except:
        print("there was a problem creating this file")
print("the file has been created")


#         for ee in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(i).read(), re.I):
#                 print ee
#                 textfile.write(ee+'\n')
# textfile.close()

# with open ('outfile', 'rb') as fp:
#     itemlist = pickle.load(fp)with open ('outfile', 'rb') as fp:
#     itemlist = pickle.load(fp) ;:
