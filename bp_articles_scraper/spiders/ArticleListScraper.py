import scrapy
from scrapy.loader import ItemLoader
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy_selenium import SeleniumRequest
from datetime import datetime
import os
import json
import sys
from bs4 import BeautifulSoup


class ArticlelistscraperSpider(scrapy.Spider):
    name = "ArticleListScraper"
    start_urls = []

    def __init__(self, *args, **kwargs):
        super(ArticlelistscraperSpider, self).__init__(*args, **kwargs)

        #retrieve the json file
        json_file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'organization_config.json')
        with open(json_file_path, 'r') as file:
            self.organization_config = json.load(file)

        self.start_urls = [
            self.organization_config[kwargs.get('organization_id')]["url"],
            self.organization_config[kwargs.get('organization_id')]["url"] + "?page=2",
            self.organization_config[kwargs.get('organization_id')]["url"] + "?page=3"
        ]

        self.operation = "create"
        self.organization_id = kwargs.get('organization_id')


    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url, 
                callback=self.parse,
                wait_time=random.uniform(1, 20)
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