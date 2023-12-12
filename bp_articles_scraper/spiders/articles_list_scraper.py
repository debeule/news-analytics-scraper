import scrapy
from scrapy_selenium import SeleniumRequest
from bs4 import BeautifulSoup
import random
import json


class Articleslistscraper(scrapy.Spider):
    name = "articles_list_scraper"
    start_urls = []

    def __init__(self, organization_id=None, *args, **kwargs):
        super(Articleslistscraper, self).__init__(*args, **kwargs)

        file_path =  './bp_articles_scraper/organization_config.json'
        with open(file_path, 'r') as file:
            self.organization_config = json.load(file)

        self.start_urls = [
            self.organization_config[str(organization_id)]["url"] + "?page=1",
            self.organization_config[str(organization_id)]["url"] + "?page=2",
            self.organization_config[str(organization_id)]["url"] + "?page=3"
        ]

        self.operation = "create"
        self.organization_id = str(organization_id)

    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url, 
                callback=self.parse,
                wait_time=random.uniform(5, 20)
            )

    def parse(self, response):
            
        soup = BeautifulSoup(response.body, 'html.parser')
        
        articles = soup.find_all('li', class_='results__list-item')
        
        for article in articles:
            
            data = {
                'main_title': article.find('h2', class_='ankeiler__title').text,
                'url': article.find('a', class_='ankeiler__link')['href'],
                'organization_id': self.organization_id,
            }
            
            yield data