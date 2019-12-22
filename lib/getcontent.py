# encoding=utf8
import pickle
import hashlib
from bs4 import BeautifulSoup
import urllib2
import urllib
from urllib import urlretrieve
import urlparse
import io
import sys
import yaml
from time import sleep


images_folder = "/var/jenkins_home/data/readingNewsCongo/assets/images/"
html_folder = "/var/jenkins_home/data/readingNewsCongo/assets/html_files/"
yaml_folder = "/var/jenkins_home/data/readingNewsCongo/assets/content_yaml_files/"
urls_folder = "/var/jenkins_home/data/readingNewsCongo/assets/urls_text_files/"

def radiookapiContent(soup):
    body = soup.findAll("div", {"class" : "inside panels-flexible-row-inside panels-flexible-row-3-3-inside clearfix"})
    body = body[0].text
    body = body.encode('utf-8')
    signature = " #RDC @LecongolaisNet"
    short_message = body + signature
    return body, short_message
def get_content_default(soup):
    title = soup.title.text
    title = title.encode('utf-8')
    signature = " #RDC @LecongolaisNet"
    tweet_message = title + signature 
    #date_published= [meta.get('content') for meta in soup.find_all('meta', itemprop='datePublished')]
    #body = soup.findAll("div", {"class" : "inside panels-flexible-row-inside panels-flexible-row-3-3-inside clearfix"})
    #body = body[0].text
    #short_message = body + signature
    return title, tweet_message

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
def get_images_default():
    return "001_image.jpg"
    
def download_image(images_url, url):
    if images_url[0] != "001_image.jpg":
        img_url = images_url[0]
        file_name = hashlib.sha224(img_url).hexdigest() + ".jpg"
        urlretrieve(img_url, file_name)
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
def get_formated_article_default(title, tweet_message, date_accessed, date_published, url, image_filename):
    title, tweet_message, date_accessed, date_published, url, image_filename = title, tweet_message, date_accessed, date_published, url, image_filename
    body = ""
    short_message = ""
    formated_article = {'title': title, 'message': body, 'short_message': short_message,'tweet_message': tweet_message, 'original_url': url, 'lecongolais_url':'http://lecongolais.net','date_published': date_published, 'date_accessed': date_accessed, 'picture': image_filename, 'categories':'RDC-Politique-Societe-Economie'}
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
def write_links(links_file_name, links_list):
    try:
        with open(links_file_name, 'wb') as fp:
            pickle.dump(links_list, fp)
            print("the file has been created: %s" %links_file_name)
    except:
        print("there was a problem creating this file: %s" %links_file_name )
        pass
def process_list_urls_default(list_urls, today_date):
    articles = {}
    date_published = today_date
    year = int(date_published[0:4])
    month = int(date_published[5:7])
    day = int(date_published[8:10])
    yaml_file_name = "rdc-" + date_published + ".yml"
    i = 0
    for item in list_urls:
        try:
            print item
            url = item
            i += 1
            article = hashlib.sha224(url).hexdigest()
            print("hashlib works")

    # This packages the request (it doesn't make it)
            request = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
    # Sends the request and catches the response
            response = urllib2.urlopen(request)
            print("the request was made")
    #Extracts the response
            html = response.read()
            print("I have read the response")
    # it is important to have the date we have accessed this data
            date_accessed = response.info()['date']
            print("I have read the date")
    # Let us write the html to file locally for archiving purposes

    # Below is the format of the filename of the html data.
            html_file_name_end = "rdc-" + date_published + "-%s" %i + ".html"
            print("I have created the file end")
            html_file_name = html_folder + html_file_name_end
            print("I have created the filename")
    # take it to BeautifulSoup
            soup = BeautifulSoup(html, "html.parser")
            print("I have the soup")
        #date_infos = soup.findAll("div", {"class" : "pane-content"})[2].p.text
            image_filename = get_images_default()
            print(image_filename)
            title, tweet_message = get_content_default(soup)
            print(title)
        #title, body, short_message, tweet_message = clean_up(title, body, short_message, tweet_message)

    # Now we get the infos formated as we would like it
            formated_article = get_formated_article_default(title, tweet_message, date_published, date_published, url, image_filename)
            articles[article] = formated_article
            write_html(html_file_name, html)
            sleep(2)
        except:
            print("Oops!",sys.exc_info()[0],"occured.")
            pass
    yaml_file_name = yaml_folder + yaml_file_name
    write_yaml(yaml_file_name, articles)
    print "the file %s has been created" %yaml_file_name 
    return yaml_file_name
