import os
from dotenv import load_dotenv  

load_dotenv()

BOT_NAME = "bp_articles_scraper"

SPIDER_MODULES = ["bp_articles_scraper.spiders"]
NEWSPIDER_MODULE = "bp_articles_scraper.spiders"

ROBOTSTXT_OBEY = False

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

DOWNLOADER_MIDDLEWARES = {
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
}

ITEM_PIPELINES = {
    'bp_articles_scraper.pipelines.create_article_pipeline.CreateArticlePipeline': 100,
    'bp_articles_scraper.pipelines.update_article_pipeline.UpdateArticlePipeline': 200,
}

DATABASE_URL = f"{os.getenv('DB_CONNECTION')}://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:3306/{os.getenv('DB_DATABASE')}"

PROXY_URL = f"http://{os.getenv("BRIGHTDATA_USERNAME")}:{os.getenv("BRIGHTDATA_PASSWORD")}@{os.getenv("BRIGHTDATA_HOST")}:PORT"
