from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
import time
from selenium.webdriver.chrome.options import Options

class SeleniumMiddleware:

    def __init__(self):
        self.driver = None

        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        #use tmp instead of /dev/shm (not ideal because meomory ==> disk)
        options.add_argument('--disable-dev-shm-usage')

        self.driver = webdriver.Chrome(executable_path=r'/usr/bin/chromedriver', options=options)
        

    def process_request(self, request, spider):
        self.driver.get(request.url)

        if not self.driver.get_cookies():
            self.handle_iframe()
            
            
        return HtmlResponse(self.driver.current_url, body=self.driver.page_source, encoding='utf-8', request=request)

    
    def handle_iframe(self):
        iframe_id = "sp_message_iframe_901952"

        iframe = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, iframe_id))
        )

        self.driver.switch_to.frame(iframe)

        accept_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.pg-accept-button'))
        )

        accept_button.click()
        
        time.sleep(5)


        # Switch back to the main frame
        self.driver.switch_to.default_content() 

        # Wait for the page to load
        time.sleep(10)

                
    def spider_closed(self, spider):
        self.driver.quit()