from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
from seleniumwire import webdriver
import json


class SeleniumMiddleware:

    privacy_consent_clicked = False        

    def process_request(self, request, spider):
        
        self.driver = webdriver.Chrome(
            executable_path='/usr/bin/chromedriver',
            options=request.meta['options'],
            seleniumwire_options=request.meta['proxy']
        )
        
        if request.meta.get('testing') is not None:
            
            with open('./bp_articles_scraper/organization_config.json', 'r') as file:
                
                file_data = json.load(file)[str(request.meta.get('organization_id'))]
                self.structure = file_data['structure']

            
            self.driver.get(request.url)  

            if not self.privacy_consent_clicked:
                self.handle_cookie_consent()

        self.driver.get(request.url)
        
        return HtmlResponse(self.driver.current_url, body=self.driver.page_source, encoding='utf-8', request=request)
        
    
    def handle_cookie_consent(self):

        if self.structure['iframe_selector'] != "None":
            
            iframe = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, self.structure['iframe_selector']))
            )

            self.driver.switch_to.frame(iframe)
            
            
        accept_button = WebDriverWait(self.driver, 9).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.structure['button_selector']))
        )
        
        accept_button.click()

        WebDriverWait(self.driver, 8).until(
            EC.staleness_of(iframe)
        )

        self.privacy_consent_clicked = True 

                
    def spider_closed(self, spider):
        self.driver.quit()