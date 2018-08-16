import sys
import os

date_published = date_published
research_key = date_published + "-RDC"
files = [f for f in os.listdir(".") if f.startswith(research_key)]
for f in files:
    message = getMessage(f)

def getMessage(f):
    pass 
