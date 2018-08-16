# processing_yaml.py filename or folder_name
import sys
import yaml
import io
from os import listdir

#  import dbOperations
#  import newsLetter
#  import pdfcreator
#  import tweeting
#  import facebook


def processFile(yamlfile):
    with open(yamlfile, "r") as stream:
        try:
            articles = yaml.load(stream)
            return articles
        except yaml.YAMLError as exc:
            print "The system failed to read the yaml file"

def processFolder(yamlfolder):
    articles_collection = {}
    path = "/home/mavungu/Lecongolais.net/facebook/"
    folder = path + yamlfolder
    for yamlfile in listdir(folder):
        articles = processFile(yamlfile)
        articles_collection.update(articles)
    return articles_collection

def print_articles(yamlfile):
    articles = processFile(yamlfile)
    for article in articles:
        individual_article = articles[article]
        print individual_article["title"]
        print individual_article["tweet_message"]
        print individual_article["original_url"]
        print individual_article["picture"]
        print("\n")
    print len(articles)

def print_folder(yamlfolder):
    articles = processFolder(yamlfolder)
    for article in articles:
        individual_article = articles[article]
        print individual_article["title"]
        print individual_article["tweet_message"]
        print individual_article["original_url"]
        print individual_article["picture"]
        print("\n")
    print len(articles)
def tweeting(yamlfile):
     pass

def facebooking(yamlfile):
    pass

def wordpressing(yamlfile):
    pass

def wordpressing(yamlfolder):
    pass

def emailing(yamlfile):
    pass

def fileMongo(yamlfile):
    pass

def folderMongo(yamlfolder):
    pass

def filePostgresql(yamlfile):
    pass

def folderPostgresql(yamlfolder):
    pass

def rewriting(yamlfile):
    pass

def rewriting(yamlfolder):
    pass


def main():
    if sys.argv[1].endswith(".yml"):
        processFile(sys.argv[1])
    else:
        processFolder(argv[1])


if __name__ == "__main__":
    main()
