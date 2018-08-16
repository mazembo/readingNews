import urllib
import re

symbolslist= ["AAPL", "SPY", "GOOG", "NFLX" ]

i = 0
while i < len(symbolslist):
    url = "http://finance.yahoo.com/q?s=" +symbolslist[i]+ "&ql=1"
    htmlfile = urllib.urlopen(url)
    htmltext = htmlfile.read()
    regex = '<span id="yfs_184_aapl">(.+?)</span>'
    pattern = re.compile(regex)
    price = re.findall(pattern, htmltext)
    print price
    i+=1
