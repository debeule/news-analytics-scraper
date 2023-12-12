from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from bp_articles_scraper.models.article import Article

Base = declarative_base()


class UpdateArticlePipeline:
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

        if spider.operation == 'update':

            session = self.Session()

            article = Article(
                main_title=item.get('main_title'),
                url=item.get('url')
            )

            try:
                session.add(article)
                session.commit()

            except Exception as e:
                session.rollback()
                
                raise

            finally:
                session.close()


        return item