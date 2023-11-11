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

ITEM_PIPELINES = {
    'bp_articles_scraper.pipelines.DatabasePipeline': 300,
}

DATABASE_URL = f"{os.getenv('DB_CONNECTION')}://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:3306/{os.getenv('DB_DATABASE')}"
