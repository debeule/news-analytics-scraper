from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

class SeleniumMiddleware:

    consent_cookies = None

    def __init__(self):
        option = webdriver.ChromeOptions()

        option.add_argument("--headless")

        if SeleniumMiddleware.consent_cookies:
            # Add consent cookies to the Chrome options
            for cookie in SeleniumMiddleware.consent_cookies:
                option.add_argument(f"--cookie={cookie['name']}={cookie['value']}")

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)


    def process_request(self, request, spider):

        self.driver.get(request.url)

        if SeleniumMiddleware.consent_cookies == None:

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
        SeleniumMiddleware.consent_cookies = self.driver.get_cookies()


        # Switch back to the main frame
        self.driver.switch_to.default_content() 

        # Wait for the page to load
        time.sleep(10)

                
    def spider_closed(self, spider):
        self.driver.quit()