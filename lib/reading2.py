import urllib2
import urllib
from bs4 import BeautifulSoup 

url = ""
request = urllib2.Request(url, headers={'User-Agent' : 'Chrome'})
response = urllib2.urlopen(request)
html = response.read()
