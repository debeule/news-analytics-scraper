from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    main_title = Column(Text)
    full_content = Column(Text, nullable=True)
    url = Column(Text)
    created_at = Column(DateTime(timezone=True))