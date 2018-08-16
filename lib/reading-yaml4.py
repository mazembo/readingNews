import yaml

with open("2017-04-04.yml", 'r') as stream:
  articles = yaml.load(stream)
  for article in articles:
      artikle = articles[article]
      print article
      print artikle['picture']
      print artikle['tweet_message']
      print type(artikle)
      print len(artikle)
      print artikle
      print "\n"
     # print len(article)
     # print type(article)
