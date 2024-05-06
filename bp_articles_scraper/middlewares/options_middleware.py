from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.options import Options as ChromeOptions



class OptionsMiddleware:
    
    def __init__(self):
        self.options = ChromeOptions()
        
        self.options.add_argument('--headless=new')
        # self.options.add_argument("start-maximized")
        self.options.add_argument('--no-sandbox')

        #use tmp instead of /dev/shm (not ideal because meomory ==> disk)
        self.options.add_argument('--disable-dev-shm-usage')

        self.options.add_argument('--disable-javascript')
        self.options.add_argument('--disable-images')

        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option('useAutomationExtension', False)

        
        extensions_path = '/code/extensions/'
        # self.options.add_argument('load-extension=/app/extensions/bypass-paywalls-chrome-master')
        self.options.add_extension(extensions_path + 'bypass-paywalls.crx')
        self.options.add_extension(extensions_path + 'add-block-plus.crx')
        # self.options.add_extension(extensions_path + 'request-blocker.crx')

    def process_request(self, request, spider):

        request.meta['options'] = self.options