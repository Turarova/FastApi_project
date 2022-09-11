from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import databases
# from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://aigerim:1@localhost/news_db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
database = databases.Database(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()
