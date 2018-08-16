import urllib2
import urllib
from bs4 import BeautifulSoup

url = "http://www.radiookapi.net/2017/02/09/actualite/societe/la-pluie-de-mardi-fait-4-morts-kinshasa"
request = urllib2.Request(url, headers={'User-Agent' : 'Chrome'})
response = urllib2.urlopen(request)
html = response.read()
soup = BeautifulSoup(html, "html.parser")
content = soup.findAll('div', attrs={'id':'article_area'})
print type (content)
