from util.Decorators import *
from util.Constant import *
from util.Parser import *
from util.UrlRefiner import *
from MaxPageExractor import extract_max_page

@deprecated
def extract_community_link():
    soup = lxml_parser(INVEN_MAIN)
    community_list = soup.find("div",{"class":"genre"}).find_all("li")
    for community in community_list:
        link = community.find("a").attrs['href']
        game_id = get_game_id(link)
        game_ko = community.get_text()
        print(game_id)

def extract_board_links():
    for community in GAME_COMMUNITY:
        max_page = extract_max_page(COMMUNITY_BOARD_BASE_URL,community)
        if max_page == 1 : exit()
        for page in range(1, max_page+1):
            TARGET_URL = COMMUNITY_BOARD_BASE_URL(community,page)
            extract_board_data(TARGET_URL)

def extract_board_data(link):
    pass
    #parse link & extract title,content...


extract_board_links()