from util.Parser import lxml_parser

def extract_max_page(base, key):
    TARGET_URL = base.format(key,1)
    soup = lxml_parser(TARGET_URL)
    pages = soup.select("a.pg")
    return int(pages[-1].get_text()) if len(pages) > 1 else 1