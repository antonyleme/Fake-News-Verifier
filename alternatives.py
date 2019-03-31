from googlesearch import search
import news

def find(term):
    r = []
    for url in search(term, stop=10):
        r.append(url)
    return r
