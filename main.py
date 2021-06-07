import os
import requests
from bs4 import BeautifulSoup

page = 12
rootURL = "https://www.liuli.cat/wp/comic.html"
url = rootURL + "/page/" + str(page)
# url = "https://www.liuli.cat/wp/83200.html"
r1 = requests.get(url)

folder = "liuli"
isExists = os.path.exists(folder)
if not isExists:
    os.makedirs(folder)
os.chdir(folder)

# f = open("11.html", "w", encoding="utf-8")
# f.write(r1.text)
# f.close()

soup = BeautifulSoup(r1.text, 'lxml')
# soup.body.div.section.div.article.header.h1.a['href']
# print(soup.body.div.section.div.article.header.h1.a['href'])
articles = soup.body.div.section.div.find_all("article")
# print(articles[1])

hrefs = []
for article in articles:
    print(article.header.h1.a['href'])
    # hrefs.append(article.header.h1.a['href'])


# pattern = r'name="__VIEWSTATE" value="(.*?)"'

# f = open("130_1.html", "w", encoding="utf-8")
# f.write(r1.text)
# f.close()

# print(r1.text)
# print(r1.encoding)





