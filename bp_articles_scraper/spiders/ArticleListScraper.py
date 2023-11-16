import scrapy
from scrapy.loader import ItemLoader
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy_selenium import SeleniumRequest
from datetime import datetime


class ArticlelistscraperSpider(scrapy.Spider):
    name = "ArticleListScraper"
    start_urls = []

    def __init__(self, *args, **kwargs):
        super(ArticlelistscraperSpider, self).__init__(*args, **kwargs)

        self.start_urls = [kwargs.get('scrape_url', None)]
        self.start_urls += [self.start_urls[0] + "?page=2", self.start_urls[0] + "?page=3"]
        self.operation = kwargs.get('operation', 'insert')

        self.pages_to_scrape = 3


    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url, 
                callback=self.parse,
                wait_time=random.uniform(1, 20),
                meta={'iframe': 'iframe#sp_message_iframe_901952'}
            )

    def parse(self, response):

        for page_num in range(1, self.pages_to_scrape + 1):
            articles = response.xpath('//li[@class="results__list-item"]')
            
            for article in articles:
                #get the time of the article and convert it to a datetime
                created_at = datetime.strptime(article.xpath('.//time[@class="ankeiler__timestamp"]/text()').get(), "%H:%M")

                data = {
                    'main_title': article.xpath('.//h2[@class="ankeiler__title"]/text()').get(),
                    'url': article.xpath('.//a[@class="ankeiler__link"]/@href').get(),
                    'created_at': created_at
                }

                yield data 


            # if page_num < self.pages_to_scrape:
            #     print("hier")
            #     print(self.start_urls[0])
            #     next_page_link = self.start_urls[0] + "?page=" + str(page_num)

            #     yield SeleniumRequest(
            #         url=next_page_link,
            #         callback=self.parse,
            #         wait_time=random.uniform(1, 20),
            #         meta={'iframe': 'iframe#sp_message_iframe_901952'}
            #     )