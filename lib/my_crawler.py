from crawler import Crawler
crawler = Crawler()
crawler.crawl('http://www.jeuneafrique.com/pays/rd-congo/')
# displays the urls
print crawler.content['http://www.jeuneafrique.com/pays/rd-congo/'].keys()
