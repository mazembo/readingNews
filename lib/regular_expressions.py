import re

# re.search(pattern, text)
# re.findall 

match = re.search("iip", "I have got a piig")
match.group()


def find(pattern, text):
    match = re.search(pattern, text)
    if match:
        print match.group()
    else:
        print "Not found"
