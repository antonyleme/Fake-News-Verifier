import alternatives
import news
import sys
import json

url = sys.argv[1]
primary = news.get(url, True)
alt = alternatives.get(primary[0], url)

links = alt[0]
titulos = []
sites = []
for link in links:
    titulos.append(news.title(link))
    sites.append(news.domain(link))

vector = [primary[1], primary[2], primary[3], alt[0].__len__(), alt[1][0], alt[1][1], primary[0], url, links, titulos, sites]

print(json.dumps(vector))
