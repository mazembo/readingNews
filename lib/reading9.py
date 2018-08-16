from bs4 import BeautifulSoup
import urllib2
import urllib
from urllib import urlretrieve
from urlparse import urlparse
import io
import sys
import yaml
import pickle
import hashlib
#  import getContent
#  import getImage
#  import getLinks
#  import dbOperations
#  import newsLetter
#  import pdfcreator
#  import tweeting
#  import facebook

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
def process_textfile(textfile, today_date):
    with open (textfile, 'rb') as fp:
        itemlist = pickle.load(fp)
    new_itemlist = sorted(set(itemlist))
    articles = {}
    date_published = today_date
    yaml_file_name = date_published + ".yml"
    i = 0
    for item in new_itemlist:
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
        date_infos = soup.findAll("div", {"class" : "pane-content"})[2].p.text
        images_url = []
        images_url = get_images_okapi(soup)
        image_filename = download_image(images_url, url)
        title, body, short_message, tweet_message = get_content(soup)
        title, body, short_message, tweet_message = clean_up(title, body, short_message, tweet_message)

    # Now we get the infos formated as we would like it
        formated_article = get_formated_article(title, body, short_message, tweet_message, date_accessed, date_published, url, image_filename)
        articles[article] = formated_article
        write_html(html_file_name, html)


    write_yaml(yaml_file_name, articles)
# print (articles)
# print len(articles)
# print type(articles)
#write_file(articles)
def makeSoup(url):
    request = urllib2.Request(url, headers = {"User-Agent" : "Chrome"})
    response = urllib2.urlopen(request)
    html = response.read()
    date_accessed = response.info()['date']
    soup = BeautifulSoup(html, "html.parser")
    return soup, date_accessed
def getUrls(date, country):
    filename = "%s-rootlinks.txt" %country
    with open(filename, "r") as f:
        urls_list = [ line.rstrip(u'\n')for line in f]
        # various ways of getting links of the day...
        # write various ways of getting links of the day based on the root_url
        for link in urls_list:
            print link
        #link_name = urlparse(link)[1].split(".")[1]


def processFile(links_file, date):
    pass

# The main function processes the command line instructions. Two possibilities
# reading-news.py 2017-02-24 rdc : this command produces a text file with relevant links for the day. The file is named rdc-2017-02-24.text
# reading-news.py rdc-2017-02-24.txt : This processes the file of links producing a yaml file in the following format: rdc-2017-02-24.yml and save infos to databases.
def main():
    if len(sys.argv) == 3:
        date = sys.argv[1].replace("-", "/")
        country = sys.argv[2]
        getUrls(date, country)
    elif len(sys.argv) == 2:
        links_file = sys.argv[1]
        date = links_file[-14:-4]
        processFile(links_file, date)
    else:
        print "check number of arguments"
        exit()


#this is the standard boilerplate that calls the main() function.
if __name__ == "__main__":
    main()

#Here are  the methods (functions) that need to be implemented
# getImageOkapi getImageJa getImageLemonde getImageRfi getImageLesoir getImageBeniLubero getImageActualite getImagePolitico getImageLepotentiel getImageLephare
# getContentOkapi getContentJa getContentLemonde getContentRfi getContentLesoir getContentBeniLubero getContentActualite getContentPolitico getContentLepotentiel getContentLephare
# common methos : makeSoup(html), download(link), writeHtml writeYaml
# command lines structure:
# browsing.py date (2017-02-22) : the script should get all news links of the dqteand write them to a File
# browsing.py 2017-02-22.txt (read the file, download contents in the form of 2017-02-22.yml )
# save to DB (Mongo and PostgreSQL)
# load to wordpress through a php script
# dispatch to twitter and facebook
# send via emails as newsletter and PDF
# display on various frontends plateforms (Android, IOS, angular App calling an API end-point)
