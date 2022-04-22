from model.NewsDataModel import NewsData
from Parser import *
from util.Constant import *
from UrlRefiner import *
from util.LoggingTime import *


links = []
data={}

@logging_time
def extract_news_link():
    for n in range(1, MAX_PAGE+1):
        TARGET_URL = FIGHT_BASE_URL+str(n)
        soup = lxml_parser(TARGET_URL)
        
        news_list = soup.find_all(attrs={'class':'item has_img clearfix'})
        for news in news_list:
            link = anscii_encode(news.find("h1").find("a").attrs['href'],"공략")
            links.append(link)
    print(len(links))

def extract_news_data(link):
    soup = lxml_parser(link)
    try:
        title = soup.find(attrs={"class":"title"}).find("h1").get_text()
    except:
        title = title= soup.find_all(attrs={"class":"title"})[1].find("h1").get_text()

    dict = {
        "link" : link,
        "date" : soup.find("dd").get_text(),
        "title" : title,
        "writer" : soup.find(attrs={"class":"writer"}).get_text(),
        "content" : soup.find(attrs={"class":"content webzineNewsViewContent"}).get_text()
    }
    nd = NewsData(dict)
    nd.print_data()

@logging_time
def extract_all_data(links):
    for link in links:
        extract_news_data(link)
        time.sleep(0.2)

extract_news_link()
extract_all_data(links)