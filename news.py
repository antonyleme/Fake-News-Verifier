from bs4 import BeautifulSoup
import urllib.request

def title(url):
    soup = BeautifulSoup(urllib.request.urlopen(url), "lxml")
    title = soup.title.string.split("-")
    return title
