import yaml

with open("2016-12-04.yml", 'r') as stream:
  articles = yaml.load(stream)
  print len(articles)
  print type(articles)
  print articles['article2']
  print articles['article2']['picture']
