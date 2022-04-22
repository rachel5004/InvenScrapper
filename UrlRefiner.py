from urllib.parse import quote
def anscii_encode(link, word):
    link = link.replace(word, quote(word))
    return link