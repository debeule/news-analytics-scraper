import os
from dotenv import load_dotenv 
from shutil import which 

load_dotenv()

BOT_NAME = "bp_articles_scraper"

SPIDER_MODULES = ["bp_articles_scraper.spiders"]
NEWSPIDER_MODULE = "bp_articles_scraper.spiders"

# LOG_FILE = 'scrapy.log'
LOG_LEVEL = "DEBUG"

TWISTED_REACTOR = "twisted.internet.epollreactor.EPollReactor"
FEED_EXPORT_ENCODING = "utf-8"

DOWNLOADER_MIDDLEWARES = {
    'bp_articles_scraper.middlewares.proxy_middleware.ProxyMiddleware': 100,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 200,
    'bp_articles_scraper.middlewares.selenium_middleware.SeleniumMiddleware': 300,
}

ITEM_PIPELINES = {
    'bp_articles_scraper.pipelines.create_article_pipeline.CreateArticlePipeline': 100,
    'bp_articles_scraper.pipelines.update_article_pipeline.UpdateArticlePipeline': 200,
}

DATABASE_URL = f"{os.getenv('DB_CONNECTION')}://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:3306/{os.getenv('DB_DATABASE')}"

PROXY_URL = f"http://{os.getenv('OXYLABS_USERNAME')}:{os.getenv('OXYLABS_PASSWORD')}@{os.getenv('OXYLABS_URL')}:{os.getenv('OXYLABS_PORT')}"