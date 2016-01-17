import urllib.request
from bs4 import BeautifulSoup

def file_write(op):
        file = open("data.txt", "w", encoding='utf-8')
        file.write(op)
        file.close()

def get_data(u):
        op = ""
        html=urllib.request.urlopen(u)
        data = html.read().decode('utf-8', 'ignore');
        soup=BeautifulSoup(data)
        res = [i.text.replace('\n', ' ').strip() for i in soup.find_all('p')]
        for p in res:
                op = op + p
        file_write(op)

url = 'https://en.wikipedia.org/wiki/Adivasi';
get_data(url)
