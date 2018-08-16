from pymongo import MongoClient
import sys
import os
import datetime
import yaml
# remaining issues: discovery of files in folder and exception handling if yaml file can't be loaded
# below I initialize the connection to the mongodb and indicate the name of the database in which I will write documents
connection = MongoClient("localhost:27017")
mydb = connection.news
#The function below takes a folder path, a folder of yaml files and writes all documents into the mongodb
def processYamlFolder(folderpath):
    list_of_files = os.listdir(folderpath)
    for item in list_of_files:
        processYamlFile(item)
#The function below takes a yaml file and insert its content (in the form of a list of dictionaries ) into the mongodb
def processYamlFile(filename):
    year = int(filename[0:4])
    month = int(filename[5:7])
    day = int(filename[8:10])
    articles = yamlToList(filename)
    for article in articles:
        article["date_published"] = datetime.datetime(year, month, day, 0, 0, 0)
        insertOne(article)

def insertOne(object):
    mydb.articles.insert(object)
    print "An object has been saved into mongodb"

def insertMultiple(collection):
    for item in collection:
        insertOne(item)
    print "A collection has been saved into mongodb"

def yamlToList(filename):
    with open(filename, "r") as stream:
        #try:
        articles = yaml.load(stream)
        #except:
        #    print "The file %s could not be read properly." %filename
        #    pass
        final_articles = []
        for key, value in articles.iteritems():
            final_articles.append(value)
        return final_articles
def main():
    argument = sys.argv[1]
    if argument.endswith("ml"):
        processYamlFile(argument)
    else:
        processYamlFolder(argument)


if __name__ == "__main__":
    main()
