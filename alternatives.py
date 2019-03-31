from googlesearch import search
import news
import difflib

def find(term):
    results = []
    for url in search(term, stop=10):
        results.append(url)
    return results

def get(term):
    results = find(term)
    alt = []
    for result in results:
        print(result)
        try:
            print(news.title(result))
            sequence = difflib.SequenceMatcher(isjunk=None, a=term, b=news.title(result))
            difference = sequence.ratio()*100
            difference = round(difference,1)
            print(difference)
            if difference > 60:
                alt.append(result)
        except:
            print("")
    return media(alt)

def media(alt):
    rank = 0
    note = 0
    for a in alt:
        inf = news.get(a, False)
        note += inf[0] / alt.__len__()
        rank += inf[1] / alt.__len__()
    return [note, rank]
    
    
        


