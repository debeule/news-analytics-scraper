import scrapy


class BpArticlesScraperItem(scrapy.Item):
    full_content = scrapy.Field()
    pass
