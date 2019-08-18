import os
import sys
import pickle
import datetime
from bs4 import BeautifulSoup
import urllib2
import urllib
from urllib import urlretrieve
import urlparse
import io
import re
from time import sleep
import requests

def librebelgiqueLinks(url, date):
    # for the link: http://www.rfi.fr/afrique/
   links = []
   url = url 
   root_url = ""
   for i in range(1,331):
       url = "http://www.rfi.fr/recherche/?Search[term]=rdc&Search[page]={}".format(i)
       for l in re.findall('''href=["'](.[^"']+)["']''', html, re.I):
           full_link = root_url + l
           links.append(full_link)
   return links
       
def librebelgiqueLinksDefault(html, date):
    # for the link: http://www.rfi.fr/afrique/
   links = []
   html = html 
   root_url = ""
   
   
   for l in re.findall('''href=["'](.[^"']+)["']''', html, re.I):
      links.append(l)
   links = sorted(set(links))
   librebelgique_links_final = []
   for link in links:
        match = re.search(r'/\d\d\d\d+/\w\w\w\w\w+', link)
        if match:
            librebelgique_links_final.append(link)
        else:
            pass
   return librebelgique_links_final




def lemondeLinks():
    # for the link: http://www.rfi.fr/afrique/
   links = []
   root_url = "http://www.rfi.fr"
   for i in range(1,331):
       url = "http://www.rfi.fr/recherche/?Search[term]=rdc&Search[page]={}".format(i)
       html, date_accessed = getHtml(url)
       for l in re.findall('''href=["'](.[^"']+)["']''', html, re.I):
           full_link = root_url + l
           links.append(full_link)
   return links
       
def lemondeLinksDefault(html, date):
    # for the link: http://www.rfi.fr/afrique/
   links = []
   html = html 
   root_url = "https://www.lemonde.fr"
   for link in re.findall('''href=["'](.[^"']+)["']''', html, re.I):
       if "2019" in link:
           if link.startswith("http"):
               links.append(link)
           else:
               full_link = root_url + link
               links.append(full_link)
   return links



def voixameriqueLinks():
    # for the link: http://www.rfi.fr/afrique/
   links = []
   root_url = "http://www.rfi.fr"
   for i in range(1,331):
       url = "http://www.rfi.fr/recherche/?Search[term]=rdc&Search[page]={}".format(i)
       html, date_accessed = getHtml(url)
       for l in re.findall('''js-href=["'](.[^"']+)["']''', html, re.I):
           full_link = root_url + l
           links.append(full_link)
   return links
       
def voixameriqueLinksDefault(html, date):
    # for the link: http://www.rfi.fr/afrique/
   links = []
   root_url = "https://www.voaafrique.com"
   html = html
   soup = getBeautifulSoup(html) 
   nodes = soup.findAll("button", {"class": "btn btn--link ctc__button ctc__button--news"})
   for node in nodes:
       link = node.get("js-href")
       links.append(link)
   return links


def lepotentielLinks():
    # for the link: http://www.rfi.fr/afrique/
   links = []
   root_url = "http://www.rfi.fr"
   for i in range(1,331):
       url = "http://www.rfi.fr/recherche/?Search[term]=rdc&Search[page]={}".format(i)
       html, date_accessed = getHtml(url)
       for l in re.findall('''href=["'](.[^"']+)["']''', html, re.I):
           full_link = root_url + l
           links.append(full_link)
   return links
       
def lepotentielLinksDefault(html, date):
    # for the link: http://www.rfi.fr/afrique/
   links = []
   html = html 
   root_url = "https://www.lepotentielonline.net"
   for l in re.findall('''href=["'](.[^"']+)["']''', html, re.I):
       full_link = l
       if "2019" in full_link:
           links.append(full_link)
   return links

def congoindependantLinks():
    # for the link: http://www.rfi.fr/afrique/
   links = []
   root_url = "http://www.rfi.fr"
   for i in range(1,331):
       url = "http://www.rfi.fr/recherche/?Search[term]=rdc&Search[page]={}".format(i)
       html, date_accessed = getHtml(url)
       for l in re.findall('''href=["'](.[^"']+)["']''', html, re.I):
           full_link = root_url + l
           links.append(full_link)
   return links
       
def congoindependantLinksDefault(html, date):
    # for the link: http://www.rfi.fr/afrique/
   links = []
   html = html 
   root_url = "https://www.congoindependant.com"
   for link in re.findall('''href=["'](.[^"']+)["']''', html, re.I):
       if "congoindependant" in link:
            links.append(link)
   new_links = []
   for link in links:
       if not link.__contains__("tag"):
           new_links.append(link)
   final_links = []
   for link in new_links: 
       if not (link.__contains__("category")):
            final_links.append(link)
   return final_links










def rfiLinks():
    # for the link: http://www.rfi.fr/afrique/
   links = []
   root_url = "http://www.rfi.fr"
   for i in range(1,331):
       url = "http://www.rfi.fr/recherche/?Search[term]=rdc&Search[page]={}".format(i)
       html, date_accessed = getHtml(url)
       for l in re.findall('''href=["'](.[^"']+)["']''', html, re.I):
           full_link = root_url + l
           links.append(full_link)
   return links
       
