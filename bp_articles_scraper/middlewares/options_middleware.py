from selenium.webdriver.chrome.options import Options


class OptionsMiddleware:
    
    def __init__(self):
        self.options = Options()
        
        self.options.add_argument('--headless')
        self.options.add_argument("start-maximized")
        self.options.add_argument('--no-sandbox')
        #use tmp instead of /dev/shm (not ideal because meomory ==> disk)
        self.options.add_argument('--disable-dev-shm-usage')

        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option('useAutomationExtension', False)

        
        extension_path = '/usr/src/app/extensions/bypass-paywalls-chrome-master/'
        self.options.add_argument(f'--load-extension={extension_path}')



    def process_request(self, request, spider):

        request.meta['options'] = self.options