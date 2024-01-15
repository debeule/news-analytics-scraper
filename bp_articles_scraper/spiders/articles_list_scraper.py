import scrapy
from scrapy_selenium import SeleniumRequest
from bs4 import BeautifulSoup
import random
import json
from scrapy.utils.project import get_project_settings


class Articleslistscraper(scrapy.Spider):
    
    name = 'articles_list_scraper'
    start_urls = []


    def __init__(self, organization_id=None, *args, **kwargs):

        super(Articleslistscraper, self).__init__(*args, **kwargs)

        settings = get_project_settings()


        with open('./bp_articles_scraper/organization_config.json', 'r') as file:
            
            config_file = json.load(file)[str(organization_id)]

        base_url = config_file['url']
        
        num_pages = settings['AMOUNT_OF_PAGES_TO_SCRAPE']

        if config_file['paginated']:
            for page in range(1, num_pages - 1):
                self.start_urls.append(base_url + '?page=' + str(page))
        
        if not config_file['paginated']:
            self.start_urls = [base_url]
            
        self.structure = config_file['structure']
        self.operation = 'create'
        self.organization_id = str(organization_id)


    def start_requests(self):

        for url in self.start_urls:

            yield SeleniumRequest(
                url = url, 
                callback = self.parse,
                wait_time = random.uniform(5, 20),
                meta = {'organization_id': self.organization_id}
            )

    def parse(self, response):

        soup = BeautifulSoup(response.body, 'html.parser')

        # print(soup.prettify())

        articles = []

        sections = soup.find_all('section')

        for section in sections:

            identifier_element = section.find(self.structure['list_identifier'])

            if identifier_element and identifier_element.get_text() == self.structure['list_identifier_content']:
                articles = section.find_all(self.structure['article_element'])

                break

        for article in articles:
                
                try:
                    data = {}

                    main_title = article.find(self.structure['article_title']).get_text()
                    print(main_title)

                    url_element = article

                    if self.structure['article_link_element'] != 'self':
                        url_element = article.find(self.structure['article_link_element'])
                    
                    url = url_element.get('href')

                    data = {
                        'main_title': main_title,
                        'url': url,
                        'organization_id': self.organization_id,
                    }
                    
                    yield data

                except Exception as e:
                    print('exception: ' + e)
                    continue
                    