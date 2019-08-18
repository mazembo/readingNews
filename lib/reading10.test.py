
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
    urls_folder = '/mnt/volume_dielais/readingNews/assets/urls_text_files/'
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
    laprosperite  = str(list_of_sites[11])
    mediacongo =  str(list_of_sites[12])
    deskeco =    str(list_of_sites[13])
    lecongolaiscd = str(list_of_sites[14])
    forumdesas = str(list_of_sites[15])
    theguardian = str(list_of_sites[16])
    financialtimes = str(list_of_sites[17])
    bloomberg = str(list_of_sites[18])
    bloomberggoogle = str(list_of_sites[19])
    cnn = str(list_of_sites[20])
    france24 = str(list_of_sites[21])
    france24google = str(list_of_sites[22])
    tv5monde = str(list_of_sites[23])
    africanews = str(list_of_sites[24])
    africanewsrdc = str(list_of_sites[25])
    topcongofm = str(list_of_sites[26])


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

     try:
        deskeco_html, deskeco_date_accessed = gl.getHtml(deskeco)
    except:
        print "there was a problem to connect to the site: %s" %deskeco
        pass
    try:
        lecongolaiscd_html, lecongolaiscd_date_accessed = gl.getHtml2(lecongolaiscd)
    except:
        print "there was a problem to connect to the site: %s" %actualite
        pass
    try:
        laprosperite_html, laprosperite_date_accessed = gl.getHtml(laprosperite)
    except:
        print "there was a problem to connect to the site: %s" %laprosperite
        pass
    try:
        mediacongo_html, mediacongo_date_accessed = gl.getHtml(mediacongo)
    except:
        print "there was a problem to connect to the site: %s" %mediacongo
        pass
    try:
        forumdesas_html, forumdesas_date_accessed = gl.getHtml(forumdesas)
    except:
        print "there was a problem to connect to the site: %s" %forumdesas
        pass
    try:
        theguardian_html, theguardian_date_accessed = gl.getHtml(theguardian)
    except:
        print "there was a problem to connect to the site: %s" %theguardian
        pass
    try:
        financialtimes_html, financialtimes_date_accessed = gl.getHtml(financialtimes)
    except:
        print "there was a problem to connect to the site: %s" %financialtimes
        pass
    try:
        bloomberg_html, bloomberg_date_accessed = gl.getHtml(bloomberg)
    except:
        print "there was a problem to connect to the site: %s" %bloomberg
        pass

    try:
        bloomberggoogle_html, bloomberggoogle_date_accessed = gl.getHtml(bloomberggoogle)
    except:
        print "there was a problem to connect to the site: %s" %bloomberggoogle
        pass
    try:
        cnn_html, cnn_date_accessed = gl.getHtml(cnn)
    except:
        print "there was a problem to connect to the site: %s" %cnn
        pass
    try:
        france24_html, france24_date_accessed = gl.getHtml(france24)
    except:
        print "there was a problem to connect to the site: %s" %france24
        pass


    try:
        france24google_html, france24google_date_accessed = gl.getHtml(france24google)
    except:
        print "there was a problem to connect to the site: %s" %france24google
        pass
    try:
        africanews_html, africanews_date_accessed = gl.getHtml(africanews)
    except:
        print "there was a problem to connect to the site: %s" %africanews
        pass

    try:
        tv5monde_html, tv5monde_date_accessed = gl.getHtml(tv5monde)
    except:
        print "there was a problem to connect to the site: %s" %tv5monde
        pass
    try:
        africanewsrdc_html, africanewsrdc_date_accessed = gl.getHtml(africanewsrdc)
    except:
        print "there was a problem to connect to the site: %s" %africanewsrdc
        pass
    try:
        topcongofm_html, topcongofm_date_accessed = gl.getHtml(topcongofm)
    except:
        print "there was a problem to connect to the site: %s" %france24
        pass
    # get links for the 14 new sites

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
    for link in jeuneafrique_links:
        print link
    for link in rfi_links:
        print link

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
    
    # for 14 sites get the links 

    try:
        deskeco_links = gl.deskecoLinks(deskeco_html, deskeco_date_published, deskeco)
    except:
        pass
    print "printing the okapi list "
    print deskeco_links
    for link in deskeco_links:
        print link
    
    try:
        lecongolaiscd_links = gl.lecongolaiscdLinks(lecongolaiscd_html, lecongolaiscd_date_published, lecongolaiscd)
    except:
        pass
    print "printing the okapi list "
    print lecongolaiscd_links
    for link in lecongolaiscd_links:
        print link

    try:
        laprosperite_links = gl.laprosperiteLinks(laprosperite_html, laprosperite_date_published, laprosperite)
    except:
        pass
    print "printing the okapi list "
    print laprosperite_links
    for link in laprosperite_links:
        print link

    try:
        mediacongo_links = gl.mediacongoLinks(mediacongo_html, mediacongo_date_published, mediacongo)
    except:
        pass
    print "printing the okapi list "
    print mediacongo_links
    for link in mediacongo_links:
        print link

    try:
        forumdesas_links = gl.forumdesasLinks(forumdesas_html, forumdesas_date_published, forumdesas)
    except:
        pass
    print "printing the okapi list "
    print forumdesas_links
    for link in forumdesas_links:
        print link

    try:
        theguardian_links = gl.theguardianLinks(theguardian_html, theguardian_date_published, theguardian)
    except:
        pass
    print "printing the okapi list "
    print theguardian_links
    for link in theguardian_links:
        print link

    try:
        financialtimes_links = gl.financialtimesLinks(financialtimes_html, financialtimes_date_published, financialtimes)
    except:
        pass
    print "printing the okapi list "
    print financialtimes_links
    for link in financialtimes_links:
        print link

    try:
        bloomberg_links = gl.bloombergLinks(bloomberg_html, bloomberg_date_published, bloomberg)
    except:
        pass
    print "printing the okapi list "
    print bloomberg_links
    for link in bloomberg_links:
        print link

    try:
        bloomberggoogle_links = gl.bloomberggoogleLinks(bloomberggoogle_html, bloomberggoogle_date_published, bloomberggoogle)
    except:
        pass
    print "printing the okapi list "
    print bloomberggoogle_links
    for link in bloomberggoogle_links:
        print link

    
    try:
        cnn_links = gl.cnnLinks(cnn_html, cnn_date_published, cnn)
    except:
        pass
    print "printing the okapi list "
    print cnn_links
    for link in cnn_links:
        print link

    try:
        france24_links = gl.france24Links(france24_html, france24_date_published, france24)
    except:
        pass
    print "printing the okapi list "
    print france24_links
    for link in france24_links:
        print link

    try:
        france24google_links = gl.france24googleLinks(france24google_html, france24google_date_published, france24google)
    except:
        pass
    print "printing the okapi list "
    print france24google_links
    for link in france24google_links:
        print link
    
    try:
        tv5monde_links = gl.tv5mondeLinks(tv5monde_html, tv5monde_date_published, tv5monde)
    except:
        pass
    print "printing the okapi list "
    print tv5monde_links
    for link in tv5monde_links:
        print link

    try:
        africanewsrdc_links = gl.africanewsrdcLinks(africanewsrdc_html, africanewsrdc_date_published, africanewsrdc)
    except:
        pass
    print "printing the okapi list "
    print africanewsrdc_links
    for link in africanewsrdc_links:
        print link


    try:
        topcongofm_links = gl.topcongofmLinks(topcongofm_html, topcongofm_date_published, topcongofm)
    except:
        pass
    print "printing the okapi list "
    print topcongofm_links
    for link in topcongofm_links:
        print link


    

    


    # creating a consolidated list of links

    consolidated_links_list = radiookapi_links + politico_links + actualite_links + benilubero_links + jeuneafrique_links + rfi_links + librebelgique_links + lemonde_links + voixamerique_links + lepotentiel_links + congoindependant_links 
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
