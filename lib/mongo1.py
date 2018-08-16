# mongo1.py

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

# data base name : 'test-database-1'
mydb = client['news']

# import datetime
#
# myrecord = {
#         "author": "Duke",
#         "title" : "PyMongo 101",
#         "tags" : ["MongoDB", "PyMongo", "Tutorial"],
#         "date" : datetime.datetime.utcnow()
#         }
#
# record_id = mydb.mytable.insert(myrecord)
#
# print record_id
# print mydb.collection_names()
articles = mydb.articles.find()
for article in articles:
    print article 
# print articles
