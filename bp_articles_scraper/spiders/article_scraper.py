import scrapy
from scrapy_selenium import SeleniumRequest
import random

class ArticleScraperSpider(scrapy.Spider):
    name = "articleScraper"
    allowed_domains = ["a.a"]
    start_urls = []

    def __init__(self, article_url=None, *args, **kwargs):
        super(ArticleScraperSpider, self).__init__(*args, **kwargs)

        self.start_urls = [str(article_url)]
        self.operation = "update"

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url, 
                callback=self.parse,
                wait_time=random.uniform(5, 20)
            )