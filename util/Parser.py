import requests
from bs4 import BeautifulSoup as bs

def html_parser(url):
    result = requests.get(url)
    soup = bs(result.text, "html.parser")
    return soup

from urllib.request import urlopen
def lxml_parser(url):
    html = urlopen(url)
    soup = bs(html.read(), "lxml")
    return soup

from urllib.parse import urlparse
# url example: https://lostark.inven.co.kr/
def get_game_id(url):
    return urlparse(url).netloc.split(".")[0]

    