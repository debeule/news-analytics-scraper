import os


class ProxyMiddleware:

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)
    
    def __init__(self, settings):
        self.settings = settings


    def process_request(self, request, spider):
        
        request.meta['proxy'] = {
            'proxy': {
                'http': f'https://{self.settings.get("AUTH_PROXY_URL")}',
                'https': f'https://{self.settings.get("AUTH_PROXY_URL")}'
            }
        }