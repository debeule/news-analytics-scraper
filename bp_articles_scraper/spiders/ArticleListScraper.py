import scrapy
from scrapy.loader import ItemLoader

class ArticlelistscraperSpider(scrapy.Spider):
    name = "ArticleListScraper"
    start_urls = []

    def __init__(self, *args, **kwargs):
        super(ArticlelistscraperSpider, self).__init__(*args, **kwargs)
        self.start_urls = [kwargs.get('scrape_url', None)]
        self.operation = kwargs.get('operation', 'insert')

    def parse(self, response):
        articles = response.xpath('//li[@class="results__list-item"]')

        for article in articles:
            data = {
                'main_title': article.xpath('.//h2[@class="ankeiler__title"]/text()').get(),
                'url': article.xpath('.//a[@class="ankeiler__link"]/@href').get(),
            }

            yield data