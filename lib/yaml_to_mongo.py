import requests
import yaml
import io
import os
import sys

def apiCall(article, address):
    try:
        r = requests.post(address, data = article)
        print r.status_code
        print r.text
        print "\n"
    except:
        pass


def cleanUp(filename, raw_articles):
    date_elements = filename.rstrip(".yml").split("-")

    return articles

def readYaml(filename):
    with open(filename, "r") as stream:
        articles = yaml.load(stream)
        return articles

# Reading a yaml file
def writeToMongo(yaml_file, address):
    filename = yaml_file
    address = address
    raw_articles = readYaml(filename)
    final_articles = cleanUp(filename, raw_articles)
    for article_id in final_articles:
        article = articles[article_id]
        try:
            apiCall(article, address)
        except:
            pass

def writeFolderMongo(foldername):
    pass


def main():
    argument = sys.argv[1]
    address = "http://localhost:3000/api/articles"
    if argument.endswith("ml"):
        writeToMongo(argument, address)
    else:
        writeFolderMongo(argument, address)




if __name__ == "__main__":
    main()
