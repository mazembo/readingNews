#!python2
# py -2 -m pip install BeautifulSoup4
# How to run this script? read below:
# py -2 extract_links.py
# py -2 reading8.py 2018-02-06.txt 2018-02-06


from bs4 import BeautifulSoup
import urllib2
import urllib
from urllib import urlretrieve
import urlparse
import io
import sys
import yaml
import pickle
import hashlib
#import YamlTomongo
import datetime
import getlinks as gl

images_folder = "/var/jenkins_home/data/readingNewsCongo/assets/images/"
yaml_folder = "/var/jenkins_home/data/readingNewsCongo/assets/content_yaml_files/"
html_folder = "/var/jenkins_home/data/readingNewsCongo/assets/html_files/"
urls_folder = "/var/jenkins_home/data/readingNewsCongo/assets/urls_text_files/"

def get_content(soup):
    title = soup.title.text
    signature = " #RDC @LecongolaisNet"
    tweet_message = title
    #date_published= [meta.get('content') for meta in soup.find_all('meta', itemprop='datePublished')]
    body = soup.findAll("div", {"class" : "inside panels-flexible-row-inside panels-flexible-row-3-3-inside clearfix"})
    body = body[0].text
    short_message = body + signature
    return title, body, short_message, tweet_message

def get_images_okapi(soup):
    images = []
    for img in soup.find_all("div", {"class" : "inside panels-flexible-row-inside panels-flexible-row-3-3-inside clearfix"})[0].find_all('img'):
        temp = img.get('src')
        images.append(temp)
    if len(images) > 0:
        return images
    else:
        images.append("001_image.jpg")
        return images
def download_image(images_url, url):
    if images_url[0] != "001_image.jpg":
        img_url = images_url[0]
        file_name = hashlib.sha224(img_url).hexdigest() + ".jpg"
        file_name_full = images_folder + file_name
        #print img_url
        if "photos." in img_url:
            img_url = "https:" + img_url 
        urlretrieve(img_url, file_name_full)
        return file_name

    else:
        file_name = images_url[0]
        return file_name

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
def get_formated_article(title, body, short_message, tweet_message, date_accessed, date_published, url, image_filename):
    title, body, short_message, tweet_message, date_accessed, date_published, url, image_filename = title, body, short_message, tweet_message, date_accessed, date_published, url, image_filename
    formated_article = {'title': title, 'message': body, 'short_message': short_message,'tweet_message': tweet_message, 'original_url': url, 'lecongolais_url':'http://lecongolais.net','date_published': date_published, 'date_accessed': date_accessed, 'picture': image_filename, 'categories':'RDC-Politique-Societe-Economie'}
    return formated_article
def write_html(html_file_name, html):
    filename = html_folder + html_file_name
    out_file = open(html_file_name, "w")
    out_file.write(html)
    out_file.close
    print "We have created the file: %s" %html_file_name
def write_yaml(yaml_file_name, articles):
    with open(yaml_file_name, 'w') as yaml_file:
        yaml.dump(articles, yaml_file, encoding='utf-8', allow_unicode=True, default_flow_style=False)
        print "We have created the file: %s" %yaml_file_name
#put the name of the text file containing urls
def process_textfile(textfile, today_date):
    textfile = urls_folder + textfile
    with open (textfile, 'rb') as fp:
        itemlist = pickle.load(fp)
    new_itemlist = sorted(set(itemlist))
    articles = {}
    date_published = today_date
    year = int(date_published[0:4])
    month = int(date_published[5:7])
    day = int(date_published[8:10])
    yaml_file_name = date_published + ".yml"
    i = 0
    for item in new_itemlist:
        try:
            print item
            url = item
            i += 1
            article = hashlib.sha224(url).hexdigest()

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
            html_file_name_end = date_published + "-%s" %i + ".html"
            html_file_name = html_folder + html_file_name_end
    # take it to BeautifulSoup
            soup = BeautifulSoup(html, "html.parser")
    # Now get all the images, download them and pass a list of them
    #images = get_images(soup)
    # Now we get the most important pieces of information from the beautifulsoup object
            #date_infos = soup.findAll("div", {"class" : "pane-content"})[2].p.text
            images_url = []
            images_url = get_images_okapi(soup)
            image_filename = download_image(images_url, url)
            title, body, short_message, tweet_message = get_content(soup)
            title, body, short_message, tweet_message = clean_up(title, body, short_message, tweet_message)

    # Now we get the infos formated as we would like it
            formated_article = get_formated_article(title, body, short_message, tweet_message, date_accessed, date_published, url, image_filename)
            articles[article] = formated_article
            write_html(html_file_name, html)
        except:
            print("Oops!",sys.exc_info()[0],"occured.")
            pass


    yaml_file_name = yaml_folder + yaml_file_name
    write_yaml(yaml_file_name, articles)
    #print "we are about to save the articles to MongoDB"
    #list_articles = YamlTomongo.dicToList(articles)
    #YamlTomongo.insertMultiple(list_articles, year, month, day)
    #print "the collection of articles has been saved to the MongoDB"

# print (articles)
# print len(articles)
# print type(articles)
#write_file(articles)
def main():
    published_date = datetime.datetime.now().strftime('%Y-%m-%d')
    date_text_file = published_date + ".txt"  
    process_textfile(date_text_file, published_date)
#this is the standard boilerplate that calls the main() function.
# python 2018-01-31.txt 2018-01-31

if __name__ == "__main__":
    main()
# specify in the script the paths for html files, for yaml files, and for related images
# the path for images: ""
