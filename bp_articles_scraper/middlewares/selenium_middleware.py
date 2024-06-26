from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
from seleniumwire import webdriver
import json
from time import sleep

class SeleniumMiddleware:

    def process_request(self, request, spider):

        self.driver = webdriver.Chrome(
            executable_path='/usr/bin/chromedriver',
            options=request.meta['options'],
            seleniumwire_options=request.meta['proxy']
        )
        
        self.driver.request_interceptor = self.block_unneccesary_requests

        self.driver.get(request.url)  
        
        if request.meta.get('testing') is None:
            
            with open('./bp_articles_scraper/organization_config.json', 'r') as file:
                
                file_data = json.load(file)[str(request.meta.get('organization_id'))]
                self.structure = file_data['structure']

            self.handle_cookie_consent()
        
        response = HtmlResponse(self.driver.current_url, body=self.driver.page_source, encoding='utf-8', request=request)

        self.driver.quit()

        return response
        
    
    def handle_cookie_consent(self):

        if self.structure['iframe_selector'] != "None":
            try: 
                iframe = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.ID, self.structure['iframe_selector']))
                )

                self.driver.switch_to.frame(iframe)

            except: iframe = None
            
        try:
            accept_button = WebDriverWait(self.driver, 11).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, self.structure['button_selector']))
            )
            
        except: accept_button = None

        if accept_button: accept_button.click()

        if self.structure['iframe_selector'] != "None":
            WebDriverWait(self.driver, 8).until
            (
                EC.staleness_of(iframe)
            )
        
        self.driver.switch_to.default_content()

        WebDriverWait(self.driver, 7).until
        (
            EC.presence_of_element_located((By.TAG_NAME, self.structure['list_element']))
        )

        sleep(3)

    def block_unneccesary_requests(self, request):

        keywords = ['image', 'img', 'font', 'css', 'google', 'googleapis' 'issue', 'analytics', 'ico', 'tracker', 'design', 'welcome']
        if any(keyword in request.url for keyword in keywords):
            request.abort()
    
    def interceptor(self, request):
        
        if request.path.endswith(('.png', '.jpg', '.gif')):
            request.abort()


                
    def spider_closed(self, spider):
        self.driver.quit()