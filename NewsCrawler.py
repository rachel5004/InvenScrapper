from soupsieve import select
from model.PostDataModel import PostData
from util.Decorators import *
from util.Constant import *
from util.Parser import *
from util.UrlRefiner import *
from MaxPageExractor import extract_max_page

MAX_PAGES = {}

def get_max_pages():
    for i in range(1, NEWS_MAX_PREMONTH+1):
        NEWS_MAX_PAGE = extract_max_page(NEWS_BASE_URL,i)
        MAX_PAGES[i] = NEWS_MAX_PAGE

@logging_time
def extract_all_data():
    for premonth in range(1, NEWS_MAX_PREMONTH+1):
        for page in range(1, int(MAX_PAGES[premonth])):
            TARGET_URL = NEWS_BASE_URL.format(page, premonth)
            extract_news_link(TARGET_URL)

@logging_time
def extract_news_link(target):
    soup = lxml_parser(target)
    news_links = soup.select("td div.content a")
    for data in news_links:
        link = data['href']
        extract_news_data(link)

def extract_news_data(link):
    soup = lxml_parser(link)
    data = {
        "date" : soup.select_one("dl.date dd").get_text(),
        "title" : soup.select_one("div.title h1").get_text(),
        "content" : soup.select_one("div.webzineNewsViewContent").get_text(),
        "writer" : soup.select_one("div.writer").get_text(),
        "link" : link
    }
    pd = PostData(data)
    pd.print_data()


get_max_pages()
extract_all_data()