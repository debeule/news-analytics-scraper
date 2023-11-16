import requests
from scrapy import signals
from scrapy.downloadermiddlewares.httpcompression import HttpCompressionMiddleware
from scrapy.utils.project import get_project_settings

class ProxyMiddleware:
    def __init__(self, settings):
        self.settings = settings

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def process_request(self, request, spider):
        request.meta['proxy'] = self.settings.get("PROXY_URL")