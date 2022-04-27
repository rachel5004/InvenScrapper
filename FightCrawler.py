from MaxPageExractor import extract_max_page
from util.Decorators import *
from util.Constant import *
from util.Parser import *
from util.UrlRefiner import *
from model.PostDataModel import PostData

links = []

@logging_time
def extract_fight_link():
    max_page = extract_max_page(FIGHT_BASE_URL,"")
    for page in range(1, max_page+1):
        TARGET_URL = FIGHT_BASE_URL.format(page,"")
        soup = lxml_parser(TARGET_URL)
        news_list = soup.find_all(attrs={'class':'item has_img clearfix'})
        for news in news_list:
            link = anscii_encode(news.find("h1").find("a").attrs['href'],"공략")
            links.append(link)

def extract_fight_data(link):
    soup = lxml_parser(link)
    print(link)
    try:
        title = soup.find(attrs={"class":"title"}).find("h1").get_text()
    except:
        title = title= soup.find_all(attrs={"class":"title"})[1].find("h1").get_text()

    data = {
        "link" : link,
        "date" : soup.find("dd").get_text(),
        "title" : title,
        "writer" : soup.find(attrs={"class":"writer"}).get_text(),
        "content" : soup.find(attrs={"class":"webzineNewsViewContent"}).get_text()
    }
    pd = PostData(data)
    pd.print_data()

@logging_time
def extract_all_data(links):
    for link in links:
        extract_fight_data(link)
        time.sleep(0.2)

extract_fight_link()
extract_all_data(links)