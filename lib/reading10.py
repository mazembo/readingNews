# py -2 reading10.py rdc
# encoding=utf8
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
#import YamlTomongo as ym
import getlinkstest as gl
import getcontent as gc
from time import sleep
import datetime
import hashlib

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
    urls_folder = '/var/jenkins_home/data/readingNewsCongo/assets/urls_text_files/'
    filename = urls_folder + country_name + ".txt"
    date_prefix = gl.getDatetimeLong()
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
    librebelgique = str(list_of_sites[6])
    lemonde = str(list_of_sites[7])
    voixamerique = str(list_of_sites[8])
    lepotentiel = str(list_of_sites[9])
    congoindependant = str(list_of_sites[10])

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
    try:
        librebelgique_html, librebelgique_date_accessed = gl.getHtml(librebelgique)
    except:
        print "there was a problem to connect to the site: %s" %librebelgique
        pass
    try:
        lemonde_html, lemonde_date_accessed = gl.getHtml(lemonde)
    except:
        print "there was a problem to connect to the site: %s" %lemonde
        pass

    try:
        voixamerique_html, voixamerique_date_accessed = gl.getHtml(voixamerique)
    except:
        print "there was a problem to connect to the site: %s" %voixamerique
        pass
    try:
        lepotentiel_html, lepotentiel_date_accessed = gl.getHtml(lepotentiel)
    except:
        print "there was a problem to connect to the site: %s" %lepotentiel
        pass
    try:
        congoindependant_html, congoindependant_date_accessed = gl.getHtml(congoindependant)
    except:
        print "there was a problem to connect to the site: %s" %congoindependant
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
    #for rfi 

    rfi_date_published = gl.getDatetimeSlash()
    try: 
        rfi_links = gl.rfiLinksDefault()
    except:
        pass
   # for librebelgique  
   
    librebelgique_date_published = gl.getDatetimeSlash()
    try:
        librebelgique_links = gl.librebelgiqueLinksDefault(librebelgique_html, librebelgique_date_published)
    except:
        pass
    # for lemonde.fr
    lemonde_date_published = gl.getDatetimeSlash()
    try:
        lemonde_links = gl.lemondeLinksDefault(lemonde_html, lemonde_date_published)
    except:
        pass
    # for voix de l amerique
    voixamerique_date_published = gl.getDatetimeSlash()
    try:
        voixamerique_links = gl.voixameriqueLinksDefault(voixamerique_html, voixamerique_date_published)
    except:
        pass

    # for lepotentiel 
    lepotentiel_date_published = gl.getDatetimeSlash()
    try:
        lepotentiel_links = gl.lepotentielLinksDefault(lepotentiel_html, lepotentiel_date_published)
    except:
        pass

    # for congoindependant 
    congoindependant_date_published = gl.getDatetimeSlash()
    try:
        congoindependant_links = gl.congoindependantLinksDefault(congoindependant_html, congoindependant_date_published)
    except:
        pass

   
    # print jeuneafrique_links
    #for link in jeuneafrique_links:
    #    print link
    #for link in rfi_links:
    #    print link

    #print benilubero_html
    print benilubero_links 
    print librebelgique_links
    for link in librebelgique_links:
        print link
    print lemonde_links
    for link in lemonde_links:
        print link


    print voixamerique_links

    print lepotentiel_links
    for link in lepotentiel_links:
        print link

    print congoindependant_links
    for link in congoindependant_links:
        print link


    # creating a consolidated list of links

    consolidated_links_list = radiookapi_links + politico_links + actualite_links + benilubero_links + rfi_links + librebelgique_links + lemonde_links + voixamerique_links + lepotentiel_links + congoindependant_links 
    gc.write_links(output_filename, consolidated_links_list)
    print "the file has been created %s" %output_filename
    # writing the consolidated_links_list to a filege

    # Now getting the content and picture
    published_date = datetime.datetime.now().strftime('%Y-%m-%d')    
    yaml_file_articles = gc.process_list_urls_default(consolidated_links_list, published_date)




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
