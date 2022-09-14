from sqlalchemy import Text, String, Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database.db import Base


class Arcticle(Base):
    __tablename__ = "article"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    text = Column(Text)
    image = Column(String)

article = Arcticle.__table__

class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text)
    created_at = Column(DateTime)
    atricle_id = Column(Integer, ForeignKey('comment.id'), nullable=False)

    user = relationship("User", back_populates = "comment")
    article = relationship("Article", back_populates = "comment")

comment = Comment.__table__