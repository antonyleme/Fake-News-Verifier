from bs4 import BeautifulSoup
import urllib.request
import requests
from urllib.parse import urlparse

def title(url):
    soup = BeautifulSoup(urllib.request.urlopen(url), "lxml")
    title = soup.title.string.replace("|", "-").split("-")
    return title[0]

def author(url):
    return 0

def opr(domain):
    headers = {'API-OPR':'w0gswkcgcwcgs04o4kkcko0oo04k480co0gwg00k'}
    url = 'https://openpagerank.com/api/v1.0/getPageRank?domains%5B0%5D=' + domain
    request = requests.get(url, headers=headers)
    return request.json()

def get(url, primary):
    domain = urlparse(url).netloc
    apiRequest = opr(domain)
    note = float(apiRequest['response'][0]['page_rank_decimal']) / 10
    rank = 1 - float(apiRequest['response'][0]['rank']) / 3000000000
    if primary:
        return [title(url), author(url), note, rank]
    else:
        return [note, rank]