import urllib.request
from bs4 import BeautifulSoup

u='http://fortune.com/2015/12/31/wall-street-market-performance-worries-year/'
r=urllib.request.urlopen(u)
soup=BeautifulSoup(r.read(),'html.parser')

res = [i.text.replace('\n', ' ').strip() for i in soup.find_all('p')]
for p in res:
        print(p)