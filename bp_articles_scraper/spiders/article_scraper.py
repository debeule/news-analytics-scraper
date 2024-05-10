import scrapy
from scrapy_selenium import SeleniumRequest
from bs4 import BeautifulSoup
import random
import json
from scrapy.utils.project import get_project_settings


class ArticleScraper(scrapy.Spider):
    
    name = 'article_scraper'
    start_urls = []


    def __init__(self, organization_id=None, url=None, *args, **kwargs):
        super(ArticleScraper, self).__init__(*args, **kwargs)

        self.organization_id = str(organization_id)
        self.start_urls = url

        with open('./bp_articles_scraper/organization_config.json', 'r') as file:
            config_file = json.load(file)[str(organization_id)]
            
        self.keywords = config_file['keywords']
        
        self.article = ''


    def start_requests(self):
        yield SeleniumRequest(
            url = self.start_urls, 
            callback = self.parse,
            wait_time = random.uniform(5, 20),
            meta = {'organization_id': self.organization_id}
        )


    def parse(self, response):
        soup = BeautifulSoup(response.body, 'html.parser')

        try:
            unwanted_elements = (soup.find_all(lambda tag:
                tag.name and any(keyword in tag.name.lower() for keyword in self.keywords))
            )

            for element in unwanted_elements:
                element.decompose()

            elements_with_class = soup.find_all(class_=True)

            unwanted_elements = []

            for element in elements_with_class:
                class_names = element.get('class')

                for class_name in class_names:
                    if any(keyword in class_name for keyword in self.keywords):
                        unwanted_elements.append(element)

            for element in unwanted_elements:
                element.decompose()

            self.article = ''.join(soup.stripped_strings)
            
        except Exception as e:
            print(e)
        
        
        return {'result': self.article}