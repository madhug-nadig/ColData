import urllib.request
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re

def get_url(query):
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

def file_write(qry,u ,op, i):
        i =  qry+ ".txt"
        file = open(i, "a", encoding='utf-8')
        file.write('\nData from: ' + u + '\n \n')
        file.write(op)
        file.write('\n \n')
        file.close()

def get_data(qry,u, i):
		print("getting data for " + qry)
		op = ""
		try:
			theurl = Request(u, headers = {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' })
			html=urllib.request.urlopen(theurl)
			data = html.read().decode('utf-8', 'ignore')
			soup=BeautifulSoup(data, 'html.parser')
			res = [i.text.replace('\n', ' ').strip() for i in soup.find_all('p')]
			for p in res:
					op = op + p + '\n'
			file_write(qry, u,op, i)
		except:
			print("HTTP exception (Most probable)")

def get_queries():
        try:
            f = open('query.txt', 'r')
            qs = f.readlines()
            f.close()
            qs = list(map(lambda s: s.strip(), qs))
            print(qs)
            return qs
        except IOError as e:
            print("\nPlease choose the correct path for query.txt! ")

def main():
	queries = get_queries()
	if queries:
		for iter in range(len(queries)):
				query = queries[iter]
				url = get_links(query)
				
				for i in range(8):
					if i< len(url):
						get_data(query, url[i], i)

if __name__ == "__main__":main()