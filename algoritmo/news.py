from bs4 import BeautifulSoup
import urllib.request
import requests
from urllib.parse import urlparse

"""Método para pegar o titulo de uma noticia a partir da url"""
def title(url):
    soup = BeautifulSoup(urllib.request.urlopen(url), "lxml")
    title = soup.title.string.replace("|", "-").split("-")
    return title[0]

"""Método para pegar o autor de uma notícia a partir da url"""
def author(url):
    return 0

"""Método para pegar a nota e o rank de uma notícia a partir do domínio"""
def opr(d):
    headers = {'API-OPR':'w0gswkcgcwcgs04o4kkcko0oo04k480co0gwg00k'}
    url = 'https://openpagerank.com/api/v1.0/getPageRank?domains%5B0%5D=' + d
    request = requests.get(url, headers=headers)
    return request.json()

"""Método para pegar o domínio"""
def domain(url):
    return urlparse(url).netloc

"""Método para pegar todas as informações de uma notícia"""
def get(url, primary):
    d = domain(url)
    apiRequest = opr(d)
    note = float(apiRequest['response'][0]['page_rank_decimal']) / 10
    #rank = 1 - float(apiRequest['response'][0]['rank']) / 3000000000
    rank = float(apiRequest['response'][0]['rank'])
    if primary:
        return [title(url), author(url), note, rank]
    else:
        return [note, rank]
