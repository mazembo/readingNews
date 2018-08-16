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
def clean_up(title, body, short_message, tweet_message):
    title = title.replace(":", "--")
    body =  body.replace(":", "--")
    short_message = short_message.replace(":", "--")
    tweet_message = tweet_message.replace(":", "--")
    title = title.replace("\n", " ")
    body =  body.replace("\n", " ")
    short_message = short_message.replace("\n", " ")
    tweet_message = tweet_message.replace("\n", " ")
    title = title.replace("\t", " ")
    body =  body.replace("\t", " ")
    short_message = short_message.replace("\t", " ")
    tweet_message = tweet_message.replace("\t", " ")
    title = title.replace("\\x", " ")
    body =  body.replace("\\x", " ")
    short_message = short_message.replace("\\x", " ")
    tweet_message = tweet_message.replace("\\x", " ")
    return title, body, short_message, tweet_message



def get_formated_article(title, body, short_message, tweet_message, date_accessed, date_published, url):
    title, body, short_message, tweet_message, date_accessed, date_published, url = title, body, short_message, tweet_message, date_accessed, date_published, url
    formated_article = {'title': title, 'message': body, 'short_message': short_message,'tweet_message': tweet_message, 'original_url': url, 'lecongolais_url':'http://lecongolais.net','date_published': date_published, 'date_accessed': date_accessed}
    return formated_article
def write_html(html_file_name, html):
    out_file = open(html_file_name, "w")
    out_file.write(html)
    out_file.close
    print "We have created the file: %s" %html_file_name
def write_yaml(yaml_file_name, articles):
    with open(yaml_file_name, 'w') as yaml_file:
        yaml.dump(articles, yaml_file, encoding='utf-8', allow_unicode=True, default_flow_style=False)
        print "We have created the file: %s" %yaml_file_name
#put the name of the text file containing urls
urls_file = "2016-12-28.txt"
with open(urls_file, 'r') as f:
    urls_list = [line.rstrip(u'\n') for line in f]
articles = {}
date_published = "2016-12-28"
yaml_file_name = date_published + ".yml"
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

    # Below is the format of the filename of the html data.
    html_file_name = date_published + "-%s" %i + ".html"

    # take it to BeautifulSoup
    soup = BeautifulSoup(html, "html.parser")
    # Now get all the images, download them and pass a list of them
    #images = get_images(soup)
    # Now we get the most important pieces of information from the beautifulsoup object
    title, body, short_message, tweet_message = get_content(soup)
    title, body, short_message, tweet_message = clean_up(title, body, short_message, tweet_message)

    # Now we get the infos formated as we would like it
    formated_article = get_formated_article(title, body, short_message, tweet_message, date_accessed, date_published, url)
    articles[article] = formated_article
    write_html(html_file_name, html)
write_yaml(yaml_file_name, articles)
# print (articles)
# print len(articles)
# print type(articles)
#write_file(articles)