def rfiLinksDefault():
    # for the link: http://www.rfi.fr/afrique/
   links = []
   root_url = "http://www.rfi.fr"
   url = "http://www.rfi.fr/recherche/?Search[term]=rdc&Search[page]=1"
   html, date_accessed = getHtml(url)
   for l in re.findall('''href=["'](.[^"']+)["']''', html, re.I):
       full_link = root_url + l
       if "2019" in full_link:
           links.append(full_link)
   return links

def jeuneAfrique(soup):
    # for the link: http://www.jeuneafrique.com/pays/rd-congo
    links = []
    for link in soup3.findAll("a"):
        if numbers in link:   #
            links.append(link.get("href"))
# sites with published date in full link such as wordpress sites. radiookapi.net is an example of this.
def wordpress(html, date):
    links = []
    for i in re.findall('''href=["'](.[^"']+)["']''', html, re.I):
        full_link = root_url + i
        if date_published in full_link:
            links.append(full_link)
    return links
# a series of functions that return the date object which will be needed for naming files and defining the published (or accessed ) date and time of articles
def getDatetimeLong():
    time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    return time
def getDatetimeShort():
    time = datetime.datetime.now().strftime('%Y-%m-%d')
    return time
def getDatetimeSlash():
    time = datetime.datetime.now().strftime('%Y/%m/%d')
    return time
def getDatetimeOne():
    time = datetime.datetime.now().strftime('%Y%m%d')
    return time
# call str(time) in order to convert date object into a string
def getHtml(url):
    request = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
    response = urllib2.urlopen(request)
    html = response.read()
    date_accessed = response.info()['date']
    return html, date_accessed
def getHtml2(url):
    page = requests.get(url)
    return page.content, page.headers['Date']

def getHtmlByForce(url):
    page = ""
    while page == "":
        try:
            page = requests.get(url)
            return page.content, page.headers['Date']
        except:
            sleep(5)
            continue

def getBeautifulSoup(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup

def saveLinks(links):
    with open(filename, 'wb') as fp:
        pickle.dump(links, fp)
    print "the file %s has been created " %s
# the function below fetches all links in the radiookapi.net homepage and returns them.
def okapiLinks(html, date_published, url):
    root_url = url
    links = []
    for i in re.findall('''href=["'](.[^"']+)["']''', html, re.I):
        full_link = root_url + i
        # for radio okapi
        if date_published in full_link:
            links.append(full_link)
    links = sorted(set(links))
    return links
def politicoLinks(html, date_published, url):
    root_url = url
    links = []
    for i in re.findall('''href=["'](.[^"']+)["']''', html, re.I):
        full_link = i
        # for radio okapi
        if date_published in full_link:
            links.append(full_link)
    links = sorted(set(links))
    return links
def actualiteLinks(html, date_published, url):
    root_url = url
    links = []
    for i in re.findall('''href=["'](.[^"']+)["']''', html, re.I):
        full_link = i
        # for radio okapi
        if date_published in full_link:
            links.append(root_url[:-1] + full_link)
    links = sorted(set(links))
    return links
def beniluberoLinks(html, url):
    # root_url = url
    links = []
    for link in re.findall('''href=["'](.[^"']+)["']''', html, re.I):
        #full_link = i
        # for radio okapi
        # if date_published in full_link:
        if link.startswith(url):
            links.append(link)
    links = sorted(set(links))
    return links
def jeuneafriqueLinks(html, url):
    root_url = "http://www.jeuneafrique.com"
    links = []
    for i in re.findall('''href=["'](.[^"']+)["']''', html, re.I):
        full_link = root_url + i
        # for radio okapi
        # if date_published in full_link:
        links.append(full_link)
    links = sorted(set(links))
    jeuneafrique_links_final = []
    for link in links:
        match = re.search(r'/\d\d\d\d+/\w\w\w\w\w+', link)
        if match:
            jeuneafrique_links_final.append(link)
        else:
            pass
    return jeuneafrique_links_final
def genericLinks(html, url):
    root_url = url
    links = []
    for i in re.findall('''href=["'](.[^"']+)["']''', html, re.I):
        full_link = root_url + i
        # for radio okapi
        # if date_published in full_link:
        links.append(full_link)
    links = sorted(set(links))
    return links
def deskecoLinks(html, url):
    pass 
def lecongolaiscdLinks(html, url):
    pass
def laprosperiteLinks(html, url):
    pass
def mediacongoLinks(html, url):
    pass
def forumdesasLinks(html, url):
    pass
def theguardianLinks(html, url):
    pass
def financialtimesLinks(html, url):
    pass
def bloombergLinks(html, url):
    pass
def bloomberggoogleLinks(html, url):
    pass
def cnnLinks(html, url):
    pass
def france24Links(html, url):
    pass
def france24googleLinks(html, url):
    pass
def tv5mondeLinks(html, url):
    pass
def africanewsrdcLinks(html, url):
    pass
def topcongofmLinks(html, url):
    pass

