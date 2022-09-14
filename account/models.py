from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from database.db import Base


class User(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)
    activation_code = Column(String)

    comment = relationship("Comment", back_populates="owner")
    article = relationship("Article", back_populates="owner")

user = User.__table__