import urllib.request

from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
        r = urllib.request.urlopen(self.site)
        html = r.read()
        parser = "html.parser"
        sp = BeautifulSoup(html, parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "html" in url:
                print("\n" + url)

# news = "https://news.google.com/"
news = "https://news.google.com/stories/CAAqOQgKIjNDQklTSURvSmMzUnZjbmt0TXpZd1NoTUtFUWlieW9Ld2tZQU1FZlBCQTZvV1ZDOUNLQUFQAQ?hl=ja&gl=JP&ceid=JP%3Aja"
Scraper(news).scrape()
