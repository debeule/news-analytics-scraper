import os
from dotenv import load_dotenv

load_dotenv()

BOT_NAME = "bp_articles_scraper"

SPIDER_MODULES = ["bp_articles_scraper.spiders"]
NEWSPIDER_MODULE = "bp_articles_scraper.spiders"

# LOG_FILE = 'scrapy.log'
LOG_LEVEL = "INFO"

TWISTED_REACTOR = "twisted.internet.epollreactor.EPollReactor"
FEED_EXPORT_ENCODING = "utf-8"

DOWNLOADER_MIDDLEWARES = {
    'bp_articles_scraper.middlewares.proxy_middleware.ProxyMiddleware': 200,
    'bp_articles_scraper.middlewares.options_middleware.OptionsMiddleware': 300,
    'bp_articles_scraper.middlewares.user_agent_middleware.UserAgentMiddleware': 400,
    'bp_articles_scraper.middlewares.selenium_middleware.SeleniumMiddleware': 500,
}

ITEM_PIPELINES = {
    # 'bp_articles_scraper.pipelines.create_article_pipeline.CreateArticlePipeline': 100,
    # 'bp_articles_scraper.pipelines.update_article_pipeline.UpdateArticlePipeline': 200,
}

DATABASE_URL = f"{os.getenv('DB_CONNECTION')}://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:3306/{os.getenv('DB_DATABASE')}"

PROXY_URL = f"{os.getenv('OXYLABS_URL')}:{os.getenv('OXYLABS_PORT')}"
AUTH_PROXY_URL = f"{os.getenv('OXYLABS_USERNAME')}:{os.getenv('OXYLABS_PASSWORD')}@{os.getenv('OXYLABS_URL')}:{os.getenv('OXYLABS_PORT')}"

AMOUNT_OF_PAGES_TO_SCRAPE = 2