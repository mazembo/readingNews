#!python2
import io
import sys
import pickle 

print "what is your file's name?"
filename = input(">")
print filename 
with open(filename, "r") as fp
    itemlist = pickle.load(fp)
    for item in itemlist:
        print item 