from bs4 import BeautifulSoup
import urllib2
import urllib
import urlparse
import io
import yaml

def get_content(soup):
    title = soup.title.string
    tweet_message = title
    #date_published= [meta.get('content') for meta in soup.find_all('meta', itemprop='datePublished')]
    body = soup.body.text
    short_message = body
    return title, body, short_message, tweet_message
def get_images(soup):
    images = []
    for img in soup.select('img'):
        img_url = urlparse.urljoin(url, img['src'])
        print img_url
        file_name = img['src'].split('/')[-1]
        print file_name
        urlretrieve(img_url, file_name)
        images.append(file_name)
    return images
def get_formated_article(article, title, body, short_message, tweet_message, date_accessed, date_published, url):
    article, title, body, short_message, tweet_message, date_accessed, date_published, url = article, title, body, short_message, tweet_message, date_accessed, date_published, url
    formated_article = {article:{'title': title, 'message': body, 'short_message': short_message,'tweet_message': tweet_message, 'original_url': url, 'lecongolais_url':'http://lecongolais.net','date_published': date_published, 'date_accessed': date_accessed}}
    return formated_article
def write_file(content):
    content = content
    with open('2016-11-26.yaml', 'w') as f:
      yaml.dump(content, f, default_flow_style=False)
urls_file = "2016-11-06.txt"
with open(urls_file, 'r') as f:
    urls_list = [line.rstrip(u'\n') for line in f]
articles = []
i = 0
for item in urls_list:
    print item
    url = item
    i += 1
    article = "article_%s" %i
    # This packages the request (it doesn't make it)
    request = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
    # Sends the request and catches the response
    response = urllib2.urlopen(request)
    #Extracts the response
    html = response.read()
    # it is important to have the date we have accessed this data
    date_accessed = response.info()['date']
    # Let us write the html to file locally for archiving purposes
    date_published = "12-12-2016"
    # take it to BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    # Now get all the images, download them and pass a list of them
    #images = get_images(soup)
    # Now we get the most important pieces of information from the beautifulsoup object
    title, body, short_message, tweet_message = get_content(soup)
    # Now we get the infos formated as we would like it
    formated_article = get_formated_article(article, title, body, short_message, tweet_message, date_accessed, date_published, url)
    articles.append(formated_article)
print (articles)
print len(articles)
print type(articles)
#write_file(articles)
