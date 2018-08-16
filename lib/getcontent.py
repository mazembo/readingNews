import pickle

def radiookapiContent(soup):
    body = soup.findAll("div", {"class" : "inside panels-flexible-row-inside panels-flexible-row-3-3-inside clearfix"})
    body = body[0].text
    short_message = body + signature
    return body, short_message
def get_content(soup):
    title = soup.title.text
    signature = " #RDC @LecongolaisNet"
    tweet_message = title
    #date_published= [meta.get('content') for meta in soup.find_all('meta', itemprop='datePublished')]
    body = soup.findAll("div", {"class" : "inside panels-flexible-row-inside panels-flexible-row-3-3-inside clearfix"})
    body = body[0].text
    short_message = body + signature
    return title, body, short_message, tweet_message

def get_images_okapi(soup):
    images = []
    for img in soup.find_all("div", {"class" : "inside panels-flexible-row-inside panels-flexible-row-3-3-inside clearfix"})[0].find_all('img'):
        temp = img.get('src')
        images.append(temp)
    if len(images) > 0:
        return images
    else:
        images.append("001_image.jpg")
        return images
def download_image(images_url, url):
    if images_url[0] != "001_image.jpg":
        img_url = images_url[0]
        file_name = hashlib.sha224(img_url).hexdigest() + ".jpg"
        urlretrieve(img_url, file_name)
        return file_name

    else:
        file_name = images_url[0]
        return file_name

def clean_up(title, body, short_message, tweet_message):
    title = title.replace(":", "--")
    body =  body.replace(":", "--")
    short_message = short_message.replace(":", "--")
    tweet_message = tweet_message.replace(":", "--")
    title = title.replace("\n", " ")
    body =  body.replace("\n", " ")
    short_message = short_message.replace("\n", " ")
    tweet_message = tweet_message.replace("\n", " ")
    title = title.replace("\t", " ")
    body =  body.replace("\t", " ")
    short_message = short_message.replace("\t", " ")
    tweet_message = tweet_message.replace("\t", " ")
    title = title.replace("\\x", " ")
    body =  body.replace("\\x", " ")
    short_message = short_message.replace("\\x", " ")
    tweet_message = tweet_message.replace("\\x", " ")
    return title, body, short_message, tweet_message
def get_formated_article(title, body, short_message, tweet_message, date_accessed, date_published, url, image_filename):
    title, body, short_message, tweet_message, date_accessed, date_published, url, image_filename = title, body, short_message, tweet_message, date_accessed, date_published, url, image_filename
    formated_article = {'title': title, 'message': body, 'short_message': short_message,'tweet_message': tweet_message, 'original_url': url, 'lecongolais_url':'http://lecongolais.net','date_published': date_published, 'date_accessed': date_accessed, 'picture': image_filename, 'categories':'RDC-Politique-Societe-Economie'}
    return formated_article
def write_html(html_file_name, html):
    out_file = open(html_file_name, "w")
    out_file.write(html)
    out_file.close
    print "We have created the file: %s" %html_file_name
def write_yaml(yaml_file_name, articles):
    with open(yaml_file_name, 'w') as yaml_file:
        yaml.dump(articles, yaml_file, encoding='utf-8', allow_unicode=True, default_flow_style=False)
        print "We have created the file: %s" %yaml_file_name
def write_links(links_file_name, links_list):
    try:
        with open(links_file_name, 'wb') as fp:
            pickle.dump(links_list, fp)
            print("the file has been created: %s" %links_file_name)
    except:
        print("there was a problem creating this file: %s" %links_file_name )
        pass
