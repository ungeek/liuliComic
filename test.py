from bs4 import BeautifulSoup
# import lxml

css_soup = BeautifulSoup('<p class="body"></p>', 'lxml')
# css_soup.p['class']
print(css_soup.p['class'])
# <class 'bs4.element.Tag'>