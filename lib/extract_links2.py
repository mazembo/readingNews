from urllib import urlretrieve
import re, urllib2
import pickle
import sys

# textfile = file('depth_1.txt','wt')
def get_links(textfile, published_date):
    date_published = published_date.replace("-", "/")
    date_published_bis = published_date.replace("-", "")
    with open(textfile, 'r') as f:
        urls_list = [line.rstrip(u'\n') for line in f]
    for item in urls_list:
        request = urllib2.Request(item, headers={'User-Agent' : "Magic Browser"})
        response = urllib2.urlopen(request)
        html = response.read()
        links = []
        for i in re.findall('''href=["'](.[^"']+)["']''', html, re.I):
            full_link = item + i
    # for radio okapi
            if date_published or date_published_bis in full_link:
                links.append(full_link)

    print links
        # outfile = published_date + ".txt"
        # with open(outfile, 'wb') as fp:
        #     pickle.dump(links, fp)
        # print "the file has been created"
def main():
    textfile, published_date = sys.argv[1], sys.argv[2]
    get_links(textfile, published_date)

if __name__ == '__main__':
    main()
