import alternatives
import news

url = "https://g1.globo.com/mundo/noticia/2019/03/31/apos-cogitar-transferir-embaixada-bolsonaro-anuncia-escritorio-diplomatico-em-jerusalem.ghtml"
primary = news.get(url, True)
alt = alternatives.get(primary[0], url)

vector = [primary[1], primary[2], primary[3], alt[0], alt[1][0], alt[1][1]]

print(vector)