import scrapy
from scrapy_selenium import SeleniumRequest
import random
from bs4 import BeautifulSoup

class MyIpScraperSpider(scrapy.Spider):

    name = "my_ip_scraper"
    start_urls = ['https://www.whatismybrowser.com/detect/what-is-my-user-agent/']

    def start_requests(self):

        yield SeleniumRequest(
            url = self.start_urls[0], 
            callback = self.parse,
            wait_time = random.uniform(5, 20)
        )

    def parse(self, response):
            
        soup = BeautifulSoup(response.body, 'html.parser')

        print(soup.prettify())