import json
import os
import re
import requests
from bs4 import BeautifulSoup

page = 1
rootURL = "https://www.liuli.cat/wp/comic.html"
url = rootURL + "/page/" + str(page)
hrefs = []
resource_list = []


def find_href(text):
    soup = BeautifulSoup(text, 'lxml')
    articles = soup.body.div.section.div.find_all("article")
    global hrefs
    for article in articles:
        try:
            hrefs.append(article.header.h1.a['href'])
        except:
            print('guanggao')
    pass


def find_page(url1):
    print(url1)
    r1 = requests.get(url1)
    if r1.status_code == 404:
        return
    else:
        find_href(r1.text)
        global page
        page = page + 1
        url1 = rootURL + "/page/" + str(page)
        find_page(url1)
    pass


def save_json_to_file(filename):
    folder = "liuli"
    isExists = os.path.exists(folder)
    if not isExists:
        os.makedirs(folder)
    os.chdir(folder)
    with open(filename, 'w+', encoding="utf-8") as output_file:
        output_file.write(json.dumps(resource_list, indent=4, sort_keys=True, ensure_ascii=False))
    pass


def get_megnet(text):
    soup1 = BeautifulSoup(text, 'lxml')
    print(soup1.body.div.article.header.h1.string)
    title = soup1.body.div.article.header.h1.string
    str1 = soup1.body.div.article.get_text()
    str1 = re.sub(r'([^0-9a-zA-Z])([0-9a-zA-Z]{5,30})[^0-9a-zA-Z]{5,30}([0-9a-zA-Z]{5,30})([^0-9a-zA-Z])', r'\1\2\3\4', str1)
    hashe = re.findall(r'[^0-9a-fA-F]([0-9a-fA-F]{40})[^0-9a-fA-F]', str1)
    print(hashe)
    try:
        hashe[0] = 'magnet:?xt=urn:btih:' + hashe[0]

        new_resource = {'title': title, 'magnets': hashe[0]}
    except:
        print("not fund megnet!")
    global resource_list
    resource_list.append(new_resource)
    save_json_to_file('resource_list.json')
    pass


def open_page(hrefs1):

    for href in hrefs1:
        r2 = requests.get(href)
        get_megnet(r2.text)
    pass


find_page(url)
open_page(hrefs)


