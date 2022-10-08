# from datetime import datetime
# from enum import auto
from sqlalchemy.sql import func
from sqlalchemy import Text, String, Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database.db import Base
# from account.models import User


class Arcticle(Base):
    __tablename__ = "article"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    text = Column(Text)
    image = Column(String)
    comment = relationship("Comment", back_populates = "article")


article = Arcticle.__table__

class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    # created_at = Column(DateTime autoincrement=True, auto_now_add=datetime.now())
    article_id = Column(Integer, ForeignKey('article.id'), nullable=False)
    user_email = Column(String, ForeignKey('account.email'), nullable=False)


    user = relationship("User", back_populates = "comment")
    article = relationship("Article", back_populates = "comment")

comment = Comment.__table__