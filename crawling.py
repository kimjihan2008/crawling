import urllib.request
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=view&query=%EB%94%94%EB%AF%B8%EA%B3%A0&oquery=%EB%94%94%EB%AF%B8%EA%B3%A0+%EC%9E%85%EC%8B%9C&tqi=hCGFAlp0Jy0ssE8sKeKssssst6G-024998&mode=normal'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all(class_ = 'api_txt_lines total_tit _cross_trigger')

data = []

for i in title:
    href = i.attrs['href']
    print(f'{i.get_text()} / {href} ')
