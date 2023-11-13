import scrapy
from scrapy.loader import ItemLoader

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ArticlelistscraperSpider(scrapy.Spider):
    name = "ArticleListScraper"
    start_urls = []

    def __init__(self, *args, **kwargs):
        super(ArticlelistscraperSpider, self).__init__(*args, **kwargs)
        self.start_urls = [kwargs.get('scrape_url', None)]
        self.operation = kwargs.get('operation', 'insert')

    def parse(self, response):

        #headless browser for javascript rendering (cookies / consent)
        driver = webdriver.Chrome()
        driver.get(response.url)

        try:
            # Wait for the consent element to be clickable
            consent_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '.fc-cta-consent'))
            )
            consent_button.click()

            # Print out the entire page source
            print(driver.page_source)

            articles = response.xpath('//li[@class="results__list-item"]')

            for article in articles:
                data = {
                    'main_title': article.xpath('.//h2[@class="ankeiler__title"]/text()').get(),
                    'url': article.xpath('.//a[@class="ankeiler__link"]/@href').get(),
                }

                yield data


        finally:
            driver.quit()


        