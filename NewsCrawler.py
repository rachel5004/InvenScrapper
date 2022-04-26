from soupsieve import select
from model.PostDataModel import PostData
from util.LoggingTime import *
from util.Constant import *
from Parser import *
from UrlRefiner import *

MAX_PAGES = {}

def extract_max_page():
    for i in range(1, NEWS_MAX_PREMONTH+1):
        TARGET_URL = NEWS_BASE_URL.format(1, i)
        soup = lxml_parser(TARGET_URL)
        NEWS_MAX_PAGE = soup.select("a.pg")[-1].get_text()
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


extract_max_page()
extract_all_data()