import scrapy
from urllib.parse import urlencode
import http.client
import os


class ArticlelistscraperSpider(scrapy.Spider):        

    name = "ArticleListScraper"
    start_urls = self.settings.get('START_URLS')
    allowed_domains = self.settings.get('ALLOWED_DOMAINS')


    proxyUrl = os.environ.get("proxy.url")
    conn = http.client.HTTPSConnection(proxyUrl)

    scrapeUrl = "https://www.scrapethissite.com/pages/"

    conn.request(
        "GET", 
        "/v2/general",
        headers = {urlencode(os.environ.get("SCRAPINGANT_API_KEY"))},
    )


    def parse(self, response):
        pass