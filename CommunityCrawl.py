from util.LoggingTime import *
from util.Constant import *
from Parser import *
from UrlRefiner import *


def extract_community_link():
    soup = lxml_parser(INVEN_MAIN)
    community_list = soup.find("div",{"class":"genre"}).find_all("li")

    for community in community_list:
        game = community.get_text()
        link = community.find("a").attrs['href']

extract_community_link()