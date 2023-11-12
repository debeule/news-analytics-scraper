import scrapy
from scrapy.http import HtmlResponse
from scrapy.loader import ItemLoader

class ArticlelistscraperSpider(scrapy.Spider):
    name = "ArticleListScraper"
    start_urls = []

    def __init__(self, *args, **kwargs):
        super(ArticlelistscraperSpider, self).__init__(*args, **kwargs)
        self.start_urls = [kwargs.get('scrape_url', None)]

    def parse(self, response):
        full_content = response.body.decode(response.encoding)
        yield {"full_content": full_content}