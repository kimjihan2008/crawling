import urllib.request
from bs4 import BeautifulSoup

url = #찾고 싶은 url
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all(class_ = '클래스이름')

data = []

for i in title:
    href = i.attrs['href']
    print(f'{i.get_text()} / {href} ')
