# this is the final file for these functions 
# worked as expected on 01 february 2018
from pymongo import MongoClient
import sys
import os
import datetime
import yaml

# I define here a number of variables which will be combined with command line input to provide a full absolute path to files and folders

folder_path = "C:\\Users\\mazem\\myprojects-2018\\python\\readingNews\\assets\\passed-yaml-files"
hostname = "mongodb://127.0.0.1:27017"

# remaining issues: discovery of files in folder and exception handling if yaml file can't be loaded
# below I initialize the connection to the mongodb and indicate the name of the database in which I will write documents
connection = MongoClient(hostname)
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
    articles = yamlToDict(filename)
    #print(articles) 
    #print (type(articles))
    #check that articles is a non empty dic and whether it has values  
    if not articles:
        pass
    elif len(articles) == 0:
        pass
          
    else:
        list_articles = dicToList(articles)
        for article in list_articles:
            article["date_published"] = datetime.datetime(year, month, day, 0, 0, 0)
            insertOne(article)

    
# The function below takes a document and inserts it into the articles collection in mongodb
def insertOne(object):
    mydb.articles.insert(object)
    print ("An object has been saved into mongodb")

# The function below takes a collection of documents and insert them one by one into the articles collection in mongodb 
def insertMultiple(collection, year, month, day):
    for item in collection:
        item["date_published"] = datetime.datetime(year, month, day, 0, 0, 0)
        insertOne(item)

# The below function takes a yaml file and returns objects in a form of a dictionnary
def yamlToDict(filename):
    filename = folder_path + "\\" + filename 
    try:
        with open(filename, "r") as stream:
            articles = yaml.load(stream)
            return articles
    except:
        print ("The file %s could not be read properly." %filename)
        articles = {}
        return articles 
# This function helps to convert the dictionnary generated from the above function into a list of objects so that they are easily inserted into the mongodb collection named articles 
def dicToList(articles):
    final_articles = []
    for key, value in articles.items():
        final_articles.append(value)
    return final_articles
# here is the main function to launch the program 
# python YamlTomongo.py 2017-10-30.yml
# python YamlTomongo.py default to loading the specified folder in the script
def main():
    
    if len(sys.argv) > 1:
        processYamlFile(sys.argv[1])
    else:
        processYamlFolder(folder_path)


if __name__ == "__main__":
    main()
