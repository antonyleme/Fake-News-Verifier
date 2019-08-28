from googlesearch import search
import news
import difflib

"""Método para pesquisar as fontes no google"""
def find(term):
    results = []
    for url in search(term, stop=10):
        results.append(url)
    return results

"""Método para pegar as médias dos ranks e das notas"""
def media(alt):
    rank = 0
    note = 0
    for a in alt:
        inf = news.get(a, False)
        note += inf[0] / alt.__len__()
        rank += inf[1] / alt.__len__()
    return [note, rank]

"""Método para pegar todas as informações das fontes alternativas"""
def get(term, url):
    results = find(term)
    alt = []
    for result in results:
        #print(result)
        try:
            #print(news.title(result))
            sequence = difflib.SequenceMatcher(isjunk=None, a=term, b=news.title(result))
            difference = sequence.ratio()*100
            difference = round(difference,1)
            #print(difference)
            if difference > 60 and news.domain(result) != news.domain(url):
                print(news.title(result))
                alt.append(result)
        except:
            print("")

    return [alt, media(alt)]




