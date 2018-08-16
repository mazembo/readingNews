import re

def find(pat, text):
  match = re.search(pat, text)
  if match:
      print match.group()
  else:
      print "not found"
