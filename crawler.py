import urllib.request
from bs4 import BeautifulSoup

def getData(u):
        html=urllib.request.urlopen(u)
        data = html.read().decode('utf-8', 'ignore');
        soup=BeautifulSoup(data)
        res = [i.text.replace('\n', ' ').strip() for i in soup.find_all('p')]
        for p in res:
                print(p)

url = 'https://en.wikipedia.org/wiki/Adivasi';
getData(url)
