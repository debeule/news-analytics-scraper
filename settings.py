BOT_NAME = "bp_articles_scraper"

SPIDER_MODULES = ["bp_articles_scraper.spiders"]
NEWSPIDER_MODULE = "bp_articles_scraper.spiders"

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"


ROBOTSTXT_OBEY = False

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
}

SCRAPER_CONSTANTS = {
    'proxy' : {
        'url' : "api.scrapingant.com"
    }
}
