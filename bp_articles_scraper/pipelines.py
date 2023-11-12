from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from bp_articles_scraper.models.article import Article

Base = declarative_base()

class DatabasePipeline:
    def __init__(self, database_url):
        self.engine = create_engine(database_url)
        self.Session = sessionmaker(bind=self.engine)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(database_url=crawler.settings.get('DATABASE_URL'))

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        session = self.Session()

        article = Article(full_content=item.get('full_content'))

        try:
            session.add(article)
            session.commit()
        except Exception as e:
            session.rollback()
            raise
        finally:
            session.close()

        return item
