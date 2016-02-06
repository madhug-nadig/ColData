import urllib.request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re


def get_url(query):
        if " " not in query:
                query = "http://duckduckgo.com/html/?q=" + query
        else:
                qarr = query.split()
                q = [x for x in qarr]
                query = "http://duckduckgo.com/html/?q=" + '+'.join(q)
        return query

def get_links(query):
        search_url = get_url(query)
        site = urllib.request.urlopen(search_url)
        data = site.read()
        the_links = []
        parsed = BeautifulSoup(data)
        for links in parsed.findAll('div', {'class': re.compile('links_main*')}):
                the_links.append(links.a['href'])
        return the_links

def file_write(op, i):
        i = str(i) + ".txt"
        file = open(i, "w", encoding='utf-8')
        file.write(op)
        file.close()

def get_data(u, i):
        op = ""
        theurl = Request(u, headers = {'User-Agent': 'Mozilla/5.0'})
        html=urllib.request.urlopen(theurl)
        data = html.read().decode('utf-8', 'ignore');
        soup=BeautifulSoup(data)
        res = [i.text.replace('\n', ' ').strip() for i in soup.find_all('p')]
        for p in res:
                op = op + p + '\n'
        file_write(op, i)

query = "Matheran"
url = get_links(query)
#get_data(url[0])

for i in range(8):
    get_data(url[i], i)
