
# py -2 reading10.py rdc
from bs4 import BeautifulSoup
import urllib2
import urllib
from urllib import urlretrieve
import urlparse
import io
import sys
import yaml
import pickle
import hashlib
import YamlTomongo as ym
import getlinks as gl
import getcontent as gc
from time import sleep
# consolidated_links_list = []
# okapi_links_list = []
# rfi_links_list = []
# jeuneAfrique_links_list = [] and so on
# So read the country file and initialise these arrays
# Only validated links to be included in consolidated_links_list... and let it be an array of arrays
# the array of arrays (consolidated list) to be written in disk with pickle
# we initialise a big Dictionnary which will host all the elements found in the array of arrays...
# Now we go through each array of the arrays... if the array has at least one element... we ready each element...
# And we place the element in the Dictionnary
# We end with writing to disks and to the db...

#put the name of the text file containing urls

def readNewsRdcongo(country_name):
    # Initializing a set of placeholders variables
    list_of_sites = []
    filename = country_name + ".txt"
    date_prefix = gl.getDatetimeLong()
    urls_folder = 'C:\\Users\\mazem\\myprojects-2018\\python\\readingNews\\assets\\urls-text-files\\'
    output_filename = urls_folder + date_prefix + '-' + country_name + '.txt'
    with open (filename, 'rb') as fp:
        itemlist = [line.rstrip(u'\n')for line in fp]
        for item in itemlist:
            list_of_sites.append(item)
    print list_of_sites
    # Site by site
    # First site: radiookapi.net
    #
    radiookapi = str(list_of_sites[0])
    print radiookapi
    actualite = str(list_of_sites[1])
    politico = str(list_of_sites[2])
    rfi = str(list_of_sites[3])
    jeuneafrique = str(list_of_sites[4])
    benilubero = str(list_of_sites[5])

    # # We connect to grab the html and date_accessed of every site listed above
    try:
        radiookapi_html, radiookapi_date_accessed = gl.getHtml(radiookapi)
    except:
        print "there was a problem to connect to the site: %s" %radiookapi
        pass
    try:
        actualite_html, actualite_date_accessed = gl.getHtml2(actualite)
    except:
        print "there was a problem to connect to the site: %s" %actualite
        pass
    try:
        politico_html, politico_date_accessed = gl.getHtml(politico)
    except:
        print "there was a problem to connect to the site: %s" %politico
        pass
    try:
        rfi_html, rfi_date_accessed = gl.getHtml(rfi)
    except:
        print "there was a problem to connect to the site: %s" %rfi
        pass
    try:
        jeuneafrique_html, jeuneafrique_date_accessed = gl.getHtml(jeuneafrique)
    except:
        print "there was a problem to connect to the site: %s" %jeuneafrique
        pass
    try:
        benilubero_html, benilubero_date_accessed = gl.getHtml(benilubero)
    except:
        print "there was a problem to connect to the site: %s" %benilubero
        pass

    # Getting list of urls of the site radiookapi.net
    radiookapi_date_published = gl.getDatetimeSlash()
    # Getting links
    # if html content is not grabbed for some reason, the script ends. So the statement getting links from html should be placed in a try statement in order to handle the exception
    try:
        radiookapi_links = gl.okapiLinks(radiookapi_html, radiookapi_date_published, radiookapi)
    except:
        pass
    print "printing the okapi list "
    print radiookapi_links
    for link in radiookapi_links:
        print link

    # For Politico.cd

    politico_date_published = gl.getDatetimeSlash()
    try:
        politico_links = gl.politicoLinks(politico_html, politico_date_published, politico)
    except:
        pass
    # print politico_links
    for link in politico_links:
        print link

    # For Actualite.cd
    actualite_date_published = gl.getDatetimeSlash()
    try:
        actualite_links = gl.actualiteLinks(actualite_html, actualite_date_published, actualite)
    except:
        pass
    # print actualite_links
    for link in actualite_links:
        print link

    # For benilubero.com
    benilubero_date_published = gl.getDatetimeSlash()
    try:
        benilubero_links = gl.beniluberoLinks(benilubero_html, benilubero)
    except:
        pass
    # print benilubero_links
    for link in benilubero_links:
        print link
    # For jeuneafrique.com
    jeuneafrique_date_published = gl.getDatetimeSlash()
    try:
        jeuneafrique_links = gl.jeuneafriqueLinks(jeuneafrique_html, jeuneafrique)
    except:
        pass
    # print jeuneafrique_links
    for link in jeuneafrique_links:
        print link

    # creating a consolidated list of links

    consolidated_links_list = radiookapi_links + politico_links + actualite_links + benilubero_links + jeuneafrique_links
    gc.write_links(output_filename, consolidated_links_list)
    print "the file has been created %s" %output_filename
    # writing the consolidated_links_list to a filege

    # Now getting the content and pictures




def main():
    theme = sys.argv[1]
    if theme == "rdc":
        readNewsRdcongo(theme)
    # elseif theme == "rsa":
    #     readNewsRsa(theme)
    # elseif theme == "ch":
    #     readNewsCh(theme)
    # elseif theme == "france":
    #     readNewsFrance(theme)
    # elseif theme == "tech":
    #     readingNewsTech(theme)
    # elseif theme == "job":
    #     readingNewsJob(them)


#this is the standard boilerplate that calls the main() function.
if __name__ == "__main__":
    main()
