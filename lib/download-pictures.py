from bs4 import BeautifulSoup
import urllib2
import urllib
import urlparse
import io
#put the name of the text file containing urls
urls_file = "2016-12-28.txt"
with open(urls_file, 'r') as f:
    urls_list = [line.rstrip(u'\n') for line in f]
images = []
for item in urls_list:
    print item
    url = item
        # This packages the request (it doesn't make it)
    request = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
    # Sends the request and catches the response
    response = urllib2.urlopen(request)
    #Extracts the response
    html = response.read()
    # it is important to have the date we have accessed this data
    date_accessed = response.info()['date']
    # Let us write the html to file locally for archiving purposes

        # take it to BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    # Now get all the images, download them and pass a list of them

    for img in soup.select('img'):
        img_url = urlparse.urljoin(url, img['src'])
        print img_url
        file_name = img['src'].split('/')[-1]
        print file_name
        urlretrieve(img_url, file_name)
        images.append(file_name)
print "Here are all the image names: %s" %images
